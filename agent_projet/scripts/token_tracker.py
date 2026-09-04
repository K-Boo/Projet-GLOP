import os
import sys
import glob
import json
import time
import re
import unicodedata
from datetime import datetime, timedelta

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich import box
    RICH_AVAILABLE = True
    console = Console()
except ImportError:
    RICH_AVAILABLE = False
    console = None

# Quotas par defaut (tokens)
DEFAULT_DAILY_QUOTA = 1_000_000   # 1M tokens/jour
DEFAULT_WEEKLY_QUOTA = 5_000_000  # 5M tokens/semaine

# Facteurs environnementaux par 1000 tokens (Luccioni et al. 2023, Shaolei Ren et al. 2023)
ECO_FACTORS = {
    "flash_lite": {"wh": 0.10, "ml": 0.25},
    "flash":      {"wh": 0.35, "ml": 0.80},
    "pro":        {"wh": 1.20, "ml": 2.00},
    "default":    {"wh": 0.35, "ml": 0.80}
}

def clean_ascii(text):
    if not text:
        return ""
    text = text.replace("«", "\"").replace("»", "\"")
    text = text.replace("“", "\"").replace("”", "\"")
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace("…", "...").replace("–", "-").replace("—", "-")
    text = text.replace("€", "EUR").replace("°", "deg")
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(c for c in normalized if not unicodedata.combining(c))

def get_brain_dir():
    user_home = os.path.expanduser("~")
    return os.path.join(user_home, ".gemini", "antigravity", "brain")

def find_all_transcripts():
    base = get_brain_dir()
    pattern = os.path.join(base, "*", ".system_generated", "logs", "transcript.jsonl")
    return sorted(glob.glob(pattern), key=os.path.getmtime, reverse=True)

def find_latest_transcript():
    ts = find_all_transcripts()
    return ts[0] if ts else None

def parse_iso_datetime(ts_str, default_dt):
    if not ts_str:
        return default_dt
    try:
        clean = ts_str.replace("Z", "+00:00")
        return datetime.fromisoformat(clean).astimezone().replace(tzinfo=None)
    except Exception:
        return default_dt

def compute_quotas_all_sessions(daily_quota=DEFAULT_DAILY_QUOTA, weekly_quota=DEFAULT_WEEKLY_QUOTA):
    transcripts = find_all_transcripts()
    now = datetime.now()
    today_midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week_ago = today_midnight - timedelta(days=7)

    today_in = 0
    today_out = 0
    week_in = 0
    week_out = 0

    for tf in transcripts:
        file_mtime = datetime.fromtimestamp(os.path.getmtime(tf))
        if file_mtime < week_ago:
            continue
        try:
            with open(tf, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        data = json.loads(line)
                    except Exception:
                        continue

                    dt = parse_iso_datetime(data.get("created_at"), file_mtime)
                    stype = data.get("type", "")
                    tok_in = 0
                    tok_out = 0

                    if stype == "USER_INPUT":
                        tok_in = len(data.get("content") or "") // 4
                    elif stype == "PLANNER_RESPONSE":
                        tok_out = (len(data.get("content") or "") + len(data.get("thinking") or "")) // 4
                    elif stype == "GENERIC":
                        tok_in = len(data.get("content") or "") // 4

                    if dt >= today_midnight:
                        today_in += tok_in
                        today_out += tok_out
                    if dt >= week_ago:
                        week_in += tok_in
                        week_out += tok_out
        except Exception:
            pass

    today_total = today_in + today_out
    week_total = week_in + week_out

    today_wh = (today_total / 1000.0) * ECO_FACTORS["default"]["wh"]
    today_ml = (today_total / 1000.0) * ECO_FACTORS["default"]["ml"]
    week_wh = (week_total / 1000.0) * ECO_FACTORS["default"]["wh"]
    week_ml = (week_total / 1000.0) * ECO_FACTORS["default"]["ml"]

    return {
        "today_in": today_in,
        "today_out": today_out,
        "today_total": today_total,
        "today_quota": daily_quota,
        "today_ratio": min(today_total / max(daily_quota, 1), 1.0),
        "today_wh": today_wh,
        "today_ml": today_ml,
        "week_in": week_in,
        "week_out": week_out,
        "week_total": week_total,
        "week_quota": weekly_quota,
        "week_ratio": min(week_total / max(weekly_quota, 1), 1.0),
        "week_wh": week_wh,
        "week_ml": week_ml
    }

def extract_turns_from_transcript(file_path):
    if not os.path.isfile(file_path):
        return []

    steps = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        steps.append(json.loads(line))
                    except Exception:
                        pass
    except Exception:
        return []

    user_indices = [i for i, s in enumerate(steps) if s.get("type") == "USER_INPUT"]
    turns = []
    current_parent_model = "Gemini 3.8 Flash"

    for pos, u_idx in enumerate(user_indices):
        next_u_idx = user_indices[pos + 1] if pos + 1 < len(user_indices) else len(steps)
        u_step = steps[u_idx]
        u_content = u_step.get("content", "")

        if "Model Selection" in u_content:
            match = re.search(r"Model Selection from (.*?) to (.*?)\.", u_content)
            if match:
                current_parent_model = match.group(2).strip()

        prompt_text = u_content
        if "<USER_REQUEST>" in prompt_text and "</USER_REQUEST>" in prompt_text:
            prompt_text = prompt_text.split("<USER_REQUEST>")[1].split("</USER_REQUEST>")[0].strip()
        prompt_text = clean_ascii(prompt_text.replace("\n", " ").strip())
        if len(prompt_text) > 85:
            prompt_text = prompt_text[:82] + "..."

        t_in = len(u_content) // 4
        t_out = 0
        subagents = []
        model_tier = "flash"

        for s in steps[u_idx + 1:next_u_idx]:
            stype = s.get("type")
            cnt = s.get("content") or ""
            thk = s.get("thinking") or ""
            tcalls = s.get("tool_calls") or []

            if stype == "PLANNER_RESPONSE":
                t_out += (len(cnt) + len(thk)) // 4
            elif stype == "GENERIC":
                t_in += len(cnt) // 4

            for tc in tcalls:
                if tc.get("name") == "invoke_subagent":
                    args = tc.get("args", {})
                    for sub in args.get("Subagents", []):
                        role = clean_ascii(sub.get("Role", "Sous-Agent"))
                        m = sub.get("Model", "flash")
                        subagents.append((role, m))
                        if m == "pro":
                            model_tier = "pro"
                        elif m == "flash_lite" and model_tier != "pro":
                            model_tier = "flash_lite"

        total_tok = t_in + t_out
        if subagents:
            sub_strs = [f"{r} [{m}]" for r, m in subagents[:2]]
            model_display = f"{current_parent_model} + " + ", ".join(sub_strs)
        else:
            model_display = f"{current_parent_model} (Orchestrateur)"

        wh = (total_tok / 1000.0) * ECO_FACTORS.get(model_tier, ECO_FACTORS["default"])["wh"]
        ml = (total_tok / 1000.0) * ECO_FACTORS.get(model_tier, ECO_FACTORS["default"])["ml"]

        ts_str = u_step.get("created_at", "")
        time_display = ts_str[11:19] if len(ts_str) >= 19 else time.strftime("%H:%M:%S")

        turns.append({
            "time": time_display,
            "prompt": prompt_text,
            "model": clean_ascii(model_display),
            "model_tier": model_tier,
            "in_tokens": t_in,
            "out_tokens": t_out,
            "total_tokens": total_tok,
            "wh": wh,
            "ml": ml
        })

    return turns

def build_rich_bar(ratio, width=10):
    ratio = min(max(ratio, 0.0), 1.0)
    filled = int(ratio * width)
    unfilled = width - filled
    pct = ratio * 100.0
    
    col = "green" if ratio < 0.40 else ("yellow" if ratio < 0.75 else "red")
    t = Text()
    t.append("[" + ("#" * filled), style=f"bold {col}")
    t.append(("-" * unfilled) + "] ", style="dim")
    t.append(f"{pct:4.1f}%", style=f"bold {col}")
    return t

def render_ascii_bar(ratio, width=10):
    ratio = min(max(ratio, 0.0), 1.0)
    filled = int(ratio * width)
    unfilled = width - filled
    pct = ratio * 100.0
    return f"[{'#' * filled}{'-' * unfilled}] {pct:4.1f}%"

def display_dashboard(turns, quotas, conv_id=""):
    if not turns:
        print("Aucune requete enregistree dans la session active.")
        return

    last = turns[-1]

    if RICH_AVAILABLE:
        # En-tete
        title_text = Text()
        title_text.append("SHOPLOC ", style="bold white")
        title_text.append("| ", style="dim")
        title_text.append("SUIVI DES TOKENS, ROUTAGE LLM & GREEN FINOPS", style="bold cyan")
        
        sub_info = f"Session : {conv_id[:16]}... | {time.strftime('%H:%M:%S')}"
        console.print(Panel(title_text, subtitle=sub_info, style="cyan", box=box.ROUNDED))

        # 1. Quotas & Bilan Ecologique (Jour & Semaine)
        quota_table = Table(box=box.ROUNDED, expand=True, title="[bold cyan]1. Quotas & Bilan Ecologique Global[/bold cyan]")
        quota_table.add_column("Periode", style="bold white")
        quota_table.add_column("Jauge d'Utilisation")
        quota_table.add_column("Tokens Consommes", justify="right", style="bold white")
        quota_table.add_column("Energie", justify="right", style="yellow")
        quota_table.add_column("Eau", justify="right", style="blue")

        j_bar = build_rich_bar(quotas["today_ratio"], width=10)
        w_bar = build_rich_bar(quotas["week_ratio"], width=10)

        quota_table.add_row(
            "Jour (24h)",
            j_bar,
            f"{quotas['today_total']:,} / {quotas['today_quota']:,}",
            f"{quotas['today_wh']:.1f} Wh",
            f"{quotas['today_ml']:.1f} mL"
        )
        quota_table.add_row(
            "Semaine (7j)",
            w_bar,
            f"{quotas['week_total']:,} / {quotas['week_quota']:,}",
            f"{quotas['week_wh']:.1f} Wh",
            f"{quotas['week_ml']:.1f} mL"
        )
        console.print(quota_table)

        # 2. Derniere Requete en Direct (Carte Lisible)
        led_sec = int((last["wh"] / 10.0) * 3600)
        led_display = f"{led_sec} sec" if led_sec < 60 else f"{led_sec // 60} min {led_sec % 60} sec"
        gorgees = last["ml"] / 25.0

        live_text = Text()
        live_text.append("Heure    : ", style="dim")
        live_text.append(f"{last['time']}   ", style="bold white")
        live_text.append("|  LLM Utilise : ", style="dim")
        live_text.append(f"{last['model']}\n", style="bold green")

        live_text.append("Requete  : ", style="dim")
        live_text.append(f"\"{last['prompt']}\"\n", style="white")

        live_text.append("Tokens   : ", style="dim")
        live_text.append(f"Entree: {last['in_tokens']:,}  |  Sortie: {last['out_tokens']:,}  |  ", style="dim cyan")
        live_text.append(f"Total Requete: {last['total_tokens']:,} tokens\n", style="bold cyan")

        live_text.append("Green AI : ", style="dim")
        live_text.append(f"{last['wh']:.2f} Wh ", style="bold yellow")
        live_text.append(f"(equiv. {led_display} ampoule LED 10W)  |  ", style="dim yellow")
        live_text.append(f"{last['ml']:.1f} mL d'eau ", style="bold blue")
        live_text.append(f"(equiv. ~{gorgees:.1f} gorgee(s))", style="dim blue")

        console.print(Panel(
            live_text,
            title="[bold cyan]2. Derniere Requete en Direct[/bold cyan]",
            box=box.ROUNDED,
            style="white"
        ))

        # 3. Historique Recent des Requetes
        if len(turns) > 1:
            hist_table = Table(box=box.ROUNDED, expand=True, title="[bold cyan]3. Historique Recent des Requetes[/bold cyan]")
            hist_table.add_column("Heure", style="dim", justify="center", width=8)
            hist_table.add_column("LLM", style="green", width=12)
            hist_table.add_column("Tokens", justify="right", style="cyan", width=10)
            hist_table.add_column("Energie", justify="right", style="yellow", width=9)
            hist_table.add_column("Eau", justify="right", style="blue", width=8)
            hist_table.add_column("Requete Utilisateur", style="white", ratio=1)

            for t in turns[-5:-1]:
                llm_short = t["model"]
                if "Flash" in llm_short:
                    llm_short = "Gemini Flash"
                elif "Pro" in llm_short:
                    llm_short = "Gemini Pro"
                elif "Lite" in llm_short:
                    llm_short = "Flash Lite"

                prompt_s = t["prompt"]
                if len(prompt_s) > 35:
                    prompt_s = prompt_s[:32] + "..."

                hist_table.add_row(
                    t["time"],
                    llm_short,
                    f"{t['total_tokens']:,}",
                    f"{t['wh']:.2f} Wh",
                    f"{t['ml']:.1f} mL",
                    prompt_s
                )
            console.print(hist_table)

    else:
        print("=" * 72)
        print("  SHOPLOC FINOPS & GREEN AI TRACKER")
        print("=" * 72)
        print(f"  Quota Jour    : {render_ascii_bar(quotas['today_ratio'])} ({quotas['today_total']:,} / {quotas['today_quota']:,} tok)")
        print(f"  Quota Semaine : {render_ascii_bar(quotas['week_ratio'])} ({quotas['week_total']:,} / {quotas['week_quota']:,} tok)")
        print(f"  Conso Jour    : {quotas['today_wh']:.2f} Wh | {quotas['today_ml']:.1f} mL d'eau")
        print("-" * 72)
        print("DERNIERE REQUETE :")
        print(f"  Heure   : {last['time']}")
        print(f"  LLM     : {last['model']}")
        print(f"  Prompt  : \"{last['prompt']}\"")
        print(f"  Tokens  : In: {last['in_tokens']:,} | Out: {last['out_tokens']:,} | Total: {last['total_tokens']:,}")
        print(f"  Energie : {last['wh']:.2f} Wh (equiv. {(last['wh']/10.0)*3600:.0f}s ampoule LED 10W)")
        print(f"  Eau     : {last['ml']:.1f} mL (equiv. {last['ml']/25.0:.1f} gorgees)")
        print("=" * 72)

def run_live_watch(file_path):
    print("Demarrage du moniteur en direct ShopLoc (Ctrl+C pour quitter)...")
    last_turn_count = -1
    last_file_size = -1

    try:
        while True:
            time.sleep(1.5)
            if not os.path.isfile(file_path):
                continue
            cur_size = os.path.getsize(file_path)
            if cur_size != last_file_size:
                last_file_size = cur_size
                turns = extract_turns_from_transcript(file_path)
                if len(turns) != last_turn_count:
                    last_turn_count = len(turns)
                    quotas = compute_quotas_all_sessions()
                    conv_id = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(file_path))))
                    if RICH_AVAILABLE:
                        console.clear()
                    else:
                        os.system("cls" if os.name == "nt" else "clear")
                    display_dashboard(turns, quotas, conv_id)
    except KeyboardInterrupt:
        print("\nArret du moniteur.")

def run_stream_log(file_path):
    print("Mode flux continu active (Ctrl+C pour quitter)...")
    last_seen_count = 0
    try:
        while True:
            time.sleep(1.5)
            if not os.path.isfile(file_path):
                continue
            turns = extract_turns_from_transcript(file_path)
            if len(turns) > last_seen_count:
                quotas = compute_quotas_all_sessions()
                for t in turns[last_seen_count:]:
                    print(f"[{t['time']}] LLM: {t['model']}")
                    print(f"         Prompt : \"{t['prompt']}\"")
                    print(f"         Tokens : In {t['in_tokens']:,} / Out {t['out_tokens']:,} (Total: {t['total_tokens']:,})")
                    print(f"         Impact : {t['wh']:.2f} Wh | {t['ml']:.1f} mL d'eau")
                    print(f"         Quotas : Jour {quotas['today_total']:,} tok ({quotas['today_ratio']*100:.1f}%) | Semaine {quotas['week_total']:,} tok ({quotas['week_ratio']*100:.1f}%)")
                    print("-" * 72)
                last_seen_count = len(turns)
    except KeyboardInterrupt:
        print("\nArret du mode flux continu.")

def main():
    tf = find_latest_transcript()
    if not tf:
        print("[ERREUR] Aucun journal de session Antigravity detecte.")
        sys.exit(1)

    conv_id = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(tf))))
    args = sys.argv[1:]

    if "--stream" in args:
        run_stream_log(tf)
    elif "--watch" in args:
        turns = extract_turns_from_transcript(tf)
        quotas = compute_quotas_all_sessions()
        if RICH_AVAILABLE:
            console.clear()
        else:
            os.system("cls" if os.name == "nt" else "clear")
        display_dashboard(turns, quotas, conv_id)
        run_live_watch(tf)
    else:
        turns = extract_turns_from_transcript(tf)
        quotas = compute_quotas_all_sessions()
        display_dashboard(turns, quotas, conv_id)

if __name__ == "__main__":
    main()

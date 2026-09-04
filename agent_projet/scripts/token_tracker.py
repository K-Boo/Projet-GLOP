import os
import sys
import glob
import json
import time

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.layout import Layout
    from rich.text import Text
    from rich import box
    RICH_AVAILABLE = True
    console = Console()
except ImportError:
    RICH_AVAILABLE = False
    console = None

def find_latest_transcript():
    user_home = os.path.expanduser("~")
    base_dir = os.path.join(user_home, ".gemini", "antigravity", "brain")
    pattern = os.path.join(base_dir, "*", ".system_generated", "logs", "transcript.jsonl")
    transcripts = glob.glob(pattern)
    if not transcripts:
        return None
    transcripts.sort(key=os.path.getmtime, reverse=True)
    return transcripts[0]

def parse_transcript_data(file_path):
    if not os.path.isfile(file_path):
        return None

    steps = []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                steps.append(json.loads(line))
            except Exception:
                continue

    if not steps:
        return None

    # Extraction des metriques globales
    steps_count = len(steps)
    user_messages = sum(1 for s in steps if s.get("type") == "USER_INPUT")
    model_responses = sum(1 for s in steps if s.get("type") == "PLANNER_RESPONSE")
    
    total_in_chars = sum(len(s.get("content") or "") for s in steps if s.get("type") == "USER_INPUT")
    total_out_chars = sum(len(s.get("content") or "") + len(s.get("thinking") or "") for s in steps if s.get("type") == "PLANNER_RESPONSE")
    
    total_in_tokens = total_in_chars // 4
    total_out_tokens = total_out_chars // 4
    total_session_tokens = total_in_tokens + total_out_tokens

    # Repartition des outils
    tools_breakdown = {}
    subagents_invoked = []
    heavy_calls = []

    for s in steps:
        tool_calls = s.get("tool_calls") or []
        for tc in tool_calls:
            tname = tc.get("name") or "unknown"
            tools_breakdown[tname] = tools_breakdown.get(tname, 0) + 1
            args = tc.get("args") or {}
            if tname == "invoke_subagent":
                subs = args.get("Subagents", [])
                for sub in subs:
                    subagents_invoked.append({
                        "role": sub.get("Role", "Inconnu"),
                        "model": sub.get("Model", "inherit")
                    })
        content = s.get("content") or ""
        if len(content) > 4000 and s.get("type") == "GENERIC":
            heavy_calls.append(len(content))

    # Analyse du dernier tour
    last_user_idx = -1
    for i in range(len(steps) - 1, -1, -1):
        if steps[i].get("type") == "USER_INPUT":
            last_user_idx = i
            break

    last_turn_info = None
    if last_user_idx != -1:
        u_step = steps[last_user_idx]
        u_content = u_step.get("content") or ""
        clean_prompt = u_content
        if "<USER_REQUEST>" in clean_prompt and "</USER_REQUEST>" in clean_prompt:
            clean_prompt = clean_prompt.split("<USER_REQUEST>")[1].split("</USER_REQUEST>")[0].strip()
        clean_prompt = clean_prompt.replace("\n", " ").strip()
        if len(clean_prompt) > 85:
            clean_prompt = clean_prompt[:82] + "..."

        turn_in_chars = len(u_content)
        turn_out_chars = 0
        turn_tools = {}

        for step in steps[last_user_idx + 1:]:
            stype = step.get("type", "")
            cnt = step.get("content") or ""
            thk = step.get("thinking") or ""
            tcalls = step.get("tool_calls") or []
            if stype == "PLANNER_RESPONSE":
                turn_out_chars += len(cnt) + len(thk)
            elif stype == "GENERIC":
                turn_in_chars += len(cnt)
            for tc in tcalls:
                name = tc.get("name") or "unknown"
                turn_tools[name] = turn_tools.get(name, 0) + 1

        t_in_tokens = turn_in_chars // 4
        t_out_tokens = turn_out_chars // 4
        t_total_tokens = t_in_tokens + t_out_tokens

        last_turn_info = {
            "prompt": clean_prompt,
            "in_tokens": t_in_tokens,
            "out_tokens": t_out_tokens,
            "total_tokens": t_total_tokens,
            "tools": turn_tools,
            "tools_count": sum(turn_tools.values())
        }

    conv_id = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(file_path))))

    return {
        "conv_id": conv_id,
        "file_path": file_path,
        "steps_count": steps_count,
        "user_messages": user_messages,
        "model_responses": model_responses,
        "total_in_tokens": total_in_tokens,
        "total_out_tokens": total_out_tokens,
        "total_session_tokens": total_session_tokens,
        "tools_breakdown": tools_breakdown,
        "subagents_invoked": subagents_invoked,
        "heavy_calls_count": len(heavy_calls),
        "last_turn": last_turn_info
    }

def render_gauge(value, max_value, width=28):
    ratio = min(max(value / max_value, 0.0), 1.0)
    filled = int(ratio * width)
    unfilled = width - filled
    percent = ratio * 100
    
    if ratio < 0.25:
        color = "green"
    elif ratio < 0.60:
        color = "yellow"
    else:
        color = "red"

    bar = f"[{color}]{'#' * filled}[/{color}][dim]{'-' * unfilled}[/dim] {percent:>4.1f}%"
    return bar

def display_rich_dashboard(data):
    if not console:
        return

    conv_id = data["conv_id"]
    steps = data["steps_count"]
    tot_tokens = data["total_session_tokens"]
    last_turn = data["last_turn"]

    # 1. Header
    header_text = Text()
    header_text.append("SHOPLOC ", style="bold white")
    header_text.append("| ", style="dim")
    header_text.append("MONITEUR FINOPS & TABLEAU DE BORD DE CONSOMMATION EN DIRECT", style="bold cyan")
    header_panel = Panel(
        header_text,
        subtitle=f"Master 2 MIAGE (UE GLOP) - Session : {conv_id} - {time.strftime('%H:%M:%S')}",
        style="cyan",
        box=box.ROUNDED
    )
    console.print(header_panel)

    # 2. Table Derniere Requete (Live Turn)
    if last_turn:
        turn_table = Table(box=box.ROUNDED, expand=True, title="[bold cyan]1. Mesure de la Derniere Requete en Direct[/bold cyan]")
        turn_table.add_column("Requete Utilisateur", style="white", ratio=3)
        turn_table.add_column("Appels d'Outils", style="yellow", justify="center", ratio=2)
        turn_table.add_column("Entree (In)", style="green", justify="right", ratio=1)
        turn_table.add_column("Sortie (Out)", style="magenta", justify="right", ratio=1)
        turn_table.add_column("Total Tour", style="bold cyan", justify="right", ratio=1)

        tools_str = f"{last_turn['tools_count']} appel(s)"
        if last_turn['tools']:
            tools_str += "\n" + "\n".join(f"{k} x{v}" for k, v in list(last_turn['tools'].items())[:3])

        turn_table.add_row(
            f"\"{last_turn['prompt']}\"",
            tools_str,
            f"~{last_turn['in_tokens']:,}",
            f"~{last_turn['out_tokens']:,}",
            f"~{last_turn['total_tokens']:,}"
        )
        console.print(turn_table)

    # 3. Tables Session Globale & Outils
    grid = Table.grid(expand=True)
    grid.add_column(ratio=1)
    grid.add_column(ratio=1)

    # Table Metriques Session
    sess_table = Table(box=box.ROUNDED, expand=True, title="[bold cyan]2. Cumul & Contexte de la Session[/bold cyan]")
    sess_table.add_column("Indicateur", style="dim white")
    sess_table.add_column("Valeur Mesuree", style="bold white", justify="right")

    sess_table.add_row("Etapes Enregistrees", f"{steps} etapes")
    sess_table.add_row("Messages Utilisateur", f"{data['user_messages']}")
    sess_table.add_row("Reponses Modele", f"{data['model_responses']}")
    sess_table.add_row("Jetons Entree Cumules", f"~{data['total_in_tokens']:,}")
    sess_table.add_row("Jetons Sortie Cumules", f"~{data['total_out_tokens']:,}")
    sess_table.add_row("Charge Contexte (1M)", render_gauge(tot_tokens, 1000000, width=18))

    # Table Outils
    tool_table = Table(box=box.ROUNDED, expand=True, title="[bold cyan]3. Outils les Plus Sollicites[/bold cyan]")
    tool_table.add_column("Nom de l'Outil", style="yellow")
    tool_table.add_column("Appels", justify="right", style="bold white")
    tool_table.add_column("Part", justify="right", style="dim green")

    tot_tools = sum(data["tools_breakdown"].values()) or 1
    for tname, cnt in sorted(data["tools_breakdown"].items(), key=lambda x: x[1], reverse=True)[:5]:
        pct = (cnt / tot_tools) * 100
        tool_table.add_row(tname, f"{cnt}", f"{pct:4.1f}%")

    grid.add_row(sess_table, tool_table)
    console.print(grid)

    # 4. Panel Recommandations FinOps
    recs = []
    if steps > 25:
        recs.append("[bold red]ATTENTION QUOTA :[/bold red] Cette session a depasse 25 etapes. Chaque requete reinjecte l'ensemble de l'historique. Cloturez la session pour restaurer un cout minimal (1 Session = 1 Tache).")
    if data["heavy_calls_count"] > 0:
        recs.append(f"[bold yellow]AVERTISSEMENT FLUX :[/bold yellow] {data['heavy_calls_count']} appel(s) volumineux detecte(s). Utilisez le filtrage grep ou des limites de lignes pour alleger le contexte.")
    if not data["subagents_invoked"]:
        recs.append("[bold cyan]CONSEIL ARCHITECTURE :[/bold cyan] Invoquez des sous-agents avec 'flash' ou 'flash_lite' pour reduire de 70% la charge de raisonnement du modele principal.")

    if not recs:
        recs_text = "[bold green]Statut Excellent :[/bold green] Consommation sobre, session propre et respect rigoureux de la frugalite agentique."
    else:
        recs_text = "\n".join(f"* {r}" for r in recs)

    rec_panel = Panel(
        recs_text,
        title="[bold yellow]4. Diagnostic & Recommandations FinOps[/bold yellow]",
        box=box.ROUNDED,
        style="white"
    )
    console.print(rec_panel)

def display_ascii_dashboard(data):
    print("=" * 70)
    print(f"  SHOPLOC FINOPS MONITOR — SESSION : {data['conv_id']}")
    print("=" * 70)
    lt = data["last_turn"]
    if lt:
        print("DERNIERE REQUETE EN DIRECT :")
        print(f"  Prompt       : \"{lt['prompt']}\"")
        print(f"  Appels outils: {lt['tools_count']} appel(s)")
        print(f"  Jetons Entree: ~{lt['in_tokens']:,} tokens | Sortie: ~{lt['out_tokens']:,} tokens")
        print(f"  Total Requete: ~{lt['total_tokens']:,} tokens")
        print("-" * 70)
    print("CUMUL DE LA SESSION :")
    print(f"  Etapes       : {data['steps_count']} | Messages: {data['user_messages']}")
    print(f"  Total Jetons : ~{data['total_session_tokens']:,} tokens")
    print("=" * 70)

def render_dashboard(file_path):
    data = parse_transcript_data(file_path)
    if not data:
        print("Impossible d'extraire les donnees de session.")
        return
    if RICH_AVAILABLE:
        display_rich_dashboard(data)
    else:
        display_ascii_dashboard(data)

def watch_live(file_path):
    if RICH_AVAILABLE:
        console.clear()
    else:
        os.system("cls" if os.name == "nt" else "clear")

    render_dashboard(file_path)
    last_size = os.path.getsize(file_path) if os.path.isfile(file_path) else 0

    try:
        while True:
            time.sleep(1.2)
            if os.path.isfile(file_path):
                cur_size = os.path.getsize(file_path)
                if cur_size != last_size:
                    last_size = cur_size
                    if RICH_AVAILABLE:
                        console.clear()
                    else:
                        os.system("cls" if os.name == "nt" else "clear")
                    render_dashboard(file_path)
    except KeyboardInterrupt:
        print("\nArret du moniteur FinOps.")

def main():
    args = sys.argv[1:]
    path = find_latest_transcript()
    if not path:
        print("Aucun fichier journal de session Antigravity detecte.")
        sys.exit(1)

    if "--watch" in args:
        watch_live(path)
    else:
        render_dashboard(path)

if __name__ == "__main__":
    main()

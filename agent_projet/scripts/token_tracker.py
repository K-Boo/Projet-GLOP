import os
import sys
import glob
import json
import time

def find_latest_transcript():
    user_home = os.path.expanduser("~")
    base_dir = os.path.join(user_home, ".gemini", "antigravity", "brain")
    pattern = os.path.join(base_dir, "*", ".system_generated", "logs", "transcript.jsonl")
    transcripts = glob.glob(pattern)
    if not transcripts:
        return None
    transcripts.sort(key=os.path.getmtime, reverse=True)
    return transcripts[0]

def analyze_last_turn(file_path):
    if not os.path.isfile(file_path):
        print(f"Erreur : Le fichier journal n'existe pas : {file_path}")
        return

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
        print("Aucune etape enregistree dans le journal.")
        return

    # Identifier la derniere requete utilisateur
    last_user_idx = -1
    for i in range(len(steps) - 1, -1, -1):
        if steps[i].get("type") == "USER_INPUT":
            last_user_idx = i
            break

    if last_user_idx == -1:
        print("Aucun message utilisateur detecte dans le journal.")
        return

    user_step = steps[last_user_idx]
    user_content = user_step.get("content") or ""
    # Nettoyage balise USER_REQUEST si presente
    clean_prompt = user_content
    if "<USER_REQUEST>" in clean_prompt and "</USER_REQUEST>" in clean_prompt:
        clean_prompt = clean_prompt.split("<USER_REQUEST>")[1].split("</USER_REQUEST>")[0].strip()
    clean_prompt = clean_prompt.replace("\n", " ")[:90]

    turn_input_chars = len(user_content)
    turn_output_chars = 0
    tool_calls_breakdown = {}
    tool_calls_total = 0

    for step in steps[last_user_idx + 1:]:
        step_type = step.get("type", "")
        content = step.get("content") or ""
        thinking = step.get("thinking") or ""
        tool_calls = step.get("tool_calls") or []

        if step_type == "PLANNER_RESPONSE":
            turn_output_chars += len(content) + len(thinking)
        elif step_type == "GENERIC":
            turn_input_chars += len(content)

        for tc in tool_calls:
            tool_calls_total += 1
            tname = tc.get("name") or "unknown"
            tool_calls_breakdown[tname] = tool_calls_breakdown.get(tname, 0) + 1

    est_turn_in = turn_input_chars // 4
    est_turn_out = turn_output_chars // 4
    est_turn_total = est_turn_in + est_turn_out

    # Cumul total session
    tot_in = sum(len(s.get("content") or "") for s in steps if s.get("type") == "USER_INPUT") // 4
    tot_out = sum(len(s.get("content") or "") + len(s.get("thinking") or "") for s in steps if s.get("type") == "PLANNER_RESPONSE") // 4

    print("=" * 68)
    print("  CONSOMMATION DE JETONS EN DIRECT - DERNIERE REQUETE")
    print("=" * 68)
    print(f"Requete utilisateur  : \"{clean_prompt}\"")
    print(f"Appels d'outils      : {tool_calls_total} appel(s)")
    if tool_calls_breakdown:
        details = ", ".join(f"{k} x{v}" for k, v in tool_calls_breakdown.items())
        print(f"  * Details outils   : {details}")
    print("-" * 68)
    print("MESURE DE LA REQUETE :")
    print(f"  - Jetons d'entree tour (donnees/outils) : ~{est_turn_in:,} tokens")
    print(f"  - Jetons de sortie tour (reponse/code)  : ~{est_turn_out:,} tokens")
    print(f"  - Total pour cette requete              : ~{est_turn_total:,} tokens")
    print("-" * 68)
    print(f"CUMUL TOTAL DE LA SESSION : ~{tot_in + tot_out:,} tokens ({len(steps)} etapes)")
    if len(steps) > 25:
        print("  [!] Conseil FinOps : Pensez a cloturer la session pour eviter l'accumulation du contexte.")
    print("=" * 68)

def analyze_transcript(file_path):
    if not os.path.isfile(file_path):
        print(f"Erreur : Le fichier journal n'existe pas : {file_path}")
        return

    steps_count = 0
    user_messages = 0
    model_responses = 0
    tool_calls_count = 0
    tools_breakdown = {}
    subagents_invoked = []
    
    total_input_chars = 0
    total_output_chars = 0
    heavy_commands = []

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
            except Exception:
                continue

            steps_count += 1
            step_type = data.get("type", "")
            content = data.get("content") or ""
            thinking = data.get("thinking") or ""
            tool_calls = data.get("tool_calls") or []

            if step_type == "USER_INPUT":
                user_messages += 1
                total_input_chars += len(content)
            elif step_type == "PLANNER_RESPONSE":
                model_responses += 1
                total_output_chars += len(content) + len(thinking)

            for call in tool_calls:
                tool_calls_count += 1
                name = call.get("name") or "unknown"
                tools_breakdown[name] = tools_breakdown.get(name, 0) + 1
                
                args = call.get("args") or {}
                if name == "invoke_subagent":
                    subs = args.get("Subagents", [])
                    for s in subs:
                        subagents_invoked.append({
                            "role": s.get("Role", "Inconnu"),
                            "model": s.get("Model", "inherit"),
                            "type": s.get("TypeName", "standard")
                        })
                elif name == "run_command":
                    cmd = args.get("CommandLine", "")
                    if len(content) > 4000:
                        heavy_commands.append((cmd[:50], len(content)))

    est_input_tokens = total_input_chars // 4
    est_output_tokens = total_output_chars // 4
    total_est_tokens = est_input_tokens + est_output_tokens

    print("=" * 68)
    print("  RAPPORT D'AUDIT GLOBAL DE LA SESSION - FINOPS")
    print("=" * 68)
    conv_id = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(file_path))))
    print(f"Session ID           : {conv_id}")
    print(f"Nombre d'etapes      : {steps_count}")
    print(f"Messages utilisateur : {user_messages}")
    print(f"Reponses modele      : {model_responses}")
    print(f"Appels d'outils      : {tool_calls_count}")
    print("-" * 68)
    print("REPARTITION DE LA CONSOMMATION ESTIMEE :")
    print(f"  - Jetons d'entree (prompt & historique) : ~{est_input_tokens:,} tokens ({total_input_chars:,} caracteres)")
    print(f"  - Jetons de sortie (generation & code)  : ~{est_output_tokens:,} tokens ({total_output_chars:,} caracteres)")
    print(f"  - Total cumule estime                   : ~{total_est_tokens:,} tokens")
    print("-" * 68)
    print("REPARTITION DES OUTILS LES PLUS SOLLICITES :")
    for tool_name, count in sorted(tools_breakdown.items(), key=lambda x: x[1], reverse=True)[:6]:
        print(f"  * {tool_name:<26} : {count:>3} appels")
    
    if subagents_invoked:
        print("-" * 68)
        print("SOUS-AGENTS INVOQUES & NIVEAUX DE MODELES :")
        for sa in subagents_invoked:
            print(f"  * Role: {sa['role']:<24} | Modele: {sa['model']:<10} | Type: {sa['type']}")
    
    print("-" * 68)
    print("RECOMMANDATIONS D'OPTIMISATION DE QUOTA GEMINI PRO :")
    recs = []
    if steps_count > 25:
        recs.append("ATTENTION : La session depasse 25 etapes. Cloturez la session pour eviter le cout quadratique d'historique (Regle : 1 Session = 1 Tache).")
    if heavy_commands:
        recs.append(f"ALERTE : {len(heavy_commands)} commande(s) ont genere un volume important de sortie (>4000 caracteres). Pensez a filtrer via grep ou --silent.")
    if not subagents_invoked:
        recs.append("CONSEIL : Utilisez les sous-agents avec 'flash' ou 'flash_lite' pour isoler les taches subalternes et reduire de 70% la charge de contexte.")
    
    if not recs:
        print("  -> Excellent : Consommation sobre et conforme aux directives d'efficience.")
    else:
        for r in recs:
            print(f"  [!] {r}")

    print("=" * 68)

def watch_live(file_path):
    print(f"Mode surveillance active (Watch Mode) sur : {file_path}")
    print("En attente de nouvelles requetes... (Ctrl+C pour arreter)")
    last_size = 0
    if os.path.isfile(file_path):
        last_size = os.path.getsize(file_path)

    try:
        while True:
            time.sleep(1.5)
            if os.path.isfile(file_path):
                cur_size = os.path.getsize(file_path)
                if cur_size != last_size:
                    last_size = cur_size
                    # Si une nouvelle reponse complete a ete ecrite
                    analyze_last_turn(file_path)
    except KeyboardInterrupt:
        print("\nArret de la surveillance en direct.")

def main():
    args = sys.argv[1:]
    path = find_latest_transcript()
    if not path:
        print("Aucun fichier journal de session Antigravity detecte.")
        sys.exit(1)

    if "--watch" in args:
        watch_live(path)
    elif "--last" in args:
        analyze_last_turn(path)
    else:
        analyze_transcript(path)

if __name__ == "__main__":
    main()

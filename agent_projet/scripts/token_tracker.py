import os
import sys
import glob
import json

def find_latest_transcript():
    user_home = os.path.expanduser("~")
    base_dir = os.path.join(user_home, ".gemini", "antigravity", "brain")
    pattern = os.path.join(base_dir, "*", ".system_generated", "logs", "transcript.jsonl")
    transcripts = glob.glob(pattern)
    if not transcripts:
        return None
    transcripts.sort(key=os.path.getmtime, reverse=True)
    return transcripts[0]

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

    # Approximation 1 token ~= 4 characteres
    est_input_tokens = total_input_chars // 4
    est_output_tokens = total_output_chars // 4
    total_est_tokens = est_input_tokens + est_output_tokens

    print("=" * 66)
    print("  RAPPORT D'AUDIT DE CONSOMMATION DE JETONS & GESTION FINOPS")
    print("=" * 66)
    conv_id = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(file_path))))
    print(f"Session ID           : {conv_id}")
    print(f"Fichier journal      : {file_path}")
    print(f"Nombre d'etapes      : {steps_count}")
    print(f"Messages utilisateur : {user_messages}")
    print(f"Reponses modele      : {model_responses}")
    print(f"Appels d'outils      : {tool_calls_count}")
    print("-" * 66)
    print("REPARTITION DE LA CONSOMMATION ESTIMEE :")
    print(f"  - Jetons d'entree (prompt & historique) : ~{est_input_tokens:,} tokens ({total_input_chars:,} caracteres)")
    print(f"  - Jetons de sortie (generation & code)  : ~{est_output_tokens:,} tokens ({total_output_chars:,} caracteres)")
    print(f"  - Total cumule estime                   : ~{total_est_tokens:,} tokens")
    print("-" * 66)
    print("REPARTITION DES OUTILS LES PLUS SOLLICITES :")
    for tool_name, count in sorted(tools_breakdown.items(), key=lambda x: x[1], reverse=True)[:6]:
        print(f"  * {tool_name:<26} : {count:>3} appels")
    
    if subagents_invoked:
        print("-" * 66)
        print("SOUS-AGENTS INVOQUES & NIVEAUX DE MODELES :")
        for sa in subagents_invoked:
            print(f"  * Role: {sa['role']:<24} | Modele: {sa['model']:<10} | Type: {sa['type']}")
    
    print("-" * 66)
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

    print("=" * 66)

def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = find_latest_transcript()
        if not path:
            print("Aucun fichier journal de session Antigravity detecte.")
            sys.exit(1)
    analyze_transcript(path)

if __name__ == "__main__":
    main()

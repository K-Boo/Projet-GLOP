import sys
import os
import time
import webbrowser
import warnings

# Force UTF-8 stdout/stderr on Windows to handle third-party library banners
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Suppress database schema warnings from phoenix dependencies
warnings.filterwarnings("ignore")

def main():
    print("=" * 65, flush=True)
    print("  SHOPLOC OBSERVABILITE & TRACKING DE TOKENS (ARIZE PHOENIX)", flush=True)
    print("=" * 65, flush=True)
    print("  Technologie : Arize Phoenix (Open Source, 100% Local)", flush=True)
    print("  Port local  : 6006", flush=True)
    print("  URL Web     : http://localhost:6006", flush=True)
    print("  OTLP Traces : http://localhost:6006/v1/traces", flush=True)
    print("=" * 65, flush=True)
    print("\n[1/2] Demarrage du serveur Phoenix en local...", flush=True)

    try:
        import phoenix as px
    except ImportError:
        print("[ERREUR] Le module 'phoenix' n'est pas installe.", flush=True)
        print("Veuillez executer : python agent_projet/scripts/setup_env.py", flush=True)
        sys.exit(1)

    os.environ["PHOENIX_PORT"] = "6006"
    os.environ["PHOENIX_HOST"] = "127.0.0.1"

    try:
        session = px.launch_app()
    except Exception as e:
        print(f"[ERREUR] Impossible de demarrer le serveur Phoenix : {e}", flush=True)
        sys.exit(1)
    
    server_url = getattr(session, "url", "http://localhost:6006/")
    print(f"[2/2] Serveur actif sur {server_url}", flush=True)
    print("      Ouverture automatique de l'interface web dans votre navigateur...", flush=True)
    
    time.sleep(1)
    try:
        webbrowser.open(server_url)
    except Exception:
        pass

    print("\n" + "=" * 65, flush=True)
    print("  TABLEAU DE BORD LOCAL PRET", flush=True)
    print("  - Visualisation des tokens d'entree/sortie", flush=True)
    print("  - Traces et spans de chaque requete LLM / Agent", flush=True)
    print("  - Metriques de latence et distribution des couts", flush=True)
    print("  - Stockage 100% en local (aucune cle API ni cloud requis)", flush=True)
    print("=" * 65, flush=True)
    print("\nAppuyez sur Ctrl+C dans cette fenetre pour arreter le serveur.\n", flush=True)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nArret du serveur Arize Phoenix...", flush=True)
        px.close_app()
        print("Serveur arrete proprement.", flush=True)

if __name__ == "__main__":
    main()

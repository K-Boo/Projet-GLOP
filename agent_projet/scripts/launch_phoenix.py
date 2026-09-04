import sys
import time
import webbrowser
import os

def main():
    print("=" * 65)
    print("  SHOPLOC OBSERVABILITE & TRACKING DE TOKENS (ARIZE PHOENIX)")
    print("=" * 65)
    print("  Technologie : Arize Phoenix (Open Source, 100% Local)")
    print("  Port local  : 6006")
    print("  URL Web     : http://localhost:6006")
    print("  OTLP Traces : http://localhost:6006/v1/traces")
    print("=" * 65)
    print("\n[1/2] Demarrage du serveur Phoenix en local...")

    try:
        import phoenix as px
    except ImportError:
        print("[ERREUR] Le module 'phoenix' n'est pas installe.")
        print("Veuillez executer : python agent_projet/scripts/setup_env.py")
        sys.exit(1)

    # Launch Arize Phoenix server on port 6006
    session = px.launch(port=6006, host="127.0.0.1")
    
    print("[2/2] Serveur actif sur http://localhost:6006")
    print("      Ouverture automatique de l'interface web dans votre navigateur...")
    
    time.sleep(1)
    try:
        webbrowser.open("http://localhost:6006")
    except Exception:
        pass

    print("\n" + "=" * 65)
    print("  TABLEAU DE BORD LOCAL PRET")
    print("  - Visualisation des tokens d'entree/sortie")
    print("  - Traces et spans de chaque requete LLM / Agent")
    print("  - Metriques de latence et distribution des couts")
    print("  - Stockage 100% en local (aucune cle API ni cloud requis)")
    print("=" * 65)
    print("\nAppuyez sur Ctrl+C dans cette fenetre pour arreter le serveur.\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nArret du serveur Arize Phoenix...")
        px.close()
        print("Serveur arrete proprement.")

if __name__ == "__main__":
    main()

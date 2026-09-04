import os
import sys
import subprocess
import json

REQUIRED_PACKAGES = {
    "pymupdf": "pymupdf",
    "reportlab": "reportlab",
    "pypdf": "pypdf",
    "PIL": "pillow",
    "rich": "rich",
    "phoenix": "arize-phoenix"
}

SUBFOLDERS = [
    "01_Cadrage_Metier_R1",
    "02_Etude_Financiere_R3",
    "03_Architecture_Technique_R4_R5",
    "04_Presentations_Diaporamas",
    "05_Demonstrations_Videos"
]

def check_and_install_packages():
    print("[1/4] Verification des dependances Python...")
    missing = []
    for mod_name, pkg_name in REQUIRED_PACKAGES.items():
        try:
            __import__(mod_name)
        except ImportError:
            missing.append(pkg_name)
    
    if missing:
        print(f"  -> Installation des packages manquants : {missing}...")
        cmd = [sys.executable, "-m", "pip", "install"] + missing
        subprocess.check_call(cmd)
        print("  -> Packages installes avec succes.")
    else:
        print("  -> Toutes les dependances Python (y compris Arize Phoenix) sont operationnelles.")

def check_pdf_engine():
    print("[2/4] Verification du moteur de rendu PDF (Edge / Chromium)...")
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
    ]
    found = None
    for c in candidates:
        if os.path.exists(c):
            found = c
            break
    
    if found:
        print(f"  -> Moteur headless detecte : {found}")
        return found
    else:
        print("  -> ATTENTION : Aucun binaire Edge/Chrome detecte sur les chemins standards.")
        return None

def check_and_setup_drive():
    print("[3/4] Verification et configuration de Google Drive...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
    local_cfg = os.path.join(repo_root, "config.local.json")
    
    drive_path = None
    
    # 1. Check local config if already exists
    if os.path.isfile(local_cfg):
        try:
            with open(local_cfg, "r", encoding="utf-8") as f:
                data = json.load(f)
                custom = data.get("drive_path")
                if custom and os.path.isdir(custom):
                    drive_path = custom
        except Exception:
            pass

    # 2. Check standard candidate paths
    if not drive_path:
        candidates = [
            r"G:\Mon Drive\Projet-GLOP",
            r"G:\My Drive\Projet-GLOP",
            r"G:\Drives partages\Projet-GLOP",
            r"D:\Mon Drive\Projet-GLOP",
            r"D:\My Drive\Projet-GLOP",
            os.path.expanduser(r"~\Google Drive\Projet-GLOP"),
            os.path.expanduser(r"~\Mon Drive\Projet-GLOP"),
            os.path.expanduser(r"~\My Drive\Projet-GLOP")
        ]
        for c in candidates:
            if os.path.isdir(c):
                drive_path = c
                break

    # 3. Check any drive letter containing Mon Drive / My Drive
    if not drive_path:
        for letter in "GDEFHCBA":
            for sub in ["Mon Drive", "My Drive"]:
                parent = os.path.join(f"{letter}:\\", sub)
                if os.path.isdir(parent):
                    # Propose creating Projet-GLOP inside it
                    target = os.path.join(parent, "Projet-GLOP")
                    os.makedirs(target, exist_ok=True)
                    drive_path = target
                    break
            if drive_path:
                break

    if drive_path and os.path.isdir(drive_path):
        print(f"  -> Dossier Google Drive detecte : {drive_path}")
        # Ensure all category subfolders exist
        for sub in SUBFOLDERS:
            sub_dir = os.path.join(drive_path, sub)
            os.makedirs(sub_dir, exist_ok=True)
        print(f"  -> Les {len(SUBFOLDERS)} sous-dossiers de livrables sont initialises.")
        
        # Save to config.local.json if not G:\ default
        if not drive_path.startswith(r"G:\Mon Drive\Projet-GLOP"):
            with open(local_cfg, "w", encoding="utf-8") as f:
                json.dump({"drive_path": drive_path}, f, indent=2)
            print(f"  -> Configuration locale sauvegardee dans {local_cfg}")
        return True
    else:
        print("  -> ATTENTION : Google Drive pour ordinateur n'a pas ete detecte.")
        print("     Installez 'Google Drive pour ordinateur', connectez votre compte,")
        print("     puis relancez ce script.")
        return False

def check_git_remote():
    print("[4/4] Verification du depot Git...")
    try:
        out = subprocess.check_output(["git", "remote", "-v"], text=True, stderr=subprocess.DEVNULL)
        if "K-Boo/Projet-GLOP" in out:
            print("  -> Depot distant origin 'K-Boo/Projet-GLOP' valide.")
            return True
        else:
            print(f"  -> Remote actuel :\n{out}")
            return True
    except Exception as e:
        print(f"  -> Erreur Git : {e}")
        return False

def main():
    print("=" * 60)
    print("  ALIGNEMENT AUTOMATIQUE DE L'ENVIRONNEMENT SHOPLOC GLOP")
    print("=" * 60)
    check_and_install_packages()
    check_pdf_engine()
    drive_ok = check_and_setup_drive()
    git_ok = check_git_remote()
    print("=" * 60)
    if drive_ok and git_ok:
        print("SUCCES : La machine est 100% conforme a la configuration d'equipe.")
    else:
        print("AVERTISSEMENT : Configuration partielle (voir alertes ci-dessus).")
    print("=" * 60)

if __name__ == "__main__":
    main()

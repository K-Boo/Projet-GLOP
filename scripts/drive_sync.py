import os
import shutil
import sys

# Category folders on Google Drive
CATEGORIES = {
    "cadrage": "01_Cadrage_Metier_R1",
    "finance": "02_Etude_Financiere_R3",
    "architecture": "03_Architecture_Technique_R4_R5",
    "slides": "04_Presentations_Diaporamas",
    "videos": "05_Demonstrations_Videos",
    "general": "00_Documents_Generaux"
}

def find_drive_root():
    # 1. Environment variable override
    env_path = os.environ.get("GLOP_DRIVE_DIR") or os.environ.get("GLOP_DRIVE_PATH")
    if env_path and os.path.isdir(env_path):
        return env_path

    # 2. Known standard paths for Google Drive Desktop on Windows/Mac/Linux
    candidates = [
        r"G:\Mon Drive\Projet-GLOP",
        r"G:\My Drive\Projet-GLOP",
        r"G:\Drives partags\Projet-GLOP",
        r"G:\Shared Drives\Projet-GLOP",
        r"D:\Mon Drive\Projet-GLOP",
        r"D:\My Drive\Projet-GLOP",
        os.path.expanduser(r"~\Google Drive\Projet-GLOP"),
        os.path.expanduser(r"~\Mon Drive\Projet-GLOP"),
        os.path.expanduser(r"~\My Drive\Projet-GLOP")
    ]

    for candidate in candidates:
        if os.path.isdir(candidate):
            return candidate

    # 3. Search for any mounted Google Drive letter containing Projet-GLOP
    for letter in "GDEFHCBA":
        for sub in ["Mon Drive", "My Drive"]:
            p = os.path.join(f"{letter}:\\", sub, "Projet-GLOP")
            if os.path.isdir(p):
                return p

    return None

def detect_category(file_path):
    filename = os.path.basename(file_path).lower()
    ext = os.path.splitext(filename)[1].lower()

    if ext in [".pptx", ".ppt", ".key"]:
        return CATEGORIES["slides"]
    if ext in [".mp4", ".mov", ".avi", ".mkv", ".webm"]:
        return CATEGORIES["videos"]
    if ext in [".xlsx", ".xls", ".csv"] or "financ" in filename or "r3" in filename:
        return CATEGORIES["finance"]
    if "archi" in filename or "r4" in filename or "r5" in filename or "c4" in filename:
        return CATEGORIES["architecture"]
    if "r1" in filename or "cadrage" in filename or "questionnaire" in filename:
        return CATEGORIES["cadrage"]

    if ext == ".pdf":
        return CATEGORIES["cadrage"]

    return CATEGORIES["general"]

def sync_to_drive(file_path, category=None):
    if not os.path.exists(file_path):
        print(f"[Drive Sync Error] Source file does not exist: {file_path}")
        return False

    drive_root = find_drive_root()
    if not drive_root:
        print("[Drive Sync Warning] Google Drive 'Projet-GLOP' folder not found on this machine.")
        print("Set the environment variable GLOP_DRIVE_DIR or install Google Drive for Desktop.")
        return False

    if not category:
        category = detect_category(file_path)

    target_dir = os.path.join(drive_root, category)
    os.makedirs(target_dir, exist_ok=True)

    dest_path = os.path.join(target_dir, os.path.basename(file_path))
    shutil.copy2(file_path, dest_path)
    print(f"[Drive Sync OK] Synchronized to Google Drive: {dest_path}")
    return dest_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python drive_sync.py <file_path> [category_folder]")
        sys.exit(1)

    src = sys.argv[1]
    cat = sys.argv[2] if len(sys.argv) > 2 else None
    sync_to_drive(src, cat)

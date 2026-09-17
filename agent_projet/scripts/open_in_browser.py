#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UTILITAIRE DE LANCEMENT NAVIGATEUR CHROME (open_in_browser.py)
Master 2 MIAGE — Universite de Lille — UE GLOP (2026-2027)

Ouvre directement n importe quel fichier HTML, rapport ou livrable dans Google Chrome
pour afficher le rendu graphique reel et non le code source brut.

Usage:
    python agent_projet/scripts/open_in_browser.py agent_projet/docs/NOUVEAUX_VISUELS_PASTEL.html
    python agent_projet/scripts/open_in_browser.py agent_projet/design/styleguide.html
    python agent_projet/scripts/open_in_browser.py --all
"""

import argparse
import json
import os
import subprocess
import sys


def get_chrome_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    config_file = os.path.join(project_root, "config.local.json")

    # 1. Verification dans config.local.json
    if os.path.exists(config_file):
        try:
            with open(config_file, "r", encoding="utf-8") as f:
                cfg = json.load(f)
                custom_path = cfg.get("default_browser_path")
                if custom_path and os.path.exists(custom_path):
                    return custom_path
        except Exception:
            pass

    # 2. Emplacements standards Google Chrome
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None


def open_file_in_chrome(file_path):
    chrome_bin = get_chrome_path()
    if not chrome_bin:
        print("[ERREUR] Google Chrome est introuvable sur le systeme.")
        sys.exit(1)

    abs_path = os.path.abspath(file_path)
    if not os.path.exists(abs_path):
        print(f"[ERREUR] Fichier introuvable : {abs_path}")
        sys.exit(1)

    # Conversion en URI locale
    file_uri = f"file:///{abs_path.replace(os.sep, '/')}"
    print(f"[ACTION] Lancement de Google Chrome pour le rendu de : {abs_path}")

    try:
        subprocess.Popen([chrome_bin, "--new-window", file_uri], shell=False)
        print(f"[SUCCES] Page ouverte dans une nouvelle fenetre Google Chrome : {file_uri}")
    except Exception as e:
        print(f"[ERREUR] Echec lors du lancement de Chrome : {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Ouvrir un fichier HTML dans Google Chrome")
    parser.add_argument("file", nargs="?", help="Chemin vers le fichier HTML a visualiser")
    parser.add_argument("--showcase", action="store_true", help="Ouvrir le showcase des nouveaux visuels pastel")
    parser.add_argument("--styleguide", action="store_true", help="Ouvrir le guide de style et nuancier")
    parser.add_argument("--gallery", action="store_true", help="Ouvrir la galerie des livrables")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    docs_dir = os.path.join(project_root, "agent_projet", "docs")
    design_dir = os.path.join(project_root, "agent_projet", "design")

    if args.showcase:
        open_file_in_chrome(os.path.join(docs_dir, "NOUVEAUX_VISUELS_PASTEL.html"))
    elif args.styleguide:
        open_file_in_chrome(os.path.join(design_dir, "styleguide.html"))
    elif args.gallery:
        open_file_in_chrome(os.path.join(docs_dir, "GALERIE_LIVRABLES.html"))
    elif args.file:
        open_file_in_chrome(args.file)
    else:
        # Par defaut, ouvrir le showcase des visuels
        open_file_in_chrome(os.path.join(docs_dir, "NOUVEAUX_VISUELS_PASTEL.html"))


if __name__ == "__main__":
    main()

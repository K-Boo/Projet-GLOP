#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXPORT VISUAL PNG — Moteur de conversion d'HTML/SVG en image PNG haute resolution
Master 2 MIAGE — Universite de Lille — UE GLOP (2026-2027)

Permet de convertir n'importe quel composant visuel HTML/SVG en image PNG
pour insertion directe dans les fichiers Markdown du Cahier des Charges.

Usage:
    python agent_projet/scripts/export_visual_png.py --component matrice_positionnement --output agent_projet/docs/01_Cadrage_Et_Cahier_Des_Charges_R1/figures/fig_1_1_matrice_positionnement.png
"""

import argparse
import os
import subprocess
import sys
import pymupdf


def find_edge_binary():
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium"
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return "msedge"


def export_html_to_png(html_content, output_png_path, dpi=200):
    output_png_path = os.path.abspath(output_png_path)
    os.makedirs(os.path.dirname(output_png_path), exist_ok=True)
    temp_pdf_path = output_png_path.replace(".png", "_temp.pdf")
    temp_html_path = output_png_path.replace(".png", "_temp.html")

    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    edge_bin = find_edge_binary()
    file_uri = f"file:///{temp_html_path.replace(os.sep, '/')}"
    cmd = [
        edge_bin,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={temp_pdf_path}",
        file_uri
    ]
    subprocess.run(cmd, check=True)

    # Conversion PDF -> PNG via PyMuPDF
    doc = pymupdf.open(temp_pdf_path)
    if len(doc) > 0:
        page = doc[0]
        pix = page.get_pixmap(dpi=dpi)
        pix.save(output_png_path)
    doc.close()

    # Nettoyage des fichiers temporaires
    for p in [temp_html_path, temp_pdf_path]:
        if os.path.exists(p):
            os.remove(p)

    if os.path.exists(output_png_path):
        size = os.path.getsize(output_png_path)
        print(f"[SUCCES] Image PNG generee : {output_png_path} ({size} octets)")
        return True
    return False


def main():
    parser = argparse.ArgumentParser(description="Export d'un composant HTML/SVG en PNG haute resolution")
    parser.add_argument("--component", "-c", required=True, help="Nom du composant dans agent_projet/templates/components/")
    parser.add_argument("--output", "-o", required=True, help="Chemin du fichier PNG de sortie")
    parser.add_argument("--dpi", type=int, default=200, help="Resolution DPI (defaut: 200)")

    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    agent_projet_dir = os.path.join(project_root, "agent_projet")
    comp_file = os.path.join(agent_projet_dir, "templates", "components", f"{args.component}.html")
    theme_css_file = os.path.join(agent_projet_dir, "design", "theme.css")

    if not os.path.exists(comp_file):
        print(f"[ERREUR] Composant introuvable : {comp_file}")
        sys.exit(1)

    with open(comp_file, "r", encoding="utf-8") as f:
        comp_content = f.read()

    theme_css = ""
    if os.path.exists(theme_css_file):
        with open(theme_css_file, "r", encoding="utf-8") as f:
            theme_css = f.read()

    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/latin-modern-web@1.0.0/style.css">
  <style>
    {theme_css}
    body {{
      margin: 0;
      padding: 16px;
      background: #FFFFFF;
      display: flex;
      justify-content: center;
      align-items: center;
    }}
    .diagram-container {{
      margin: 0 !important;
      width: 100%;
    }}
  </style>
</head>
<body>
  {comp_content}
</body>
</html>"""

    success = export_html_to_png(full_html, args.output, dpi=args.dpi)
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()

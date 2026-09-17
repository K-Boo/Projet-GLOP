#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MOTEUR DE GENERATION ET CAPTURE DE MAQUETTES UI (render_mockups.py)
Master 2 MIAGE — Universite de Lille — UE GLOP (2026-2027)

Compile les interfaces utilisateurs HTML/CSS (Pierre senior, Suzanne caisse, Marius admin)
en PDF vectoriel puis les convertit en captures d'ecran PNG haute resolution (200 DPI) via PyMuPDF.

Usage:
    python agent_projet/scripts/render_mockups.py --export-png
"""

import argparse
import os
import subprocess
import pymupdf

def find_edge_binary():
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium"
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return "chrome"

def main():
    parser = argparse.ArgumentParser(description="Moteur de capture PNG des maquettes d'interfaces ShopLoc")
    parser.add_argument("--export-png", action="store_true", help="Compiler et exporter les maquettes en PNG haute definition")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    agent_projet_dir = os.path.join(project_root, "agent_projet")
    templates_dir = os.path.join(agent_projet_dir, "templates", "components")
    design_dir = os.path.join(agent_projet_dir, "design")
    docs_dir = os.path.join(agent_projet_dir, "docs")
    mockups_output_dir = os.path.join(docs_dir, "mockups")
    os.makedirs(mockups_output_dir, exist_ok=True)

    wireframe_src = os.path.join(templates_dir, "ui_wireframe_card.html")
    theme_css = os.path.join(design_dir, "theme.css")
    temp_html = os.path.join(mockups_output_dir, "temp_mockups.html")
    temp_pdf = os.path.join(mockups_output_dir, "temp_mockups.pdf")

    with open(theme_css, "r", encoding="utf-8") as f:
        css = f.read()

    with open(wireframe_src, "r", encoding="utf-8") as f:
        wireframe_html = f.read()

    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Maquettes d Ecrans ShopLoc — RGAA AA</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/latin-modern-web@1.0.0/style.css">
  <style>
    {css}
    @page {{
      size: A4 portrait;
      margin: 15mm 15mm 15mm 15mm;
    }}
    body {{
      max-width: 900px;
      margin: 0 auto;
      background: #FFFFFF;
      padding: 10px;
    }}
  </style>
</head>
<body>
  <div class="title-block" style="margin-bottom: 12pt;">
    <h1 class="latex-main-title">Interfaces Utilisateurs Clés — Projet ShopLoc</h1>
    <div class="latex-sub-title">Conformité RGAA Niveau AA & Principes d Ergonomie Opérative</div>
  </div>
  {wireframe_html}
</body>
</html>
"""

    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(full_html)

    edge_bin = find_edge_binary()
    cmd = [
        edge_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={temp_pdf}",
        temp_html
    ]
    subprocess.run(cmd, check=True)

    if os.path.exists(temp_pdf):
        doc = pymupdf.open(temp_pdf)
        for page_num in range(len(doc)):
            page = doc[page_num]
            pix = page.get_pixmap(dpi=200)
            png_out = os.path.join(mockups_output_dir, f"maquettes_ecrans_page_{page_num+1}.png")
            pix.save(png_out)
            print(f"[SUCCES] Capture PNG haute definition generee : {png_out} ({os.path.getsize(png_out)} octets)")
        doc.close()

    # Nettoyage des fichiers temporaires
    if os.path.exists(temp_html):
        os.remove(temp_html)
    if os.path.exists(temp_pdf):
        os.remove(temp_pdf)

if __name__ == "__main__":
    main()

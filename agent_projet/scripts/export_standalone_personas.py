#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXPORT STANDALONE PERSONAS — Génère un document PDF A4 Paysage autonome pour chacun des 4 personas.
"""
import os
import re
import subprocess

def find_edge_binary():
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return "msedge"

def create_printable_html(source_html_path, temp_html_path):
    with open(source_html_path, "r", encoding="utf-8") as f:
        content = f.read()

    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Fiche Persona ShopLoc</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    @page {{
      size: A4 landscape;
      margin: 0;
    }}
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: 'Poppins', sans-serif;
      background: #FFFFFF;
      color: #243342;
      display: flex;
      justify-content: center;
      align-items: center;
      width: 297mm;
      height: 210mm;
      padding: 6mm 10mm;
      box-sizing: border-box;
      overflow: hidden;
    }}
    .figure-card {{
      width: 100% !important;
      max-width: 1050px !important;
      margin: 0 auto !important;
      border: none !important;
      box-shadow: none !important;
      padding: 0 !important;
    }}
    svg {{
      width: 100% !important;
      height: auto !important;
      max-height: 190mm !important;
    }}
  </style>
</head>
<body>
{content}
</body>
</html>
"""
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    components_dir = os.path.join(project_root, "agent_projet", "templates", "components")
    output_dir = os.path.join(project_root, "agent_projet", "docs", "01_Cadrage_Et_Cahier_Des_Charges_R1", "personas")
    os.makedirs(output_dir, exist_ok=True)

    targets = [
        ("persona_pierre_dupont.html", "02_persona_pierre_dupont.pdf"),
        ("persona_suzanne_lemaire.html", "02_persona_suzanne_lemaire.pdf"),
        ("persona_marius_vasseur.html", "02_persona_marius_vasseur.pdf"),
        ("persona_julie_arthur.html", "02_persona_julie_arthur.pdf"),
    ]

    edge_bin = find_edge_binary()

    for comp_name, pdf_name in targets:
        src_html = os.path.join(components_dir, comp_name)
        out_pdf = os.path.join(output_dir, pdf_name)
        temp_html = os.path.join(output_dir, f"temp_{comp_name}")

        create_printable_html(src_html, temp_html)

        file_uri = f"file:///{temp_html.replace(os.sep, '/')}"
        cmd = [
            edge_bin,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={out_pdf}",
            file_uri
        ]
        subprocess.run(cmd, check=True)

        if os.path.exists(temp_html):
            os.remove(temp_html)

        if os.path.exists(out_pdf):
            size = os.path.getsize(out_pdf)
            print(f"[SUCCES] PDF généré : {out_pdf} ({size} octets)")

if __name__ == "__main__":
    main()

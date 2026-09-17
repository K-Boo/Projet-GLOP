#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXPORT STEP 02 PNGS — Exporte les 3 modèles visuels de l'Étape 02 en PNG haute résolution
et les copie dans le dossier d'artefacts pour affichage direct.
"""
import os
import re
import shutil
import subprocess
import sys

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

def extract_svg_and_dimensions(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    svg_match = re.search(r'(<svg[^>]*>.*?</svg>)', content, re.DOTALL)
    if not svg_match:
        raise ValueError(f"Aucun bloc <svg> trouve dans {html_path}")

    svg_content = svg_match.group(1)
    viewbox_match = re.search(r'viewBox=["\']\s*([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s*["\']', svg_content)
    if viewbox_match:
        vx, vy, vw, vh = map(float, viewbox_match.groups())
        width = int(vw)
        height = int(vh)
    else:
        width = 1140
        height = 760

    return svg_content, width, height

def export_svg_to_png(svg_content, width, height, output_png_path, scale=2):
    output_png_path = os.path.abspath(output_png_path)
    os.makedirs(os.path.dirname(output_png_path), exist_ok=True)
    temp_html = output_png_path.replace(".png", "_temp_render.html")

    html_page = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    html, body {{
      width: {width}px;
      height: {height}px;
      background: #FFFFFF;
      overflow: hidden;
      margin: 0;
      padding: 0;
    }}
    svg {{
      display: block;
      width: {width}px;
      height: {height}px;
    }}
  </style>
</head>
<body>
{svg_content}
</body>
</html>
"""

    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_page)

    edge_bin = find_edge_binary()
    file_uri = f"file:///{temp_html.replace(os.sep, '/')}"

    cmd = [
        edge_bin,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--force-device-scale-factor={scale}",
        f"--window-size={width},{height}",
        f"--screenshot={output_png_path}",
        file_uri
    ]
    subprocess.run(cmd, check=True)

    if os.path.exists(temp_html):
        os.remove(temp_html)

    if os.path.exists(output_png_path):
        size = os.path.getsize(output_png_path)
        print(f"[SUCCES] Graphique exporte : {output_png_path} ({width}x{height} @{scale}x, {size} octets)")
        return True
    return False

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    components_dir = os.path.join(project_root, "agent_projet", "templates", "components")
    figures_dir = os.path.join(project_root, "agent_projet", "docs", "01_Cadrage_Et_Cahier_Des_Charges_R1", "figures")
    artifact_dir = r"C:\Users\hpome\.gemini\antigravity\brain\dffeb669-85f2-442c-85f2-eaba15fd3f95"

    targets = [
        ("persona_pierre_dupont.html", "fig_2_1a_persona_pierre.png"),
        ("persona_suzanne_lemaire.html", "fig_2_1b_persona_suzanne.png"),
        ("persona_marius_vasseur.html", "fig_2_1c_persona_marius.png"),
        ("persona_julie_arthur.html", "fig_2_1d_persona_julie_arthur.png"),
        ("user_journey_map_pierre.html", "fig_2_2_user_journey_pierre.png"),
        ("user_journey_map_actifs.html", "fig_2_3_user_journey_actifs.png"),
    ]

    for comp_name, png_name in targets:
        html_file = os.path.join(components_dir, comp_name)
        out_png = os.path.join(figures_dir, png_name)
        svg_content, w, h = extract_svg_and_dimensions(html_file)
        export_svg_to_png(svg_content, w, h, out_png, scale=2)

        # Copie dans le dossier artifact pour embeding si possible
        if os.path.exists(artifact_dir):
            dest = os.path.join(artifact_dir, png_name)
            shutil.copy2(out_png, dest)
            print(f"[COPIE] Copie dans artefacts : {dest}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXPORT DIAGRAM SVG ONLY
Extrait le SVG pur des fichiers templates et l'exporte en PNG haute résolution (2x)
parfaitement détouré selon sa viewBox, sans conteneur A4, sans cadre externe et sans marge superflue.
"""

import os
import re
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
        width = 920
        height = 460

    return svg_content, width, height

def export_svg_to_png(svg_content, width, height, output_png_path, scale=2):
    output_png_path = os.path.abspath(output_png_path)
    os.makedirs(os.path.dirname(output_png_path), exist_ok=True)
    temp_html = output_png_path.replace(".png", "_temp_render.html")

    # Wrapper HTML minimaliste pixel-perfect calé sur les dimensions exactes du SVG
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

    # 1. Figure 1.1 : Bete a cornes
    bete_html = os.path.join(components_dir, "bete_a_cornes.html")
    bete_png = os.path.join(figures_dir, "fig_1_1_bete_a_cornes.png")
    svg_bete, w_bete, h_bete = extract_svg_and_dimensions(bete_html)
    export_svg_to_png(svg_bete, w_bete, h_bete, bete_png, scale=2)

    # 2. Figure 1.2 : Matrice de positionnement
    matrice_html = os.path.join(components_dir, "matrice_positionnement.html")
    matrice_png = os.path.join(figures_dir, "fig_1_2_matrice_positionnement.png")
    svg_matrice, w_matrice, h_matrice = extract_svg_and_dimensions(matrice_html)
    export_svg_to_png(svg_matrice, w_matrice, h_matrice, matrice_png, scale=2)

if __name__ == "__main__":
    main()

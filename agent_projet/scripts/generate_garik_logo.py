#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur du logo officiel pour l'entreprise Garik.
Génère logo_garik.svg et logo_garik.png.
"""
import os
import pymupdf

def generate_logo():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 130" width="600" height="130" style="font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="grad-g" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3A8A" />
      <stop offset="100%" stop-color="#0284C7" />
    </linearGradient>
    <linearGradient id="grad-accent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669" />
      <stop offset="100%" stop-color="#10B981" />
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Fond subtil lin -->
  <rect x="2" y="2" width="596" height="126" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2" filter="url(#shadow)"/>

  <!-- Emblème graphique Garik : Monogramme G stylisé -->
  <g transform="translate(30, 20)">
    <!-- Anneau extérieur G -->
    <path d="M 45 10 A 35 35 0 1 0 75 60 L 50 60 L 50 48 L 65 48 A 23 23 0 1 1 45 22 A 23 23 0 0 1 63 30 L 73 20 A 35 35 0 0 0 45 10 Z" fill="url(#grad-g)"/>
    <!-- Nœud d'accentuation territorial (symbole d'échange local) -->
    <circle cx="50" cy="54" r="6" fill="url(#grad-accent)"/>
    <circle cx="20" cy="30" r="3.5" fill="#38BDF8"/>
    <circle cx="70" cy="30" r="3.5" fill="#34D399"/>
  </g>

  <!-- Typographie du Logo -->
  <g transform="translate(130, 22)">
    <text x="0" y="48" font-size="36" font-weight="900" letter-spacing="3px" fill="#0F172A">GARIK</text>
    <rect x="0" y="58" width="420" height="2" fill="#E2E8F0" />
    <text x="0" y="74" font-size="11.5" font-weight="600" letter-spacing="0.5px" fill="#0369A1">SOLUTIONS D'INGÉNIERIE LOGICIELLE &amp; SYSTÈMES D'INFORMATION</text>
    <text x="0" y="90" font-size="10" font-weight="500" fill="#64748B">Collectif d'élèves-ingénieurs Master 2 MIAGE · Université de Lille</text>
  </g>
</svg>"""

    output_dir = os.path.abspath("agent_projet/docs/01_Cadrage_Et_Cahier_Des_Charges_R1/figures")
    os.makedirs(output_dir, exist_ok=True)
    svg_path = os.path.join(output_dir, "logo_garik.svg")
    png_path = os.path.join(output_dir, "logo_garik.png")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated SVG: {svg_path}")

    # Conversion en PNG haute résolution via PyMuPDF
    doc = pymupdf.open(svg_path)
    page = doc[0]
    pix = page.get_pixmap(dpi=300)
    pix.save(png_path)
    print(f"Generated PNG: {png_path} ({pix.width}x{pix.height})")

if __name__ == "__main__":
    generate_logo()

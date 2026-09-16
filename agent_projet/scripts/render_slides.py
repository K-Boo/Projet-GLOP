#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MOTEUR DE PRESENTATIONS & DIAPORAMAS WEB / PDF 16:9 (render_slides.py)
Master 2 MIAGE — Universite de Lille — UE GLOP (2026-2027)

Compile des diaporamas de soutenance (format 15 min + 5 min Q&A) en :
1. Une application web HTML5 responsive et interactive avec navigation clavier.
2. Un document PDF 16:9 vectoriel imprime via le navigateur headless.

Usage:
    python agent_projet/scripts/render_slides.py <source_slides.md> [--output <dest.pdf>]
    python agent_projet/scripts/render_slides.py --demo
"""

import argparse
import base64
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
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser"
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return "msedge"

def get_base64_logos(assets_dir):
    univ_logo = os.path.join(assets_dir, "logo_univ_lille.png")
    fst_logo = os.path.join(assets_dir, "logo_fst_informatique.png")
    b64_univ, b64_fst = "", ""
    if os.path.exists(univ_logo):
        with open(univ_logo, "rb") as f:
            b64_univ = base64.b64encode(f.read()).decode("utf-8")
    if os.path.exists(fst_logo):
        with open(fst_logo, "rb") as f:
            b64_fst = base64.b64encode(f.read()).decode("utf-8")
    return b64_univ, b64_fst

def clean_inline(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    return text

def parse_slides_markdown(md_text):
    raw_slides = md_text.split('\n---\n')
    slides = []
    for raw in raw_slides:
        lines = [l.strip() for l in raw.strip().split('\n') if l.strip()]
        if not lines:
            continue
        title = ""
        content = []
        for line in lines:
            if line.startswith('# ') and not title:
                title = line[2:]
            elif line.startswith('## ') and not title:
                title = line[3:]
            elif line.startswith('- ') or line.startswith('* '):
                content.append(f"<li>{clean_inline(line[2:])}</li>")
            else:
                content.append(f"<p>{clean_inline(line)}</p>")
        slides.append({"title": title, "body": content})
    return slides

def build_slides_html(slides, b64_univ, b64_fst):
    slides_divs = []
    for idx, slide in enumerate(slides):
        is_title = (idx == 0)
        slide_class = "slide title-slide" if is_title else "slide content-slide"
        
        header_html = ""
        if not is_title:
            header_html = f"""
            <div class="slide-header">
              <span class="header-project">ShopLoc — M2 MIAGE GLOP</span>
              <span class="header-univ">Universite de Lille</span>
            </div>
            """

        body_html = "\n".join(slide["body"])
        if "<li>" in body_html:
            body_html = f"<ul>{body_html}</ul>"

        slides_divs.append(f"""
        <section class="{slide_class}" id="slide-{idx+1}">
          {header_html}
          <div class="slide-body">
            <h2 class="slide-title">{clean_inline(slide['title'])}</h2>
            <div class="slide-text">
              {body_html}
            </div>
          </div>
          <div class="slide-footer">
            <span class="footer-team">Equipe ShopLoc</span>
            <span class="footer-counter">{idx+1} / {len(slides)}</span>
          </div>
        </section>
        """)

    all_slides_html = "\n".join(slides_divs)

    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Diaporama Soutenance ShopLoc — Master 2 MIAGE</title>
  <style>
    @page {{
      size: 16in 9in;
      margin: 0;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      padding: 0;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #0F172A;
      color: #0F172A;
    }}
    .slides-deck {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
      padding: 20px;
    }}
    .slide {{
      width: 960px;
      height: 540px;
      background: #FFFFFF;
      border-radius: 6px;
      padding: 30px 45px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
      page-break-after: always;
    }}
    /* Mode Presentation Plein Ecran */
    @media print {{
      body {{ background: transparent; }}
      .slides-deck {{ padding: 0; gap: 0; }}
      .slide {{
        width: 100vw;
        height: 100vh;
        border-radius: 0;
        box-shadow: none;
      }}
    }}
    .slide-header {{
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      font-weight: 600;
      color: #64748B;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 1.5px solid #0F2A4A;
      padding-bottom: 8px;
    }}
    .slide-body {{
      flex-grow: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 15px 0;
    }}
    .slide-title {{
      font-size: 26px;
      color: #0F2A4A;
      margin: 0 0 16px 0;
      font-weight: 800;
      letter-spacing: -0.02em;
    }}
    .slide-text {{
      font-size: 15px;
      line-height: 1.6;
      color: #334155;
    }}
    .slide-text ul {{
      margin: 0;
      padding-left: 24px;
    }}
    .slide-text li {{
      margin-bottom: 10px;
    }}
    .slide-footer {{
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      color: #94A3B8;
      border-top: 1px solid #E2E8F0;
      padding-top: 8px;
    }}
    .title-slide {{
      background: linear-gradient(135deg, #0F2A4A 0%, #1E3A8A 100%);
      color: #FFFFFF;
      justify-content: center;
      align-items: center;
      text-align: center;
    }}
    .title-slide .slide-title {{
      color: #FFFFFF;
      font-size: 34px;
      margin-bottom: 8px;
    }}
    .title-slide .slide-text {{
      color: #E2E8F0;
      font-size: 17px;
    }}
    .title-slide .slide-footer {{
      position: absolute;
      bottom: 20px;
      width: calc(100% - 90px);
      border-top: 1px solid rgba(255, 255, 255, 0.2);
      color: rgba(255, 255, 255, 0.7);
    }}
  </style>
</head>
<body>

<div class="slides-deck">
  {all_slides_html}
</div>

</body>
</html>
"""
    return full_html

def main():
    parser = argparse.ArgumentParser(description="Moteur de diaporamas ShopLoc (HTML5 / PDF 16:9)")
    parser.add_argument("source", nargs="?", help="Fichier Markdown des diapositives")
    parser.add_argument("--output", "-o", help="Chemin du PDF de sortie")
    parser.add_argument("--demo", action="store_true", help="Generer le diaporama de demonstration officiel")

    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    docs_dir = os.path.join(project_root, "agent_projet", "docs")
    assets_dir = os.path.join(docs_dir, "assets")

    b64_univ, b64_fst = get_base64_logos(assets_dir)
    edge_bin = find_edge_binary()

    demo_md = """# Projet ShopLoc — Soutenance R1
Cadre de Developpement, Modeles Economiques & Trajectoire d Architecture
Master 2 MIAGE — Universite de Lille — UE GLOP (2026-2027)

---

# 1. Vision Strategique & Probleme Territorial
- Desertification commerciale accrue des centres-villes face au e-commerce mondialise.
- Fracture d usage numerique frappant les populations seniors (persona Pierre, 74 ans).
- Predation financiere des plateformes privees (commissions excessives sur les commerçants).
- Reponse ShopLoc : Ancrage physique pietonnier, gratuite citoyenne et souverainete communale.

---

# 2. Les 4 Personas Cibles
- **Pierre (74 ans)** : Senior habitue du centre-ville, carte physique QR code, interface contrastée.
- **Suzanne (22 ans)** : Commerçante dynamique, saisie d inventaire simplifiée, caisse rapide.
- **Marius (27 ans)** : Administrateur territorial, tableau de bord economique agrege, anonymisation RGPD.
- **Julie & Arthur (31/34 ans)** : Actifs urbains, panier Click & Collect multi-boutiques sans livraison.

---

# 3. Dualite du Programme de Fidelisation
- **Moteur Marchand (Decentralise)** : Chaque commerçant dispose de sa propre base de points fidélité.
- **Moteur Territorial VFP (Communal)** : Regit la regularite (10 passages minimum en 15 jours).
- Declenchement de l avantage : 1 ticket de bus ou 20 minutes de parking municipal offert.
- Etancheite stricte entre les deux moteurs pour eviter toute distorsion financiere.

---

# 4. Trajectoire d Architecture & Frugalite Run
- **Monolithe Modulaire Multi-Tenant** : Modularite par briques activables (Feature Flags).
- Rejet des microservices purs : Elimination de la complexite et des couts de reseau.
- Base de donnees relationnelle PostgreSQL avec partitionnement logique par commune.
- Mocks RESTful isoles pour la simulation des systemes partenaires (voirie, transports, banques).
"""

    md_content = demo_md
    output_html = os.path.join(docs_dir, "Diaporama_ShopLoc_Soutenance.html")
    output_pdf = args.output or os.path.join(docs_dir, "Diaporama_ShopLoc_Soutenance.pdf")

    if args.source and not args.demo:
        with open(args.source, "r", encoding="utf-8") as f:
            md_content = f.read()

    slides = parse_slides_markdown(md_content)
    html_rendered = build_slides_html(slides, b64_univ, b64_fst)

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_rendered)
    print(f"[SUCCES] Diaporama HTML genere : {output_html}")

    # Impression headless 16:9
    args_edge = [
        edge_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf}",
        output_html
    ]
    subprocess.run(args_edge, check=True)
    if os.path.exists(output_pdf):
        print(f"[SUCCES] Diaporama PDF 16:9 genere : {output_pdf} ({os.path.getsize(output_pdf)} octets)")

if __name__ == "__main__":
    main()

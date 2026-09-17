#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ASSEMBLEUR DU SHOWCASE DES NOUVEAUX VISUELS PASTEL (assemble_showcase.py)
Assemble les 6 gabarits modulaires en une page HTML complète pour consultation directe navigateur.
"""

import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    docs_dir = os.path.join(project_root, "agent_projet", "docs")
    templates_dir = os.path.join(project_root, "agent_projet", "templates", "components")
    design_dir = os.path.join(project_root, "agent_projet", "design")

    with open(os.path.join(design_dir, "theme.css"), "r", encoding="utf-8") as f:
        theme_css = f.read()

    components = [
        ("apte_pieuvre.html", "1. Méthode APTE — Bête à Cornes & Diagramme Pieuvre (Figure 1.1 & 1.2)"),
        ("bpmn_swimlane_template.html", "2. Processus Métier BPMN 2.0 — Click & Collect et Retrait (Figure 3.1)"),
        ("lean_canvas.html", "3. Modèle Stratégique — Lean Canvas 9 Cases"),
        ("matrice_positionnement.html", "4. Positionnement Concurrentiel — Matrice 2 Axes (Figure 1.3)"),
        ("merise_mcd_template.html", "5. Modèle Conceptuel de Données Merise & Dictionnaire Booktabs (Figure 4.1)"),
        ("ui_wireframe_card.html", "6. Maquettes d Interfaces — Inspiration Ollca, Senior Pierre & Caisse Suzanne")
    ]

    html_parts = []
    for filename, title in components:
        filepath = os.path.join(templates_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            sec_id = filename.replace(".html", "")
            html_parts.append(f"""
    <section id="{sec_id}" style="margin-bottom: 45px;">
      <div style="border-bottom: 2px solid #243342; padding-bottom: 8px; margin-bottom: 16px;">
        <h2 style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13pt; color: #243342; margin: 0; text-transform: uppercase; letter-spacing: 0.04em;">{title}</h2>
      </div>
      {content}
    </section>
            """)

    nav_links = "".join([f'<a class="nav-link" href="#{fn.replace(".html", "")}">{tit.split("—")[0].strip()}</a>' for fn, tit in components])

    full_page = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Showcase — Nouveaux Visuels & Schémas ShopLoc (Pastel Craft)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/latin-modern-web@1.0.0/style.css">
  <style>
    {theme_css}
    body {{
      max-width: 1140px;
      margin: 30px auto;
      padding: 0 24px;
      background: #FAF9F6;
      font-family: 'Poppins', sans-serif;
    }}
    .nav-bar {{
      position: sticky;
      top: 10px;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(8px);
      border: 1px solid #DCD6CD;
      border-radius: 12px;
      padding: 10px 16px;
      margin-bottom: 30px;
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      box-shadow: 0 4px 16px rgba(36, 51, 66, 0.05);
      z-index: 100;
    }}
    .nav-link {{
      font-size: 8pt;
      font-weight: 700;
      color: #243342;
      text-decoration: none;
      padding: 5px 12px;
      border-radius: 6px;
      background: #F5F2EB;
      transition: all 0.2s;
    }}
    .nav-link:hover {{
      background: #C26750;
      color: #FFFFFF;
    }}
  </style>
</head>
<body>
  <div style="text-align: center; margin-bottom: 25px; padding-bottom: 15px; border-bottom: 1.5pt solid #243342;">
    <div style="display: inline-flex; align-items: center; gap: 8px; margin-bottom: 6px;">
      <span style="width: 8px; height: 8px; border-radius: 50%; background: #C26750; display: inline-block;"></span>
      <span style="font-size: 9pt; font-weight: 700; color: #C26750; text-transform: uppercase; letter-spacing: 0.1em;">Direction Artistique Pastel Craft — Inspiration Ollca</span>
    </div>
    <h1 style="font-size: 22pt; font-weight: 700; color: #243342; margin: 0 0 6pt 0;">Showcase des Nouveaux Schémas & Diagrammes ShopLoc</h1>
    <div style="font-size: 10.5pt; color: #5A6578;">Rendu vectoriel pur sans perte (100% interactif) &bull; Lin doux, Ardoise brumeux, Terracotta, Sauge, Ocre miel &bull; Zéro Emoji</div>
  </div>

  <div style="background: linear-gradient(135deg, #243342 0%, #1A2530 100%); color: #FFFFFF; border-radius: 14px; padding: 18px 24px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 18px rgba(36,51,66,0.15);">
    <div>
      <div style="display: inline-flex; align-items: center; gap: 8px; margin-bottom: 4px;">
        <span style="background: #C26750; color: #FFFFFF; font-size: 8pt; font-weight: 700; padding: 2px 8px; border-radius: 9999px; text-transform: uppercase;">NOUVEAU — APPLICATION PLEINE PAGE</span>
        <strong style="font-size: 13pt; letter-spacing: -0.01em;">Prototype Web App ShopLoc (Réplique Ollca Authentique)</strong>
      </div>
      <div style="font-size: 9pt; opacity: 0.85;">Expérience e-commerce 1320px sans marges étriquées, police Poppins, grille 12 colonnes, switch client/senior/caisse interactif.</div>
    </div>
    <a href="SHOPLOC_WEB_APP.html" target="_blank" style="background: #C26750; color: #FFFFFF; text-decoration: none; padding: 10px 22px; border-radius: 9999px; font-weight: 700; font-size: 9.5pt; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 2px 8px rgba(194,103,80,0.35); flex-shrink: 0;">
      <span>Ouvrir l'App Web</span>
      &rarr;
    </a>
  </div>

  <nav class="nav-bar">
    <span style="font-size: 8pt; font-weight: 700; color: #8E3D2A; display: flex; align-items: center;">Navigation directe :</span>
    {nav_links}
  </nav>

  {''.join(html_parts)}
</body>
</html>"""

    out_path = os.path.join(docs_dir, "NOUVEAUX_VISUELS_PASTEL.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_page)
    print(f"[SUCCES] Showcase genere avec succes : {out_path}")

if __name__ == "__main__":
    main()

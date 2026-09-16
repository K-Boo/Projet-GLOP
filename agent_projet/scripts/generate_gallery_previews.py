#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERATEUR D'APERÇUS VISUELS DE TOUS LES LIVRABLES (generate_gallery_previews.py)
Master 2 MIAGE — Universite de Lille — UE GLOP (2026-2027)

Cree des echantillons minimaux de chaque famille de livrables :
1. Livrable R1 (Cahier des Charges A4)
2. Livrable R3 (Etude Financiere A4)
3. Livrable R4 (Architecture Technique & Mocks A4)
4. Diagramme BPMN 2.0 (Processus 4 couloirs SVG)
5. Diagramme MCD Merise & Dictionnaire Booktabs (SVG)
6. Modeles Strategiques (Lean Canvas, APTE, Matrice 2 axes)
7. Maquettes d'Ecrans Personas (Pierre, Suzanne, Marius)
8. Diaporama de Soutenance 16:9

Compile les PDF via Edge headless et exporte des vignettes PNG haute definition via PyMuPDF,
puis assemble la page vitrine 'GALERIE_LIVRABLES.html'.
"""

import base64
import os
import subprocess
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

def compile_html_to_pdf(html_content, output_pdf, edge_bin):
    temp_html = output_pdf.replace(".pdf", "_temp.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    cmd = [
        edge_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf}",
        temp_html
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(temp_html):
        os.remove(temp_html)

def pdf_first_page_to_png(pdf_path, png_path, dpi=150):
    doc = pymupdf.open(pdf_path)
    if len(doc) > 0:
        page = doc[0]
        pix = page.get_pixmap(dpi=dpi)
        pix.save(png_path)
    doc.close()

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    agent_projet_dir = os.path.join(project_root, "agent_projet")
    docs_dir = os.path.join(agent_projet_dir, "docs")
    assets_dir = os.path.join(docs_dir, "assets")
    design_dir = os.path.join(agent_projet_dir, "design")
    templates_dir = os.path.join(agent_projet_dir, "templates", "components")
    galerie_dir = os.path.join(docs_dir, "galerie")
    os.makedirs(galerie_dir, exist_ok=True)

    edge_bin = find_edge_binary()
    b64_univ, b64_fst = get_base64_logos(assets_dir)

    with open(os.path.join(design_dir, "theme.css"), "r", encoding="utf-8") as f:
        theme_css = f.read()

    # =========================================================================
    # 1. ECHANTILLON MINIMAL : LIVRABLE R1 (CAHIER DES CHARGES A4)
    # =========================================================================
    r1_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Apercu — Livrable R1 Cahier des Charges</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/latin-modern-web@1.0.0/style.css">
  <style>{theme_css}</style>
</head>
<body>
  <div class="institution-header">
    <img class="institution-logo" src="data:image/png;base64,{b64_univ}">
    <img class="institution-logo" src="data:image/png;base64,{b64_fst}">
  </div>
  <div class="title-block">
    <h1 class="latex-main-title">Cahier des Charges & Cadrage Fonctionnel</h1>
    <div class="latex-sub-title">Livrable R1 — Plateforme ShopLoc (Master 2 MIAGE GLOP)</div>
  </div>
  <div class="cartouche-container">
    <table class="cartouche-table">
      <tr><th>Intitule Projet</th><td>Plateforme ShopLoc — Marketplace & Fidelite Territoriale</td></tr>
      <tr><th>Reference</th><td><code class="latex-code">GLOP-2026-R1-CDC-v1.0</code></td></tr>
      <tr><th>Statut</th><td><span class="badge badge-success">Gabarit Valide</span></td></tr>
      <tr><th>Tag Email</th><td><code class="latex-code">[GLOP]</code></td></tr>
    </table>
  </div>
  <div class="abstract-box">
    <div class="abstract-title">Synthese Executive</div>
    <p class="abstract-text">Ce document formalise les 9 sections canoniques du cahier des charges ShopLoc...</p>
  </div>
  <h2 class="section-heading">Table des Matieres (Extrait)</h2>
  <ul style="list-style:none; padding-left:0; font-size:9pt; line-height:1.6;">
    <li><strong>1. Cadrage Strategique & Expression du Besoin (APTE & Lean Canvas)</strong></li>
    <li><strong>2. Personas & Parcours Utilisateurs Cibles</strong></li>
    <li><strong>3. Modelisation des Processus Metiers (BPMN 2.0)</strong></li>
    <li><strong>4. Modelisation Conceptuelle des Donnees (MCD Merise & Dictionnaire)</strong></li>
    <li><strong>5. Architecture de l Information, Ergonomie & Accessibilite RGAA AA</strong></li>
  </ul>
</body>
</html>"""
    r1_pdf = os.path.join(galerie_dir, "echantillon_r1_cdc.pdf")
    compile_html_to_pdf(r1_html, r1_pdf, edge_bin)
    pdf_first_page_to_png(r1_pdf, os.path.join(galerie_dir, "thumb_r1_cdc.png"))

    # =========================================================================
    # 2. ECHANTILLON MINIMAL : LIVRABLE R3 (ETUDE FINANCIERE A4)
    # =========================================================================
    r3_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Apercu — Livrable R3 Etude Financiere</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/latin-modern-web@1.0.0/style.css">
  <style>{theme_css}</style>
</head>
<body>
  <div class="institution-header">
    <img class="institution-logo" src="data:image/png;base64,{b64_univ}">
    <img class="institution-logo" src="data:image/png;base64,{b64_fst}">
  </div>
  <div class="title-block">
    <h1 class="latex-main-title">Etude Financiere & Couts Complets</h1>
    <div class="latex-sub-title">Livrable R3 — Modele Economique & Rentabilite Pluriannuelle</div>
  </div>
  <div class="cartouche-container">
    <table class="cartouche-table">
      <tr><th>Reference</th><td><code class="latex-code">GLOP-2026-R3-FINANCE-v1.0</code></td></tr>
      <tr><th>Methode</th><td>Couts Complets (Centres d Analyse & UO) et Direct Costing</td></tr>
      <tr><th>Statut</th><td><span class="badge badge-brand">Gabarit R3</span></td></tr>
    </table>
  </div>
  <h2 class="section-heading">1. Compte de Resultat Previsionnel (Extrait 3 Ans)</h2>
  <div class="table-wrapper">
    <table class="booktabs">
      <thead>
        <tr><th>Poste Comptable (€)</th><th>Annee 1</th><th>Annee 2</th><th>Annee 3</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Chiffre d Affaires Global</strong></td><td>84 000</td><td>168 000</td><td>252 000</td></tr>
        <tr><td>- Charges Directes de Developpement</td><td>45 000</td><td>20 000</td><td>15 000</td></tr>
        <tr><td>- Charges d Exploitation (Run & Cloud)</td><td>6 200</td><td>11 400</td><td>16 800</td></tr>
        <tr><td><strong>Resultat Net d Exploitation</strong></td><td><strong>+12 400</strong></td><td><strong>+48 600</strong></td><td><strong>+82 100</strong></td></tr>
      </tbody>
    </table>
  </div>
  <div class="callout-box callout-success">
    <strong>Seuil de Rentabilite (SR) :</strong> Le point mort financier est atteint au mois 8 d exploitation avec 14 collectivites clientes.
  </div>
</body>
</html>"""
    r3_pdf = os.path.join(galerie_dir, "echantillon_r3_finance.pdf")
    compile_html_to_pdf(r3_html, r3_pdf, edge_bin)
    pdf_first_page_to_png(r3_pdf, os.path.join(galerie_dir, "thumb_r3_finance.png"))

    # =========================================================================
    # 3. ECHANTILLON MINIMAL : LIVRABLES R4/R5 (ARCHITECTURE & API REST)
    # =========================================================================
    r4_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Apercu — Livrable R4 Architecture Technique</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/latin-modern-web@1.0.0/style.css">
  <style>{theme_css}</style>
</head>
<body>
  <div class="institution-header">
    <img class="institution-logo" src="data:image/png;base64,{b64_univ}">
    <img class="institution-logo" src="data:image/png;base64,{b64_fst}">
  </div>
  <div class="title-block">
    <h1 class="latex-main-title">Dossier d Architecture Technique</h1>
    <div class="latex-sub-title">Livrable R4 — Monolithe Modulaire, Conteneurisation & Contrats OpenAPI</div>
  </div>
  <div class="cartouche-container">
    <table class="cartouche-table">
      <tr><th>Reference</th><td><code class="latex-code">GLOP-2026-R4-ARCHI-v1.0</code></td></tr>
      <tr><th>Architecture</th><td>Monolithe Modulaire Multi-Tenant (PostgreSQL 16, Docker)</td></tr>
    </table>
  </div>
  <h2 class="section-heading">1. Contrats d API RESTful (Extrait OpenAPI 3.1)</h2>
  <div class="table-wrapper">
    <table class="booktabs">
      <thead>
        <tr><th>Methode</th><th>Route API</th><th>Description & Securite</th><th>Reponse</th></tr>
      </thead>
      <tbody>
        <tr><td><code>POST</code></td><td><code>/api/v1/passages</code></td><td>Enregistrement passage caisse (JWT Commerçant)</td><td><span class="badge badge-success">201 Created</span></td></tr>
        <tr><td><code>POST</code></td><td><code>/api/v1/commandes</code></td><td>Reservation Click & Collect avec verrou 2PC</td><td><span class="badge badge-success">200 OK</span></td></tr>
        <tr><td><code>GET</code></td><td><code>/api/v1/mobilites/status</code></td><td>Calcul regularite VFP fenetre glissante 15j</td><td><span class="badge badge-brand">200 Data</span></td></tr>
      </tbody>
    </table>
  </div>
</body>
</html>"""
    r4_pdf = os.path.join(galerie_dir, "echantillon_r4_archi.pdf")
    compile_html_to_pdf(r4_html, r4_pdf, edge_bin)
    pdf_first_page_to_png(r4_pdf, os.path.join(galerie_dir, "thumb_r4_archi.png"))

    # =========================================================================
    # 4. CAPTURE DES COMPOSANTS GRAPHIQUES (BPMN, MCD, LEAN CANVAS, APTE, UI)
    # =========================================================================
    components = [
        ("lean_canvas", "thumb_lean_canvas.png"),
        ("apte_pieuvre", "thumb_apte_pieuvre.png"),
        ("matrice_positionnement", "thumb_matrice.png"),
        ("ui_wireframe_card", "thumb_ui_wireframes.png"),
        ("bpmn_swimlane_template", "thumb_bpmn_swimlanes.png"),
        ("merise_mcd_template", "thumb_merise_mcd.png")
    ]

    for comp_name, thumb_name in components:
        comp_file = os.path.join(templates_dir, f"{comp_name}.html")
        if os.path.exists(comp_file):
            with open(comp_file, "r", encoding="utf-8") as f:
                c_content = f.read()
            c_html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>{theme_css}body{{max-width:960px;margin:20px auto;background:#FFF;padding:10px;}}</style></head><body>{c_content}</body></html>"""
            c_pdf = os.path.join(galerie_dir, f"temp_{comp_name}.pdf")
            compile_html_to_pdf(c_html, c_pdf, edge_bin)
            pdf_first_page_to_png(c_pdf, os.path.join(galerie_dir, thumb_name))
            if os.path.exists(c_pdf):
                os.remove(c_pdf)

    # 5. Diaporama de soutenance (Thumbnail slide 1)
    diaporama_pdf = os.path.join(docs_dir, "Diaporama_ShopLoc_Soutenance.pdf")
    if os.path.exists(diaporama_pdf):
        pdf_first_page_to_png(diaporama_pdf, os.path.join(galerie_dir, "thumb_diaporama.png"))

    # =========================================================================
    # 6. ASSEMBLAGE DE LA PAGE DE GALERIE VITRINE (GALERIE_LIVRABLES.html)
    # =========================================================================
    galerie_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Galerie Visuelle des Livrables — Projet ShopLoc</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/latin-modern-web@1.0.0/style.css">
  <style>
    {theme_css}
    body {{
      max-width: 1100px;
      margin: 30px auto;
      padding: 0 20px;
      background: #F8FAFC;
    }}
    .gallery-header {{
      text-align: center;
      margin-bottom: 25px;
      padding-bottom: 15px;
      border-bottom: 1.5pt solid var(--color-brand-primary);
    }}
    .cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 20px;
      margin-bottom: 30px;
    }}
    .deliverable-card {{
      background: #FFFFFF;
      border: 1pt solid #CBD5E1;
      border-radius: 6pt;
      overflow: hidden;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
      display: flex;
      flex-direction: column;
    }}
    .deliverable-card:hover {{
      box-shadow: 0 8px 12px -1px rgba(0, 0, 0, 0.1);
      border-color: var(--color-brand-primary);
    }}
    .card-thumb-container {{
      height: 190px;
      background: #F1F5F9;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      border-bottom: 1pt solid #E2E8F0;
    }}
    .card-thumb {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}
    .card-body {{
      padding: 12px 14px;
      flex-grow: 1;
      display: flex;
      flex-direction: column;
    }}
    .card-tag {{
      font-size: 7.5pt;
      font-family: var(--font-sans);
      font-weight: bold;
      text-transform: uppercase;
      color: var(--color-brand-primary);
      margin-bottom: 4pt;
    }}
    .card-title {{
      font-size: 10.5pt;
      font-weight: bold;
      color: #0F172A;
      margin-bottom: 6pt;
    }}
    .card-desc {{
      font-size: 8.5pt;
      color: #475569;
      line-height: 1.4;
      margin-bottom: 10pt;
    }}
    .card-footer {{
      margin-top: auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 8pt;
      border-top: 0.5pt solid #E2E8F0;
      font-size: 8pt;
    }}
    .card-link {{
      color: var(--color-brand-primary);
      text-decoration: none;
      font-weight: bold;
    }}
    .card-link:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>

<div class="gallery-header">
  <div class="institution-header" style="border-bottom: none; margin-bottom: 6pt;">
    <img class="institution-logo" src="data:image/png;base64,{b64_univ}">
    <img class="institution-logo" src="data:image/png;base64,{b64_fst}">
  </div>
  <h1 class="latex-main-title" style="margin-bottom: 4pt;">Galerie Visuelle des Livrables & Modèles</h1>
  <div class="latex-sub-title">Vue Panoramique de Validation des Formats — Master 2 MIAGE GLOP (2026-2027)</div>
</div>

<div class="cards-grid">

  <!-- 1. CAHIER DES CHARGES R1 -->
  <div class="deliverable-card">
    <div class="card-thumb-container">
      <img class="card-thumb" src="galerie/thumb_r1_cdc.png" alt="Livrable R1">
    </div>
    <div class="card-body">
      <div class="card-tag">Livrable Officiel R1</div>
      <div class="card-title">Cahier des Charges & Cadrage Métier</div>
      <div class="card-desc">Format A4 LaTeX-Modern avec logos officiels, cartouche GLOP, Table des Matières dynamique et tableaux Booktabs.</div>
      <div class="card-footer">
        <span class="badge badge-success">Document A4</span>
        <a class="card-link" href="galerie/echantillon_r1_cdc.pdf" target="_blank">Ouvrir PDF</a>
      </div>
    </div>
  </div>

  <!-- 2. ETUDE FINANCIERE R3 -->
  <div class="deliverable-card">
    <div class="card-thumb-container">
      <img class="card-thumb" src="galerie/thumb_r3_finance.png" alt="Livrable R3">
    </div>
    <div class="card-body">
      <div class="card-tag">Livrable Officiel R3</div>
      <div class="card-title">Étude Financière & Coûts Complets</div>
      <div class="card-desc">Compte de Résultat 3 ans, Bilan équilibré, centres d'analyse (Build, Run, Support) et seuil de rentabilité communal.</div>
      <div class="card-footer">
        <span class="badge badge-brand">Document A4</span>
        <a class="card-link" href="galerie/echantillon_r3_finance.pdf" target="_blank">Ouvrir PDF</a>
      </div>
    </div>
  </div>

  <!-- 3. ARCHITECTURE TECHNIQUE R4 -->
  <div class="deliverable-card">
    <div class="card-thumb-container">
      <img class="card-thumb" src="galerie/thumb_r4_archi.png" alt="Livrable R4">
    </div>
    <div class="card-body">
      <div class="card-tag">Livrable Officiel R4/R5</div>
      <div class="card-title">Dossier Technique & Contrats d'API</div>
      <div class="card-desc">Spécifications OpenAPI 3.1, architecture conteneurisée Docker, monolithe modulaire et mocks des partenaires.</div>
      <div class="card-footer">
        <span class="badge badge-brand">Dossier A4</span>
        <a class="card-link" href="galerie/echantillon_r4_archi.pdf" target="_blank">Ouvrir PDF</a>
      </div>
    </div>
  </div>

  <!-- 4. BPMN 2.0 (SECTION 03) -->
  <div class="deliverable-card">
    <div class="card-thumb-container">
      <img class="card-thumb" src="galerie/thumb_bpmn_swimlanes.png" alt="BPMN 2.0">
    </div>
    <div class="card-body">
      <div class="card-tag">Section 03 — Processus</div>
      <div class="card-title">BPMN 2.0 à Couloirs d'Acteurs</div>
      <div class="card-desc">4 Swimlanes (Citoyen, Commerçant, ShopLoc, Mobilité), passerelles XOR, flux de messages, rendu pastel vectoriel.</div>
      <div class="card-footer">
        <span class="badge badge-warning">SVG Vectoriel</span>
        <a class="card-link" href="preview_bpmn_swimlane_template.html" target="_blank">Voir SVG</a>
      </div>
    </div>
  </div>

  <!-- 5. MCD MERISE (SECTION 04) -->
  <div class="deliverable-card">
    <div class="card-thumb-container">
      <img class="card-thumb" src="galerie/thumb_merise_mcd.png" alt="MCD Merise">
    </div>
    <div class="card-body">
      <div class="card-tag">Section 04 — Données</div>
      <div class="card-title">MCD Merise & Dictionnaire Booktabs</div>
      <div class="card-desc">Entités avec clés soulignées, associations verbales, cardinalités explicites 0,n / 1,1 et dictionnaire PostgreSQL.</div>
      <div class="card-footer">
        <span class="badge badge-warning">SVG + Booktabs</span>
        <a class="card-link" href="preview_merise_mcd_template.html" target="_blank">Voir MCD</a>
      </div>
    </div>
  </div>

  <!-- 6. LEAN CANVAS (SECTION 01) -->
  <div class="deliverable-card">
    <div class="card-thumb-container">
      <img class="card-thumb" src="galerie/thumb_lean_canvas.png" alt="Lean Canvas">
    </div>
    <div class="card-body">
      <div class="card-tag">Section 01 — Synthèse</div>
      <div class="card-title">Lean Canvas Panoramique (9 Blocs)</div>
      <div class="card-desc">Grille de synthèse 9 cases format A4 paysage reliant les personas, les canaux, les coûts complets et les revenus.</div>
      <div class="card-footer">
        <span class="badge badge-success">Grille A4 Paysage</span>
        <a class="card-link" href="preview_lean_canvas.html" target="_blank">Voir Canvas</a>
      </div>
    </div>
  </div>

  <!-- 7. METHODE APTE (SECTION 01) -->
  <div class="deliverable-card">
    <div class="card-thumb-container">
      <img class="card-thumb" src="galerie/thumb_apte_pieuvre.png" alt="Méthode APTE">
    </div>
    <div class="card-body">
      <div class="card-tag">Section 01 — Besoin</div>
      <div class="card-title">Bête à Cornes & Diagramme Pieuvre</div>
      <div class="card-desc">Analyse fonctionnelle normalisée AFNOR : énonciation du besoin canonique, fonctions principales FP et contraintes FC.</div>
      <div class="card-footer">
        <span class="badge badge-warning">SVG Vectoriel</span>
        <a class="card-link" href="preview_apte_pieuvre.html" target="_blank">Voir Schémas</a>
      </div>
    </div>
  </div>

  <!-- 8. MATRICE DE POSITIONNEMENT (SECTION 01) -->
  <div class="deliverable-card">
    <div class="card-thumb-container">
      <img class="card-thumb" src="galerie/thumb_matrice.png" alt="Matrice 2 axes">
    </div>
    <div class="card-body">
      <div class="card-tag">Section 01 — Marché</div>
      <div class="card-title">Matrice Concurrentielle (2 Axes)</div>
      <div class="card-desc">Positionnement stratégique : flux piétonnier en centre-ville vs délocalisation, gratuité usager vs commissions privées.</div>
      <div class="card-footer">
        <span class="badge badge-warning">Cadran SVG</span>
        <a class="card-link" href="preview_matrice_positionnement.html" target="_blank">Voir Matrice</a>
      </div>
    </div>
  </div>

  <!-- 9. MAQUETTES PERSONAS (SECTION 05) -->
  <div class="deliverable-card">
    <div class="card-thumb-container">
      <img class="card-thumb" src="galerie/thumb_ui_wireframes.png" alt="Maquettes UI">
    </div>
    <div class="card-body">
      <div class="card-tag">Section 05 — Ergonomie</div>
      <div class="card-title">Zonings & Maquettes d'Interfaces</div>
      <div class="card-desc">Cartes accessibles : Pierre senior (carte QR physique), Suzanne commerçante (terminal caisse), Marius (dashboard RGPD).</div>
      <div class="card-footer">
        <span class="badge badge-brand">HTML RGAA AA</span>
        <a class="card-link" href="preview_ui_wireframe_card.html" target="_blank">Voir Maquettes</a>
      </div>
    </div>
  </div>

  <!-- 10. DIAPORAMA DE SOUTENANCE -->
  <div class="deliverable-card">
    <div class="card-thumb-container">
      <img class="card-thumb" src="galerie/thumb_diaporama.png" alt="Diaporama 16:9">
    </div>
    <div class="card-body">
      <div class="card-tag">Support Oral 15 min</div>
      <div class="card-title">Diaporama Soutenance (Format 16:9)</div>
      <div class="card-desc">Support de présentation interactif HTML5 et PDF vectoriel 16:9 conforme à la charte et sans emoji.</div>
      <div class="card-footer">
        <span class="badge badge-success">Web & PDF 16:9</span>
        <a class="card-link" href="Diaporama_ShopLoc_Soutenance.pdf" target="_blank">Ouvrir Slides</a>
      </div>
    </div>
  </div>

</div>

</body>
</html>"""

    galerie_html_path = os.path.join(docs_dir, "GALERIE_LIVRABLES.html")
    with open(galerie_html_path, "w", encoding="utf-8") as f:
        f.write(galerie_html)

    print(f"[SUCCES] Galerie visuelle generee : {galerie_html_path}")

if __name__ == "__main__":
    main()

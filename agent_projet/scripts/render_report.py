#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MOTEUR DE COMPILATION UNIVERSEL DE LIVRABLES SHOPLOC (render_report.py)
Master 2 MIAGE — Universite de Lille — UE GLOP (2026-2027)

Compile n'importe quel fichier Markdown ou template HTML en document PDF A4 vectoriel
conforme a la charte academique, avec Table des Matieres dynamique, Booktabs,
cartouche normalise GLOP, et verification integrale de securite (anti-pieges IA & zero emoji).

Usage:
    python agent_projet/scripts/render_report.py <source.md> [--output <dest.pdf>] [--toc]
    python agent_projet/scripts/render_report.py --preview-styleguide
"""

import argparse
import base64
import os
import re
import shutil
import subprocess
import sys

# Detection automatique du binaire Chromium / Edge headless
def find_edge_binary():
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return "msedge"

# Chargement et encodage base64 des logos officiels
def get_base64_logos(assets_dir):
    univ_logo = os.path.join(assets_dir, "logo_univ_lille.png")
    fst_logo = os.path.join(assets_dir, "logo_fst_informatique.png")
    
    b64_univ = ""
    b64_fst = ""
    if os.path.exists(univ_logo):
        with open(univ_logo, "rb") as f:
            b64_univ = base64.b64encode(f.read()).decode("utf-8")
    if os.path.exists(fst_logo):
        with open(fst_logo, "rb") as f:
            b64_fst = base64.b64encode(f.read()).decode("utf-8")
    return b64_univ, b64_fst

# Nettoyage et formatage inline du markdown vers HTML
def clean_inline(text):
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" style="color: #243342; text-decoration: underline; font-weight: 500;">\1</a>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.*?)`', r'<code class="latex-code">\1</code>', text)
    return text

# Conversion d'une table Markdown en table Booktabs HTML
def markdown_table_to_booktabs(table_lines):
    if len(table_lines) < 2:
        return ""
    headers = [clean_inline(c.strip()) for c in table_lines[0].strip('|').split('|')]
    rows = []
    for line in table_lines[2:]:
        if '|' in line:
            cells = [clean_inline(c.strip()) for c in line.strip('|').split('|')]
            rows.append(cells)
    
    html = ['<div class="table-wrapper"><table class="booktabs">', '<thead><tr>']
    for h in headers:
        html.append(f'<th>{h}</th>')
    html.append('</tr></thead><tbody>')
    for row in rows:
        html.append('<tr>')
        for cell in row:
            html.append(f'<td>{cell}</td>')
        html.append('</tr>')
    html.append('</tbody></table></div>')
    return '\n'.join(html)

# Parseur générique Markdown vers structure HTML élégante
def parse_markdown_to_html(md_text, meta, b64_univ, b64_fst, css_content, generate_toc=False, no_cartouche=False):
    lines = md_text.split('\n')
    body_html = []
    toc_items = []
    
    in_list = False
    in_item = False
    in_table = False
    table_buffer = []

    def close_list():
        nonlocal in_list, in_item
        if in_item:
            body_html.append('</li>')
            in_item = False
        if in_list:
            body_html.append('</ul>')
            in_list = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Gestion des tableaux Markdown
        if stripped.startswith('|') and stripped.endswith('|'):
            if not in_table:
                in_table = True
                table_buffer = []
            table_buffer.append(stripped)
            i += 1
            continue
        elif in_table:
            in_table = False
            body_html.append(markdown_table_to_booktabs(table_buffer))
            table_buffer = []

        # Separateur horizontal
        if stripped == '---':
            close_list()
            i += 1
            continue

        if not stripped:
            i += 1
            continue

        # Banniere de section majeure (H1)
        if stripped.startswith('# '):
            close_list()
            title = clean_inline(stripped[2:])
            sec_id = f"sec-{len(toc_items)+1}"
            slug = re.sub(r'[^a-zA-Z0-9_-]', '-', title.lower()).strip('-')
            toc_items.append((1, title, sec_id))
            body_html.append(f'<div id="{sec_id}" class="wave-banner"><a id="{slug}"></a>{title}</div>')
            i += 1
            continue

        # Titre de section H2
        if stripped.startswith('## '):
            close_list()
            title = clean_inline(stripped[3:])
            sec_id = f"sec-{len(toc_items)+1}"
            slug = re.sub(r'[^a-zA-Z0-9_-]', '-', title.lower()).strip('-')
            toc_items.append((2, title, sec_id))
            body_html.append(f'<h2 id="{sec_id}" class="section-heading"><a id="{slug}"></a>{title}</h2>')
            i += 1
            continue

        # Titre de sous-section H3
        if stripped.startswith('### '):
            close_list()
            title = clean_inline(stripped[4:])
            sec_id = f"sec-h3-{i}"
            body_html.append(f'<h3 id="{sec_id}" class="subsection-heading">{title}</h3>')
            i += 1
            continue

        # Titre de sous-sous-section H4
        if stripped.startswith('#### '):
            close_list()
            title = clean_inline(stripped[5:])
            body_html.append(f'<h4 class="category-heading">{title}</h4>')
            i += 1
            continue

        # Encarts de décision / validation
        if 'color: #166534' in stripped or 'Arbitrage MOA' in stripped or 'Décision validée' in stripped or 'Decision validee' in stripped:
            close_list()
            clean_txt = re.sub(r'</?span[^>]*>', '', stripped)
            clean_txt = re.sub(r'</?strong>', '', clean_txt).strip('* -')
            body_html.append(f'<div class="callout-box callout-success"><strong>Validation MOA :</strong> {clean_inline(clean_txt)}</div>')
            i += 1
            continue

        # Encarts d'attente d'arbitrage
        if 'color: #c2410c' in stripped or 'Statut : En attente' in stripped or 'arbitrage MOA' in stripped:
            close_list()
            clean_txt = re.sub(r'</?span[^>]*>', '', stripped)
            clean_txt = re.sub(r'</?strong>', '', clean_txt).strip('* -')
            body_html.append(f'<div class="callout-box callout-warning"><strong>{clean_inline(clean_txt)}</strong></div>')
            i += 1
            continue

        # Lignes d'indentation / continuation d'un item de liste
        if (line.startswith('  ') or line.startswith('\t')) and in_item and stripped:
            body_html.append(f'<br><span style="display:inline-block; margin-top: 1.5pt; color: #334155;">{clean_inline(stripped)}</span>')
            i += 1
            continue

        # Listes a puces
        if stripped.startswith('- ') or stripped.startswith('* '):
            if in_item:
                body_html.append('</li>')
                in_item = False
            if not in_list:
                body_html.append('<ul style="margin: 3pt 0 4pt 16pt; padding: 0; font-size: 9.5pt; line-height: 1.35; text-align: left;">')
                in_list = True
            body_html.append(f'<li style="margin-bottom: 4pt; text-align: left;">{clean_inline(stripped[2:])}')
            in_item = True
            i += 1
            continue

        # Balises et blocs HTML bruts (SVG, div, conteneurs)
        if stripped.startswith('<') and not (stripped.startswith('<code') or stripped.startswith('<span') or stripped.startswith('<strong>') or stripped.startswith('<em>')):
            close_list()
            body_html.append(stripped)
            i += 1
            continue

        # Blocs de code preformate (```)
        if stripped.startswith('```'):
            close_list()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            i += 1 # sauter la fermeture ```
            code_content = '\n'.join(code_lines)
            body_html.append(f'<pre style="background: #F8FAFC; border: 1pt solid #E2E8F0; padding: 8pt; border-radius: 4pt; font-family: monospace; font-size: 8.5pt; overflow-x: auto;"><code>{code_content}</code></pre>')
            continue

        # Paragraphes normaux
        close_list()
        body_html.append(f'<p style="margin: 4pt 0; text-align: left;">{clean_inline(stripped)}</p>')
        i += 1

    close_list()
    if in_table:
        body_html.append(markdown_table_to_booktabs(table_buffer))

    # Assemblage de la Table des Matières (TOC) si requise
    toc_html = ""
    if generate_toc and len(toc_items) > 3:
        toc_lines = ['<h2 class="section-heading">Table des Matières</h2>', '<ul style="list-style: none; padding-left: 0; font-size: 8.5pt; line-height: 1.38;">']
        for level, title, sec_id in toc_items:
            indent = "0" if level == 1 else "14pt"
            font_weight = "bold" if level == 1 else "normal"
            margin_top = "5pt" if level == 1 else "1.5pt"
            toc_lines.append(f'<li style="padding-left: {indent}; font-weight: {font_weight}; margin-top: {margin_top};"><a href="#{sec_id}" style="text-decoration: none; color: #0F2A4A;">{title}</a></li>')
        toc_lines.append('</ul><div style="page-break-after: always;"></div>')
        toc_html = '\n'.join(toc_lines)

    # Cartouche administratif normalise ou en-tete compact
    if no_cartouche:
        header_meta_html = f"""
    <div class="cartouche-compact">
      <span><strong>Reference :</strong> <code class="latex-code">{meta.get('ref', 'GLOP-2026-LIVRABLE-v1.0')}</code></span> &nbsp;|&nbsp;
      <span><strong>Statut :</strong> <span class="badge badge-success">{meta.get('status', 'Version 1.0 Formelle')}</span></span> &nbsp;|&nbsp;
      <span><strong>Date :</strong> {meta.get('date', '18 Septembre 2026')}</span> &nbsp;|&nbsp;
      <span><strong>Transparence :</strong> Élaboré avec assistance IA (validé par l'équipe)</span>
    </div>
        """
        page_break_after_header = ""
    else:
        header_meta_html = f"""
    <div class="cartouche-container">
      <table class="cartouche-table">
        <tr><th>Intitule du Projet</th><td>Plateforme ShopLoc — Marketplace & Fidelisation Territoriale</td></tr>
        <tr><th>Identifiant Officiel</th><td><code class="latex-code">MiageShopLoc</code></td></tr>
        <tr><th>Titre du Document</th><td>{meta.get('title', 'Livrable Officiel')}</td></tr>
        <tr><th>Reference Documentaire</th><td><code class="latex-code">{meta.get('ref', 'GLOP-2026-LIVRABLE-v1.0')}</code></td></tr>
        <tr><th>Contexte Academique</th><td>Master 2 MIAGE — UE Genie Logiciel par la Pratique (2026-2027)</td></tr>
        <tr><th>Maitrise d Ouvrage (MOA)</th><td>Laurence Duchien, Anne Etien, Francois Secchi, Jeremy Woirhaye</td></tr>
        <tr><th>Entreprise Soumissionnaire</th><td>Garik (Equipe de 5 etudiants Master 2 MIAGE)</td></tr>
        <tr><th>Date de remise</th><td>18 Septembre 2026 (18h00)</td></tr>
        <tr><th>Statut du document</th><td><span class="badge badge-success">Version 1.0 — Formelle</span></td></tr>
        <tr><th>Assistance IA &amp; Transparence</th><td>Document élaboré avec l'assistance d'une intelligence artificielle (Antigravity), sous la direction, la relecture critique et la validation intégrale de l'équipe d'ingénierie Garik.</td></tr>
      </table>
    </div>
        """
        page_break_after_header = '<div style="page-break-after: always;"></div>'

    body_joined = "\n".join(body_html)
    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>{meta.get('title', 'Livrable ShopLoc')}</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/latin-modern-web@1.0.0/style.css">
  <style>
    {css_content}
  </style>
</head>
<body>

<div class="institution-header">
  <img class="institution-logo" src="data:image/png;base64,{b64_univ}" alt="Universite de Lille">
  <img class="institution-logo" src="data:image/png;base64,{b64_fst}" alt="Faculte des Sciences et Technologies">
</div>

<div class="title-block">
  <h1 class="latex-main-title">{meta.get('title', 'Livrable ShopLoc')}</h1>
  <div class="latex-sub-title">{meta.get('subtitle', 'Master 2 MIAGE — UE GLOP 2026-2027')}</div>
</div>

{header_meta_html}

{f'<div class="abstract-box"><div class="abstract-title">Preambule</div><p class="abstract-text">{meta.get("preamble")}</p></div>' if meta.get("preamble") else ''}

{page_break_after_header}

{toc_html}

{body_joined}

</body>
</html>
"""
    return full_html

# Compilation HTML vers PDF A4 via le navigateur headless
def compile_html_to_pdf(html_content, output_pdf_path, edge_bin):
    output_pdf_path = os.path.abspath(output_pdf_path)
    temp_html_path = output_pdf_path.replace(".pdf", "_temp.html")
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(script_dir))
    args = [
        edge_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf_path}",
        temp_html_path
    ]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError:
        if not os.path.exists(output_pdf_path) or os.path.getsize(output_pdf_path) == 0:
            raise
    
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)

    if os.path.exists(output_pdf_path):
        size = os.path.getsize(output_pdf_path)
        print(f"SUCCESS: Generated PDF at {output_pdf_path} ({size} octets)")
        return True
    return False

def merge_appendices_if_available(output_pdf):
    if not os.path.exists(output_pdf):
        return
    import pymupdf

    doc_dir = os.path.dirname(os.path.abspath(output_pdf))
    personas_dir = os.path.join(doc_dir, "personas")
    cvs_dir = os.path.join(doc_dir, "annexes_cv")

    if not os.path.exists(personas_dir) and not os.path.exists(cvs_dir):
        return

    doc = pymupdf.open(output_pdf)
    base_pages = len(doc)

    # Determiner la position d'insertion des Personas (apres Annexe 1, juste avant Annexe 2)
    idx_annexe2 = None
    for i in range(len(doc) - 1, 1, -1):
        lines = [l.strip().upper() for l in doc[i].get_text("text").split("\n")]
        if any(l.startswith("ANNEXE 2 :") for l in lines):
            idx_annexe2 = i
            break

    # 1. Insertion des fiches Personas A4 paysage (1 page par persona)
    persona_files = [
        ("02_persona_pierre_dupont.pdf", "Annexe 1.1 : Fiche Persona — Pierre Dupont (Retraité Citoyen, 74 ans)"),
        ("02_persona_suzanne_lemaire.pdf", "Annexe 1.2 : Fiche Persona — Suzanne Lemaire (Artisane Boulangère, 22 ans)"),
        ("02_persona_marius_vasseur.pdf", "Annexe 1.3 : Fiche Persona — Marius Vasseur (Cadre Territorial / DSI, 27 ans)"),
        ("02_persona_julie_arthur.pdf", "Annexe 1.4 : Fiche Persona — Julie & Arthur (Jeune Foyer Éco-Actif, 31 et 34 ans)")
    ]

    inserted_personas = 0
    if os.path.exists(personas_dir):
        insert_pos = idx_annexe2 if idx_annexe2 is not None else len(doc)
        for fname, title in persona_files:
            p_path = os.path.join(personas_dir, fname)
            if os.path.exists(p_path):
                pdoc = pymupdf.open(p_path)
                doc.insert_pdf(pdoc, from_page=0, to_page=0, start_at=insert_pos + inserted_personas)
                pdoc.close()
                inserted_personas += 1

    # 2. Insertion des CVs officiels de l'équipe (1 page par CV a la fin)
    cv_files = [
        ("01_CV_Khalil_Bouchama.pdf", "Annexe 2.1 : CV — Khalil Bouchama"),
        ("02_CV_Abdelkader_Heddi.pdf", "Annexe 2.2 : CV — Abdelkader Heddi"),
        ("03_CV_Gautam_Demeulemeester.pdf", "Annexe 2.3 : CV — Gautam Demeulemeester"),
        ("04_CV_Rayane_Alli.pdf", "Annexe 2.4 : CV — Rayane Alli"),
        ("05_CV_Ilyas_Ait_Ali.pdf", "Annexe 2.5 : CV — Ilyas Ait Ali")
    ]

    inserted_cvs = 0
    if os.path.exists(cvs_dir):
        for fname, title in cv_files:
            c_path = os.path.join(cvs_dir, fname)
            if os.path.exists(c_path):
                cdoc = pymupdf.open(c_path)
                doc.insert_pdf(cdoc, from_page=0, to_page=0)
                cdoc.close()
                inserted_cvs += 1

    if inserted_personas > 0 or inserted_cvs > 0:
        toc = [
            [1, "Page de Garde & Cartouche GLOP", 1],
            [1, "Table des Matières", 2],
            [1, "1. Présentation de l'entreprise Garik", 3],
            [1, "2. Équipe projet et répartition des rôles", 4],
            [2, "2.1. Présentation synthétique des compétences", 4],
            [2, "2.2. Répartition des rôles opérationnels", 5],
            [2, "2.3. Organisation Scrum Master tournant", 5],
            [1, "3. Exigences fonctionnelles et modélisation du besoin", 6],
            [2, "3.1. Cadre général et objectifs", 6],
            [2, "3.2. Identification des acteurs et benchmark", 7],
            [2, "3.3. Analyse des profils utilisateurs cibles (Personas)", 8],
            [2, "3.4. Cartographie des récits utilisateurs (USM - A4 Paysage)", 9],
            [2, "3.5. Découpage modulaire du système", 10],
            [1, "4. Premiers choix justifiés d'outils logiciels", 11],
            [2, "4.1. Architecture globale 3-Tiers (A4 Paysage)", 12],
            [2, "4.2. Pile technologique et justifications", 13],
            [1, "5. Diagramme de Gantt annuel prévisionnel", 14],
            [1, "6. Étude financière et méthode des coûts complets", 16],
            [2, "6.1. Définition des centres et charges", 16],
            [2, "6.2. Tableau de répartition des charges indirectes", 17],
            [2, "6.3. Calcul du coût de revient complet", 18],
            [2, "6.4. Application de la marge bénéficiaire cible (20 %)", 18],
            [2, "6.5. Comparatif des modèles économiques et choix SaaS", 19],
            [1, "Annexe 1 : Fiches détaillées des Personas (Format A4 Paysage)", 20],
            [2, "Annexe 1.1 : Fiche Persona — Pierre Dupont (Retraité Citoyen, 74 ans)", 21],
            [2, "Annexe 1.2 : Fiche Persona — Suzanne Lemaire (Artisane Boulangère, 22 ans)", 22],
            [2, "Annexe 1.3 : Fiche Persona — Marius Vasseur (Cadre Territorial / DSI, 27 ans)", 23],
            [2, "Annexe 1.4 : Fiche Persona — Julie & Arthur (Jeune Foyer Éco-Actif, 31 & 34 ans)", 24],
            [1, "Annexe 2 : Curricula Vitæ de l'équipe Garik", 25],
            [2, "Annexe 2.1 : CV — Khalil Bouchama", 26],
            [2, "Annexe 2.2 : CV — Abdelkader Heddi", 27],
            [2, "Annexe 2.3 : CV — Gautam Demeulemeester", 28],
            [2, "Annexe 2.4 : CV — Rayane Alli", 29],
            [2, "Annexe 2.5 : CV — Ilyas Ait Ali", 30],
        ]
        doc.set_toc(toc)
        tmp_pdf = output_pdf + ".merged.tmp"
        doc.save(tmp_pdf)
        doc.close()
        shutil.move(tmp_pdf, output_pdf)
        print(f"[SUCCES FUSION] {inserted_personas} fiches Personas (A4 Paysage) et {inserted_cvs} CVs fusionnes. Signets PDF integres. Total : {base_pages + inserted_personas + inserted_cvs} pages.")
    else:
        doc.close()

def main():
    parser = argparse.ArgumentParser(description="Moteur de compilation de livrables academiques GLOP en PDF A4")
    parser.add_argument("source", help="Fichier Markdown ou HTML source a compiler")
    parser.add_argument("--output", "-o", help="Chemin du PDF genere en sortie")
    parser.add_argument("--title", default="ShopLoc — Cahier des Charges & Cadrage R1", help="Titre officiel du document")
    parser.add_argument("--subtitle", default="Master 2 MIAGE — UE Genie Logiciel par la Pratique 2026-2027", help="Sous-titre academique")
    parser.add_argument("--ref", default="GLOP-2026-LIVRABLE-R1-v1.0", help="Reference normalisee du livrable")
    parser.add_argument("--toc", action="store_true", help="Generer une table des matieres dynamique")
    parser.add_argument("--no-cartouche", action="store_true", help="Ne pas afficher le grand cartouche administratif et permettre l enchainement direct du contenu")
    parser.add_argument("--preview-styleguide", action="store_true", help="Generer uniquement le guide de style visuel ShopLoc")

    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    agent_projet_dir = os.path.dirname(script_dir)
    docs_dir = os.path.join(agent_projet_dir, "docs")
    design_dir = os.path.join(agent_projet_dir, "design")

    assets_dir = os.path.join(docs_dir, "assets")
    theme_css_path = os.path.join(design_dir, "theme.css")

    edge_bin = find_edge_binary()
    b64_univ, b64_fst = get_base64_logos(assets_dir)

    with open(theme_css_path, "r", encoding="utf-8") as f:
        theme_css = f.read()

    # Mode apercu du guide de style
    if args.preview_styleguide:
        styleguide_html_path = os.path.join(design_dir, "styleguide.html")
        output_pdf = os.path.join(design_dir, "Styleguide_ShopLoc_Officiel.pdf")
        if os.path.exists(styleguide_html_path):
            with open(styleguide_html_path, "r", encoding="utf-8") as f:
                html_c = f.read()
            compile_html_to_pdf(html_c, output_pdf, edge_bin)
        return

    source_path = os.path.abspath(args.source)
    if not os.path.exists(source_path):
        print(f"Erreur : fichier source introuvable : {source_path}")
        sys.exit(1)

    if not args.output:
        base, _ = os.path.splitext(source_path)
        output_pdf = base + ".pdf"
    else:
        output_pdf = os.path.abspath(args.output)

    with open(source_path, "r", encoding="utf-8") as f:
        source_content = f.read()

    meta = {
        "title": args.title,
        "subtitle": args.subtitle,
        "ref": args.ref,
        "status": "Version 1.0 — Validee"
    }

    html_content = parse_markdown_to_html(source_content, meta, b64_univ, b64_fst, theme_css, generate_toc=args.toc, no_cartouche=args.no_cartouche)
    compile_html_to_pdf(html_content, output_pdf, edge_bin)

    # Fusion des annexes Personas et CVs si presentes
    merge_appendices_if_available(output_pdf)

    # Verification de securite post-compilation sur le PDF
    try:
        import verify_deliverables
        registry = verify_deliverables.load_canary_registry()
        violations = verify_deliverables.check_file(output_pdf, registry)
        if violations:
            print(f"[ALERTE CRITIQUE] Le PDF genere contient des violations de securite :")
            for v in violations:
                print(f"  [{v['type']}] {v.get('location', '')} : {v.get('detail', '')}")
            if os.path.exists(output_pdf):
                os.remove(output_pdf)
            sys.exit(1)
    except Exception as e:
        print(f"[Avertissement Securite PDF] : {e}")

if __name__ == "__main__":
    main()

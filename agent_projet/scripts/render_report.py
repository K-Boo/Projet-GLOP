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
            toc_items.append((1, title, sec_id))
            body_html.append(f'<div id="{sec_id}" class="wave-banner">{title}</div>')
            i += 1
            continue

        # Titre de section H2
        if stripped.startswith('## '):
            close_list()
            title = clean_inline(stripped[3:])
            sec_id = f"sec-{len(toc_items)+1}"
            toc_items.append((2, title, sec_id))
            body_html.append(f'<h2 id="{sec_id}" class="section-heading">{title}</h2>')
            i += 1
            continue

        # Titre de sous-section H3
        if stripped.startswith('### '):
            close_list()
            title = clean_inline(stripped[4:])
            sec_id = f"sec-{len(toc_items)+1}"
            toc_items.append((3, title, sec_id))
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
        toc_lines = ['<h2 class="section-heading">Table des Matières</h2>', '<ul style="list-style: none; padding-left: 0; font-size: 9pt; line-height: 1.6;">']
        for level, title, sec_id in toc_items:
            indent = "0" if level == 1 else ("16pt" if level == 2 else "32pt")
            font_weight = "bold" if level == 1 else "normal"
            toc_lines.append(f'<li style="padding-left: {indent}; font-weight: {font_weight};"><a href="#{sec_id}" style="text-decoration: none; color: #0F2A4A;">{title}</a></li>')
        toc_lines.append('</ul><div style="page-break-after: always;"></div>')
        toc_html = '\n'.join(toc_lines)

    # Cartouche administratif normalise ou en-tete compact
    if no_cartouche:
        header_meta_html = f"""
    <div class="cartouche-compact">
      <span><strong>Reference :</strong> <code class="latex-code">{meta.get('ref', 'GLOP-2026-LIVRABLE-v1.0')}</code></span> &nbsp;|&nbsp;
      <span><strong>Statut :</strong> <span class="badge badge-success">{meta.get('status', 'Version 1.0 Formelle')}</span></span> &nbsp;|&nbsp;
      <span><strong>Date :</strong> {meta.get('date', '17 Septembre 2026')}</span>
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
        <tr><th>Date & Statut</th><td>{meta.get('date', '17 Septembre 2026')} — <span class="badge badge-success">{meta.get('status', 'Version 1.0 Formelle')}</span></td></tr>
        <tr><th>Tag Communications</th><td><code class="latex-code">[GLOP]</code> (obligatoire dans tout objet de courriel)</td></tr>
        <tr><th>Transparence IA</th><td>Ce document a ete structure avec l assistance d outils d ingenierie logicielle.</td></tr>
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

def main():
    parser = argparse.ArgumentParser(description="Moteur de compilation universel de livrables ShopLoc")
    parser.add_argument("source", nargs="?", help="Fichier Markdown ou HTML source a compiler")
    parser.add_argument("--output", "-o", help="Chemin du PDF de sortie")
    parser.add_argument("--title", "-t", default="Livrable Officiel ShopLoc", help="Titre du document")
    parser.add_argument("--subtitle", "-s", default="Master 2 MIAGE — UE GLOP", help="Sous-titre du document")
    parser.add_argument("--ref", "-r", default="GLOP-2026-LIVRABLE-v1.0", help="Reference documentaire")
    parser.add_argument("--toc", action="store_true", help="Generer automatiquement une Table des Matieres")
    parser.add_argument("--no-cartouche", action="store_true", help="Ne pas afficher le grand cartouche administratif et permettre l enchainement direct du contenu")
    parser.add_argument("--preview-styleguide", action="store_true", help="Compiler le guide de style visuel en PDF")

    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    agent_projet_dir = os.path.join(project_root, "agent_projet")
    design_dir = os.path.join(agent_projet_dir, "design")
    docs_dir = os.path.join(agent_projet_dir, "docs")
    assets_dir = os.path.join(docs_dir, "assets")
    theme_css_path = os.path.join(design_dir, "theme.css")

    edge_bin = find_edge_binary()
    b64_univ, b64_fst = get_base64_logos(assets_dir)

    with open(theme_css_path, "r", encoding="utf-8") as f:
        theme_css = f.read()

    # Mode aperçu du guide de style
    if args.preview_styleguide:
        styleguide_html_path = os.path.join(design_dir, "styleguide.html")
        output_pdf = os.path.join(design_dir, "Styleguide_ShopLoc_Officiel.pdf")
        with open(styleguide_html_path, "r", encoding="utf-8") as f:
            sg_html = f.read()
        compile_html_to_pdf(sg_html, output_pdf, edge_bin)
        return

    if not args.source:
        print("Veuillez specifier un fichier source Markdown ou utiliser --preview-styleguide.")
        sys.exit(1)

    source_path = os.path.abspath(args.source)
    output_pdf = args.output or source_path.replace(".md", ".pdf")

    # Verification de securite pre-compilation
    try:
        import verify_deliverables
        registry = verify_deliverables.load_canary_registry()
        violations = verify_deliverables.check_file(source_path, registry)
        if violations:
            print("[ECHEC SECURITE] Le fichier contient des violations critiques :")
            for v in violations:
                print(f"  [{v['type']}] {v['location']} : {v['detail']}")
            sys.exit(1)
    except Exception as e:
        print(f"[Avertissement Securite] : {e}")

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

import base64
import os
import re
import subprocess
import pymupdf

def clean_inline(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.*?)`', r'<code class="latex-code">\1</code>', text)
    return text

def parse_markdown_to_latex_html(md_text, b64_univ, b64_fst):
    lines = md_text.split('\n')
    
    html_parts = []
    in_table = False
    table_rows = []
    in_list = False
    in_question = False
    
    section_num = 0
    question_in_section = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Skip original logo HTML or separator comments
        if '<div align="center"' in line or '<!-- EN-TÊTE' in line or 'assets/logo_' in line or '</table>' in line and not in_table:
            i += 1
            continue
        if '<tr' in line or '<td' in line or '</div>' in line and not in_table:
            i += 1
            continue
            
        # Tables
        if stripped.startswith('|') and stripped.endswith('|'):
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(stripped)
            i += 1
            continue
        elif in_table:
            in_table = False
            html_parts.append('<div class="table-wrapper"><table class="booktabs">')
            is_header = True
            for r in table_rows:
                cells = [c.strip() for c in r.strip('|').split('|')]
                if all(re.match(r'^:?-+:?$', c) for c in cells):
                    is_header = False
                    continue
                tag = 'th' if is_header else 'td'
                row_str = '<tr>' + ''.join(f'<{tag}>{clean_inline(c)}</{tag}>' for c in cells) + '</tr>'
                html_parts.append(row_str)
            html_parts.append('</table></div>')
            table_rows = []

        # Empty lines
        if not stripped:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            i += 1
            continue

        # Skip main markdown H1/H2 if rendered in title block
        if stripped.startswith('# QUESTIONNAIRE D\'INSTRUCTION'):
            i += 1
            continue
        if stripped.startswith('## Cadrage Fonctionnel'):
            i += 1
            continue
            
        # Metadata section title
        if stripped.startswith('## Informations Générales'):
            html_parts.append('<h2 class="latex-section-table-title">Informations Générales sur le Document</h2>')
            i += 1
            continue

        # Objectif du document / Abstract
        if stripped.startswith('### Objectif du Document'):
            if in_question:
                html_parts.append('</div>')
                in_question = False
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            abstract_paras = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('---') and not lines[i].strip().startswith('## '):
                if lines[i].strip():
                    abstract_paras.append(clean_inline(lines[i].strip()))
                i += 1
            html_parts.append('<div class="latex-abstract">')
            html_parts.append('<div class="latex-abstract-title">Préambule & Objectif du Questionnaire</div>')
            for p in abstract_paras:
                html_parts.append(f'<p class="latex-abstract-p">{p}</p>')
            html_parts.append('</div>')
            continue

        # Section headers
        if stripped.startswith('## '):
            if in_question:
                html_parts.append('</div>')
                in_question = False
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            sec_title = clean_inline(stripped[3:])
            section_num += 1
            question_in_section = 0
            html_parts.append(f'<h2 class="latex-section">{sec_title}</h2>')
            i += 1
            continue

        # Question header
        if stripped.startswith('### Q.'):
            if in_question:
                html_parts.append('</div>')
                in_question = False
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            in_question = True
            question_in_section += 1
            q_title = clean_inline(stripped[4:])
            html_parts.append('<div class="latex-question-block">')
            html_parts.append(f'<h3 class="latex-question-heading">Question {section_num}.{question_in_section} ({q_title})</h3>')
            i += 1
            continue

        # Question body
        if stripped.startswith('* **La question** :'):
            content = stripped[len('* **La question** :'):].strip()
            html_parts.append(f'<p class="latex-question-statement"><strong>Question :</strong> {clean_inline(content)}</p>')
            i += 1
            continue

        # Question interest
        if stripped.startswith('* **L\'intérêt** :'):
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            content = stripped[len('* **L\'intérêt** :'):].strip()
            html_parts.append(f'<p class="latex-question-interest"><strong>Intérêt pour le projet :</strong> {clean_inline(content)}</p>')
            i += 1
            continue

        # List items
        if stripped.startswith('- ') or stripped.startswith('* '):
            if not in_list:
                html_parts.append('<ul class="latex-itemize">')
                in_list = True
            item_text = clean_inline(stripped[2:])
            html_parts.append(f'<li>{item_text}</li>')
            i += 1
            continue

        # Sub-list items (indented)
        if stripped.startswith('  - ') or stripped.startswith('    * ') or stripped.startswith('  * '):
            if not in_list:
                html_parts.append('<ul class="latex-itemize">')
                in_list = True
            item_text = clean_inline(stripped.lstrip('-* '))
            html_parts.append(f'<li>{item_text}</li>')
            i += 1
            continue

        # Dividers
        if stripped == '---':
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            i += 1
            continue

        # Regular paragraphs
        if in_list:
            html_parts.append('</ul>')
            in_list = False
        html_parts.append(f'<p class="latex-p">{clean_inline(stripped)}</p>')
        i += 1

    if in_table:
        html_parts.append('<div class="table-wrapper"><table class="booktabs">')
        is_header = True
        for r in table_rows:
            cells = [c.strip() for c in r.strip('|').split('|')]
            if all(re.match(r'^:?-+:?$', c) for c in cells):
                is_header = False
                continue
            tag = 'th' if is_header else 'td'
            row_str = '<tr>' + ''.join(f'<{tag}>{clean_inline(c)}</{tag}>' for c in cells) + '</tr>'
            html_parts.append(row_str)
        html_parts.append('</table></div>')

    if in_list:
        html_parts.append('</ul>')
    if in_question:
        html_parts.append('</div>')

    body_html = '\n'.join(html_parts)

    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Questionnaire de Cadrage Métier — Projet ShopLoc</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/latin-modern-web@1.0.0/style.css">
<style>
  @page {{
    size: A4 portrait;
    margin: 24mm 20mm 24mm 20mm;
    @top-left {{
      content: "Projet ShopLoc — Questionnaire de Cadrage Métier";
      font-family: "Latin Modern Roman", "Computer Modern", "Times New Roman", Times, serif;
      font-size: 8.5pt;
      font-style: italic;
      color: #333333;
      border-bottom: 0.5pt solid #888888;
      padding-bottom: 4pt;
      margin-bottom: 8pt;
    }}
    @top-right {{
      content: "Master 2 MIAGE — UE GLOP (2026-2027)";
      font-family: "Latin Modern Roman", "Computer Modern", "Times New Roman", Times, serif;
      font-size: 8.5pt;
      font-style: italic;
      color: #333333;
      border-bottom: 0.5pt solid #888888;
      padding-bottom: 4pt;
      margin-bottom: 8pt;
    }}
    @bottom-center {{
      content: counter(page);
      font-family: "Latin Modern Roman", "Computer Modern", "Times New Roman", Times, serif;
      font-size: 9.5pt;
      color: #111111;
    }}
  }}

  @page :first {{
    @top-left {{
      content: "";
      border-bottom: none;
    }}
    @top-right {{
      content: "";
      border-bottom: none;
    }}
    @bottom-center {{
      content: "1";
    }}
  }}

  *, *:before, *:after {{
    box-sizing: border-box;
  }}

  body {{
    font-family: "Latin Modern Roman", "LM Roman 10", "Computer Modern", "TeX Gyre Termes", "Times New Roman", Times, serif;
    font-size: 10pt;
    line-height: 1.38;
    color: #000000;
    background: #ffffff;
    margin: 0;
    padding: 0;
    text-align: justify;
    text-justify: inter-word;
    hyphens: auto;
  }}

  /* HEADER WITH LOGOS */
  .institution-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12pt;
    padding-bottom: 8pt;
    border-bottom: 0.6pt solid #000000;
  }}

  .institution-logo {{
    height: 42px;
    max-width: 210px;
    object-fit: contain;
  }}

  /* DOCUMENT TITLE */
  .title-block {{
    text-align: center;
    margin-top: 14pt;
    margin-bottom: 18pt;
  }}

  .latex-main-title {{
    font-size: 15pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin: 0 0 6pt 0;
    line-height: 1.25;
  }}

  .latex-sub-title {{
    font-size: 11pt;
    font-style: italic;
    color: #222222;
    margin: 0 0 10pt 0;
  }}

  .latex-section-table-title {{
    font-size: 11pt;
    font-weight: bold;
    margin-top: 14pt;
    margin-bottom: 6pt;
    text-align: left;
    page-break-after: avoid;
  }}

  /* BOOKTABS TABLE */
  .table-wrapper {{
    margin: 8pt 0 14pt 0;
    width: 100%;
  }}

  table.booktabs {{
    width: 100%;
    border-collapse: collapse;
    font-size: 9pt;
    line-height: 1.35;
    border-top: 1.5pt solid #000000;
    border-bottom: 1.5pt solid #000000;
  }}

  table.booktabs th:first-child, table.booktabs td:first-child {{
    width: 32%;
  }}

  table.booktabs th:last-child, table.booktabs td:last-child {{
    width: 68%;
  }}

  table.booktabs th {{
    font-weight: bold;
    text-align: left;
    padding: 5pt 7pt;
    border-bottom: 0.75pt solid #000000;
    background: transparent;
  }}

  table.booktabs td {{
    padding: 4pt 7pt;
    vertical-align: top;
    border-bottom: 0.3pt solid #e0e0e0;
    background: transparent;
  }}

  table.booktabs tr:last-child td {{
    border-bottom: none;
  }}

  /* ABSTRACT / PREAMBLE */
  .latex-abstract {{
    margin: 12pt 20pt 16pt 20pt;
    padding: 6pt 12pt;
    border-top: 0.5pt solid #888888;
    border-bottom: 0.5pt solid #888888;
  }}

  .latex-abstract-title {{
    font-size: 10pt;
    font-weight: bold;
    text-align: center;
    margin-bottom: 4pt;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}

  .latex-abstract-p {{
    font-size: 9pt;
    font-style: italic;
    line-height: 1.35;
    margin: 0;
    text-align: justify;
  }}

  /* NUMBERED SECTION */
  h2.latex-section {{
    font-size: 11.5pt;
    font-weight: bold;
    color: #000000;
    margin-top: 18pt;
    margin-bottom: 6pt;
    padding-bottom: 2pt;
    border-bottom: 0.5pt solid #666666;
    page-break-after: avoid;
    text-align: left;
  }}

  /* QUESTION BLOCK */
  .latex-question-block {{
    margin-top: 8pt;
    margin-bottom: 10pt;
    page-break-inside: avoid;
  }}

  h3.latex-question-heading {{
    font-size: 10pt;
    font-weight: bold;
    color: #000000;
    margin: 0 0 3pt 0;
    page-break-after: avoid;
    text-align: left;
  }}

  .latex-question-statement {{
    font-size: 9.5pt;
    margin: 0 0 3pt 0;
    line-height: 1.35;
    text-align: justify;
  }}

  .latex-question-interest {{
    font-size: 9.5pt;
    margin: 4pt 0 0 0;
    line-height: 1.35;
    text-align: justify;
    font-style: italic;
  }}

  .latex-question-interest strong {{
    font-style: normal;
  }}

  /* ITEMIZE LIST */
  ul.latex-itemize {{
    margin: 3pt 0 4pt 16pt;
    padding: 0;
    font-size: 9.5pt;
    line-height: 1.35;
  }}

  ul.latex-itemize li {{
    margin-bottom: 2pt;
    text-align: justify;
  }}

  .latex-p {{
    font-size: 9.5pt;
    line-height: 1.35;
    margin: 4pt 0;
    text-align: justify;
  }}

  .latex-code {{
    font-family: "Latin Modern Mono", "Courier New", Courier, monospace;
    font-size: 8.5pt;
    color: #000000;
    background: transparent;
  }}
</style>
</head>
<body>

<div class="institution-header">
  <img class="institution-logo" src="data:image/png;base64,{b64_univ}" alt="Université de Lille">
  <img class="institution-logo" src="data:image/png;base64,{b64_fst}" alt="Faculté des Sciences et Technologies - Département Informatique">
</div>

<div class="title-block">
  <h1 class="latex-main-title">Questionnaire de Cadrage Métier</h1>
  <div class="latex-sub-title">Projet ShopLoc — Clarification des Besoins & Levée des Zones d'Ombre (Livrable R1)</div>
</div>

{body_html}

</body>
</html>
"""
    return full_html

def main():
    root = r"c:\Users\hpome\Documents\M2_MIAGE\GLOP\ShopLoc"
    md_path = os.path.join(root, "docs", "QUESTIONNAIRE_METIER_DETAILLE.md")
    html_path = os.path.join(root, "docs", "ShopLoc_Cadrage_Metier.html")
    pdf_path = os.path.join(root, "docs", "ShopLoc_Cadrage_Metier_Livrable_R1.pdf")
    
    univ_logo = os.path.join(root, "docs", "assets", "logo_univ_lille.png")
    fst_logo = os.path.join(root, "docs", "assets", "logo_fst_informatique.png")

    with open(univ_logo, "rb") as f:
        b64_univ = base64.b64encode(f.read()).decode("utf-8")

    with open(fst_logo, "rb") as f:
        b64_fst = base64.b64encode(f.read()).decode("utf-8")

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    full_html = parse_markdown_to_latex_html(md_content, b64_univ, b64_fst)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print("HTML generated successfully:", html_path)

    edge_bin = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    args = [
        edge_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    
    subprocess.run(args, check=True)
    
    if os.path.exists(pdf_path):
        size = os.path.getsize(pdf_path)
        doc = pymupdf.open(pdf_path)
        print(f"SUCCESS: Generated PDF at {pdf_path} (Size: {size} bytes, Pages: {len(doc)})")
        
        # Automatic Google Drive synchronization
        try:
            import drive_sync
            drive_sync.sync_to_drive(pdf_path)
        except Exception as e:
            print(f"[Drive Sync Note] Could not sync automatically: {e}")
    else:
        print("ERROR: PDF was not generated.")

if __name__ == "__main__":
    main()

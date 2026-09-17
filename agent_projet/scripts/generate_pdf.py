import base64
import os
import re
import subprocess
import pymupdf
import shutil

def clean_inline(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.*?)`', r'<code class="latex-code">\1</code>', text)
    return text

def parse_markdown_to_latex_html(md_text, b64_univ, b64_fst, version="2.0"):
    lines = md_text.split('\n')
    
    html_parts = []
    in_list = False
    in_question = False
    
    if version == "1.0":
        doc_sub_title = "Projet ShopLoc — Clarification des Besoins & Levée des Zones d'Ombre (Livrable R1)"
        top_left_title = "Projet ShopLoc — Questionnaire de Cadrage Métier (v1.0)"
        doc_titre = "Questionnaire de cadrage fonctionnel (Première vague — Questions initiales)"
        doc_ref = "GLOP-2026-R1-QUESTIONNAIRE-v1.0"
        doc_date = "07 Septembre 2026"
        doc_statut = "Version 1.0 — Document initial de cadrage (Première vague instruite)"
        preamble_text = "Dans le cadre de l'UE GLOP et de la préparation de notre réponse technique et financière (Livrable R1), notre équipe d'étudiants a analysé l'ensemble des besoins présentés dans le sujet ShopLoc. Afin de concevoir une architecture logicielle adaptée et de lever toute ambiguïté sur les règles de gestion, nous formalisons dans ce document l'ensemble des questions de cadrage initiales et les premiers arbitrages validés avec la MOA."
    else:
        doc_sub_title = "Projet ShopLoc — Clarification des Besoins & Levée des Zones d'Ombre (Livrables R1 & R3)"
        top_left_title = "Projet ShopLoc — Questionnaire de Cadrage Métier (v2.0)"
        doc_titre = "Questionnaire de cadrage fonctionnel approfondi (Première vague instruite & Seconde vague d'approfondissement)"
        doc_ref = "GLOP-2026-R1-QUESTIONNAIRE-CONSOLIDE-v2.0"
        doc_date = "12 Septembre 2026"
        doc_statut = "Version 2.0 — Consolidée suite aux premiers retours MOA et enrichie de la seconde vague"
        preamble_text = "Dans le cadre de l'UE GLOP et de la préparation de notre réponse technique et financière (Livrable R1), notre équipe d'étudiants a analysé l'ensemble des besoins présentés dans le sujet ShopLoc. Afin de concevoir une architecture logicielle adaptée et de lever toute ambiguïté sur les règles de gestion, nous structurons ce document en deux temps : la première vague consignant les réponses et arbitrages d'ores et déjà validés lors du premier échange avec la MOA, et la seconde vague formulant les questions d'approfondissement méthodologique pour la prochaine entrevue."

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Skip top markdown title and preamble text in markdown
        if stripped.startswith('# Questionnaire de Cadrage Métier') or stripped.startswith('Ce document recense') or stripped.startswith('- Les réponses et') or stripped.startswith('- Les questions restant'):
            i += 1
            continue
            
        if stripped == '---':
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            i += 1
            continue

        if not stripped:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            i += 1
            continue

        # Major wave titles (H1)
        if stripped.startswith('# Première Vague'):
            if in_question:
                html_parts.append('</div>')
                in_question = False
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            html_parts.append('<div class="latex-wave-banner">Première Vague : Questions de Cadrage Initiales (Séance du 07/09/2026)</div>')
            i += 1
            continue

        if stripped.startswith('# SECONDE VAGUE') or stripped.startswith('# Seconde Vague'):
            if version == "1.0":
                # V1 stops at the end of the first wave
                break
            if in_question:
                html_parts.append('</div>')
                in_question = False
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            html_parts.append('<div class="latex-wave-banner" style="margin-top: 24pt; border-top: 1.5pt solid #000000; padding-top: 14pt;">Seconde Vague : Questions d\'Approfondissement Métier (Pour la 2nde Entrevue MOA)</div>')
            i += 1
            continue

        # Section headers (H2)
        if stripped.startswith('## '):
            if in_question:
                html_parts.append('</div>')
                in_question = False
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            sec_title = clean_inline(stripped[3:])
            html_parts.append(f'<h2 class="latex-section">{sec_title}</h2>')
            i += 1
            continue

        # Question header (H3)
        if stripped.startswith('### Question'):
            if in_question:
                html_parts.append('</div>')
                in_question = False
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            in_question = True
            q_title = clean_inline(stripped[4:])
            html_parts.append('<div class="latex-question-block">')
            html_parts.append(f'<h3 class="latex-question-heading">{q_title}</h3>')
            i += 1
            continue

        # Question statement
        if stripped.startswith('* **La question** :') or stripped.startswith('- **La question** :') or stripped.startswith('- **Question** :'):
            prefix_len = stripped.find(':') + 1
            content = stripped[prefix_len:].strip()
            html_parts.append(f'<p class="latex-question-statement"><strong>Question :</strong> {clean_inline(content)}</p>')
            i += 1
            continue

        # Context line inside question
        if stripped.startswith('* **Contexte** :') or stripped.startswith('- **Contexte** :'):
            prefix_len = stripped.find(':') + 1
            content = stripped[prefix_len:].strip()
            html_parts.append(f'<p class="latex-question-statement"><strong>Contexte :</strong> {clean_inline(content)}</p>')
            i += 1
            continue

        # Question interest
        if stripped.startswith('* **Intérêt pour le projet** :') or stripped.startswith('- **Intérêt pour le projet** :') or stripped.startswith('- **Intérêt projet** :'):
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            prefix_len = stripped.find(':') + 1
            content = stripped[prefix_len:].strip()
            html_parts.append(f'<p class="latex-question-interest"><strong>Intérêt pour le projet :</strong> {clean_inline(content)}</p>')
            i += 1
            continue

        # Validated decision (MOA answer in green)
        if 'color: #166534' in stripped:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            clean_text = re.sub(r'</?span[^>]*>', '', stripped)
            clean_text = re.sub(r'</?strong>', '', clean_text)
            clean_text = clean_text.strip('* ')
            if 'Réponse validée MOA' in clean_text or 'Arbitrage MOA' in clean_text:
                title = clean_text.rstrip(': ')
                body_lines = []
                j = i + 1
                while j < len(lines) and ('color: #166534' in lines[j] or (lines[j].strip() and not lines[j].strip().startswith('---') and not lines[j].strip().startswith('#') and not lines[j].strip().startswith('*') and not lines[j].strip().startswith('-') and not lines[j].strip().startswith('**'))):
                    l_clean = re.sub(r'</?span[^>]*>', '', lines[j].strip())
                    l_clean = re.sub(r'</?strong>', '', l_clean)
                    if l_clean:
                        body_lines.append(l_clean)
                    j += 1
                i = j
                full_body = ' '.join(body_lines)
                html_parts.append(f'<div class="latex-moa-decision"><strong>{title} :</strong> {clean_inline(full_body)}</div>')
                continue
            else:
                html_parts.append(f'<div class="latex-moa-decision">{clean_inline(clean_text)}</div>')
                i += 1
                continue

        # Pending decision (orange)
        if 'color: #c2410c' in stripped:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            clean_text = re.sub(r'</?span[^>]*>', '', stripped)
            clean_text = re.sub(r'</?strong>', '', clean_text)
            clean_text = clean_text.strip('* ')
            if 'En attente d\'arbitrage MOA' in clean_text or 'Statut :' in clean_text:
                title = clean_text.rstrip(': ')
                body_lines = []
                j = i + 1
                while j < len(lines) and ('color: #c2410c' in lines[j] or (lines[j].strip() and not lines[j].strip().startswith('---') and not lines[j].strip().startswith('#') and not lines[j].strip().startswith('*') and not lines[j].strip().startswith('-') and not lines[j].strip().startswith('**'))):
                    l_clean = re.sub(r'</?span[^>]*>', '', lines[j].strip())
                    l_clean = re.sub(r'</?strong>', '', l_clean)
                    if l_clean:
                        body_lines.append(l_clean)
                    j += 1
                i = j
                full_body = ' '.join(body_lines).strip()
                if title.startswith('Statut :') or title.startswith('Statut:'):
                    status_label = "Statut :"
                    status_val = title.split(':', 1)[1].strip()
                    if full_body:
                        html_parts.append(f'<div class="latex-moe-pending"><strong>{status_label}</strong> {status_val} — {clean_inline(full_body)}</div>')
                    else:
                        html_parts.append(f'<div class="latex-moe-pending"><strong>{status_label}</strong> {status_val}</div>')
                else:
                    if full_body:
                        html_parts.append(f'<div class="latex-moe-pending"><strong>{title} :</strong> {clean_inline(full_body)}</div>')
                    else:
                        html_parts.append(f'<div class="latex-moe-pending"><strong>{title}</strong></div>')
                continue
            else:
                html_parts.append(f'<div class="latex-moe-pending">{clean_inline(clean_text)}</div>')
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

        # Regular paragraphs
        if in_list:
            html_parts.append('</ul>')
            in_list = False
        html_parts.append(f'<p class="latex-p">{clean_inline(stripped)}</p>')
        i += 1

    if in_list:
        html_parts.append('</ul>')
    if in_question:
        html_parts.append('</div>')

    body_html = '\n'.join(html_parts)

    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Questionnaire de Cadrage Métier — Projet ShopLoc (Version {version})</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/latin-modern-web@1.0.0/style.css">
<style>
  @page {{
    size: A4 portrait;
    margin: 24mm 20mm 24mm 20mm;
    @top-left {{
      content: "{top_left_title}";
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
    text-align: left;
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
    width: 34%;
  }}

  table.booktabs th:last-child, table.booktabs td:last-child {{
    width: 66%;
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
    margin: 14pt 20pt 16pt 20pt;
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
    text-align: left;
  }}

  /* WAVE BANNER */
  .latex-wave-banner {{
    font-size: 12.5pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #000000;
    margin-top: 20pt;
    margin-bottom: 10pt;
    padding-bottom: 4pt;
    border-bottom: 1.2pt solid #000000;
    page-break-after: avoid;
  }}

  /* NUMBERED SECTION */
  h2.latex-section {{
    font-size: 11.5pt;
    font-weight: bold;
    color: #000000;
    margin-top: 16pt;
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
    text-align: left;
  }}

  .latex-moa-decision {{
    margin: 6pt 0 4pt 0;
    padding: 6pt 10pt;
    background-color: #f1f8f3;
    border-radius: 2pt;
    font-size: 9.5pt;
    color: #0f3e13;
    line-height: 1.45;
  }}

  .latex-moa-decision strong {{
    color: #1b5e20;
  }}

  .latex-moe-pending {{
    margin: 6pt 0 4pt 0;
    padding: 6pt 10pt;
    background-color: #fff9f5;
    border-radius: 2pt;
    font-size: 9.5pt;
    color: #7c2d12;
    line-height: 1.45;
  }}

  .latex-moe-pending strong {{
    color: #9a3412;
  }}

  .latex-question-interest {{
    font-size: 9.5pt;
    margin: 4pt 0 0 0;
    line-height: 1.35;
    text-align: left;
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
    text-align: left;
  }}

  .latex-p {{
    font-size: 9.5pt;
    line-height: 1.35;
    margin: 4pt 0;
    text-align: left;
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
  <div class="latex-sub-title">{doc_sub_title}</div>
</div>

<h2 class="latex-section-table-title">Informations Générales sur le Document</h2>
<div class="table-wrapper">
  <table class="booktabs">
    <tr><th>Champ</th><th>Information</th></tr>
    <tr><td><strong>Intitulé du Projet</strong></td><td>Projet ShopLoc — Marketplace & Fidélisation multi-commerces</td></tr>
    <tr><td><strong>Identifiant Officiel du Projet</strong></td><td><code class="latex-code">MiageShopLoc</code></td></tr>
    <tr><td><strong>Titre du Document</strong></td><td>{doc_titre}</td></tr>
    <tr><td><strong>Référence Documentaire</strong></td><td><code class="latex-code">{doc_ref}</code></td></tr>
    <tr><td><strong>Contexte Académique</strong></td><td>Master 2 MIAGE — UE Génie Logiciel par la Pratique (GLOP) 2026-2027, Université de Lille</td></tr>
    <tr><td><strong>Destinataires (MOA / MOD)</strong></td><td>Laurence Duchien, Anne Etien, François Secchi, Jérémy Woirhaye</td></tr>
    <tr><td><strong>Date de Soumission</strong></td><td>{doc_date}</td></tr>
    <tr><td><strong>Statut du Document</strong></td><td>{doc_statut}</td></tr>
    <tr><td><strong>Tag obligatoire communications</strong></td><td><code class="latex-code">[GLOP]</code> (à inclure dans tout objet de courriel)</td></tr>
    <tr><td><strong>Mention de transparence IA</strong></td><td>Ce document a été réalisé avec l'assistance d'une intelligence artificielle.</td></tr>
  </table>
</div>

<div class="latex-abstract">
  <div class="latex-abstract-title">Préambule & Objectif du Questionnaire</div>
  <p class="latex-abstract-p">{preamble_text}</p>
</div>

<div style="page-break-after: always;"></div>

{body_html}

</body>
</html>
"""
    return full_html

def compile_html_to_pdf(html_content, output_pdf_path, edge_bin):
    temp_html_path = output_pdf_path.replace(".pdf", "_temp.html")
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    args = [
        edge_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf_path}",
        temp_html_path
    ]
    subprocess.run(args, check=True)
    
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)

    if os.path.exists(output_pdf_path):
        size = os.path.getsize(output_pdf_path)
        doc = pymupdf.open(output_pdf_path)
        pages = len(doc)
        doc.close()
        print(f"SUCCESS: Generated PDF at {output_pdf_path} (Size: {size} bytes, Pages: {pages})")
        return True
    return False

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    agent_projet_dir = os.path.dirname(script_dir)
    docs_dir = os.path.join(agent_projet_dir, "docs")
    
    md_path = os.path.join(docs_dir, "QUESTIONNAIRE_METIER_DETAILLE.md")
    pdf_v1_path = os.path.join(docs_dir, "ShopLoc_Cadrage_Metier_Livrable_R1_v1.pdf")
    pdf_v2_path = os.path.join(docs_dir, "ShopLoc_Cadrage_Metier_Livrable_R1_v2.pdf")
    
    univ_logo = os.path.join(docs_dir, "assets", "logo_univ_lille.png")
    fst_logo = os.path.join(docs_dir, "assets", "logo_fst_informatique.png")

    with open(univ_logo, "rb") as f:
        b64_univ = base64.b64encode(f.read()).decode("utf-8")

    with open(fst_logo, "rb") as f:
        b64_fst = base64.b64encode(f.read()).decode("utf-8")

    # 1. Verification de securite pre-compilation (Canaris, Emojis, Pieges)
    try:
        import verify_deliverables
        registry = verify_deliverables.load_canary_registry()
        md_violations = verify_deliverables.check_file(md_path, registry)
        if md_violations:
            print("[ECHEC SECURITE] Le document source contient des violations critiques :")
            for v in md_violations:
                print(f"  [{v['type']}] {v['location']} : {v['detail']}")
            print("Generation du PDF annulee pour proteger le projet.")
            return
    except Exception as e:
        print(f"[Avertissement Securite] Verification pre-compilation : {e}")

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

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
    edge_bin = next((c for c in candidates if os.path.exists(c)), "msedge")

    # 2. Compile V1
    html_v1 = parse_markdown_to_latex_html(md_content, b64_univ, b64_fst, version="1.0")
    compile_html_to_pdf(html_v1, pdf_v1_path, edge_bin)

    # 3. Compile V2
    html_v2 = parse_markdown_to_latex_html(md_content, b64_univ, b64_fst, version="2.0")
    compile_html_to_pdf(html_v2, pdf_v2_path, edge_bin)

    # 4. Verification de securite post-compilation sur les deux PDFs
    try:
        import verify_deliverables
        registry = verify_deliverables.load_canary_registry()
        for p in [pdf_v1_path, pdf_v2_path]:
            pdf_violations = verify_deliverables.check_file(p, registry)
            if pdf_violations:
                print(f"[ALERTE CRITIQUE] Le PDF genere {p} contient des canaris ou des violations !")
                for v in pdf_violations:
                    print(f"  [{v['type']}] {v['location']} : {v['detail']}")
                os.remove(p)
                return
    except Exception as e:
        print(f"[Avertissement Securite] Verification post-compilation PDF : {e}")

    # 5. Synchronisation Google Drive et nettoyage
    drive_root = r"G:\Mon Drive\Projet-GLOP"
    drive_sub = os.path.join(drive_root, "01_Cadrage_Metier_R1")

    if os.path.isdir(drive_root):
        # Clean obsolete files on drive
        for obsolete in [os.path.join(drive_sub, "ShopLoc_Propositions_v3 (1).pdf"), os.path.join(drive_sub, "ShopLoc_Cadrage_Metier_Livrable_R1.pdf")]:
            if os.path.exists(obsolete):
                try:
                    os.remove(obsolete)
                    print(f"[Drive Cleanup] Removed obsolete file: {obsolete}")
                except Exception as e:
                    print(f"[Drive Cleanup Warning] Could not remove {obsolete}: {e}")

        # Nettoyage des fichiers a la racine du Drive pour garder une arborescence propre
        for fname in ["ShopLoc_Cadrage_Metier_Livrable_R1_v1.pdf", "ShopLoc_Cadrage_Metier_Livrable_R1_v2.pdf", "ShopLoc_Cadrage_Metier_Livrable_R1.pdf"]:
            root_file = os.path.join(drive_root, fname)
            if os.path.exists(root_file):
                try:
                    os.remove(root_file)
                    print(f"[Drive Cleanup] Supprime de la racine Drive : {fname}")
                except Exception as e:
                    print(f"[Drive Cleanup Warning] Impossible de supprimer {root_file} : {e}")

        # Deploiement exclusif de V1 et V2 dans le dossier dedie 01_Cadrage_Metier_R1
        os.makedirs(drive_sub, exist_ok=True)
        for pdf_file in [pdf_v1_path, pdf_v2_path]:
            fname = os.path.basename(pdf_file)
            shutil.copy2(pdf_file, os.path.join(drive_sub, fname))
        
        print(f"[Drive Sync OK] Synchronise V1 et V2 exclusivement dans {drive_sub}")

    # 6. Nettoyage des fichiers HTML intermediaires dans agent_projet/docs
    for f in ["ShopLoc_Cadrage_Metier.html", "ShopLoc_Cadrage_Metier_v2.html", "ShopLoc_Cadrage_Metier_v1_temp.html", "ShopLoc_Cadrage_Metier_v2_temp.html"]:
        p = os.path.join(docs_dir, f)
        if os.path.exists(p):
            os.remove(p)
            print(f"[Local Cleanup] Removed intermediate file: {f}")

if __name__ == "__main__":
    main()

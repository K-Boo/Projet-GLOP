#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur du diagramme de Gantt annuel officiel et détaillé (Figure 5.1).
Style professionnel haute précision MIAGE GLOP, intégrant la décomposition WBS,
le calendrier universitaire 2026-2027 (semaine IA, congés), le tracé du chemin
critique et le découpage fin du composant vertical Panier 2PC pour R4.
"""
import os
import pymupdf

def generate_gantt():
    svg_parts = []
    
    # Dimensions: 1960 x 1140 px for perfect spacing and 0 text collision
    width = 1960
    height = 1140
    sidebar_w = 550
    timeline_x = 570
    timeline_w = width - timeline_x - 30  # 1360 px
    
    # 7 Months: Sept 2026 to March 2027 (29 calendar weeks)
    total_weeks = 29
    col_w = timeline_w / total_weeks
    
    # Header and defs
    svg_parts.append(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif; background-color: #FAF9F6;">
  <defs>
    <filter id="shadow-soft" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#243342" flood-opacity="0.08"/>
    </filter>
    <filter id="shadow-bar" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#000000" flood-opacity="0.12"/>
    </filter>
    <marker id="arrow-crit" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 2 L 8 5 L 0 8 z" fill="#DC2626" />
    </marker>
    <marker id="arrow-amber" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 2 L 8 5 L 0 8 z" fill="#D97706" />
    </marker>
  </defs>

  <!-- FOND GLOBAL -->
  <rect x="15" y="15" width="{width - 30}" height="{height - 30}" rx="12" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1.5" />

  <!-- EN-TETE PRINCIPAL -->
  <rect x="15" y="15" width="{width - 30}" height="70" rx="12" fill="#243342" />
  <rect x="15" y="65" width="{width - 30}" height="20" fill="#243342" />
  <text x="40" y="55" font-size="20" font-weight="800" fill="#FFFFFF">ShopLoc · Diagramme de Gantt Annuel &amp; Chemin Critique (2026-2027)</text>
  <text x="960" y="54" font-size="13" font-weight="500" fill="#DCD6CD">Master 2 MIAGE · Entreprise Garik · Planification Opérationnelle &amp; Découpage Fin des Releases R1 à R5</text>

  <!-- SIDEBAR EN-TETE -->
  <rect x="15" y="85" width="{sidebar_w}" height="45" fill="#F4F2EC" stroke="#DCD6CD" stroke-width="1"/>
  <text x="35" y="112" font-size="11" font-weight="700" fill="#243342" text-transform="uppercase" letter-spacing="1">Réf / Tâche WBS</text>
  <text x="380" y="112" font-size="11" font-weight="700" fill="#243342" text-transform="uppercase" letter-spacing="1">Resp.</text>
  <text x="515" y="112" font-size="11" font-weight="700" fill="#243342" text-transform="uppercase" letter-spacing="1">Durée</text>
""")

    # Timeline Header: Months & Weeks
    months_data = [
        ("Septembre 2026", 0, 4),
        ("Octobre 2026", 4, 4),
        ("Novembre 2026", 8, 4.5),
        ("Décembre 2026", 12.5, 3.5),
        ("Janvier 2027", 16, 4.5),
        ("Février 2027", 20.5, 4),
        ("Mars 2027", 24.5, 4.5)
    ]

    svg_parts.append(f'  <!-- GRILLE CALENDRIER -->')
    svg_parts.append(f'  <g transform="translate({timeline_x}, 85)">')
    svg_parts.append(f'    <rect x="0" y="0" width="{timeline_w}" height="45" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1"/>')

    # Draw month blocks
    for m_name, m_start, m_len in months_data:
        mx = m_start * col_w
        mw = m_len * col_w
        svg_parts.append(f'    <rect x="{mx}" y="0" width="{mw}" height="25" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>')
        svg_parts.append(f'    <text x="{mx + mw/2}" y="17" text-anchor="middle" font-size="11" font-weight="700" fill="#243342">{m_name}</text>')

    # Draw 29 week indicators
    for w in range(total_weeks):
        wx = w * col_w
        svg_parts.append(f'    <rect x="{wx}" y="25" width="{col_w}" height="20" fill="#FFFFFF" stroke="#EDE8E1" stroke-width="0.8"/>')
        w_label = f"S{w+1:02d}"
        svg_parts.append(f'    <text x="{wx + col_w/2}" y="39" text-anchor="middle" font-size="8.5" font-weight="600" fill="#606B76">{w_label}</text>')
        # Vertical grid line across chart
        svg_parts.append(f'    <line x1="{wx}" y1="45" x2="{wx}" y2="{height - 90}" stroke="#F0ECE1" stroke-width="0.8" />')

    svg_parts.append('  </g>')

    # TASKS DATA: Structured by Phase with High Granularity
    rows = [
        # WP1
        {"type": "header", "title": "LOT 1 : Cadrage Métier & Appel d'Offres (Jalon R1)", "color": "#1E293B"},
        {"type": "task", "wbs": "T-01", "title": "Analyse du besoin APTE, Bête à cornes & Fonctions", "resp": "Abdelkader", "dur": "1 sem.", "start": 0, "len": 1.0, "crit": True, "c": "#334155"},
        {"type": "task", "wbs": "T-02", "title": "Personas, BPMN 2.0 (P1-P5) & Modélisation Merise 3NF", "resp": "Ilyas / Gautam", "dur": "1.5 sem.", "start": 1.0, "len": 1.5, "crit": True, "c": "#334155"},
        {"type": "task", "wbs": "T-03", "title": "Cahier des charges R1, Backlog MoSCoW & Évaluation coûts", "resp": "Collectif", "dur": "0.5 sem.", "start": 2.2, "len": 0.6, "crit": True, "c": "#334155", "m": "R1 (18/09)"},
        
        # WP2
        {"type": "header", "title": "LOT 2 : Outillage Logiciel & Socle DevOps (Jalon R2)", "color": "#C2410C"},
        {"type": "task", "wbs": "T-04", "title": "Forge GitLab, branches protégées & convention de commit", "resp": "Rayane", "dur": "1 sem.", "start": 3.0, "len": 1.0, "crit": True, "c": "#EA580C"},
        {"type": "task", "wbs": "T-05", "title": "Justifications d'outils & Guide d'installation multi-OS", "resp": "Abdelkader", "dur": "1 sem.", "start": 4.0, "len": 1.0, "crit": True, "c": "#EA580C"},
        {"type": "task", "wbs": "T-06", "title": "Pipeline GitLab CI, SonarQube (80%) & Docker multi-stage", "resp": "Khalil / Rayane", "dur": "1 sem.", "start": 5.0, "len": 1.0, "crit": True, "c": "#EA580C", "m": "R2 (12/10)"},

        # WP3
        {"type": "header", "title": "LOT 3 : Modélisation Économique & Rentabilité (Jalon R3)", "color": "#A16207"},
        {"type": "task", "wbs": "T-07", "title": "Ventilation heures d'ingénierie (1000h) & Centres d'analyse", "resp": "Gautam", "dur": "2 sem.", "start": 6.0, "len": 2.0, "crit": False, "c": "#D97706"},
        {"type": "task", "wbs": "T-08", "title": "Unités d'Œuvre, P&L 3 ans, VAN, TRI & Seuil de rentabilité", "resp": "Gautam / Abd.", "dur": "3 sem.", "start": 9.0, "len": 3.0, "crit": False, "c": "#D97706", "m": "R3 (30/11)"},

        # WP4 - CŒUR DU SUJET : ARCHITECTURE ET PANIER 2PC
        {"type": "header", "title": "LOT 4 : Architecture C4 & Composant Panier 2PC (Jalon R4)", "color": "#6D28D9"},
        {"type": "task", "wbs": "T-09", "title": "Cas d'Utilisation Cockburn (UC-01 à 05) & Risques ISO 31000", "resp": "Abdelkader / Kh.", "dur": "2 sem.", "start": 6.0, "len": 2.0, "crit": True, "c": "#7C3AED"},
        {"type": "task", "wbs": "T-10", "title": "Architecture C4 4+1, DDL PostgreSQL 16 3NF & Multi-tenant", "resp": "Ilyas / Gautam", "dur": "1 sem.", "start": 9.0, "len": 1.0, "crit": True, "c": "#7C3AED"},
        {"type": "task", "wbs": "T-11", "title": "Contrat OpenAPI 3.1 & Simulateur Bancaire 2PC (Mock REST)", "resp": "Rayane", "dur": "1 sem.", "start": 10.0, "len": 1.0, "crit": True, "c": "#7C3AED"},
        {"type": "task", "wbs": "T-12", "title": "Backend Spring Boot 3.3 : Entités JPA & Service 2PC ACID", "resp": "Gautam / Rayane", "dur": "2 sem.", "start": 11.0, "len": 2.0, "crit": True, "c": "#7C3AED"},
        {"type": "task", "wbs": "T-13", "title": "Tests TDD automatisés unitaires & intégration (JUnit >= 80%)", "resp": "Khalil", "dur": "2 sem.", "start": 12.0, "len": 2.0, "crit": True, "c": "#7C3AED"},
        {"type": "task", "wbs": "T-14", "title": "Frontend React/TS : Catalogue, Panier & Sous-commandes", "resp": "Ilyas / Abd.", "dur": "2 sem.", "start": 13.0, "len": 2.0, "crit": True, "c": "#7C3AED"},
        {"type": "task", "wbs": "T-15", "title": "Assemblage Docker, Pitch RSE & Code Freeze J-3 (15/12)", "resp": "Collectif", "dur": "0.5 sem.", "start": 14.8, "len": 0.5, "crit": True, "c": "#7C3AED", "m": "R4 (18/12)"},

        # WP5 - SEMESTRE 4 : INDUSTRIALISATION V2
        {"type": "header", "title": "LOT 5 : Solution Industrielle V2 & Clôture (Jalon R5)", "color": "#047857"},
        {"type": "task", "wbs": "T-16", "title": "Moteur batch SQL de fidélité VFP (10 passages / 15j glissants)", "resp": "Gautam", "dur": "2 sem.", "start": 17.0, "len": 2.0, "crit": True, "c": "#059669"},
        {"type": "task", "wbs": "T-17", "title": "Caisse express marchande (< 3s), scan QR & catalogue cadeaux", "resp": "Ilyas", "dur": "2 sem.", "start": 18.0, "len": 2.0, "crit": True, "c": "#059669"},
        {"type": "task", "wbs": "T-18", "title": "Titres mobilité (Bus Ilévia & Parking 20 min) + Mocks voirie", "resp": "Rayane", "dur": "2 sem.", "start": 20.0, "len": 2.0, "crit": True, "c": "#059669"},
        {"type": "task", "wbs": "T-19", "title": "Supervision municipale DSI k-anonyme & Tournée piétonne TSP", "resp": "Abdelkader / Ily.", "dur": "2 sem.", "start": 22.0, "len": 2.0, "crit": False, "c": "#059669"},
        {"type": "task", "wbs": "T-20", "title": "Tests de charge Gatling, Eco-conception & Homologation V2", "resp": "Khalil / Rayane", "dur": "2 sem.", "start": 24.0, "len": 2.0, "crit": True, "c": "#059669"},
        {"type": "task", "wbs": "T-21", "title": "Release Docker clé en main, Code Freeze J-3 (16/03) & Oral", "resp": "Collectif", "dur": "0.5 sem.", "start": 26.5, "len": 0.5, "crit": True, "c": "#059669", "m": "R5 (19/03)"},

        # TRANSVERSE
        {"type": "header", "title": "LOT 6 : Gouvernance, Qualimétrie Continue & Revues DoD (Transverse)", "color": "#475569"},
        {"type": "task", "wbs": "T-22", "title": "Assurance Qualité DoD continue, SonarQube & Code Freeze J-3", "resp": "Khalil (QA)", "dur": "27 sem.", "start": 0, "len": 27.0, "crit": False, "c": "#94A3B8", "is_continuous": True}
    ]

    curr_y = 135
    row_height = 32
    header_height = 26
    task_positions = {}

    for r in rows:
        if r["type"] == "header":
            # Header row
            h_title = r["title"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            svg_parts.append(f'  <!-- Section Header: {h_title} -->')
            svg_parts.append(f'  <g transform="translate(15, {curr_y})">')
            svg_parts.append(f'    <rect x="0" y="0" width="{width - 30}" height="{header_height}" fill="{r["color"]}" opacity="0.95"/>')
            svg_parts.append(f'    <text x="20" y="18" font-size="11.5" font-weight="700" fill="#FFFFFF">{h_title}</text>')
            svg_parts.append(f'  </g>')
            curr_y += header_height + 2
        else:
            # Task row
            y = curr_y
            title_esc = r["title"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            svg_parts.append(f'  <!-- Task: {r["wbs"]} - {title_esc} -->')
            
            # Sidebar background
            bg_sidebar = "#FFFFFF" if (y // row_height) % 2 == 0 else "#FAF9F6"
            svg_parts.append(f'  <g transform="translate(15, {y})">')
            svg_parts.append(f'    <rect x="0" y="0" width="{sidebar_w}" height="{row_height}" fill="{bg_sidebar}" stroke="#EDE8E1" stroke-width="0.8"/>')
            
            # WBS tag
            crit_badge_color = "#DC2626" if r.get("crit") else "#64748B"
            crit_badge_bg = "#FEE2E2" if r.get("crit") else "#F1F5F9"
            svg_parts.append(f'    <rect x="10" y="7" width="44" height="18" rx="3" fill="{crit_badge_bg}" stroke="{crit_badge_color}" stroke-width="0.8"/>')
            svg_parts.append(f'    <text x="32" y="20" text-anchor="middle" font-size="9" font-weight="700" fill="{crit_badge_color}">{r["wbs"]}</text>')
            
            # Title (Spaced between x=64 and x=360)
            svg_parts.append(f'    <text x="64" y="20" font-size="10.5" font-weight="600" fill="#243342">{title_esc}</text>')
            
            # Resp (x=380)
            svg_parts.append(f'    <text x="380" y="20" font-size="9.5" font-weight="500" fill="#606B76">{r["resp"]}</text>')
            
            # Dur (x=525, right aligned)
            svg_parts.append(f'    <text x="525" y="20" text-anchor="end" font-size="9.5" font-weight="600" fill="#243342">{r["dur"]}</text>')
            svg_parts.append(f'  </g>')

            # Timeline bar
            bx = timeline_x + (r["start"] * col_w)
            bw = r["len"] * col_w
            task_positions[r["wbs"]] = {"x": bx, "y": y, "w": bw, "crit": r.get("crit", False)}

            svg_parts.append(f'  <g transform="translate({bx}, {y})">')
            if r.get("is_continuous"):
                svg_parts.append(f'    <rect x="0" y="10" width="{bw}" height="10" rx="5" fill="none" stroke="{r["c"]}" stroke-width="2" stroke-dasharray="6 4"/>')
                svg_parts.append(f'    <text x="{bw/2}" y="8" text-anchor="middle" font-size="8.5" font-weight="600" fill="#64748B">Supervision Qualité &amp; Code Freeze permanent</text>')
            else:
                bar_stroke = "#DC2626" if r.get("crit") else r["c"]
                bar_sw = "1.5" if r.get("crit") else "1"
                svg_parts.append(f'    <rect x="0" y="5" width="{bw}" height="20" rx="4" fill="{r["c"]}" stroke="{bar_stroke}" stroke-width="{bar_sw}" filter="url(#shadow-bar)"/>')
                if bw > 40:
                    svg_parts.append(f'    <text x="{bw/2}" y="19" text-anchor="middle" font-size="9" font-weight="700" fill="#FFFFFF">{r["wbs"]}</text>')
                
                # Milestone Diamond
                if r.get("m"):
                    m_x = bw + 8
                    svg_parts.append(f'    <path d="M {m_x + 8} 5 L {m_x + 16} 15 L {m_x + 8} 25 L {m_x} 15 Z" fill="#DC2626" filter="url(#shadow-bar)"/>')
                    svg_parts.append(f'    <text x="{m_x + 22}" y="19" font-size="10" font-weight="800" fill="#DC2626">{r["m"]}</text>')

            svg_parts.append(f'  </g>')
            curr_y += row_height + 2

    # LIAISONS ET CHEMIN CRITIQUE (FLÈCHES)
    svg_parts.append('  <!-- FLECHES DU CHEMIN CRITIQUE -->')
    crit_edges = [
        ("T-01", "T-02"),
        ("T-02", "T-03"),
        ("T-03", "T-04"),
        ("T-04", "T-05"),
        ("T-05", "T-06"),
        ("T-06", "T-09"),
        ("T-09", "T-10"),
        ("T-10", "T-11"),
        ("T-11", "T-12"),
        ("T-12", "T-13"),
        ("T-13", "T-14"),
        ("T-14", "T-15"),
        ("T-15", "T-16"),
        ("T-16", "T-17"),
        ("T-17", "T-18"),
        ("T-18", "T-20"),
        ("T-20", "T-21")
    ]
    for src, dst in crit_edges:
        if src in task_positions and dst in task_positions:
            p1 = task_positions[src]
            p2 = task_positions[dst]
            x1 = p1["x"] + p1["w"]
            y1 = p1["y"] + 15
            x2 = p2["x"]
            y2 = p2["y"] + 15
            
            # Routing
            if x2 >= x1:
                mid_x = (x1 + x2) / 2
                path = f"M {x1} {y1} L {mid_x} {y1} L {mid_x} {y2} L {x2} {y2}"
            else:
                # Loop back
                path = f"M {x1} {y1} L {x1 + 8} {y1} L {x1 + 8} {y1 + 16} L {x2 - 10} {y1 + 16} L {x2 - 10} {y2} L {x2} {y2}"
            svg_parts.append(f'  <path d="{path}" fill="none" stroke="#DC2626" stroke-width="1.2" stroke-dasharray="3 2" marker-end="url(#arrow-crit)"/>')

    # Ligne R3 non-critique (ambre)
    if "T-06" in task_positions and "T-07" in task_positions and "T-08" in task_positions:
        p_r2 = task_positions["T-06"]
        p_t7 = task_positions["T-07"]
        p_t8 = task_positions["T-08"]
        path_r3_1 = f"M {p_r2['x'] + p_r2['w']} {p_r2['y'] + 15} L {p_t7['x']} {p_t7['y'] + 15}"
        path_r3_2 = f"M {p_t7['x'] + p_t7['w']} {p_t7['y'] + 15} L {p_t8['x']} {p_t8['y'] + 15}"
        svg_parts.append(f'  <path d="{path_r3_1}" fill="none" stroke="#D97706" stroke-width="1.2" stroke-dasharray="3 2" marker-end="url(#arrow-amber)"/>')
        svg_parts.append(f'  <path d="{path_r3_2}" fill="none" stroke="#D97706" stroke-width="1.2" stroke-dasharray="3 2" marker-end="url(#arrow-amber)"/>')

    # LEGENDE BAS DE PAGE
    leg_y = curr_y + 18
    svg_parts.append(f'  <!-- LEGENDE -->')
    svg_parts.append(f'  <g transform="translate(30, {leg_y})">')
    svg_parts.append(f'    <rect x="0" y="0" width="{width - 60}" height="42" rx="6" fill="#F4F2EC" stroke="#DCD6CD" stroke-width="1"/>')
    # Legend items
    svg_parts.append(f'    <text x="20" y="26" font-size="11" font-weight="700" fill="#243342">LÉGENDE :</text>')
    
    # Critical Path
    svg_parts.append(f'    <rect x="120" y="15" width="24" height="14" rx="3" fill="#7C3AED" stroke="#DC2626" stroke-width="1.5"/>')
    svg_parts.append(f'    <text x="152" y="26" font-size="10.5" font-weight="600" fill="#243342">Chemin critique strict (Priorité P1)</text>')

    # Non-critical Path
    svg_parts.append(f'    <rect x="470" y="15" width="24" height="14" rx="3" fill="#D97706" stroke="#D97706" stroke-width="1"/>')
    svg_parts.append(f'    <text x="502" y="26" font-size="10.5" font-weight="600" fill="#243342">Tâche parallèle avec marge libre</text>')

    # Milestone diamond
    svg_parts.append(f'    <path d="M 800 15 L 808 22 L 800 29 L 792 22 Z" fill="#DC2626"/>')
    svg_parts.append(f'    <text x="818" y="26" font-size="10.5" font-weight="700" fill="#DC2626">Jalon contractuel MOA &amp; Rendu officiel</text>')

    # Code freeze rule
    svg_parts.append(f'    <rect x="1160" y="14" width="16" height="16" rx="3" fill="#FEE2E2" stroke="#DC2626" stroke-width="1"/>')
    svg_parts.append(f'    <text x="1184" y="26" font-size="10.5" font-weight="600" fill="#243342">Buffer Code Freeze J-3 (Aucun ajout fonctionnel)</text>')

    # Critical path arrows
    svg_parts.append(f'    <line x1="1540" y1="22" x2="1570" y2="22" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="3 2" marker-end="url(#arrow-crit)"/>')
    svg_parts.append(f'    <text x="1580" y="26" font-size="10.5" font-weight="600" fill="#243342">Dépendance du chemin critique</text>')

    svg_parts.append(f'  </g>')

    svg_parts.append('</svg>')
    
    svg_content = "\n".join(svg_parts)

    output_dir = os.path.abspath("agent_projet/docs/01_Cadrage_Et_Cahier_Des_Charges_R1/figures")
    os.makedirs(output_dir, exist_ok=True)
    svg_path = os.path.join(output_dir, "fig_5_1_gantt_annuel_officiel.svg")
    png_path = os.path.join(output_dir, "fig_5_1_gantt_annuel_officiel.png")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated SVG: {svg_path}")

    try:
        doc = pymupdf.open(svg_path)
        page = doc[0]
        pix = page.get_pixmap(dpi=300)
        pix.save(png_path)
        print(f"Generated PNG: {png_path} ({pix.width}x{pix.height})")
    except Exception as e:
        print(f"Failed to generate PNG using pymupdf: {e}")

if __name__ == "__main__":
    generate_gantt()

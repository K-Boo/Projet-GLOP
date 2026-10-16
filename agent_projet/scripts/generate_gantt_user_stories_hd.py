#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERATE GANTT USER STORIES HD (Figure 5.2)
Projet ShopLoc (MiageShopLoc) - M2 MIAGE GLOP 2026-2027
Inspire du GUIDE_PROMPTING_AGENTIQUE.md et de l'arbitrage R1 Soutenance

Ce script genere le diagramme de Gantt annuel haute definition granularise
par User Story INVEST (US-01 a US-18) synchronise avec le MVP R4 et les extensions R5.
"""

import os
import sys
from pathlib import Path

try:
    import pymupdf
    PYMUPDF_AVAILABLE = True
except ImportError:
    PYMUPDF_AVAILABLE = False


def generate_gantt_user_stories():
    width = 1960
    height = 1260
    sidebar_w = 580
    timeline_x = 600
    timeline_w = width - timeline_x - 30  # 1330 px

    total_weeks = 29
    col_w = timeline_w / total_weeks

    svg_parts = []
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
  </defs>

  <!-- FOND GLOBAL -->
  <rect x="15" y="15" width="{width - 30}" height="{height - 30}" rx="12" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1.5" />

  <!-- EN-TETE PRINCIPAL -->
  <rect x="15" y="15" width="{width - 30}" height="70" rx="12" fill="#243342" />
  <rect x="15" y="65" width="{width - 30}" height="20" fill="#243342" />
  <text x="40" y="55" font-size="20" font-weight="800" fill="#FFFFFF">ShopLoc · Diagramme de Gantt Granulaire par User Story INVEST (2026-2027)</text>
  <text x="960" y="54" font-size="13" font-weight="500" fill="#DCD6CD">Master 2 MIAGE · Entreprise Garik · Planification Agile Alignée sur le MVP R4 &amp; Extensions R5</text>

  <!-- SIDEBAR EN-TETE -->
  <rect x="15" y="85" width="{sidebar_w}" height="45" fill="#F4F2EC" stroke="#DCD6CD" stroke-width="1"/>
  <text x="35" y="112" font-size="11" font-weight="700" fill="#243342" text-transform="uppercase" letter-spacing="1">Réf / User Story INVEST</text>
  <text x="410" y="112" font-size="11" font-weight="700" fill="#243342" text-transform="uppercase" letter-spacing="1">Resp. / Service</text>
  <text x="545" y="112" font-size="11" font-weight="700" fill="#243342" text-transform="uppercase" letter-spacing="1">Est.</text>
""")

    # Calendrier 7 mois (Septembre 2026 a Mars 2027)
    months_data = [
        ("Septembre 2026", 0, 4),
        ("Octobre 2026", 4, 4),
        ("Novembre 2026", 8, 4.5),
        ("Décembre 2026", 12.5, 3.5),
        ("Janvier 2027", 16, 4.5),
        ("Février 2027", 20.5, 4),
        ("Mars 2027", 24.5, 4.5)
    ]

    svg_parts.append('  <!-- GRILLE CALENDRIER -->')
    svg_parts.append(f'  <g transform="translate({timeline_x}, 85)">')
    svg_parts.append(f'    <rect x="0" y="0" width="{timeline_w}" height="45" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1"/>')

    for m_name, m_start, m_len in months_data:
        mx = m_start * col_w
        mw = m_len * col_w
        svg_parts.append(f'    <rect x="{mx}" y="0" width="{mw}" height="25" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>')
        svg_parts.append(f'    <text x="{mx + mw/2}" y="17" text-anchor="middle" font-size="11" font-weight="700" fill="#243342">{m_name}</text>')

    for w in range(total_weeks):
        wx = w * col_w
        svg_parts.append(f'    <rect x="{wx}" y="25" width="{col_w}" height="20" fill="#FFFFFF" stroke="#EDE8E1" stroke-width="0.8"/>')
        w_label = f"S{w+1:02d}"
        svg_parts.append(f'    <text x="{wx + col_w/2}" y="39" text-anchor="middle" font-size="8.5" font-weight="600" fill="#606B76">{w_label}</text>')
        svg_parts.append(f'    <line x1="{wx}" y1="45" x2="{wx}" y2="{height - 90}" stroke="#F0ECE1" stroke-width="0.8" />')

    svg_parts.append('  </g>')

    # Rows structured by Sprints & User Stories
    rows = [
        # CADRAGE & SOCLE
        {"type": "header", "title": "PHASE AMONT : Cadrage Métier R1 & Socle DevOps R2 (Sept-Oct 2026)", "color": "#1E293B"},
        {"type": "task", "ref": "T-01..03", "title": "Cahier des charges R1, APTE, Merise 3NF & Étude initiale", "resp": "Collectif Garik", "dur": "3 SP", "start": 0, "len": 3.0, "crit": True, "c": "#334155", "m": "R1 (18/09)"},
        {"type": "task", "ref": "T-04..06", "title": "Outillage GitLab CI, SonarQube, Docker multi-stage & Guide", "resp": "Rayane / Khalil", "dur": "5 SP", "start": 3.0, "len": 3.0, "crit": True, "c": "#EA580C", "m": "R2 (12/10)"},

        # SPRINT 1 : AUTH & CATALOGUE
        {"type": "header", "title": "SPRINT 1 : Socle Microservices, Auth & Catalogue Marchand (Novembre 2026)", "color": "#2563EB"},
        {"type": "task", "ref": "US-01", "title": "Inscription sécurisée multi-rôles (Citoyen / Commerçant)", "resp": "auth-service", "dur": "3 SP", "start": 6.5, "len": 1.5, "crit": True, "c": "#3B82F6"},
        {"type": "task", "ref": "US-02", "title": "Connexion sécurisée & Émission de token JWT", "resp": "auth-service", "dur": "2 SP", "start": 7.5, "len": 1.2, "crit": True, "c": "#3B82F6"},
        {"type": "task", "ref": "US-03", "title": "Consultation des boutiques partenaires adhérentes", "resp": "catalog-service", "dur": "2 SP", "start": 8.0, "len": 1.2, "crit": True, "c": "#2563EB"},
        {"type": "task", "ref": "US-04", "title": "Consultation du catalogue produits d'une boutique", "resp": "catalog-service", "dur": "3 SP", "start": 8.8, "len": 1.5, "crit": True, "c": "#2563EB"},
        {"type": "task", "ref": "US-05", "title": "Gestion fiches produits & stocks par le commerçant", "resp": "catalog-service", "dur": "3 SP", "start": 9.5, "len": 1.5, "crit": True, "c": "#2563EB"},
        {"type": "task", "ref": "US-06", "title": "Réservation temporaire de stock (Prepare 2PC endpoint)", "resp": "catalog-service", "dur": "5 SP", "start": 10.2, "len": 2.0, "crit": True, "c": "#1D4ED8", "m": "R3 (30/11)"},

        # SPRINT 2 : CŒUR MVP PANIER 2PC & CLICK & COLLECT
        {"type": "header", "title": "SPRINT 2 : Cœur MVP — Panier Multi-Commerces 2PC & Click & Collect (Décembre 2026)", "color": "#7C3AED"},
        {"type": "task", "ref": "US-07", "title": "Constitution du panier multi-boutiques unifié", "resp": "cart-order", "dur": "5 SP", "start": 11.0, "len": 1.8, "crit": True, "c": "#8B5CF6"},
        {"type": "task", "ref": "US-08", "title": "Orchestration transaction distribuée Two-Phase Commit (2PC)", "resp": "cart-order", "dur": "8 SP", "start": 12.0, "len": 2.2, "crit": True, "c": "#7C3AED"},
        {"type": "task", "ref": "US-09", "title": "Timeout & Compensation automatique des réservations", "resp": "cart-order", "dur": "5 SP", "start": 12.8, "len": 1.8, "crit": True, "c": "#7C3AED"},
        {"type": "task", "ref": "US-10", "title": "Choix du créneau de retrait Click & Collect chez l'artisan", "resp": "cart-order/UI", "dur": "3 SP", "start": 13.5, "len": 1.5, "crit": True, "c": "#6D28D9"},
        {"type": "task", "ref": "US-11", "title": "Interface Web ergonomique adaptée senior (Persona Pierre)", "resp": "web-ui React", "dur": "5 SP", "start": 13.2, "len": 2.0, "crit": True, "c": "#6D28D9"},
        {"type": "task", "ref": "R4-FREEZE", "title": "Assemblage Docker, Tests TDD 80%, Code Freeze J-3 & Soutenance", "resp": "Collectif Garik", "dur": "Jalon", "start": 14.8, "len": 0.5, "crit": True, "c": "#DC2626", "m": "R4 MVP (18/12)"},

        # SPRINT 3 : FIDELITE TERRITORIALE VFP
        {"type": "header", "title": "SPRINT 3 : Moteur de Fidélité Territoriale & Règle VFP 15 Jours (Février 2027)", "color": "#059669"},
        {"type": "task", "ref": "US-12", "title": "Cumul de points de fidélité lors d'un achat validé", "resp": "loyalty-vfp", "dur": "3 SP", "start": 17.5, "len": 1.5, "crit": True, "c": "#10B981"},
        {"type": "task", "ref": "US-13", "title": "Moteur d'expiration dynamique VFP (Règle glissante 15 jours)", "resp": "loyalty-vfp", "dur": "5 SP", "start": 18.5, "len": 2.0, "crit": True, "c": "#059669"},
        {"type": "task", "ref": "US-14", "title": "Dématérialisation carte de fidélité (QR Code dynamique)", "resp": "loyalty / UI", "dur": "3 SP", "start": 19.5, "len": 1.5, "crit": True, "c": "#059669"},
        {"type": "task", "ref": "US-15", "title": "Scan caisse commerçant express (< 3s) & Crédit immédiat", "resp": "loyalty / UI", "dur": "3 SP", "start": 20.2, "len": 1.8, "crit": True, "c": "#047857"},

        # SPRINT 4 : MOBILITE, SUPERVISION & HOMOLOGATION
        {"type": "header", "title": "SPRINT 4 : Titres Mobilité, Supervision DSI & Clôture V2 (Mars 2027)", "color": "#0D9488"},
        {"type": "task", "ref": "US-16", "title": "Délivrance de ticket de bus dématérialisé (Partenariat Ilévia)", "resp": "mobility-service", "dur": "3 SP", "start": 21.5, "len": 1.8, "crit": True, "c": "#14B8A6"},
        {"type": "task", "ref": "US-17", "title": "Activation des 20 minutes de parking gratuit centre-ville", "resp": "mobility-service", "dur": "3 SP", "start": 22.5, "len": 1.5, "crit": True, "c": "#0D9488"},
        {"type": "task", "ref": "US-18", "title": "Tableau de bord municipal k-anonyme (Supervision Mairie DSI)", "resp": "municipal-dash", "dur": "5 SP", "start": 23.5, "len": 2.0, "crit": False, "c": "#0D9488"},
        {"type": "task", "ref": "R5-RELEASE", "title": "Tests de charge Gatling, Homologation Docker, Code Freeze J-3", "resp": "Collectif Garik", "dur": "Jalon", "start": 26.5, "len": 0.5, "crit": True, "c": "#DC2626", "m": "R5 Final (19/03)"},

        # QUALITE TRANSVERSE
        {"type": "header", "title": "ASSURANCE QUALITE CONTINUE : DoD, SonarQube & Verify Deliverables (S01 à S29)", "color": "#475569"},
        {"type": "task", "ref": "QA-TRANS", "title": "Contrôle TDD continu (Jacoco >= 80%), Zéro Canari & Zéro Emoji", "resp": "Khalil (QA)", "dur": "Transv.", "start": 0, "len": 27.0, "crit": False, "c": "#94A3B8", "is_continuous": True}
    ]

    curr_y = 135
    row_height = 29
    header_height = 24

    for r in rows:
        if r["type"] == "header":
            h_title = r["title"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            svg_parts.append(f'  <!-- Header: {h_title} -->')
            svg_parts.append(f'  <g transform="translate(15, {curr_y})">')
            svg_parts.append(f'    <rect x="0" y="0" width="{width - 30}" height="{header_height}" fill="{r["color"]}" opacity="0.95"/>')
            svg_parts.append(f'    <text x="20" y="16.5" font-size="11" font-weight="700" fill="#FFFFFF">{h_title}</text>')
            svg_parts.append(f'  </g>')
            curr_y += header_height + 2
        else:
            y = curr_y
            title_esc = r["title"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            bg_sidebar = "#FFFFFF" if (y // row_height) % 2 == 0 else "#FAF9F6"

            svg_parts.append(f'  <!-- Task: {r["ref"]} - {title_esc} -->')
            svg_parts.append(f'  <g transform="translate(15, {y})">')
            svg_parts.append(f'    <rect x="0" y="0" width="{sidebar_w}" height="{row_height}" fill="{bg_sidebar}" stroke="#EDE8E1" stroke-width="0.8"/>')

            crit_color = "#DC2626" if r.get("crit") else "#64748B"
            crit_bg = "#FEE2E2" if r.get("crit") else "#F1F5F9"
            svg_parts.append(f'    <rect x="8" y="5" width="56" height="18" rx="3" fill="{crit_bg}" stroke="{crit_color}" stroke-width="0.8"/>')
            svg_parts.append(f'    <text x="36" y="17.5" text-anchor="middle" font-size="8.5" font-weight="700" fill="{crit_color}">{r["ref"]}</text>')

            svg_parts.append(f'    <text x="70" y="18" font-size="10" font-weight="600" fill="#243342">{title_esc}</text>')
            svg_parts.append(f'    <text x="410" y="18" font-size="9" font-weight="500" fill="#606B76">{r["resp"]}</text>')
            svg_parts.append(f'    <text x="560" y="18" text-anchor="end" font-size="9" font-weight="700" fill="#243342">{r["dur"]}</text>')
            svg_parts.append(f'  </g>')

            bx = timeline_x + (r["start"] * col_w)
            bw = r["len"] * col_w

            svg_parts.append(f'  <g transform="translate({bx}, {y})">')
            if r.get("is_continuous"):
                svg_parts.append(f'    <rect x="0" y="9" width="{bw}" height="10" rx="5" fill="none" stroke="{r["c"]}" stroke-width="2" stroke-dasharray="6 4"/>')
                svg_parts.append(f'    <text x="{bw/2}" y="7" text-anchor="middle" font-size="8.5" font-weight="600" fill="#64748B">Supervision Qualité &amp; Code Freeze permanent</text>')
            else:
                bar_stroke = "#DC2626" if r.get("crit") else r["c"]
                bar_sw = "1.5" if r.get("crit") else "1"
                svg_parts.append(f'    <rect x="0" y="4" width="{bw}" height="20" rx="4" fill="{r["c"]}" stroke="{bar_stroke}" stroke-width="{bar_sw}" filter="url(#shadow-bar)"/>')
                if bw > 35:
                    svg_parts.append(f'    <text x="{bw/2}" y="17.5" text-anchor="middle" font-size="8.5" font-weight="700" fill="#FFFFFF">{r["ref"]}</text>')

                if r.get("m"):
                    m_x = bw + 8
                    svg_parts.append(f'    <path d="M {m_x + 7} 4 L {m_x + 14} 14 L {m_x + 7} 24 L {m_x} 14 Z" fill="#DC2626" filter="url(#shadow-bar)"/>')
                    svg_parts.append(f'    <text x="{m_x + 20}" y="17.5" font-size="9.5" font-weight="800" fill="#DC2626">{r["m"]}</text>')

            svg_parts.append(f'  </g>')
            curr_y += row_height + 2

    # Legende bas de page
    svg_parts.append(f"""
  <!-- LEGENDE DU GANTT -->
  <g transform="translate(15, {height - 65})">
    <rect x="0" y="0" width="{width - 30}" height="45" rx="6" fill="#F4F2EC" stroke="#DCD6CD" stroke-width="1"/>
    <text x="20" y="27" font-size="11" font-weight="700" fill="#243342">Légende :</text>
    
    <rect x="90" y="16" width="22" height="14" rx="3" fill="#3B82F6"/>
    <text x="120" y="27" font-size="10" font-weight="600" fill="#243342">Sprint 1 (Auth &amp; Catalogues)</text>

    <rect x="300" y="16" width="22" height="14" rx="3" fill="#7C3AED"/>
    <text x="330" y="27" font-size="10" font-weight="600" fill="#243342">Sprint 2 (Cœur MVP Panier 2PC)</text>

    <rect x="540" y="16" width="22" height="14" rx="3" fill="#059669"/>
    <text x="570" y="27" font-size="10" font-weight="600" fill="#243342">Sprint 3 (Moteur Fidélité VFP 15j)</text>

    <rect x="790" y="16" width="22" height="14" rx="3" fill="#0D9488"/>
    <text x="820" y="27" font-size="10" font-weight="600" fill="#243342">Sprint 4 (Mobilité &amp; DSI)</text>

    <path d="M 1030 16 L 1037 23 L 1030 30 L 1023 23 Z" fill="#DC2626"/>
    <text x="1045" y="27" font-size="10" font-weight="700" fill="#DC2626">Jalon Contractuel &amp; Soutenance</text>

    <text x="1350" y="27" font-size="10" font-style="italic" fill="#5A6578">Vélocité cible : 22 SP / Sprint · Couverture DoD JUnit : >= 80%</text>
  </g>
</svg>""")

    script_dir = Path(__file__).resolve().parent
    output_dir = script_dir.parent / "docs" / "01_Cadrage_Et_Cahier_Des_Charges_R1" / "figures"
    os.makedirs(output_dir, exist_ok=True)

    svg_path = output_dir / "fig_5_2_gantt_user_stories_mvp.svg"
    png_path = output_dir / "fig_5_2_gantt_user_stories_mvp.png"

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_parts))
    print(f"[OK] Diagramme SVG genere : {svg_path}")

    # Conversion en PNG haute resolution via PyMuPDF
    if PYMUPDF_AVAILABLE:
        try:
            doc = pymupdf.open(str(svg_path))
            page = doc[0]
            # Zoom 2x pour un rendu ultra net (3920 x 2520 px)
            mat = pymupdf.Matrix(2.0, 2.0)
            pix = page.get_pixmap(matrix=mat, alpha=False)
            pix.save(str(png_path))
            doc.close()
            print(f"[OK] Rendu PNG HD genere : {png_path} ({pix.width}x{pix.height} px)")
        except Exception as e:
            print(f"[WARN] Impossible de generer le PNG : {e}")
    else:
        print("[WARN] PyMuPDF non disponible, PNG omis.")


if __name__ == "__main__":
    generate_gantt_user_stories()

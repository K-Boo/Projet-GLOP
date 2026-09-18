#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur du diagramme de Gantt annuel officiel (Figure 5.1).
Style Planyway épuré, uniquement la partie graphique.
"""
import os
import pymupdf

def generate_gantt():
    svg_parts = []
    
    # 1. Header and Defs
    # Height reduced to 460 to only contain the Gantt timeline, no bottom table.
    svg_parts.append("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 460" width="1600" height="460" style="font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif; background-color: #FAF9F6;">
  <defs>
    <filter id="shadow-bar" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#243342" flood-opacity="0.10"/>
    </filter>
    <marker id="arrow-crit" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 2 L 8 5 L 0 8 z" fill="#243342" />
    </marker>
  </defs>

  <!-- BACKGROUND RECT -->
  <rect x="20" y="20" width="1560" height="420" rx="12" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1.5" />
  
  <!-- HEADER -->
  <rect x="20" y="20" width="1560" height="60" rx="12" fill="#243342" />
  <rect x="20" y="60" width="1560" height="20" fill="#243342" />
  
  <text x="45" y="55" font-size="20" font-weight="800" fill="#FFFFFF">ShopLoc Gantt</text>
  <text x="210" y="53" font-size="15" font-weight="500" fill="#DCD6CD">Planning Prévisionnel Annuel</text>
  
  <!-- SIDEBAR (TASK LIST) -->
  <rect x="20" y="80" width="360" height="360" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1.5"/>
  <rect x="20" y="80" width="360" height="40" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1.5"/>
  <text x="40" y="105" font-size="13" font-weight="700" fill="#243342" text-transform="uppercase" letter-spacing="1">Livrables / Tâches</text>
  <text x="300" y="105" font-size="13" font-weight="700" fill="#243342" text-transform="uppercase" letter-spacing="1">Durée</text>
""")

    # 2. Timeline Grid (7 Months, each ~171.4px wide)
    months = ["Sept. 2026", "Oct. 2026", "Nov. 2026", "Déc. 2026", "Janv. 2027", "Févr. 2027", "Mars 2027"]
    month_width = 1200 / 7
    
    svg_parts.append('  <!-- TIMELINE GRID -->')
    svg_parts.append('  <g transform="translate(380, 80)">')
    
    svg_parts.append('    <rect x="0" y="0" width="1200" height="40" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1.5"/>')
    
    for i, m in enumerate(months):
        x = i * month_width
        svg_parts.append(f'    <!-- {m} -->')
        svg_parts.append(f'    <rect x="{x}" y="0" width="{month_width}" height="360" fill="none" stroke="#DCD6CD" stroke-width="1" stroke-dasharray="4 4" />')
        
        if i in [1, 3, 6]:
            svg_parts.append(f'    <rect x="{x}" y="40" width="{month_width}" height="320" fill="#243342" fill-opacity="0.02" />')
        
        svg_parts.append(f'    <rect x="{x}" y="0" width="{month_width}" height="40" fill="none" stroke="#DCD6CD" stroke-width="1.5" />')
        svg_parts.append(f'    <text x="{x + month_width/2}" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#243342">{m}</text>')
        
    svg_parts.append('  </g>')

    # 3. Tasks Data
    # Planyway minimal style: one main color, simple labels
    tasks = [
        {"y": 140, "title": "Jalon R1 · Cahier des Charges", "dur": "2 sem.", "c": "#243342", "start": 0.2, "len": 0.5, "milestone": "R1 (18/09)", "id": 1},
        {"y": 190, "title": "Jalon R2 · Outillage & DevOps", "dur": "3 sem.", "c": "#243342", "start": 0.7, "len": 0.8, "milestone": "R2 (12/10)", "id": 2},
        {"y": 240, "title": "Jalon R3 · Viabilité Financière", "dur": "7 sem.", "c": "#243342", "start": 1.5, "len": 1.2, "milestone": "R3 (30/11)", "id": 3},
        {"y": 290, "title": "Jalon R4 · Architecture V1", "dur": "9 sem.", "c": "#243342", "start": 1.5, "len": 1.7, "milestone": "R4 (18/12)", "id": 4},
        {"y": 340, "title": "Jalon R5 · Système Complet V2", "dur": "11 sem.", "c": "#243342", "start": 3.7, "len": 3.0, "milestone": "R5 (19/03)", "id": 5},
        {"y": 390, "title": "Assurance Qualité Continue", "dur": "25 sem.", "c": "#88929c", "start": 0.2, "len": 6.5, "is_continuous": True, "id": 6},
    ]

    svg_parts.append('  <!-- TASKS -->')
    for t in tasks:
        # Sidebar Task Item
        svg_parts.append(f'  <!-- Task: {t["title"]} -->')
        svg_parts.append(f'  <g transform="translate(20, {t["y"]})">')
        svg_parts.append(f'    <rect x="15" y="0" width="330" height="35" rx="4" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1"/>')
        title_esc = t["title"].replace("&", "&amp;")
        svg_parts.append(f'    <text x="30" y="22" font-size="13" font-weight="600" fill="#243342">{title_esc}</text>')
        svg_parts.append(f'    <text x="315" y="22" text-anchor="end" font-size="12" font-weight="500" fill="#606B76">{t["dur"]}</text>')
        svg_parts.append(f'  </g>')

        # Timeline Bar
        bar_x = 380 + (t["start"] * month_width)
        bar_w = t["len"] * month_width
        
        svg_parts.append(f'  <g transform="translate({bar_x}, {t["y"] + 2})">')
        if t.get("is_continuous"):
            svg_parts.append(f'    <rect x="0" y="10" width="{bar_w}" height="10" rx="5" fill="none" stroke="{t["c"]}" stroke-width="2" stroke-dasharray="6 4"/>')
        else:
            svg_parts.append(f'    <rect x="0" y="0" width="{bar_w}" height="30" rx="4" fill="{t["c"]}" filter="url(#shadow-bar)"/>')
            short_title = title_esc.split("·")[0].strip()
            # Milestone diamond
            m_x = bar_w
            # the diamond shape at the end of the bar
            svg_parts.append(f'    <path d="M {m_x + 15} 5 L {m_x + 25} 15 L {m_x + 15} 25 L {m_x + 5} 15 Z" fill="#C26750" filter="url(#shadow-bar)"/>')
            svg_parts.append(f'    <text x="{m_x + 32}" y="19" font-size="11" font-weight="700" fill="#C26750">{t["milestone"]}</text>')
        svg_parts.append(f'  </g>')

    # 4. Dependencies (Arrows)
    svg_parts.append('  <!-- DEPENDENCIES (CRITICAL PATH) -->')
    
    def draw_dependency(t1, t2):
        # We start from bottom-right of t1 bar
        x1 = 380 + (t1["start"] + t1["len"]) * month_width - 15
        y1 = t1["y"] + 32
        
        # We end at top-left of t2 bar
        x2 = 380 + t2["start"] * month_width + 15
        y2 = t2["y"] + 2
        
        mid_y = (y1 + y2) / 2
        
        # If t2 starts exactly where t1 ends or before, we need a different routing
        if x1 > x2 - 20: 
            # Route it carefully leftwards to avoid crossing the bars badly
            mid_y = y1 + 10
            path = f"M {x1} {y1} L {x1} {mid_y} L {x2} {mid_y} L {x2} {y2}"
        else:
            path = f"M {x1} {y1} L {x1} {mid_y} L {x2} {mid_y} L {x2} {y2}"
        
        svg_parts.append(f'  <path d="{path}" fill="none" stroke="#243342" stroke-width="1.5" marker-end="url(#arrow-crit)"/>')

    # R1 -> R2
    draw_dependency(tasks[0], tasks[1])
    
    # R2 -> R4
    # Note: R3 is between R2 and R4. We must avoid crossing R3 text. 
    # R2 ends at 1.5, R4 starts at 1.5. R3 starts at 1.5.
    # We will manually route R2 -> R4 to bypass R3 on the left.
    r2 = tasks[1]
    r4 = tasks[3]
    x1 = 380 + (r2["start"] + r2["len"]) * month_width - 15
    y1 = r2["y"] + 32
    x2 = 380 + r4["start"] * month_width + 15
    y2 = r4["y"] + 2
    
    # R3 is at y=240, height 35. So from 240 to 275.
    # We will route the arrow to x = 380 + 1.5*mw - 25, which is left of the bars.
    bypass_x = 380 + r4["start"] * month_width - 20
    path_r2_r4 = f"M {x1} {y1} L {x1} {y1 + 8} L {bypass_x} {y1 + 8} L {bypass_x} {y2 - 10} L {x2} {y2 - 10} L {x2} {y2}"
    svg_parts.append(f'  <path d="{path_r2_r4}" fill="none" stroke="#243342" stroke-width="1.5" marker-end="url(#arrow-crit)"/>')

    # R4 -> R5
    draw_dependency(tasks[3], tasks[4])

    # 5. Today / Current Date Line
    today_x = 380 + 0.5 * month_width
    svg_parts.append('  <!-- TODAY MARKER -->')
    svg_parts.append(f'  <line x1="{today_x}" y1="80" x2="{today_x}" y2="440" stroke="#C26750" stroke-width="1.5" stroke-dasharray="6 4"/>')
    svg_parts.append(f'  <rect x="{today_x - 35}" y="68" width="70" height="20" rx="4" fill="#C26750" />')
    svg_parts.append(f'  <text x="{today_x}" y="82" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">AUJOURD\'HUI</text>')

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

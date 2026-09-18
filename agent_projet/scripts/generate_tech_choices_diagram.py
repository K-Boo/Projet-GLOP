#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pymupdf

def generate_tech_diagram_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 820" width="1440" height="820" style="font-family: 'Plus Jakarta Sans', 'Poppins', sans-serif;">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;display=swap');
    </style>
    <filter id="shadow-soft" x="-2%" y="-2%" width="104%" height="106%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#243342" flood-opacity="0.06"/>
    </filter>
    <filter id="shadow-card" x="-4%" y="-6%" width="108%" height="116%">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2" flood-color="#243342" flood-opacity="0.05"/>
    </filter>
  </defs>

  <!-- FOND GLOBAL -->
  <rect x="5" y="5" width="1430" height="810" rx="14" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1.2" filter="url(#shadow-soft)"/>

  <!-- EN-TÊTE -->
  <rect x="25" y="20" width="1390" height="52" rx="8" fill="#243342" />
  <rect x="38" y="32" width="28" height="28" rx="6" fill="#C26750" />
  <text x="52" y="51" text-anchor="middle" font-size="13" font-weight="800" fill="#FFFFFF">SL</text>
  <text x="78" y="44" font-size="14" font-weight="700" fill="#FFFFFF">Architecture Applicative Prévisionnelle (Jalon R1) — ShopLoc</text>
  <text x="78" y="59" font-size="10" font-weight="400" fill="#EBF0F5">Modulaire, Conteneurisée, Épurée avec les Logos Officiels (Charte UI)</text>
  <text x="1400" y="51" text-anchor="end" font-size="11" font-weight="600" fill="#DCD6CD">Master 2 MIAGE · Garik</text>

  <!-- TIER 1 : CLIENTS WEB & MOBILES -->
  <rect x="25" y="85" width="1390" height="155" rx="10" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1.2" filter="url(#shadow-card)"/>
  <rect x="25" y="85" width="1390" height="32" rx="10" fill="#EBF0F5" />
  <text x="45" y="106" font-size="11.5" font-weight="700" fill="#243342">TIER 1 — INTERFACES UTILISATEURS (Progressive Web App)</text>
  
  <g transform="translate(1250, 89)">
    <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/react/react-original.svg" x="0" y="0" width="24" height="24" />
    <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/typescript/typescript-original.svg" x="35" y="0" width="24" height="24" />
    <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tailwindcss/tailwindcss-original.svg" x="70" y="0" width="24" height="24" />
  </g>

  <!-- Carte 1.1 -->
  <g transform="translate(45, 126)">
    <rect x="0" y="0" width="425" height="100" rx="8" fill="#FBEEEA" stroke="#D88B77" stroke-width="1" />
    <circle cx="40" cy="35" r="20" fill="#C26750" />
    <text x="40" y="41" text-anchor="middle" font-size="16" font-weight="800" fill="#FFFFFF">👤</text>
    <text x="75" y="32" font-size="11" font-weight="700" fill="#8E3D2A">ESPACE CITOYEN</text>
    <text x="75" y="47" font-size="9" font-weight="500" fill="#243342">Recherche, Click &amp; Collect, Fidélité, VFP</text>
  </g>

  <!-- Carte 1.2 -->
  <g transform="translate(508, 126)">
    <rect x="0" y="0" width="425" height="100" rx="8" fill="#EBF3ED" stroke="#7EA88D" stroke-width="1" />
    <circle cx="40" cy="35" r="20" fill="#4A7A5B" />
    <text x="40" y="41" text-anchor="middle" font-size="16" font-weight="800" fill="#FFFFFF">🏪</text>
    <text x="75" y="32" font-size="11" font-weight="700" fill="#2E583D">ESPACE COMMERÇANT</text>
    <text x="75" y="47" font-size="9" font-weight="500" fill="#243342">Catalogue, Commandes, Scan QR Caisse</text>
  </g>

  <!-- Carte 1.3 -->
  <g transform="translate(970, 126)">
    <rect x="0" y="0" width="425" height="100" rx="8" fill="#FEF7EB" stroke="#DCB162" stroke-width="1" />
    <circle cx="40" cy="35" r="20" fill="#C48B28" />
    <text x="40" y="41" text-anchor="middle" font-size="16" font-weight="800" fill="#FFFFFF">🏛️</text>
    <text x="75" y="32" font-size="11" font-weight="700" fill="#845A11">PORTAIL DSI MAIRIE</text>
    <text x="75" y="47" font-size="9" font-weight="500" fill="#243342">Indicateurs, Statistiques, Sondages QCM</text>
  </g>

  <!-- LIAISON FLUX TIER 1 -> TIER 2 -->
  <line x1="720" y1="240" x2="720" y2="288" stroke="#243342" stroke-width="2" stroke-dasharray="4 3"/>
  <polygon points="720,293 715,283 725,283" fill="#243342"/>
  <rect x="625" y="256" width="190" height="22" rx="11" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
  <text x="720" y="271" text-anchor="middle" font-size="9.5" font-weight="600" fill="#243342">API REST (JSON)</text>

  <!-- TIER 2 : SERVEUR BACKEND APPLICATIF -->
  <rect x="25" y="295" width="910" height="240" rx="10" fill="#FFFFFF" stroke="#8B9EAF" stroke-width="1.4" filter="url(#shadow-card)"/>
  <rect x="25" y="295" width="910" height="34" rx="10" fill="#243342" />
  <text x="45" y="316" font-size="11.5" font-weight="700" fill="#FFFFFF">TIER 2 — SERVICES MÉTIER BACKEND</text>
  
  <g transform="translate(770, 300)">
    <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg" x="0" y="0" width="24" height="24" />
    <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/spring/spring-original.svg" x="35" y="0" width="24" height="24" />
    <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/maven/maven-original.svg" x="70" y="0" width="24" height="24" />
  </g>
  
  <g transform="translate(45, 342)">
    <rect x="0" y="0" width="415" height="82" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="207" y="35" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">🔐 Profils &amp; Sécurité</text>
    <text x="207" y="55" text-anchor="middle" font-size="9" font-weight="500" fill="#5A6578">Spring Security, JWT, Plaque auto</text>
  </g>

  <g transform="translate(495, 342)">
    <rect x="0" y="0" width="415" height="82" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="207" y="35" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">🛒 Catalogue &amp; Click &amp; Collect</text>
    <text x="207" y="55" text-anchor="middle" font-size="9" font-weight="500" fill="#5A6578">Stocks, Trajets, Réservation stock</text>
  </g>

  <g transform="translate(45, 436)">
    <rect x="0" y="0" width="415" height="85" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="207" y="35" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">🎁 Double Fidélité &amp; VFP</text>
    <text x="207" y="55" text-anchor="middle" font-size="9" font-weight="500" fill="#5A6578">Cagnottage marchand, 10 passages/15j</text>
  </g>

  <g transform="translate(495, 436)">
    <rect x="0" y="0" width="415" height="85" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="207" y="35" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">📊 Statistiques Municipales</text>
    <text x="207" y="55" text-anchor="middle" font-size="9" font-weight="500" fill="#5A6578">Tableaux de bord DSI, Sondages QCM</text>
  </g>

  <!-- TIER 3 : PERSISTANCE -->
  <rect x="965" y="295" width="450" height="240" rx="10" fill="#FFFFFF" stroke="#8B9EAF" stroke-width="1.4" filter="url(#shadow-card)"/>
  <rect x="965" y="295" width="450" height="34" rx="10" fill="#243342" />
  <text x="985" y="316" font-size="11.5" font-weight="700" fill="#FFFFFF">TIER 3 — PERSISTANCE</text>

  <g transform="translate(985, 342)">
    <rect x="0" y="0" width="410" height="179" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg" x="175" y="25" width="60" height="60" />
    <text x="205" y="115" text-anchor="middle" font-size="13" font-weight="700" fill="#243342">PostgreSQL 16</text>
    <text x="205" y="135" text-anchor="middle" font-size="10" font-weight="600" fill="#2B5270">Intégrité transactionnelle (ACID)</text>
    <text x="205" y="155" text-anchor="middle" font-size="9" font-weight="400" fill="#5A6578">Volume persistant Docker</text>
  </g>

  <!-- LIAISON TIER 2 <-> TIER 3 -->
  <line x1="935" y1="415" x2="965" y2="415" stroke="#243342" stroke-width="2"/>
  <polygon points="965,415 957,411 957,419" fill="#243342"/>
  <polygon points="935,415 943,411 943,419" fill="#243342"/>

  <!-- TIER 4 : SIMULATEURS -->
  <rect x="25" y="550" width="1390" height="135" rx="10" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1.2" stroke-dasharray="4 3" filter="url(#shadow-card)"/>
  <rect x="25" y="550" width="1390" height="30" rx="10" fill="#F5F2EB" />
  <text x="45" y="570" font-size="11" font-weight="700" fill="#243342">TIER 4 — SIMULATEURS PARTENAIRES (Mocks REST)</text>
  <text x="1395" y="570" text-anchor="end" font-size="9.5" font-weight="500" fill="#5A6578">Bouchons Dockerisés pour Environnement Étudiant</text>

  <g transform="translate(45, 590)">
    <rect x="0" y="0" width="425" height="82" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="212" y="35" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">💳 Mock Banque (Izli)</text>
    <text x="212" y="55" text-anchor="middle" font-size="9" font-weight="500" fill="#5A6578">Rechargement en ligne, Paiement CB</text>
  </g>

  <g transform="translate(508, 590)">
    <rect x="0" y="0" width="425" height="82" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="212" y="35" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">🚌 Mock Transports (Ilévia)</text>
    <text x="212" y="55" text-anchor="middle" font-size="9" font-weight="500" fill="#5A6578">Génération E-Ticket VFP / QR Code</text>
  </g>

  <g transform="translate(970, 590)">
    <rect x="0" y="0" width="425" height="82" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="212" y="35" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">🅿️ Mock Voirie (Horodateurs)</text>
    <text x="212" y="55" text-anchor="middle" font-size="9" font-weight="500" fill="#5A6578">Validation des 20 min via plaque d'immatriculation</text>
  </g>

  <line x1="480" y1="535" x2="480" y2="550" stroke="#8A9BAE" stroke-width="1.5" stroke-dasharray="3 2"/>

  <!-- DEVOPS -->
  <rect x="25" y="700" width="1390" height="98" rx="10" fill="#243342" filter="url(#shadow-card)"/>
  
  <text x="45" y="733" font-size="12" font-weight="700" fill="#FFFFFF">SOCLE DEVOPS &amp; INTÉGRATION CONTINUE</text>

  <g transform="translate(45, 755)">
    <rect x="0" y="0" width="425" height="30" rx="5" fill="#FAF9F6" />
    <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg" x="10" y="3" width="24" height="24" />
    <text x="45" y="19" font-size="10" font-weight="700" fill="#243342">Docker Compose</text>
    <text x="400" y="19" text-anchor="end" font-size="9" font-weight="500" fill="#5A6578">Lancement local (docker compose up)</text>

    <rect x="463" y="0" width="425" height="30" rx="5" fill="#FAF9F6" />
    <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/gitlab/gitlab-original.svg" x="473" y="3" width="24" height="24" />
    <text x="508" y="19" font-size="10" font-weight="700" fill="#243342">GitLab (Univ. Lille)</text>
    <text x="863" y="19" text-anchor="end" font-size="9" font-weight="500" fill="#5A6578">Versioning, Intégration Continue (CI/CD)</text>

    <rect x="925" y="0" width="425" height="30" rx="5" fill="#FAF9F6" />
    <text x="935" y="20" font-size="14" font-weight="700" fill="#243342">📑</text>
    <text x="965" y="19" font-size="10" font-weight="700" fill="#243342">OpenAPI Swagger 3.1</text>
    <text x="1325" y="19" text-anchor="end" font-size="9" font-weight="500" fill="#5A6578">Documentation formelle du contrat d'interface</text>
  </g>
</svg>
"""

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    html_path = os.path.join(repo_root, "agent_projet/templates/components/tech_choices_diagram.html")
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    
    svg_content = generate_tech_diagram_svg()
    
    component_content = f"""<!-- FIGURE 4.1 : SCHÉMA D'ARCHITECTURE LOGICIELLE SHOPLOC (ICÔNES & ÉPURÉ) -->
<div class="figure-card" style="background:#FAF9F6; border:1px solid #DCD6CD; border-radius:14px; padding:20px; margin-bottom:24px; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px; border-bottom:1px solid #DCD6CD; padding-bottom:10px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#243342;"></span>
        <span style="font-size:11px; font-weight:700; color:#243342; text-transform:uppercase; letter-spacing:0.08em; font-family: 'Plus Jakarta Sans', sans-serif;">Ingénierie Logicielle &amp; DevOps</span>
      </div>
      <h3 style="font-size:16px; font-weight:700; color:#243342; margin:0; font-family: 'Plus Jakarta Sans', sans-serif;">Figure 4.1 — Architecture Applicative Prévisionnelle (Jalon R1)</h3>
    </div>
    <span style="font-size:11px; background:#FFFFFF; border:1px solid #DCD6CD; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600; font-family: 'Plus Jakarta Sans', sans-serif;">Modulaire Conteneurisée</span>
  </div>
{svg_content}
</div>
"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(component_content)
    print(f"HTML écrit : {html_path}")

    output_dir = os.path.join(repo_root, "agent_projet/docs/01_Cadrage_Et_Cahier_Des_Charges_R1/figures")
    os.makedirs(output_dir, exist_ok=True)
    svg_path = os.path.join(output_dir, "fig_4_1_choix_techniques.svg")
    png_path = os.path.join(output_dir, "fig_4_1_choix_techniques.png")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"SVG écrit : {svg_path}")

    # Note: MuPDF doesn't render web fonts or remote images nicely, so the PNG fallback will just be what MuPDF can do,
    # but the SVG/HTML will be perfect in browser or Chrome-headless print-to-pdf.
    try:
        doc = pymupdf.open(svg_path)
        page = doc[0]
        pix = page.get_pixmap(dpi=300)
        pix.save(png_path)
        print(f"Exporté PNG via PyMuPDF : {png_path} ({pix.width}x{pix.height})")
    except Exception as e:
        print(f"Avertissement MuPDF : {e}")

if __name__ == "__main__":
    main()

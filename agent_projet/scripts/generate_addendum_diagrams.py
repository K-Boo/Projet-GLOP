#!/usr/bin/env python3
"""
Générateur des 4 diagrammes vectoriels SVG officiels pour l'Addendum R1 de Garik / ShopLoc.
Charte graphique ShopLoc Pastel & Craft (sans emoji, typographie Poppins, couleurs normalisées).
"""

import os

FIGURES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "01_Cadrage_Et_Cahier_Des_Charges_R1", "figures"))
os.makedirs(FIGURES_DIR, exist_ok=True)

DEFS_SVG = """  <defs>
    <filter id="shadow-soft" x="-8%" y="-8%" width="120%" height="120%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#243342" flood-opacity="0.06"/>
    </filter>
    <filter id="shadow-elevated" x="-8%" y="-8%" width="120%" height="120%">
      <feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="#243342" flood-opacity="0.10"/>
    </filter>
    <marker id="arrow-slate" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#243342" />
    </marker>
    <marker id="arrow-terracotta" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#C26750" />
    </marker>
    <marker id="arrow-sage" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#4A7A5B" />
    </marker>
    <marker id="arrow-honey" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#C48B28" />
    </marker>
    <marker id="arrow-plum" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#6E3946" />
    </marker>
    <marker id="arrow-muted" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#8C96A5" />
    </marker>
  </defs>"""

def generate_fig_1_1_bete_a_cornes():
    """Génère la Bête à cornes APTE révisée (Citoyens, Commerçants, Mairie, Association)."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 410" width="100%" height="auto" style="overflow:visible; font-family:'Poppins', sans-serif;">
{DEFS_SVG}
  <!-- FOND GENERAL CARTE -->
  <rect x="0" y="0" width="960" height="410" rx="16" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1.2" />

  <!-- CARTE HAUT GAUCHE : A QUI LE SYSTEME REND-IL SERVICE ? -->
  <g filter="url(#shadow-soft)">
    <rect x="35" y="30" width="415" height="115" rx="12" fill="#FFFFFF" stroke="#D88B77" stroke-width="1.8" />
    <path d="M 35 42 A 12 12 0 0 1 47 30 L 438 30 A 12 12 0 0 1 450 42 L 450 56 L 35 56 Z" fill="#FBEEEA" />
    <text x="50" y="48" font-size="10.5" font-weight="700" fill="#8E3D2A" text-transform="uppercase" letter-spacing="0.06em">À qui le système rend-il service ?</text>
    <text x="50" y="78" font-size="13" font-weight="700" fill="#243342">Aux Citoyens, Artisans, Mairie &amp; Association</text>
    <text x="50" y="98" font-size="11" font-weight="400" fill="#5A6578">• Citoyens &amp; Commerçants : Pouvoir d'achat et zero commission</text>
    <text x="50" y="116" font-size="11" font-weight="400" fill="#5A6578">• Mairie &amp; Association : Dynamisation de centre-ville et mobilite</text>
  </g>

  <!-- CARTE HAUT DROITE : SUR QUOI LE SYSTEME AGIT-IL ? -->
  <g filter="url(#shadow-soft)">
    <rect x="510" y="30" width="415" height="115" rx="12" fill="#FFFFFF" stroke="#DCB162" stroke-width="1.8" />
    <path d="M 510 42 A 12 12 0 0 1 522 30 L 913 30 A 12 12 0 0 1 925 42 L 925 56 L 510 56 Z" fill="#FEF7EB" />
    <text x="525" y="48" font-size="10.5" font-weight="700" fill="#845A11" text-transform="uppercase" letter-spacing="0.06em">Sur quoi le système agit-il ?</text>
    <text x="525" y="78" font-size="13" font-weight="700" fill="#243342">Sur les flux marchands et l'animation locale</text>
    <text x="525" y="98" font-size="11" font-weight="400" fill="#5A6578">• Commandes Click &amp; Collect et passages en caisse physique</text>
    <text x="525" y="116" font-size="11" font-weight="400" fill="#5A6578">• Double cagnotte fidelite, titres Ilevia et stationnement</text>
  </g>

  <!-- BOITE PRODUIT CENTRALE : SHOPLOC EDITE PAR GARIK -->
  <g filter="url(#shadow-elevated)">
    <rect x="270" y="180" width="420" height="92" rx="16" fill="#243342" stroke="#1A2530" stroke-width="2" />
    <text x="480" y="215" text-anchor="middle" font-size="17" font-weight="700" fill="#FFFFFF" letter-spacing="0.03em">Plateforme Logicielle ShopLoc</text>
    <text x="480" y="238" text-anchor="middle" font-size="12" font-weight="500" fill="#DCB162">Editee par Entreprise Garik (Prestataire MOE Informatique)</text>
    <text x="480" y="257" text-anchor="middle" font-size="10.5" font-weight="400" fill="#FAF9F6" opacity="0.85">Marketplace Locale · Double Fidelite Territoriale · Connecteurs Mobilite</text>
  </g>

  <!-- CARTE BAS : DANS QUEL BUT ? -->
  <g filter="url(#shadow-soft)">
    <rect x="140" y="315" width="680" height="72" rx="12" fill="#FFFFFF" stroke="#7EA88D" stroke-width="1.8" />
    <path d="M 140 327 A 12 12 0 0 1 152 315 L 808 315 A 12 12 0 0 1 820 327 L 820 338 L 140 338 Z" fill="#EBF3ED" />
    <text x="480" y="331" text-anchor="middle" font-size="10" font-weight="700" fill="#2E583D" text-transform="uppercase" letter-spacing="0.06em">Dans quel but ? (Finalité Métier)</text>
    <text x="480" y="358" text-anchor="middle" font-size="12.5" font-weight="600" fill="#243342">Federer le commerce de proximite sans commission predatrice, revitaliser les centres-villes</text>
    <text x="480" y="376" text-anchor="middle" font-size="11" font-weight="400" fill="#5A6578">et valoriser le pouvoir d'achat des citoyens tout en encourageant les mobilites douces.</text>
  </g>

  <!-- FLECHES DE CONVERGENCE DE LA BETE A CORNES -->
  <path d="M 242 145 C 242 168, 330 162, 375 178" fill="none" stroke="#C26750" stroke-width="2.2" marker-end="url(#arrow-terracotta)" />
  <path d="M 718 145 C 718 168, 630 162, 585 178" fill="none" stroke="#C48B28" stroke-width="2.2" marker-end="url(#arrow-honey)" />
  <path d="M 480 272 L 480 312" fill="none" stroke="#243342" stroke-width="2.5" marker-end="url(#arrow-slate)" />
</svg>"""
    out_path = os.path.join(FIGURES_DIR, "fig_1_1_bete_a_cornes_revisee.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[OK] Genere : {out_path}")
    return svg

def generate_fig_1_2_diagramme_pieuvre():
    """Génère le Diagramme Pieuvre révisé (6 interacteurs, FP1, FP2, FP3, FC1 à FC7)."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 620" width="100%" height="auto" style="overflow:visible; font-family:'Poppins', sans-serif;">
{DEFS_SVG}
  <!-- FOND GENERAL PAYSAGE -->
  <rect x="0" y="0" width="1180" height="620" rx="16" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1.2" />

  <!-- SYSTEME CENTRAL : SHOPLOC -->
  <g filter="url(#shadow-elevated)">
    <rect x="460" y="240" width="260" height="110" rx="18" fill="#243342" stroke="#1A2530" stroke-width="2" />
    <text x="590" y="280" text-anchor="middle" font-size="18" font-weight="700" fill="#FFFFFF">Plateforme ShopLoc</text>
    <text x="590" y="304" text-anchor="middle" font-size="12" font-weight="500" fill="#DCB162">Editee par Garik (MOE)</text>
    <text x="590" y="326" text-anchor="middle" font-size="10.5" font-weight="400" fill="#FAF9F6" opacity="0.85">[Système Logiciel Évalué]</text>
  </g>

  <!-- 6 INTERACTEURS EXTERIEURS -->
  <!-- 1. Citoyen (Terracotta) -->
  <g filter="url(#shadow-soft)">
    <rect x="50" y="40" width="240" height="76" rx="12" fill="#FFFFFF" stroke="#D88B77" stroke-width="1.8" />
    <path d="M 50 52 A 12 12 0 0 1 62 40 L 278 40 A 12 12 0 0 1 290 52 L 290 62 L 50 62 Z" fill="#FBEEEA" />
    <text x="170" y="55" text-anchor="middle" font-size="9.5" font-weight="700" fill="#8E3D2A" text-transform="uppercase">Bénéficiaire Direct</text>
    <text x="170" y="86" text-anchor="middle" font-size="14" font-weight="600" fill="#243342">Citoyen / Client</text>
    <text x="170" y="104" text-anchor="middle" font-size="10" font-weight="400" fill="#5A6578">Consommateur urbain &amp; seniors</text>
  </g>

  <!-- 2. Artisan Commerçant (Sauge) -->
  <g filter="url(#shadow-soft)">
    <rect x="890" y="40" width="240" height="76" rx="12" fill="#FFFFFF" stroke="#7EA88D" stroke-width="1.8" />
    <path d="M 890 52 A 12 12 0 0 1 902 40 L 1118 40 A 12 12 0 0 1 1130 52 L 1130 62 L 890 62 Z" fill="#EBF3ED" />
    <text x="1010" y="55" text-anchor="middle" font-size="9.5" font-weight="700" fill="#2E583D" text-transform="uppercase">Bénéficiaire Direct</text>
    <text x="1010" y="86" text-anchor="middle" font-size="14" font-weight="600" fill="#243342">Artisan / Commerçant</text>
    <text x="1010" y="104" text-anchor="middle" font-size="10" font-weight="400" fill="#5A6578">Commerces de proximite &amp; bouche</text>
  </g>

  <!-- 3. Association des Commerçants (Plum/Miel) -->
  <g filter="url(#shadow-soft)">
    <rect x="910" y="255" width="240" height="76" rx="12" fill="#FFFFFF" stroke="#DCB162" stroke-width="1.8" />
    <path d="M 910 267 A 12 12 0 0 1 922 255 L 1138 255 A 12 12 0 0 1 1150 267 L 1150 277 L 910 277 Z" fill="#FEF7EB" />
    <text x="1030" y="270" text-anchor="middle" font-size="9.5" font-weight="700" fill="#845A11" text-transform="uppercase">Partenaire d'Usage</text>
    <text x="1030" y="301" text-anchor="middle" font-size="14" font-weight="600" fill="#243342">Association Commerçants</text>
    <text x="1030" y="319" text-anchor="middle" font-size="10" font-weight="400" fill="#5A6578">Federation locale &amp; gestion des lots</text>
  </g>

  <!-- 4. Mairie de Lille (Ocre miel) -->
  <g filter="url(#shadow-soft)">
    <rect x="850" y="490" width="240" height="76" rx="12" fill="#FFFFFF" stroke="#DCB162" stroke-width="1.8" />
    <path d="M 850 502 A 12 12 0 0 1 862 490 L 1078 490 A 12 12 0 0 1 1090 502 L 1090 512 L 850 512 Z" fill="#FEF7EB" />
    <text x="970" y="505" text-anchor="middle" font-size="9.5" font-weight="700" fill="#845A11" text-transform="uppercase">Collectivité Territoriale</text>
    <text x="970" y="536" text-anchor="middle" font-size="14" font-weight="600" fill="#243342">Mairie de Lille</text>
    <text x="970" y="554" text-anchor="middle" font-size="10" font-weight="400" fill="#5A6578">Politique mobilite &amp; indicateurs</text>
  </g>

  <!-- 5. Système Bancaire (Bordeaux) -->
  <g filter="url(#shadow-soft)">
    <rect x="90" y="490" width="240" height="76" rx="12" fill="#FFFFFF" stroke="#B88290" stroke-width="1.8" />
    <path d="M 90 502 A 12 12 0 0 1 102 490 L 318 490 A 12 12 0 0 1 330 502 L 330 512 L 90 512 Z" fill="#F6ECEF" />
    <text x="210" y="505" text-anchor="middle" font-size="9.5" font-weight="700" fill="#6E3946" text-transform="uppercase">Système Bancaire</text>
    <text x="210" y="536" text-anchor="middle" font-size="14" font-weight="600" fill="#243342">Passerelle Paiement / Izli</text>
    <text x="210" y="554" text-anchor="middle" font-size="10" font-weight="400" fill="#5A6578">Autorisation 2PC &amp; reglement CB</text>
  </g>

  <!-- 6. Réseau de Mobilité Urbaine (Ardoise douce) -->
  <g filter="url(#shadow-soft)">
    <rect x="40" y="255" width="240" height="76" rx="12" fill="#FFFFFF" stroke="#8B9EAF" stroke-width="1.8" />
    <path d="M 40 267 A 12 12 0 0 1 52 255 L 268 255 A 12 12 0 0 1 280 267 L 280 277 L 40 277 Z" fill="#EBF0F5" />
    <text x="160" y="270" text-anchor="middle" font-size="9.5" font-weight="700" fill="#1C2D3D" text-transform="uppercase">Réseau Urbain</text>
    <text x="160" y="301" text-anchor="middle" font-size="14" font-weight="600" fill="#243342">Mobilité Ilévia &amp; Parking</text>
    <text x="160" y="319" text-anchor="middle" font-size="10" font-weight="400" fill="#5A6578">Pass Pass NFC &amp; horodateurs</text>
  </g>

  <!-- ========================================== -->
  <!-- COUCHE 1 : TOUTES LES LIGNES ET COURBES DE LIAISON (EN ARRIÈRE-PLAN) -->
  <!-- ========================================== -->

  <!-- LIAISONS FONCTIONS PRINCIPALES (FP) -->
  <!-- FP1 : Citoyen -> ShopLoc -> Commerçant -->
  <path d="M 290 78 Q 590 140 890 78" fill="none" stroke="#C26750" stroke-width="3" stroke-linecap="round" />

  <!-- FP2 : Citoyen -> ShopLoc -> Mairie & Mobilité -->
  <path d="M 190 116 C 220 280, 580 480, 850 515" fill="none" stroke="#C48B28" stroke-width="2.5" stroke-dasharray="6,4" />

  <!-- FP3 : Association -> ShopLoc -> Commerçants -->
  <path d="M 1030 255 C 1050 185, 1040 150, 1010 116" fill="none" stroke="#4A7A5B" stroke-width="2.5" stroke-dasharray="6,4" />

  <!-- LIAISONS CONTRAINTES (FC) -->
  <!-- FC1 : Commerçant -> ShopLoc -->
  <line x1="890" y1="100" x2="720" y2="260" stroke="#7EA88D" stroke-width="1.8" />

  <!-- FC2 : Mairie -> ShopLoc -->
  <line x1="850" y1="500" x2="720" y2="340" stroke="#DCB162" stroke-width="1.8" />

  <!-- FC3 : Banque -> ShopLoc -->
  <line x1="280" y1="490" x2="460" y2="340" stroke="#B88290" stroke-width="1.8" />

  <!-- FC4 : Mobilité -> ShopLoc -->
  <line x1="280" y1="293" x2="460" y2="293" stroke="#8B9EAF" stroke-width="1.8" />

  <!-- FC5 : Citoyen -> ShopLoc -->
  <line x1="290" y1="100" x2="460" y2="260" stroke="#D88B77" stroke-width="1.8" />

  <!-- FC6 : Association -> ShopLoc -->
  <line x1="910" y1="293" x2="720" y2="293" stroke="#DCB162" stroke-width="1.8" />

  <!-- ========================================== -->
  <!-- COUCHE 2 : TOUTES LES ÉTIQUETTES ET BADGES (AU PREMIER PLAN SUR FOND OPAQUE) -->
  <!-- ========================================== -->

  <!-- Badge FP1 -->
  <g transform="translate(590, 115)">
    <rect x="-165" y="-14" width="330" height="28" rx="14" fill="#FFFFFF" stroke="#C26750" stroke-width="1.8" filter="url(#shadow-soft)" />
    <text x="0" y="5" text-anchor="middle" font-size="11" font-weight="700" fill="#C26750">FP1 : Commander en C&amp;C &amp; retirer en boutique</text>
  </g>

  <!-- Badge FP2 -->
  <g transform="translate(540, 440)">
    <rect x="-140" y="-13" width="280" height="26" rx="13" fill="#FFFFFF" stroke="#C48B28" stroke-width="1.5" filter="url(#shadow-soft)" />
    <text x="0" y="4" text-anchor="middle" font-size="10" font-weight="700" fill="#845A11">FP2 : Convertir régularité en titres mobilité</text>
  </g>

  <!-- Badge FP3 -->
  <g transform="translate(1015, 185)">
    <rect x="-120" y="-12" width="240" height="24" rx="12" fill="#FFFFFF" stroke="#4A7A5B" stroke-width="1.5" filter="url(#shadow-soft)" />
    <text x="0" y="4" text-anchor="middle" font-size="9.5" font-weight="700" fill="#2E583D">FP3 : Onboarding &amp; animation des lots</text>
  </g>

  <!-- Badge FC1 -->
  <g transform="translate(795, 175)">
    <rect x="-70" y="-11" width="140" height="22" rx="11" fill="#FFFFFF" stroke="#7EA88D" stroke-width="1.2" />
    <text x="0" y="4" text-anchor="middle" font-size="9" font-weight="600" fill="#2E583D">FC1 : Caisse &amp; scan &lt; 3s</text>
  </g>

  <!-- Badge FC2 -->
  <g transform="translate(775, 425)">
    <rect x="-75" y="-11" width="150" height="22" rx="11" fill="#FFFFFF" stroke="#DCB162" stroke-width="1.2" />
    <text x="0" y="4" text-anchor="middle" font-size="9" font-weight="600" fill="#845A11">FC2 : Secret &amp; k-anonymat</text>
  </g>

  <!-- Badge FC3 -->
  <g transform="translate(365, 420)">
    <rect x="-75" y="-11" width="150" height="22" rx="11" fill="#FFFFFF" stroke="#B88290" stroke-width="1.2" />
    <text x="0" y="4" text-anchor="middle" font-size="9" font-weight="600" fill="#6E3946">FC3 : Sécurité DSP2 &amp; 2PC</text>
  </g>

  <!-- Badge FC4 -->
  <g transform="translate(365, 293)">
    <rect x="-65" y="-11" width="130" height="22" rx="11" fill="#FFFFFF" stroke="#8B9EAF" stroke-width="1.2" />
    <text x="0" y="4" text-anchor="middle" font-size="9" font-weight="600" fill="#1C2D3D">FC4 : Pass Pass &amp; Parking</text>
  </g>

  <!-- Badge FC5 -->
  <g transform="translate(385, 175)">
    <rect x="-75" y="-11" width="150" height="22" rx="11" fill="#FFFFFF" stroke="#D88B77" stroke-width="1.2" />
    <text x="0" y="4" text-anchor="middle" font-size="9" font-weight="600" fill="#8E3D2A">FC5 : RGAA &amp; carte bi-média</text>
  </g>

  <!-- Badge FC6 -->
  <g transform="translate(815, 293)">
    <rect x="-70" y="-11" width="140" height="22" rx="11" fill="#FFFFFF" stroke="#DCB162" stroke-width="1.2" />
    <text x="0" y="4" text-anchor="middle" font-size="9" font-weight="600" fill="#845A11">FC6 : Zéro commission</text>
  </g>
</svg>"""
    out_path = os.path.join(FIGURES_DIR, "fig_1_2_diagramme_pieuvre_revisee.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[OK] Genere : {out_path}")
    return svg

def generate_fig_2_1_gouvernance():
    """Génère le Schéma de Gouvernance Tripartite & Distinction Garik / ShopLoc."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1020 500" width="100%" height="auto" style="overflow:visible; font-family:'Poppins', sans-serif;">
{DEFS_SVG}
  <!-- FOND GENERAL -->
  <rect x="0" y="0" width="1020" height="500" rx="16" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1.2" />

  <!-- NIVEAU INSTITUTIONNEL (HAUT) -->
  <!-- Mairie de Lille -->
  <g filter="url(#shadow-soft)">
    <rect x="60" y="30" width="410" height="95" rx="14" fill="#FFFFFF" stroke="#DCB162" stroke-width="1.8" />
    <path d="M 60 42 A 14 14 0 0 1 74 30 L 456 30 A 14 14 0 0 1 470 42 L 470 54 L 60 54 Z" fill="#FEF7EB" />
    <text x="75" y="47" font-size="10.5" font-weight="700" fill="#845A11" text-transform="uppercase">Commanditaire Institutionnel · Collectivité</text>
    <text x="75" y="78" font-size="14.5" font-weight="700" fill="#243342">Mairie de Lille (Direction du Commerce &amp; DSI)</text>
    <text x="75" y="98" font-size="11" font-weight="400" fill="#5A6578">• Subventions mobilite urbaine (enveloppes Ilevia &amp; voirie)</text>
    <text x="75" y="114" font-size="11" font-weight="400" fill="#5A6578">• Supervision macroscopique k-anonymisee (zero donnees marchandes)</text>
  </g>

  <!-- Association des Commerçants -->
  <g filter="url(#shadow-soft)">
    <rect x="550" y="30" width="410" height="95" rx="14" fill="#FFFFFF" stroke="#7EA88D" stroke-width="1.8" />
    <path d="M 550 42 A 14 14 0 0 1 564 30 L 946 30 A 14 14 0 0 1 960 42 L 960 54 L 550 54 Z" fill="#EBF3ED" />
    <text x="565" y="47" font-size="10.5" font-weight="700" fill="#2E583D" text-transform="uppercase">Maîtrise d'Usage Terrain · Fédération Métier</text>
    <text x="565" y="78" font-size="14.5" font-weight="700" fill="#243342">Association des Commerçants Lillois</text>
    <text x="565" y="98" font-size="11" font-weight="400" fill="#5A6578">• Validation de l'adhesion des commerçants &amp; distribution cartes QR</text>
    <text x="565" y="114" font-size="11" font-weight="400" fill="#5A6578">• Administration des lots cadeaux &amp; dotations federees</text>
  </g>

  <!-- NIVEAU PRESTATAIRE / MOE (CENTRE GAUCHE) -->
  <g filter="url(#shadow-elevated)">
    <rect x="60" y="200" width="410" height="110" rx="14" fill="#FFFFFF" stroke="#243342" stroke-width="2" />
    <path d="M 60 214 A 14 14 0 0 1 74 200 L 456 200 A 14 14 0 0 1 470 214 L 470 226 L 60 226 Z" fill="#EBF0F5" />
    <text x="75" y="219" font-size="10.5" font-weight="700" fill="#1C2D3D" text-transform="uppercase">Maîtrise d'Œuvre Informatique (MOE) · ESN Prestataire</text>
    <text x="75" y="250" font-size="15" font-weight="700" fill="#243342">Entreprise Garik (Collectif d'Ingénierie)</text>
    <text x="75" y="270" font-size="11" font-weight="400" fill="#5A6578">• Equipe de 5 ingenieurs MIAGE (Khalil, Abdelkader, Gautam, Rayane, Ilyas)</text>
    <text x="75" y="286" font-size="11" font-weight="400" fill="#5A6578">• Conception, developpement TDD, architecture Docker, maintenance SLA</text>
    <text x="75" y="302" font-size="11" font-weight="600" fill="#C26750">Prestataire juridique distinct de la plateforme editee</text>
  </g>

  <!-- NIVEAU PRODUIT LOGICIEL SAAS (CENTRE DROITE) -->
  <g filter="url(#shadow-elevated)">
    <rect x="550" y="200" width="410" height="110" rx="14" fill="#243342" stroke="#1A2530" stroke-width="2" />
    <text x="755" y="235" text-anchor="middle" font-size="16" font-weight="700" fill="#FFFFFF">Plateforme SaaS ShopLoc</text>
    <text x="755" y="258" text-anchor="middle" font-size="12" font-weight="500" fill="#DCB162">Produit Logiciel Multi-Tenant Hébergé</text>
    <text x="755" y="278" text-anchor="middle" font-size="11" font-weight="400" fill="#FAF9F6" opacity="0.85">• API REST Spring Boot 3.3 · PostgreSQL 16 ACID</text>
    <text x="755" y="295" text-anchor="middle" font-size="11" font-weight="400" fill="#FAF9F6" opacity="0.85">• Interfaces Web React 18 / PWA Citoyens, Artisans &amp; Mairie</text>
  </g>

  <!-- NIVEAU ACTEURS TERRAIN (BAS) -->
  <g filter="url(#shadow-soft)">
    <rect x="180" y="380" width="660" height="85" rx="14" fill="#FFFFFF" stroke="#8A9BAE" stroke-width="1.8" />
    <path d="M 180 394 A 14 14 0 0 1 194 380 L 826 380 A 14 14 0 0 1 840 394 L 840 404 L 180 404 Z" fill="#F5F2EB" />
    <text x="510" y="397" text-anchor="middle" font-size="10.5" font-weight="700" fill="#5A6578" text-transform="uppercase">Usagers Finaux &amp; Bénéficiaires du Territoire</text>
    <text x="310" y="428" text-anchor="middle" font-size="13.5" font-weight="700" fill="#C26750">Citoyens Consommateurs</text>
    <text x="310" y="448" text-anchor="middle" font-size="11" font-weight="400" fill="#5A6578">Achats C&amp;C, cagnotte fidelite, Ilevia</text>
    <line x1="510" y1="412" x2="510" y2="455" stroke="#DCD6CD" stroke-width="1" />
    <text x="700" y="428" text-anchor="middle" font-size="13.5" font-weight="700" fill="#4A7A5B">Artisans &amp; Commerçants</text>
    <text x="700" y="448" text-anchor="middle" font-size="11" font-weight="400" fill="#5A6578">Scan caisse rapide, zero commission</text>
  </g>

  <!-- FLECHES RELATIONNELLES EXPLICITES -->
  <!-- 1. Mairie <-> Association (Convention tripartite) -->
  <path d="M 470 77 L 550 77" fill="none" stroke="#C48B28" stroke-width="2" marker-end="url(#arrow-honey)" />
  <text x="510" y="70" text-anchor="middle" font-size="9" font-weight="600" fill="#845A11">Convention</text>

  <!-- 2. Mairie & Asso -> Garik (Cahier des charges & SLA) -->
  <path d="M 265 125 L 265 200" fill="none" stroke="#C48B28" stroke-width="2.2" marker-end="url(#arrow-honey)" />
  <text x="270" y="165" font-size="9" font-weight="600" fill="#845A11">Contrat MOE</text>

  <!-- 3. Garik -> ShopLoc (Conception, deploiement & hebergement) -->
  <path d="M 470 255 L 550 255" fill="none" stroke="#243342" stroke-width="2.5" marker-end="url(#arrow-slate)" />
  <text x="510" y="247" text-anchor="middle" font-size="9.5" font-weight="700" fill="#243342">Edite &amp; Opere</text>

  <!-- 4. ShopLoc -> Usagers (Services et interfaces applicatives) -->
  <path d="M 755 310 L 755 380" fill="none" stroke="#4A7A5B" stroke-width="2.2" marker-end="url(#arrow-sage)" />
  <text x="760" y="350" font-size="9" font-weight="600" fill="#2E583D">Web &amp; PWA</text>

  <path d="M 600 310 L 400 380" fill="none" stroke="#C26750" stroke-width="2.2" marker-end="url(#arrow-terracotta)" />
</svg>"""
    out_path = os.path.join(FIGURES_DIR, "fig_2_1_gouvernance_tripartite.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[OK] Genere : {out_path}")
    return svg

def generate_fig_3_1_use_cases_uml():
    """Génère le Diagramme Global des Cas d'Utilisation UML (norme Cockburn / AFNOR)."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 660" width="100%" height="auto" style="overflow:visible; font-family:'Poppins', sans-serif;">
{DEFS_SVG}
  <!-- FOND GENERAL -->
  <rect x="0" y="0" width="1280" height="660" rx="16" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1.2" />

  <!-- FRONTIERE DU SYSTEME SHOPLOC -->
  <rect x="280" y="30" width="720" height="600" rx="16" fill="#FFFFFF" stroke="#243342" stroke-width="2" />
  <path d="M 280 44 A 14 14 0 0 1 294 30 L 986 30 A 14 14 0 0 1 1000 44 L 1000 62 L 280 62 Z" fill="#243342" />
  <text x="640" y="52" text-anchor="middle" font-size="13" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">Système ShopLoc — Frontière Applicative &amp; Cas d'Utilisation</text>

  <!-- ACTEURS HUMAINS (GAUCHE) -->
  <!-- 1. Citoyen -->
  <g filter="url(#shadow-soft)">
    <rect x="35" y="80" width="200" height="85" rx="12" fill="#FFFFFF" stroke="#D88B77" stroke-width="1.8" />
    <circle cx="75" cy="115" r="16" fill="#FBEEEA" stroke="#D88B77" stroke-width="1.5" />
    <text x="75" y="120" text-anchor="middle" font-size="11" font-weight="700" fill="#8E3D2A">C</text>
    <text x="105" y="112" font-size="13" font-weight="700" fill="#243342">Citoyen</text>
    <text x="105" y="130" font-size="10" font-weight="500" fill="#C26750">« Acteur Principal »</text>
    <text x="105" y="145" font-size="9" font-weight="400" fill="#5A6578">Pierre / Julie</text>
  </g>

  <!-- 2. Commerçant -->
  <g filter="url(#shadow-soft)">
    <rect x="35" y="270" width="200" height="85" rx="12" fill="#FFFFFF" stroke="#7EA88D" stroke-width="1.8" />
    <circle cx="75" cy="305" r="16" fill="#EBF3ED" stroke="#7EA88D" stroke-width="1.5" />
    <text x="75" y="310" text-anchor="middle" font-size="11" font-weight="700" fill="#2E583D">A</text>
    <text x="105" y="302" font-size="13" font-weight="700" fill="#243342">Commerçant</text>
    <text x="105" y="320" font-size="10" font-weight="500" fill="#4A7A5B">« Acteur Principal »</text>
    <text x="105" y="335" font-size="9" font-weight="400" fill="#5A6578">Suzanne (Boulangère)</text>
  </g>

  <!-- 3. Association -->
  <g filter="url(#shadow-soft)">
    <rect x="35" y="470" width="200" height="85" rx="12" fill="#FFFFFF" stroke="#DCB162" stroke-width="1.8" />
    <circle cx="75" cy="505" r="16" fill="#FEF7EB" stroke="#DCB162" stroke-width="1.5" />
    <text x="75" y="510" text-anchor="middle" font-size="11" font-weight="700" fill="#845A11">G</text>
    <text x="105" y="502" font-size="13" font-weight="700" fill="#243342">Association</text>
    <text x="105" y="520" font-size="10" font-weight="500" fill="#C48B28">« Gestionnaire »</text>
    <text x="105" y="535" font-size="9" font-weight="400" fill="#5A6578">Onboarding &amp; Lots</text>
  </g>

  <!-- ACTEURS SECONDAIRES & SYSTEMES TIERS (DROITE) -->
  <!-- 4. Mairie (DSI) -->
  <g filter="url(#shadow-soft)">
    <rect x="1045" y="80" width="200" height="85" rx="12" fill="#FFFFFF" stroke="#DCB162" stroke-width="1.8" />
    <circle cx="1085" cy="115" r="16" fill="#FEF7EB" stroke="#DCB162" stroke-width="1.5" />
    <text x="1085" y="120" text-anchor="middle" font-size="11" font-weight="700" fill="#845A11">M</text>
    <text x="1115" y="112" font-size="13" font-weight="700" fill="#243342">DSI Mairie</text>
    <text x="1115" y="130" font-size="10" font-weight="500" fill="#845A11">« Superviseur »</text>
    <text x="1115" y="145" font-size="9" font-weight="400" fill="#5A6578">Marius (Cadre)</text>
  </g>

  <!-- 5. Banque Izli -->
  <g filter="url(#shadow-soft)">
    <rect x="1045" y="270" width="200" height="85" rx="12" fill="#FFFFFF" stroke="#B88290" stroke-width="1.8" />
    <rect x="1069" y="299" width="32" height="32" rx="6" fill="#F6ECEF" stroke="#B88290" stroke-width="1.5" />
    <text x="1085" y="319" text-anchor="middle" font-size="10" font-weight="700" fill="#6E3946">SI</text>
    <text x="1115" y="302" font-size="13" font-weight="700" fill="#243342">Passerelle Banque</text>
    <text x="1115" y="320" font-size="10" font-weight="500" fill="#6E3946">« Système Tiers »</text>
    <text x="1115" y="335" font-size="9" font-weight="400" fill="#5A6578">Autorisation 2PC</text>
  </g>

  <!-- 6. Mobilité Pass Pass / Parking -->
  <g filter="url(#shadow-soft)">
    <rect x="1045" y="470" width="200" height="85" rx="12" fill="#FFFFFF" stroke="#8B9EAF" stroke-width="1.8" />
    <rect x="1069" y="499" width="32" height="32" rx="6" fill="#EBF0F5" stroke="#8B9EAF" stroke-width="1.5" />
    <text x="1085" y="519" text-anchor="middle" font-size="10" font-weight="700" fill="#1C2D3D">API</text>
    <text x="1115" y="502" font-size="13" font-weight="700" fill="#243342">API Mobilité</text>
    <text x="1115" y="520" font-size="10" font-weight="500" fill="#1C2D3D">« Système Tiers »</text>
    <text x="1115" y="535" font-size="9" font-weight="400" fill="#5A6578">Ilévia &amp; Horodateur</text>
  </g>

  <!-- 5 CAS D'UTILISATION PRINCIPAUX (ELLIPSES UML DANS LE SYSTEME) -->
  
  <!-- UC-01 : Commande Click & Collect 2PC -->
  <g filter="url(#shadow-soft)">
    <ellipse cx="640" cy="115" rx="260" ry="38" fill="#FFFFFF" stroke="#C26750" stroke-width="2" />
    <text x="640" y="112" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">UC-01 : Passer Commande Click &amp; Collect Multi-Commerces</text>
    <text x="640" y="130" text-anchor="middle" font-size="10" font-weight="500" fill="#C26750">[Orchestration Two-Phase Commit 2PC ACID]</text>
  </g>

  <!-- UC-02 : Caisse & Double Fidélité -->
  <g filter="url(#shadow-soft)">
    <ellipse cx="640" cy="225" rx="260" ry="38" fill="#FFFFFF" stroke="#4A7A5B" stroke-width="2" />
    <text x="640" y="222" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">UC-02 : Enregistrer Passage Caisse Physique &amp; Double Fidélité</text>
    <text x="640" y="240" text-anchor="middle" font-size="10" font-weight="500" fill="#4A7A5B">[Scan optique &lt; 3s · Cagnotte Commerçant + Ville]</text>
  </g>

  <!-- UC-03 : Mobilité Urbaine (Bus & Parking) -->
  <g filter="url(#shadow-soft)">
    <ellipse cx="640" cy="335" rx="260" ry="38" fill="#FFFFFF" stroke="#C48B28" stroke-width="2" />
    <text x="640" y="332" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">UC-03 : Activer Titre Mobilité Douce (Ilévia &amp; Parking)</text>
    <text x="640" y="350" text-anchor="middle" font-size="10" font-weight="500" fill="#845A11">[Voucher Pass Pass Ilévia ou 20 min Stationnement Voirie]</text>
  </g>

  <!-- UC-04 : Batch VFP & Relances -->
  <g filter="url(#shadow-soft)">
    <ellipse cx="640" cy="445" rx="260" ry="38" fill="#FFFFFF" stroke="#6E3946" stroke-width="2" />
    <text x="640" y="442" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">UC-04 : Calculer Cohorte Régularité &amp; Notifier Usagers</text>
    <text x="640" y="460" text-anchor="middle" font-size="10" font-weight="500" fill="#6E3946">[Batch nocturne SQL · Métriques k-anonymisées DSI]</text>
  </g>

  <!-- UC-05 : Conventionnement & Onboarding -->
  <g filter="url(#shadow-soft)">
    <ellipse cx="640" cy="555" rx="260" ry="38" fill="#FFFFFF" stroke="#2B5270" stroke-width="2" />
    <text x="640" y="552" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">UC-05 : Conventionner Commune &amp; Onboarder Boutique</text>
    <text x="640" y="570" text-anchor="middle" font-size="10" font-weight="500" fill="#2B5270">[Validation Kbis · Insee API · RBAC 4 Niveaux]</text>
  </g>

  <!-- LIAISONS ACTEURS -> USE CASES -->
  <!-- Citoyen -> UC-01, UC-02, UC-03 -->
  <line x1="235" y1="120" x2="380" y2="120" stroke="#243342" stroke-width="1.8" />
  <line x1="235" y1="135" x2="420" y2="210" stroke="#243342" stroke-width="1.5" />
  <line x1="235" y1="150" x2="400" y2="330" stroke="#243342" stroke-width="1.5" />

  <!-- Commerçant -> UC-01 (préparation), UC-02 (scan caisse), UC-05 (onboarding) -->
  <line x1="235" y1="300" x2="420" y2="135" stroke="#243342" stroke-width="1.5" />
  <line x1="235" y1="312" x2="380" y2="230" stroke="#243342" stroke-width="1.8" />
  <line x1="235" y1="330" x2="420" y2="540" stroke="#243342" stroke-width="1.5" />

  <!-- Association -> UC-05, UC-02 (gestion lots) -->
  <line x1="235" y1="512" x2="380" y2="550" stroke="#243342" stroke-width="1.8" />
  <line x1="235" y1="495" x2="420" y2="245" stroke="#243342" stroke-width="1.5" />

  <!-- Banque -> UC-01 -->
  <line x1="1045" y1="312" x2="900" y2="125" stroke="#B88290" stroke-width="1.8" stroke-dasharray="4,3" />

  <!-- API Mobilité -> UC-03 -->
  <line x1="1045" y1="512" x2="900" y2="345" stroke="#8B9EAF" stroke-width="1.8" stroke-dasharray="4,3" />

  <!-- DSI Mairie -> UC-04, UC-05, UC-03 -->
  <line x1="1045" y1="120" x2="880" y2="440" stroke="#DCB162" stroke-width="1.8" />
  <line x1="1045" y1="135" x2="880" y2="550" stroke="#DCB162" stroke-width="1.5" />
  <line x1="1045" y1="110" x2="880" y2="330" stroke="#DCB162" stroke-width="1.5" />
</svg>"""
    out_path = os.path.join(FIGURES_DIR, "fig_3_1_use_cases_uml.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[OK] Genere : {out_path}")
    return svg

if __name__ == "__main__":
    generate_fig_1_1_bete_a_cornes()
    generate_fig_1_2_diagramme_pieuvre()
    generate_fig_2_1_gouvernance()
    generate_fig_3_1_use_cases_uml()
    print("[SUCCES] 4 diagrammes vectoriels SVG generes.")

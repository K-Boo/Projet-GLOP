#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de la page de revue visuelle de l'Étape 02 — Personas & User Journey Maps (ShopLoc)
Master 2 MIAGE — Université de Lille — UE GLOP (2026-2027)

Règle permanente 8 : Zéro languette (aucune bordure gauche/supérieure asymétrique d'accent).
Conception UI sur-mesure, symétrique, sobre et inspirée des publications d'ingénierie haut de gamme.
Zéro emoji, zéro jargon obscur, présentation conforme au standard UX Justinmind.
"""
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))
agent_projet_dir = os.path.join(project_root, "agent_projet")
comp_dir = os.path.join(agent_projet_dir, "templates", "components")
output_dir = os.path.join(agent_projet_dir, "docs", "01_Cadrage_Et_Cahier_Des_Charges_R1", "figures")
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(comp_dir, "personas_dashboard.html"), "r", encoding="utf-8") as f:
    personas_html = f.read()

with open(os.path.join(comp_dir, "user_journey_map_pierre.html"), "r", encoding="utf-8") as f:
    ujm_pierre_html = f.read()

with open(os.path.join(comp_dir, "user_journey_map_actifs.html"), "r", encoding="utf-8") as f:
    ujm_actifs_html = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Revue Visuelle Étape 02 — Personas Approfondis &amp; Parcours Utilisateurs Cibles (ShopLoc)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      background: #FAF9F6;
      color: #1E252D;
      font-family: 'Poppins', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      line-height: 1.6;
      padding: 44px 24px 88px;
    }}
    .container {{
      max-width: 1180px;
      margin: 0 auto;
    }}

    /* HEADER CARD — DESIGN ÉDITORIAL SYMÉTRIQUE SANS LANGUETTE */
    .header-card {{
      background: #FFFFFF;
      border: 1px solid #E8E6DF;
      border-radius: 16px;
      padding: 36px 36px 30px;
      margin-bottom: 40px;
      box-shadow: 0 4px 20px -2px rgba(36, 51, 66, 0.05);
    }}
    .header-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      padding-bottom: 14px;
      border-bottom: 1px solid #F0EDE8;
    }}
    .meta-tag {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 11px;
      font-weight: 700;
      color: #243342;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }}
    .meta-tag-pill {{
      display: inline-flex;
      align-items: center;
      background: #F4F2ED;
      border: 1px solid #E2DDD5;
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 600;
      color: #5A6578;
    }}
    h1 {{
      font-size: 26px;
      font-weight: 700;
      color: #243342;
      margin-bottom: 8px;
      letter-spacing: -0.015em;
    }}
    .subtitle {{
      font-size: 13.5px;
      color: #5A6578;
      margin-bottom: 22px;
    }}
    .toc-bar {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      align-items: center;
      padding-top: 14px;
      border-top: 1px solid #F0EDE8;
    }}
    .toc-label {{
      font-size: 11.5px;
      font-weight: 700;
      color: #243342;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-right: 6px;
    }}
    .toc-link {{
      font-size: 12px;
      font-weight: 600;
      color: #243342;
      text-decoration: none;
      background: #FAF9F6;
      border: 1px solid #E2DDD5;
      padding: 6px 16px;
      border-radius: 9999px;
      transition: all 0.15s ease;
    }}
    .toc-link:hover {{
      background: #243342;
      color: #FAF9F6;
      border-color: #243342;
    }}

    /* SECTION WRAPPER */
    .review-section {{
      margin-bottom: 52px;
    }}
    .section-title-bar {{
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 18px;
      padding-bottom: 10px;
      border-bottom: 1.5px solid #E8E6DF;
    }}
    .section-num {{
      font-size: 11px;
      font-weight: 700;
      color: #C26750;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 4px;
    }}
    .section-heading {{
      font-size: 20px;
      font-weight: 700;
      color: #243342;
    }}
    .badge-norme {{
      background: #EBF3ED;
      border: 1px solid #7EA88D;
      color: #2E583D;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 14px;
      border-radius: 9999px;
      letter-spacing: 0.04em;
    }}

    /* CADRE D'EXPLICATION PEDAGOGIQUE */
    .pedago-box {{
      background: #FFFFFF;
      border: 1px solid #E8E6DF;
      border-radius: 12px;
      padding: 20px 24px;
      margin-top: 18px;
      font-size: 12.5px;
      color: #374151;
      box-shadow: 0 2px 8px rgba(36, 51, 66, 0.03);
    }}
    .pedago-box h4 {{
      font-size: 13px;
      font-weight: 700;
      color: #243342;
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .pedago-box p {{
      margin-bottom: 8px;
      line-height: 1.6;
    }}
    .pedago-box p:last-child {{
      margin-bottom: 0;
    }}
    .pedago-box ul {{
      margin-left: 20px;
      margin-top: 6px;
      margin-bottom: 8px;
    }}
    .pedago-box li {{
      margin-bottom: 4px;
    }}

    /* TABLE DE SYNTHÈSE */
    .summary-table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 12px;
      font-size: 11.5px;
    }}
    .summary-table th {{
      background: #F4F2ED;
      color: #243342;
      font-weight: 700;
      text-align: left;
      padding: 8px 12px;
      border-bottom: 1.5px solid #243342;
      border-top: 1.5px solid #243342;
    }}
    .summary-table td {{
      padding: 8px 12px;
      border-bottom: 1px solid #E8E6DF;
      color: #374151;
      vertical-align: top;
    }}
    .summary-table tr:last-child td {{
      border-bottom: 1.5px solid #243342;
    }}

    /* ACTION BAR */
    .validation-card {{
      background: #FFFFFF;
      border: 1px solid #BBF7D0;
      border-radius: 14px;
      padding: 24px 28px;
      margin-top: 36px;
      box-shadow: 0 4px 16px rgba(34, 197, 94, 0.08);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
    }}
    .validation-text h3 {{
      font-size: 16px;
      font-weight: 700;
      color: #166534;
      margin-bottom: 4px;
    }}
    .validation-text p {{
      font-size: 12.5px;
      color: #4B5563;
    }}
  </style>
</head>
<body>

<div class="container">

  <!-- HEADER EDITORIAL CARD -->
  <div class="header-card">
    <div class="header-top">
      <div class="meta-tag">
        <span style="width:10px; height:10px; border-radius:50%; background:#4A7A5B;"></span>
        <span>ShopLoc • UE GLOP 2026-2027 • Master 2 MIAGE</span>
      </div>
      <div class="meta-tag-pill">Étape 02 (SEC-02) • Revue Visuelle de Co-Design</div>
    </div>
    <h1>Revue Visuelle : Personas Approfondis &amp; Parcours Cibles</h1>
    <p class="subtitle">
      Conformément aux règles du projet et au standard UX Justinmind, cette page permet de vérifier et valider les 3 modèles visuels avant la conversion en images PNG et la rédaction finale de la Section 02.
    </p>
    <div class="toc-bar">
      <span class="toc-label">Modèles Visuels :</span>
      <a href="#fig-2-1" class="toc-link">Figure 2.1 — Tableau de Bord des 4 Personas</a>
      <a href="#fig-2-2" class="toc-link">Figure 2.2 — User Journey Map : Pierre (74 ans)</a>
      <a href="#fig-2-3" class="toc-link">Figure 2.3 — User Journey Map : Julie &amp; Arthur</a>
      <a href="#validation" class="toc-link" style="background:#EBF3ED; color:#2E583D; border-color:#7EA88D;">Point de Validation</a>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- 1. FIGURE 2.1 : TABLEAU DE BORD DES 4 PERSONAS                            -->
  <!-- ========================================================================= -->
  <section id="fig-2-1" class="review-section">
    <div class="section-title-bar">
      <div>
        <div class="section-num">Modèle Visuel 01 / 03 • Cadrage Acteurs</div>
        <h2 class="section-heading">Figure 2.1 — Fiches des 4 Personas Approfondis</h2>
      </div>
      <span class="badge-norme">Accessibilité &amp; Clarté Universelle</span>
    </div>

    <!-- INSERTION DU COMPOSANT AUTONOME -->
    {personas_html}

    <!-- CADRE PÉDAGOGIQUE D'ANALYSE -->
    <div class="pedago-box">
      <h4>Rôle Stratégique &amp; Justification du Modèle Personas</h4>
      <p>
        Ce tableau de bord synthétise les 4 profils fondamentaux dégagés lors du cadrage métier :
      </p>
      <table class="summary-table">
        <thead>
          <tr>
            <th>Persona &amp; Âge</th>
            <th>Rôle &amp; Contexte Métier</th>
            <th>Canal Principal</th>
            <th>Avantage / Dispositif ShopLoc Clé</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Pierre Dupont (74 ans)</strong></td>
            <td>Retraité du centre-ville, tournée pédestre matinale rue Solférino. Exclu des applications mobiles complexes.</td>
            <td>Carte Pass Papier QR / NFC</td>
            <td>1 ticket de bus offert par jour après 10 achats sur 15 jours. Possibilité de procuration pour un proche.</td>
          </tr>
          <tr>
            <td><strong>Suzanne Lemaire (22 ans)</strong></td>
            <td>Vendeuse au Fournil, gestion des heures de pointe et préparation des paniers en boutique.</td>
            <td>Tablette Caisse Tactile</td>
            <td>Scan express en moins de 3 secondes, validation 1 clic, tableau de bord montrant la hausse des ventes.</td>
          </tr>
          <tr>
            <td><strong>Marius Vasseur (27 ans)</strong></td>
            <td>Responsable numérique en mairie, copilote avec les associations de commerçants.</td>
            <td>Portail Web Mairie</td>
            <td>Tableau de bord territorial avec données 100% anonymisées, mesure claire de l'impact des aides publiques.</td>
          </tr>
          <tr>
            <td><strong>Julie (31 ans) &amp; Arthur (34 ans)</strong></td>
            <td>Actifs urbains pressés et parents du jeune Théo (7 ans, école Jules Ferry). Temps compté et stationnement difficile.</td>
            <td>Application Mobile Simple</td>
            <td>Panier groupé multi-boutiques (Julie) et 20 minutes de parking école gratuites via plaque auto (Arthur).</td>
          </tr>
        </tbody>
      </table>
      <p style="margin-top: 10px; font-size: 11.5px; color: #5A6578;">
        <strong>Alignement Charte Graphique :</strong> Présentation symétrique sans languette, bordures complètes 1px `#E8E6DF`, badges arrondis centrés avec précision, palettes pastel adaptées à chaque rôle (Terracotta, Sauge, Ocre miel, Ardoise).
      </p>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 2. FIGURE 2.2 : USER JOURNEY MAP — PIERRE DUPONT (74 ANS)                 -->
  <!-- ========================================================================= -->
  <section id="fig-2-2" class="review-section">
    <div class="section-title-bar">
      <div>
        <div class="section-num">Modèle Visuel 02 / 03 • Parcours Citoyen Présentiel</div>
        <h2 class="section-heading">Figure 2.2 — User Journey Map : Pierre Dupont (74 ans)</h2>
      </div>
      <span class="badge-norme">Format Justinmind • Gabarit 1 Page</span>
    </div>

    <!-- INSERTION DU COMPOSANT AUTONOME -->
    {ujm_pierre_html}

    <!-- CADRE PÉDAGOGIQUE D'ANALYSE -->
    <div class="pedago-box">
      <h4>Analyse UX du Parcours de Pierre (Format Justinmind)</h4>
      <p>
        Conformément aux standards UX Design Justinmind, la modélisation intègre les 6 niveaux d'analyse chronologique :
      </p>
      <ul>
        <li><strong>Bandeau Persona &amp; Scénario :</strong> Identification du profil, contexte de vie et objectif premier (préserver le lien humain sans barrière technique).</li>
        <li><strong>Chronologie (5 Phases) :</strong> 1. Découverte &amp; Carte papier &rarr; 2. Tournée matinale &rarr; 3. Achat &amp; Scan caisse rapide &rarr; 4. Déblocage du ticket de bus &rarr; 5. Routine &amp; Fidélité pérenne.</li>
        <li><strong>Actions &amp; Points de contact :</strong> Gestes simples et physiques (comptoir boulangerie, commerces de rue, tablette commerçant, bus).</li>
        <li><strong>Pensées &amp; Points de friction :</strong> Hésitations initiales face à la technologie, peur de ralentir la file, fatigue physique de la marche.</li>
        <li><strong>Courbe Émotionnelle Vectorielle :</strong> Progression visible d'un niveau d'appréhension initial vers un état de soulagement et de satisfaction durable.</li>
        <li><strong>Solutions ShopLoc :</strong> Carte physique gratuite, zéro compte web requis, scan en moins de 3s, transport offert et système d'entraide/procuration.</li>
      </ul>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 3. FIGURE 2.3 : USER JOURNEY MAP — JULIE & ARTHUR (31/34 ANS)             -->
  <!-- ========================================================================= -->
  <section id="fig-2-3" class="review-section">
    <div class="section-title-bar">
      <div>
        <div class="section-num">Modèle Visuel 03 / 03 • Parcours Actifs &amp; Mobilité</div>
        <h2 class="section-heading">Figure 2.3 — User Journey Map : Julie &amp; Arthur (31/34 ans)</h2>
      </div>
      <span class="badge-norme">Format Justinmind • Gabarit 1 Page</span>
    </div>

    <!-- INSERTION DU COMPOSANT AUTONOME -->
    {ujm_actifs_html}

    <!-- CADRE PÉDAGOGIQUE D'ANALYSE -->
    <div class="pedago-box">
      <h4>Analyse UX du Parcours de Julie &amp; Arthur (Format Justinmind)</h4>
      <p>
        Ce parcours illustre la complémentarité entre la commande numérique et l'expérience de mobilité urbaine familiale :
      </p>
      <ul>
        <li><strong>Bandeau Persona &amp; Scénario :</strong> Parents d'un jeune enfant (Théo, 7 ans), emploi du temps serré, recherche d'efficacité et de stationnement garanti.</li>
        <li><strong>Chronologie (5 Phases) :</strong> 1. Inscription express &amp; Plaque auto &rarr; 2. Commande groupée multi-artisans &rarr; 3. Retrait en boutique &amp; Goûter école &rarr; 4. Activation des 20 min de parking gratuit &rarr; 5. Fidélité et gestion bienveillante des vacances.</li>
        <li><strong>Actions &amp; Points de contact :</strong> Interface mobile fluide, étagères de retrait chez les artisans, voirie municipale sans passage à l'horodateur.</li>
        <li><strong>Pensées &amp; Points de friction :</strong> Stress des formulaires interminables, peur des commerces fermés, coût prohibitif du stationnement scolaire.</li>
        <li><strong>Courbe Émotionnelle Vectorielle :</strong> Évolution positive depuis la charge mentale de la journée vers le soulagement d'un retrait instantané et d'un stationnement offert à 16h30.</li>
        <li><strong>Solutions ShopLoc :</strong> Panier partagé, trajet optimisé à pied, liaison de la plaque d'immatriculation avec la voirie, absence de pénalité en période de vacances.</li>
      </ul>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 4. CHECKLIST DE VALIDATION & POINT D'ARRÊT                                -->
  <!-- ========================================================================= -->
  <div id="validation" class="validation-card">
    <div class="validation-text">
      <h3>Point de Validation de l'Étape 02 (Stop &amp; Wait)</h3>
      <p>
        Les 3 modèles visuels sont prêts pour inspection. Veuillez valider leur conformité graphique (Justinmind, absence de RGAA/jargon, harmonie pastel) avant le lancement de la rédaction finale de la Section 02.
      </p>
    </div>
    <div style="font-size: 11px; color: #166534; font-weight: 600; background: #F0FDF4; border: 1px solid #86EFAC; padding: 8px 16px; border-radius: 8px;">
      Statut : En attente de validation manuelle dans le chat
    </div>
  </div>

</div>

</body>
</html>
"""

review_html_path = os.path.join(output_dir, "revue_visuels_etape_02.html")
with open(review_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[SUCCES] Page de revue generee : {review_html_path} ({len(html_content)} octets)")

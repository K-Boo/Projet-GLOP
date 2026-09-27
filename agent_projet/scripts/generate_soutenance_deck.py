#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERATEUR DU DIAPORAMA DE SOUTENANCE OFFICIEL R1 (generate_soutenance_deck.py)
Entreprise Garik — Master 2 MIAGE — Université de Lille — UE GLOP (2026-2027)

Génère une présentation HTML5 16:9 moderne, propre et épurée, sans emojis,
avec navigation clavier, fiches orateurs, intégration des diagrammes HD et export PDF vectoriel.
"""

import os
import base64
import subprocess
import sys

def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            ext = os.path.splitext(path)[1].lower()
            mime = "image/png" if ext == ".png" else "image/svg+xml" if ext == ".svg" else "image/jpeg"
            return f"data:{mime};base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

def build_deck():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(script_dir))
    
    docs_dir = os.path.join(repo_root, "agent_projet", "docs")
    pres_dir = os.path.join(docs_dir, "04_Presentations_Diaporamas")
    os.makedirs(pres_dir, exist_ok=True)
    
    # Images
    logo_univ = get_base64(os.path.join(docs_dir, "assets", "logo_univ_lille.png"))
    logo_fst = get_base64(os.path.join(docs_dir, "assets", "logo_fst_informatique.png"))
    logo_garik = get_base64(os.path.join(docs_dir, "01_Cadrage_Et_Cahier_Des_Charges_R1", "figures", "logo_garik.png"))
    fig_usm = get_base64(os.path.join(docs_dir, "01_Cadrage_Et_Cahier_Des_Charges_R1", "figures", "fig_3_3_user_story_mapping.png"))
    fig_archi = get_base64(os.path.join(docs_dir, "01_Cadrage_Et_Cahier_Des_Charges_R1", "figures", "fig_4_1_choix_techniques.png"))
    fig_gantt = get_base64(os.path.join(docs_dir, "01_Cadrage_Et_Cahier_Des_Charges_R1", "figures", "fig_5_1_gantt_annuel_officiel.png"))
    fig_matrice = get_base64(os.path.join(docs_dir, "01_Cadrage_Et_Cahier_Des_Charges_R1", "figures", "fig_1_1_matrice_positionnement.png"))

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Soutenance R1 — Entreprise Garik — Solution ShopLoc</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    @page {{
      size: 16in 9in;
      margin: 0;
    }}
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    :root {{
      --navy-dark: #0A192F;
      --navy-primary: #0F2A4A;
      --navy-surface: #132D4E;
      --slate-50: #F8FAFC;
      --slate-100: #F1F5F9;
      --slate-200: #E2E8F0;
      --slate-300: #CBD5E1;
      --slate-600: #475569;
      --slate-700: #334155;
      --slate-800: #1E293B;
      --slate-900: #0F172A;
      --blue-accent: #2563EB;
      --blue-subtle: #EFF6FF;
      --emerald-accent: #059669;
      --emerald-subtle: #ECFDF5;
      --amber-accent: #D97706;
      --amber-subtle: #FFFBEB;
    }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #020617;
      color: var(--slate-900);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      overflow-x: hidden;
    }}
    
    /* Top Progress Bar */
    #progress-container {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background: rgba(255, 255, 255, 0.1);
      z-index: 1000;
    }}
    #progress-bar {{
      height: 100%;
      width: 8.33%;
      background: linear-gradient(90deg, #3B82F6, #10B981);
      transition: width 0.3s ease;
    }}

    /* Control Toolbar */
    .toolbar {{
      position: fixed;
      bottom: 20px;
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
      padding: 8px 18px;
      border-radius: 30px;
      border: 1px solid rgba(255, 255, 255, 0.15);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
      z-index: 1000;
    }}
    .toolbar button {{
      background: transparent;
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #E2E8F0;
      padding: 6px 14px;
      font-size: 12px;
      font-weight: 600;
      border-radius: 20px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }}
    .toolbar button:hover {{
      background: var(--blue-accent);
      border-color: var(--blue-accent);
      color: #FFFFFF;
    }}
    .toolbar .slide-nav-text {{
      font-size: 13px;
      font-weight: 700;
      color: #F8FAFC;
      padding: 0 8px;
      font-variant-numeric: tabular-nums;
    }}

    /* Deck Layout */
    .deck {{
      width: 100%;
      max-width: 1280px;
      height: 720px;
      position: relative;
      margin: 20px 0;
    }}
    .slide {{
      width: 100%;
      height: 100%;
      background: #FFFFFF;
      border-radius: 12px;
      padding: 40px 55px;
      display: none;
      flex-direction: column;
      justify-content: space-between;
      position: absolute;
      top: 0;
      left: 0;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
      overflow: hidden;
    }}
    .slide.active {{
      display: flex;
    }}

    /* Print Mode (PDF 16:9 natif) */
    @media print {{
      body {{
        background: transparent !important;
        margin: 0 !important;
        padding: 0 !important;
      }}
      #progress-container, .toolbar, .speaker-notes-panel {{
        display: none !important;
      }}
      .deck {{
        max-width: none !important;
        height: auto !important;
        margin: 0 !important;
      }}
      .slide {{
        display: flex !important;
        position: relative !important;
        width: 16in !important;
        height: 9in !important;
        padding: 50px 70px !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        page-break-after: always !important;
      }}
    }}

    /* Header */
    .slide-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--slate-200);
      padding-bottom: 12px;
      margin-bottom: 16px;
    }}
    .header-left {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .header-badge {{
      background: var(--slate-100);
      color: var(--slate-700);
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .header-title {{
      font-size: 12px;
      font-weight: 600;
      color: var(--slate-600);
    }}
    .header-criteria {{
      background: var(--emerald-subtle);
      color: var(--emerald-accent);
      border: 1px solid rgba(5, 150, 105, 0.25);
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
    }}

    /* Slide Title Area */
    .title-area {{
      margin-bottom: 20px;
    }}
    .title-area h2 {{
      font-size: 28px;
      font-weight: 800;
      color: var(--navy-primary);
      letter-spacing: -0.02em;
      line-height: 1.2;
    }}
    .title-area p {{
      font-size: 14px;
      color: var(--slate-600);
      margin-top: 4px;
      font-weight: 500;
    }}

    /* Main Content Grids */
    .slide-body {{
      flex-grow: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}
    .grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      align-items: stretch;
    }}
    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      align-items: stretch;
    }}
    .grid-4 {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      align-items: stretch;
    }}

    /* Cards & Components */
    .card {{
      background: var(--slate-50);
      border: 1px solid var(--slate-200);
      border-radius: 10px;
      padding: 18px 22px;
      display: flex;
      flex-direction: column;
    }}
    .card.highlight {{
      background: #FFFFFF;
      border-color: #BFDBFE;
      box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.05);
    }}
    .card-title {{
      font-size: 15px;
      font-weight: 700;
      color: var(--navy-primary);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .card-text {{
      font-size: 13px;
      color: var(--slate-700);
      line-height: 1.55;
    }}
    .card ul {{
      list-style: none;
      padding: 0;
    }}
    .card ul li {{
      font-size: 13px;
      color: var(--slate-700);
      line-height: 1.5;
      margin-bottom: 8px;
      position: relative;
      padding-left: 16px;
    }}
    .card ul li::before {{
      content: "▪";
      position: absolute;
      left: 0;
      color: var(--blue-accent);
      font-size: 12px;
    }}
    
    /* Metrics & Big Numbers */
    .metric-box {{
      background: #FFFFFF;
      border: 1px solid var(--slate-200);
      border-radius: 8px;
      padding: 14px 16px;
      text-align: center;
    }}
    .metric-val {{
      font-size: 26px;
      font-weight: 800;
      color: var(--blue-accent);
      font-family: 'JetBrains Mono', monospace;
    }}
    .metric-label {{
      font-size: 11px;
      font-weight: 600;
      color: var(--slate-600);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-top: 4px;
    }}

    /* Diagrams & Image Display */
    .diagram-container {{
      border: 1px solid var(--slate-200);
      border-radius: 10px;
      background: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 380px;
      overflow: hidden;
      padding: 8px;
    }}
    .diagram-container img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }}

    /* Tables */
    .styled-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
    }}
    .styled-table th {{
      background: var(--slate-100);
      color: var(--navy-primary);
      text-align: left;
      padding: 9px 12px;
      font-weight: 700;
      border-bottom: 2px solid var(--slate-300);
    }}
    .styled-table td {{
      padding: 8px 12px;
      border-bottom: 1px solid var(--slate-200);
      color: var(--slate-700);
    }}
    .styled-table tr:last-child td {{
      border-bottom: none;
    }}
    .styled-table .num {{
      font-family: 'JetBrains Mono', monospace;
      font-weight: 600;
      text-align: right;
    }}

    /* Footer */
    .slide-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid var(--slate-200);
      padding-top: 12px;
      font-size: 11px;
      color: var(--slate-600);
    }}
    .footer-speaker {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #EFF6FF;
      color: #1E40AF;
      padding: 3px 10px;
      border-radius: 12px;
      font-weight: 600;
    }}
    .footer-timing {{
      color: var(--slate-600);
      font-family: 'JetBrains Mono', monospace;
      font-weight: 500;
    }}

    /* Special Slide: Cover */
    .cover-slide {{
      background: linear-gradient(135deg, #0A192F 0%, #0F2A4A 60%, #1E3A8A 100%);
      color: #FFFFFF;
      justify-content: space-between;
      padding: 55px 70px;
    }}
    .cover-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .cover-logos {{
      display: flex;
      align-items: center;
      gap: 20px;
      background: rgba(255, 255, 255, 0.08);
      padding: 8px 18px;
      border-radius: 8px;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }}
    .cover-logos img {{
      height: 38px;
      filter: brightness(0) invert(1);
    }}
    .cover-middle {{
      margin: 40px 0;
    }}
    .cover-tag {{
      display: inline-block;
      background: rgba(37, 99, 235, 0.3);
      border: 1px solid #3B82F6;
      color: #93C5FD;
      font-size: 12px;
      font-weight: 700;
      padding: 5px 14px;
      border-radius: 20px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 16px;
    }}
    .cover-middle h1 {{
      font-size: 46px;
      font-weight: 800;
      color: #FFFFFF;
      letter-spacing: -0.03em;
      line-height: 1.15;
    }}
    .cover-middle p {{
      font-size: 20px;
      color: #CBD5E1;
      margin-top: 12px;
      font-weight: 400;
      max-width: 850px;
    }}
    .cover-bottom {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 16px;
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      padding-top: 20px;
    }}
    .cover-team-member {{
      display: flex;
      flex-direction: column;
    }}
    .cover-team-member .name {{
      font-size: 13px;
      font-weight: 700;
      color: #FFFFFF;
    }}
    .cover-team-member .role {{
      font-size: 11px;
      color: #94A3B8;
      margin-top: 2px;
    }}

    /* Speaker Notes Drawer (Toggled by key 'S') */
    .speaker-notes-panel {{
      position: fixed;
      bottom: 75px;
      right: 20px;
      width: 380px;
      max-height: 280px;
      background: #0F172A;
      color: #F8FAFC;
      border: 1px solid #334155;
      border-radius: 10px;
      padding: 16px 20px;
      box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
      display: none;
      z-index: 1000;
      overflow-y: auto;
      font-size: 12px;
      line-height: 1.5;
    }}
    .speaker-notes-panel.visible {{
      display: block;
    }}
    .speaker-notes-panel h4 {{
      font-size: 13px;
      color: #38BDF8;
      margin-bottom: 8px;
      display: flex;
      justify-content: space-between;
    }}
  </style>
</head>
<body>

<div id="progress-container">
  <div id="progress-bar"></div>
</div>

<div class="deck">

  <!-- ==================== SLIDE 01 : TITRE & CARTOUCHE ==================== -->
  <section class="slide cover-slide active" id="slide-1" data-notes="Khalil Bouchama : Bonjour à tous. Nous représentons l'entreprise étudiante Garik pour vous présenter notre réponse à l'appel d'offres territorial ShopLoc. Notre objectif : réancrer les flux d'achats dans nos centres-villes grâce à une solution souveraine, sobre et inclusive.">
    <div class="cover-top">
      <div class="cover-tag">Appel d'Offres ShopLoc · Jalon R1</div>
      <div class="cover-logos">
        <img src="{logo_univ}" alt="Univ Lille">
        <img src="{logo_fst}" alt="FST Informatique">
        <img src="{logo_garik}" alt="Garik">
      </div>
    </div>
    <div class="cover-middle">
      <h1>ShopLoc — Plateforme de Vitalité Commerciale & Citoyenne</h1>
      <p>Cadrage Fonctionnel, Architecture Frugale et Étude des Coûts Complets pour les Collectivités et Commerces de Proximité.</p>
    </div>
    <div class="cover-bottom">
      <div class="cover-team-member">
        <span class="name">Khalil Bouchama</span>
        <span class="role">Scrum Master R1 · Pilotage</span>
      </div>
      <div class="cover-team-member">
        <span class="name">Abdelkader Heddi</span>
        <span class="role">Qualité, Exigences & Risques</span>
      </div>
      <div class="cover-team-member">
        <span class="name">Ilyas Ait Ali</span>
        <span class="role">Architecture Front & UX</span>
      </div>
      <div class="cover-team-member">
        <span class="name">Rayane Alli</span>
        <span class="role">Architecture Back & DevOps</span>
      </div>
      <div class="cover-team-member">
        <span class="name">Gautam Demeulemeester</span>
        <span class="role">Gestion Financière & Modèles</span>
      </div>
    </div>
  </section>

  <!-- ==================== SLIDE 02 : ENTREPRISE GARIK & GOUVERNANCE ==================== -->
  <section class="slide" id="slide-2" data-notes="Khalil Bouchama (00:00 - 03:00) : Présentation de notre entreprise Garik. Notre force réside dans la clarté de notre gouvernance : nous appliquons les 6 rôles préconisés par l'UE GLOP avec un Scrum Master tournant. Sur ce premier jalon, j'assure le pilotage et la coordination générale. Sprints de 2 semaines, rituels hebdomadaires, suivi continu sous GitLab.">
    <div class="slide-header">
      <div class="header-left">
        <span class="header-badge">Gouvernance & Équipe</span>
        <span class="header-title">Organisation du Collectif d'Ingénierie</span>
      </div>
      <span class="header-criteria">Critères 6 & 8 : Pilotage & Références de l'Entreprise</span>
    </div>
    <div class="title-area">
      <h2>L'Entreprise Garik & Organisation du Projet</h2>
      <p>Une gouvernance agile éprouvée, une responsabilisation collective et un pilotage transparent.</p>
    </div>
    <div class="slide-body">
      <div class="grid-3">
        <div class="card highlight">
          <div class="card-title">Identité de Garik</div>
          <div class="card-text">
            <ul>
              <li><strong>Positionnement :</strong> Société étudiante d'ingénierie logicielle spécialisée dans les systèmes d'information territoriaux et la frugalité numérique.</li>
              <li><strong>Valeurs clés :</strong> Souveraineté des données communales, inclusion sans fracture, transparence méthodologique et zéro jargon prédateur.</li>
              <li><strong>Environnement de travail :</strong> Forge GitLab souveraine, documentation continue sous Markdown et intégration continue stricte.</li>
            </ul>
          </div>
        </div>
        <div class="card">
          <div class="card-title">Matrice des 6 Rôles GLOP</div>
          <div class="card-text">
            <ul>
              <li><strong>Scrum Master tournant :</strong> Khalil Bouchama (R1), facilitation, vélocité et levée des blocages.</li>
              <li><strong>Qualité & Acceptation :</strong> Abdelkader Heddi, conformité aux exigences et couverture de tests.</li>
              <li><strong>Déploiement & DevOps :</strong> Rayane Alli, CI/CD, conteneurs et traçabilité.</li>
              <li><strong>Architecture Back & Front :</strong> Rayane Alli (Back) & Ilyas Ait Ali (Front).</li>
              <li><strong>Gestion Financière :</strong> Gautam Demeulemeester, centres d'analyse et TCO.</li>
            </ul>
          </div>
        </div>
        <div class="card">
          <div class="card-title">Rituels & Cadence Agile</div>
          <div class="card-text">
            <ul>
              <li><strong>Sprints de 2 semaines :</strong> Objectifs opérationnels découplés et revues d'étape formalisées.</li>
              <li><strong>Stand-up bi-hebdomadaires :</strong> Synchronisation rapide (15 min) et réallocation dynamique de la charge.</li>
              <li><strong>Gestion des risques :</strong> Registre ADR (Architecture Decision Records) historisé et buffers de sécurité de 72h.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Projet ShopLoc · UE GLOP</span>
      <span class="footer-speaker">Khalil Bouchama · Scrum Master R1</span>
      <span class="footer-timing">00:00 – 03:00</span>
    </div>
  </section>

  <!-- ==================== SLIDE 03 : PROBLEMATIQUE TERRITORIALE & BESOINS ==================== -->
  <section class="slide" id="slide-3" data-notes="Abdelkader Heddi (03:00 - 04:30) : Pourquoi ShopLoc ? Les commerces de centre-ville souffrent d'une double peine : la concurrence des plateformes e-commerce mondialisées et les commissions étouffantes de 25 à 30 % des plateformes privées. À cela s'ajoute la fracture numérique qui frappe nos aînés. ShopLoc apporte une réponse de proximité, gratuite pour l'usager et protectrice pour le commerçant.">
    <div class="slide-header">
      <div class="header-left">
        <span class="header-badge">Analyse Métier</span>
        <span class="header-title">Diagnostic Territorial & Enjeux de Proximité</span>
      </div>
      <span class="header-criteria">Critère 3 : Réponse aux Problématiques MOA</span>
    </div>
    <div class="title-area">
      <h2>Diagnostic Territorial & Problématique Métier</h2>
      <p>Redynamiser les cœurs de ville face aux géants du web tout en protégeant les marges des artisans.</p>
    </div>
    <div class="slide-body">
      <div class="grid-2">
        <div class="card">
          <div class="card-title">Les 3 Fractures Observées</div>
          <div class="card-text">
            <ul>
              <li><strong>Évasion commerciale :</strong> Perte de fréquentation piétonne au profit des zones périphériques et des marketplaces hégémoniques.</li>
              <li><strong>Prédation financière privée :</strong> Commissions confiscatoires (20 à 30 %) imposées par les acteurs privés (Deliveroo, UberEats) incompatibles avec les marges des petits commerçants.</li>
              <li><strong>Fracture numérique générationnelle :</strong> 38 % des aînés ne disposent pas d'un smartphone récent ou refusent de renseigner leur carte bancaire en ligne.</li>
            </ul>
          </div>
        </div>
        <div class="card highlight">
          <div class="card-title">La Proposition de Valeur ShopLoc</div>
          <div class="card-text">
            <ul>
              <li><strong>Gratuité absolue pour le citoyen :</strong> Aucun coût d'adhésion pour les usagers, incitation directe à fréquenter les boutiques.</li>
              <li><strong>Préservation des marges marchandes :</strong> Forfait associatif fixe modéré, sans prélèvement de commission sur les ventes.</li>
              <li><strong>Ancrage physique & piétonnier :</strong> Le numérique devient un levier pour faire franchir le seuil physique des commerces.</li>
              <li><strong>Souveraineté des données :</strong> Maîtrise publique locale conforme au RGPD et au secret des affaires.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Projet ShopLoc · UE GLOP</span>
      <span class="footer-speaker">Abdelkader Heddi · Qualité & Exigences</span>
      <span class="footer-timing">03:00 – 04:30</span>
    </div>
  </section>

  <!-- ==================== SLIDE 04 : PERSONAS & INCLUSION ==================== -->
  <section class="slide" id="slide-4" data-notes="Abdelkader Heddi (04:30 - 06:00) : Pour garantir l'adhésion de tous, nous avons conçu 4 personas réels. Pierre, 74 ans, qui utilise ShopLoc sans smartphone grâce à sa carte physique QR code. Suzanne, artisane boulangère, qui encaisse en 3 secondes sans perturber son coup de feu. Julie et Arthur, qui réservent en Click & Collect de proximité. Et Marius, à la mairie, qui pilote les retombées économiques sans violer le secret des affaires.">
    <div class="slide-header">
      <div class="header-left">
        <span class="header-badge">Expérience Utilisateur</span>
        <span class="header-title">Inclusivité & Parcours Cibles</span>
      </div>
      <span class="header-criteria">Critères 4 & 5 : Périmètre Complet & Solutions Innovantes</span>
    </div>
    <div class="title-area">
      <h2>Personas Clés & Réponses Inclusives</h2>
      <p>Une solution universelle pensée pour tous les profils de l'écosystème communal.</p>
    </div>
    <div class="slide-body">
      <div class="grid-4">
        <div class="card highlight">
          <div class="card-title">Pierre (74 ans)</div>
          <div class="card-text">
            <p><strong>Retraité de centre-ville</strong></p>
            <ul>
              <li><strong>Innovation :</strong> Carte physique avec QR code imprimé.</li>
              <li>Zéro smartphone exigé.</li>
              <li>Contraste visuel AAA (RGAA).</li>
              <li>Cumul de points automatique lors du passage en caisse.</li>
            </ul>
          </div>
        </div>
        <div class="card">
          <div class="card-title">Suzanne (22 ans)</div>
          <div class="card-text">
            <p><strong>Artisane boulangère</strong></p>
            <ul>
              <li>Scan client instantané (&lt; 3 s).</li>
              <li>Gestion de stock manuelle simplifiée.</li>
              <li>Libre choix de son barème de fidélité et de ses récompenses.</li>
              <li>Protection contre les faux passages.</li>
            </ul>
          </div>
        </div>
        <div class="card">
          <div class="card-title">Julie & Arthur (32 ans)</div>
          <div class="card-text">
            <p><strong>Jeunes actifs urbains</strong></p>
            <ul>
              <li>Panier Click & Collect multi-boutiques en une commande.</li>
              <li>Retrait piéton garanti sous 2h.</li>
              <li>Zéro livraison polluante.</li>
              <li>Suivi en direct des créneaux.</li>
            </ul>
          </div>
        </div>
        <div class="card">
          <div class="card-title">Marius (27 ans)</div>
          <div class="card-text">
            <p><strong>Cadre DSI Mairie</strong></p>
            <ul>
              <li>Tableau de bord macroscopique des flux économiques.</li>
              <li>Anonymisation RGPD stricte.</li>
              <li>Secret des affaires : chiffre d'affaires individuel masqué.</li>
              <li>Pilotage des mobilités douces.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Projet ShopLoc · UE GLOP</span>
      <span class="footer-speaker">Abdelkader Heddi · Qualité & Exigences</span>
      <span class="footer-timing">04:30 – 06:00</span>
    </div>
  </section>

  <!-- ==================== SLIDE 05 : PERIMETRE METIER & DOUBLE MOTEUR VFP ==================== -->
  <section class="slide" id="slide-5" data-notes="Ilyas Ait Ali (06:00 - 07:30) : L'innovation maîtresse de ShopLoc réside dans le découplage strict de deux moteurs de fidélité. D'un côté, le moteur marchand décentralisé : chaque commerçant gère ses points et ses cadeaux en toute indépendance. De l'autre, le moteur VFP territorial : la mairie récompense la régularité physique (10 passages en 15 jours) par des tickets de bus ou des minutes de parking.">
    <div class="slide-header">
      <div class="header-left">
        <span class="header-badge">Règles Métier</span>
        <span class="header-title">Architecture des Flux de Fidélité</span>
      </div>
      <span class="header-criteria">Critères 3 & 5 : Fonctionnalités des Services & Innovation</span>
    </div>
    <div class="title-area">
      <h2>Découplage des Moteurs de Fidélisation</h2>
      <p>Éviter toute confusion comptable grâce à deux systèmes indépendants et complémentaires.</p>
    </div>
    <div class="slide-body">
      <div class="grid-2">
        <div class="card">
          <div class="card-title">1. Moteur Marchand (Décentralisé & Privé)</div>
          <div class="card-text">
            <ul>
              <li><strong>Principe :</strong> 1 achat = X points propres au commerce chez qui le client consomme.</li>
              <li><strong>Autonomie totale :</strong> Chaque commerçant définit ses seuils et ses lots cadeaux (ex. 50 pts = baguette offerte).</li>
              <li><strong>Anti-fraude :</strong> Obligation d'un historique d'achat antérieur vérifié pour débloquer les récompenses.</li>
              <li><strong>Validité :</strong> Expiration des points marchands glissante à 1 an sans achat.</li>
            </ul>
          </div>
        </div>
        <div class="card highlight">
          <div class="card-title">2. Moteur Territorial VFP (Public & Fédérateur)</div>
          <div class="card-text">
            <ul>
              <li><strong>Objectif :</strong> Récompenser la fréquentation régulière du centre-ville, indépendamment du montant dépensé.</li>
              <li><strong>Règle d'activation VFP :</strong> Au moins <strong>10 passages physiques</strong> sur une fenêtre glissante de <strong>15 jours consécutifs</strong>.</li>
              <li><strong>Avantage territorial :</strong> Déclenchement automatique d'<strong>1 ticket de transport</strong> ou <strong>20 min de stationnement</strong>.</li>
              <li><strong>Financement :</strong> Prise en charge intégrale par la Mairie via son budget mobilités douces.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Projet ShopLoc · UE GLOP</span>
      <span class="footer-speaker">Ilyas Ait Ali · Architecture Front & UX</span>
      <span class="footer-timing">06:00 – 07:30</span>
    </div>
  </section>

  <!-- ==================== SLIDE 06 : USER STORY MAPPING ==================== -->
  <section class="slide" id="slide-6" data-notes="Ilyas Ait Ali (07:30 - 09:00) : Voici notre cartographie User Story Mapping. Nous avons priorisé le backlog selon la méthode MoSCoW en 3 jalons opérationnels. Pour le jalon R4 de décembre, nous livrons le MVP Click & Collect transactionnel avec validation 2PC. En février, nous intégrons la fidélité commerçante, et pour R5 en mars, le moteur VFP territorial complet.">
    <div class="slide-header">
      <div class="header-left">
        <span class="header-badge">Trajectoire Produit</span>
        <span class="header-title">User Story Mapping & Découpage en 3 Livrables</span>
      </div>
      <span class="header-criteria">Critères 2 & 4 : Respect des Délais & Périmètre Couvert</span>
    </div>
    <div class="title-area">
      <h2>User Story Mapping & Trajectoire en 3 Releases</h2>
      <p>Une démarche incrémentale axée sur la valeur d'usage et la sécurisation des jalons contractuels.</p>
    </div>
    <div class="slide-body">
      <div class="grid-2" style="align-items: center;">
        <div class="diagram-container">
          <img src="{fig_usm}" alt="User Story Mapping">
        </div>
        <div class="card">
          <div class="card-title">Découpage des 3 Releases</div>
          <div class="card-text">
            <ul>
              <li><strong>Release 1 (MVP — Jalon R4 / 18 Décembre 2026) :</strong>
                <br>Socle d'authentification, catalogue des boutiques, panier Click & Collect multi-commerces et protocole 2PC de réservation en boutique.</li>
              <li style="margin-top: 10px;"><strong>Release 2 (V1.5 — Février 2027) :</strong>
                <br>Moteur de fidélité marchande décentralisée, gestion simplifiée des stocks et alertes de retrait par SMS / Notification.</li>
              <li style="margin-top: 10px;"><strong>Release 3 (V2 Complète — Jalon R5 / 19 Mars 2027) :</strong>
                <br>Moteur de régularité VFP (10 passages / 15j), intégration des mobilités douces, tableau de bord Mairie agrégé et bilan d'exploitation.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Projet ShopLoc · UE GLOP</span>
      <span class="footer-speaker">Ilyas Ait Ali · Architecture Front & UX</span>
      <span class="footer-timing">07:30 – 09:00</span>
    </div>
  </section>

  <!-- ==================== SLIDE 07 : CHOIX TECHNIQUES & ARCHITECTURE ==================== -->
  <section class="slide" id="slide-7" data-notes="Rayane Alli (09:00 - 10:30) : Passons à l'architecture. Nous avons fait le choix assumé d'un monolithe modulaire 3-tiers plutôt que des microservices. Pourquoi ? Pour éliminer la complexité réseau, les surcoûts d'infrastructure et garantir l'éco-conception. Notre stack repose sur React/TypeScript en front, Java Spring Boot 3 en back, et PostgreSQL 16 partitionné par commune.">
    <div class="slide-header">
      <div class="header-left">
        <span class="header-badge">Architecture Logicielle</span>
        <span class="header-title">Stack Technique Industrielle & Frugale</span>
      </div>
      <span class="header-criteria">Critère 7 : Maîtrise des Technologies Proposées</span>
    </div>
    <div class="title-area">
      <h2>Architecture 3-Tiers Modulaire & Choix Outils</h2>
      <p>Robustesse éprouvée, modularité stricte et sobriété environnementale en exploitation (Run).</p>
    </div>
    <div class="slide-body">
      <div class="grid-2" style="align-items: center;">
        <div class="diagram-container">
          <img src="{fig_archi}" alt="Architecture Technique">
        </div>
        <div class="card">
          <div class="card-title">Justification des Choix Techniques</div>
          <div class="card-text">
            <ul>
              <li><strong>Front-end Web & Mobile :</strong> React 18 + TypeScript, rendu performant, PWA responsive, accessibilité RGAA AAA pour Pierre.</li>
              <li><strong>Back-end Modulaire :</strong> Spring Boot 3 (Java 21), injection de dépendances, architecture hexagonale, API REST sous OpenAPI 3.1.</li>
              <li><strong>Données Relationnelles :</strong> PostgreSQL 16, intégrité référentielle stricte, partitionnement multi-tenant par commune.</li>
              <li><strong>Frugalité & Éco-Conception :</strong> Rejet motivé des microservices (surconsommation CPU/RAM et complexité inutile pour 120 commerces).</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Projet ShopLoc · UE GLOP</span>
      <span class="footer-speaker">Rayane Alli · Architecture Back & DevOps</span>
      <span class="footer-timing">09:00 – 10:30</span>
    </div>
  </section>

  <!-- ==================== SLIDE 08 : TRANSACTIONNEL & MOCKS ==================== -->
  <section class="slide" id="slide-8" data-notes="Rayane Alli (10:30 - 12:00) : Deux points techniques majeurs garantissent la solidité de notre offre. D'abord, le protocole 2-Phase Commit pour le Click & Collect : les stocks physiques et virtuels restent cohérents sous 2h avec annulation automatique si non-réponse. Ensuite, la simulation réaliste des partenaires : des mocks RESTful isolés pour la banque et les valideurs de bus et parking.">
    <div class="slide-header">
      <div class="header-left">
        <span class="header-badge">Ingénierie & Fiabilité</span>
        <span class="header-title">Intégrité Transactionnelle & Mocks Partenaires</span>
      </div>
      <span class="header-criteria">Critères 5 & 7 : Solutions Métiers & Rigueur d'Ingénierie</span>
    </div>
    <div class="title-area">
      <h2>Fiabilité Transactionnelle & Démonstrateur Portable</h2>
      <p>Garantir la cohérence des stocks en magasin et simuler fidèlement l'écosystème territorial.</p>
    </div>
    <div class="slide-body">
      <div class="grid-2">
        <div class="card highlight">
          <div class="card-title">Protocole 2-Phase Commit (2PC)</div>
          <div class="card-text">
            <p><strong>Gestion du Click & Collect en &lt; 2h :</strong></p>
            <ul>
              <li><strong>Phase 1 (Prepare) :</strong> Réservation de l'article par le client, notification instantanée au commerçant, pose d'un verrou temporaire sur le stock.</li>
              <li><strong>Phase 2 (Commit) :</strong> Validation manuelle par le commerçant en boutique ; si aucune réponse sous 2h, rollback automatique et libération du stock.</li>
              <li><strong>Zéro conflit :</strong> Cohérence absolue garantie entre l'étalage physique et la plateforme en ligne.</li>
            </ul>
          </div>
        </div>
        <div class="card">
          <div class="card-title">Environnement Mocks & Déploiement Portable</div>
          <div class="card-text">
            <p><strong>Démonstrateur opérationnel clé en main :</strong></p>
            <ul>
              <li><strong>Mock Banque :</strong> Simulation des paiements sécurisés sans manipulation de données bancaires réelles.</li>
              <li><strong>Mock Voirie & Transports :</strong> Émulation des bornes de parking Indigo et des valideurs de bus Ilévia pour l'avantage VFP.</li>
              <li><strong>Profil Démonstrateur :</strong> Déploiement complet en une seule commande <code>docker compose up -d</code> pour les jurys R4 et R5.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Projet ShopLoc · UE GLOP</span>
      <span class="footer-speaker">Rayane Alli · Architecture Back & DevOps</span>
      <span class="footer-timing">10:30 – 12:00</span>
    </div>
  </section>

  <!-- ==================== SLIDE 09 : GANTT ANNUEL & JALONS ==================== -->
  <section class="slide" id="slide-9" data-notes="Gautam Demeulemeester (12:00 - 13:15) : Abordons la planification temporelle. Notre calendrier annuel est articulé autour des 5 jalons contractuels de l'UE GLOP. Le chemin critique traverse le cadrage R1, le socle architectural R4 et l'intégration complète R5. Nous avons prévu des marges de sécurité de 72h avant chaque rendu et neutralisé les semaines de coupure pour garantir 100% de ponctualité.">
    <div class="slide-header">
      <div class="header-left">
        <span class="header-badge">Planification</span>
        <span class="header-title">Calendrier Annuel & Jalons Contractuels</span>
      </div>
      <span class="header-criteria">Critère 2 : Capacité à Respecter les Délais</span>
    </div>
    <div class="title-area">
      <h2>Diagramme de Gantt & Chemin Critique</h2>
      <p>Un pilotage par les jalons contractuels garantissant la tenue stricte des échéances académiques.</p>
    </div>
    <div class="slide-body">
      <div class="grid-2" style="align-items: center;">
        <div class="diagram-container">
          <img src="{fig_gantt}" alt="Diagramme de Gantt Annuel">
        </div>
        <div class="card">
          <div class="card-title">Les 5 Jalons Officiels Contractuels</div>
          <div class="card-text">
            <table class="styled-table">
              <thead>
                <tr>
                  <th>Jalon</th>
                  <th>Échéance</th>
                  <th>Livrable Exigé</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>R1</strong></td>
                  <td>18/09/2026</td>
                  <td>Cahier des charges complet & Soutenance le 21/09</td>
                </tr>
                <tr>
                  <td><strong>R2</strong></td>
                  <td>12/10/2026</td>
                  <td>Choix des outils & mise en place opérationnelle</td>
                </tr>
                <tr>
                  <td><strong>R3</strong></td>
                  <td>30/11/2026</td>
                  <td>Évaluation financière, VAN, TRI et ROI</td>
                </tr>
                <tr>
                  <td><strong>R4</strong></td>
                  <td>18/12/2026</td>
                  <td>Architecture V1 & Prototype 2PC (Soutenance 04/01)</td>
                </tr>
                <tr>
                  <td><strong>R5</strong></td>
                  <td>19/03/2027</td>
                  <td>Système V2 complet & Bilan final (Soutenance 22/03)</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Projet ShopLoc · UE GLOP</span>
      <span class="footer-speaker">Gautam Demeulemeester · Gestion Financière</span>
      <span class="footer-timing">12:00 – 13:15</span>
    </div>
  </section>

  <!-- ==================== SLIDE 10 : COUTS COMPLETS BUILD & RUN ==================== -->
  <section class="slide" id="slide-10" data-notes="Gautam Demeulemeester (13:15 - 14:15) : Voici l'analyse détaillée de nos coûts selon la méthode des centres d'analyse. En charges directes : 480h de développement à 25€ de taux horaire chargé (12 000€) et 2 400€ d'achats cloud. En charges indirectes : 36 000€ répartis rigoureusement entre centres auxiliaires et principaux. Résultat : un coût de revient unitaire de 87,80€ par unité d'œuvre.">
    <div class="slide-header">
      <div class="header-left">
        <span class="header-badge">Analyse Financière</span>
        <span class="header-title">Méthode des Coûts Complets par Centres d'Analyse</span>
      </div>
      <span class="header-criteria">Critère 1 : Coût Détaillé du Projet (Build, Run & Maint.)</span>
    </div>
    <div class="title-area">
      <h2>Analyse des Coûts Complets (Build & Run)</h2>
      <p>Une transparence comptable totale distinguant la fabrication initiale et l'exploitation annuelle.</p>
    </div>
    <div class="slide-body">
      <div class="grid-3">
        <div class="card">
          <div class="card-title">1. Charges Directes</div>
          <div class="card-text">
            <table class="styled-table">
              <tr>
                <td>MOD Réalisation (480 h à 25 €)</td>
                <td class="num">12 000 €</td>
              </tr>
              <tr>
                <td>Achats directs Cloud & VPS</td>
                <td class="num">2 400 €</td>
              </tr>
              <tr>
                <td>Heures relation commerciale (60 h)</td>
                <td class="num">1 500 €</td>
              </tr>
              <tr>
                <td><strong>Total Charges Directes</strong></td>
                <td class="num" style="color: var(--blue-accent);"><strong>15 900 €</strong></td>
              </tr>
            </table>
          </div>
        </div>
        <div class="card highlight">
          <div class="card-title">2. Répartition Indirecte (36 k€)</div>
          <div class="card-text">
            <table class="styled-table">
              <tr>
                <th>Centre Principal</th>
                <th style="text-align: right;">Montant Réparti</th>
              </tr>
              <tr>
                <td>Production (Build, Run, Maint.)</td>
                <td class="num">24 960 €</td>
              </tr>
              <tr>
                <td>Commercial & Déploiement</td>
                <td class="num">11 040 €</td>
              </tr>
              <tr>
                <td><strong>Total Indirect Secondaire</strong></td>
                <td class="num" style="color: var(--emerald-accent);"><strong>36 000 €</strong></td>
              </tr>
            </table>
          </div>
        </div>
        <div class="card">
          <div class="card-title">3. Coûts Unitaires Clés</div>
          <div class="metric-box" style="margin-bottom: 10px;">
            <div class="metric-val">87,80 € / h</div>
            <div class="metric-label">Coût Complet Unitaire / U.O.</div>
          </div>
          <div class="card-text" style="font-size: 11px;">
            Incorpore la main-d'œuvre directe d'ingénierie ainsi que la quote-part intégrale d'outillage, serveurs et administration.
          </div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Projet ShopLoc · UE GLOP</span>
      <span class="footer-speaker">Gautam Demeulemeester · Gestion Financière</span>
      <span class="footer-timing">13:15 – 14:15</span>
    </div>
  </section>

  <!-- ==================== SLIDE 11 : BUSINESS MODEL & RENTABILITE ==================== -->
  <section class="slide" id="slide-11" data-notes="Gautam Demeulemeester (14:15 - 15:00) : Comment pérenniser la solution ? Notre modèle SaaS repose sur un forfait mensuel fixe de 40€ par boutique, souscrit par l'association des commerçants avec l'appui de la mairie. Pour une ville pilote de 120 commerces, le chiffre d'affaires atteint 88 000€. Face à un coût de revient complet de 70 800€, Garik dégage une marge nette de 17 200€, soit 19,5% de rentabilité.">
    <div class="slide-header">
      <div class="header-left">
        <span class="header-badge">Modèle Économique</span>
        <span class="header-title">Viabilité & Taux de Marge Opérationnel</span>
      </div>
      <span class="header-criteria">Critère 1 : Modèle Économique & Viabilité à Long Terme</span>
    </div>
    <div class="title-area">
      <h2>Modèle Économique SaaS & Rentabilité</h2>
      <p>Une tarification équitable sans commission sur les ventes assurant un modèle rentable et pérenne.</p>
    </div>
    <div class="slide-body">
      <div class="grid-3">
        <div class="card">
          <div class="card-title">Convention Tripartite</div>
          <div class="card-text">
            <ul>
              <li><strong>Contrat Mairie / Association :</strong> La collectivité subventionne l'ingénierie et offre les dotations VFP mobilités.</li>
              <li><strong>Adhésion Commerçants :</strong> Forfait fixe de <strong>40 € HT / mois</strong> par point de vente.</li>
              <li><strong>Zéro commission :</strong> Respect intégral des marges des commerçants de proximité.</li>
            </ul>
          </div>
        </div>
        <div class="card highlight">
          <div class="card-title">Équilibre Financier (An 1)</div>
          <div class="card-text">
            <table class="styled-table">
              <tr>
                <td>CA Prévisionnel (120 commerces + Ville)</td>
                <td class="num">88 000 €</td>
              </tr>
              <tr>
                <td>Coût de revient complet (Build + Run)</td>
                <td class="num">70 800 €</td>
              </tr>
              <tr>
                <td><strong>Marge Nette Opérationnelle</strong></td>
                <td class="num" style="color: var(--emerald-accent);"><strong>+ 17 200 €</strong></td>
              </tr>
            </table>
          </div>
        </div>
        <div class="card">
          <div class="card-title">Indicateurs de Performance</div>
          <div class="metric-box" style="margin-bottom: 10px;">
            <div class="metric-val" style="color: var(--emerald-accent);">19,5 %</div>
            <div class="metric-label">Taux de Marge Nette Garik</div>
          </div>
          <div class="metric-box">
            <div class="metric-val" style="color: var(--blue-accent);">38 Boutiques</div>
            <div class="metric-label">Point Mort (Seuil d'Équilibre)</div>
          </div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Projet ShopLoc · UE GLOP</span>
      <span class="footer-speaker">Gautam Demeulemeester · Gestion Financière</span>
      <span class="footer-timing">14:15 – 15:00</span>
    </div>
  </section>

  <!-- ==================== SLIDE 12 : SYNTHESE DE L'OFFRE & ENGAGEMENTS ==================== -->
  <section class="slide" id="slide-12" data-notes="Khalil Bouchama (Clôture) : En synthèse, l'offre de l'entreprise Garik coche l'ensemble des 8 critères du cahier des charges : un coût maîtrisé, des délais sécurisés, une architecture sobre et une vraie réponse territoriale sans exclusion. Nous sommes prêts pour le jalon R2 et entièrement à votre écoute pour la session de questions-réponses.">
    <div class="slide-header">
      <div class="header-left">
        <span class="header-badge">Clôture & Décision</span>
        <span class="header-title">Proposition de Valeur & Engagements Contractuels</span>
      </div>
      <span class="header-criteria">Synthèse des 8 Critères de Sélection</span>
    </div>
    <div class="title-area">
      <h2>Pourquoi Choisir l'Entreprise Garik ?</h2>
      <p>Une vision pragmatique, une maîtrise complète des coûts et un engagement éthique total.</p>
    </div>
    <div class="slide-body">
      <div class="grid-4">
        <div class="card highlight">
          <div class="card-title">1. Souveraineté & Frugalité</div>
          <div class="card-text">
            Zéro sur-ingénierie microservices. Hébergement local sécurisé, open-source et maîtrise intégrale des flux de données communales.
          </div>
        </div>
        <div class="card highlight">
          <div class="card-title">2. Zéro Exclusion Numérique</div>
          <div class="card-text">
            Inclusion garantie de nos aînés par la carte physique QR code et l'accessibilité contrastée RGAA AAA.
          </div>
        </div>
        <div class="card highlight">
          <div class="card-title">3. Rigueur de Livraison</div>
          <div class="card-text">
            Cadre Scrum strict, buffers de sécurité de 72h et engagement formel sur la tenue des 5 jalons contractuels.
          </div>
        </div>
        <div class="card highlight">
          <div class="card-title">4. Transparence Éthique</div>
          <div class="card-text">
            Transparence académique certifiée, code auditable sous SonarQube et respect absolu du secret des affaires.
          </div>
        </div>
      </div>
      <div style="margin-top: 24px; text-align: center; background: var(--slate-100); padding: 14px 20px; border-radius: 8px; border: 1px dashed var(--slate-300);">
        <span style="font-size: 14px; font-weight: 700; color: var(--navy-primary);">
          Merci pour votre attention — L'équipe Garik est à votre disposition pour la phase de Questions / Réponses (5 min).
        </span>
      </div>
    </div>
    <div class="slide-footer">
      <span>Projet ShopLoc · UE GLOP</span>
      <span class="footer-speaker">Khalil Bouchama · Scrum Master R1</span>
      <span class="footer-timing">15:00 — Clôture</span>
    </div>
  </section>

</div>

<!-- Interactive Toolbar -->
<div class="toolbar">
  <button onclick="prevSlide()" title="Diapositive précédente (Flèche Gauche)">❮ Précédent</button>
  <span class="slide-nav-text" id="slide-nav">01 / 12</span>
  <button onclick="nextSlide()" title="Diapositive suivante (Flèche Droite)">Suivant ❯</button>
  <button onclick="toggleNotes()" id="btn-notes" title="Activer les notes d'orateur (Touche S)">🎙️ Notes</button>
  <button onclick="toggleFullscreen()" title="Plein écran (Touche F)">⛶ Plein écran</button>
  <button onclick="window.print()" title="Exporter en PDF 16:9">🖨️ Imprimer / PDF</button>
</div>

<!-- Speaker Notes Drawer -->
<div class="speaker-notes-panel" id="notes-panel">
  <h4>
    <span>Notes de Soutenance & Conduite</span>
    <span id="notes-time" style="color: #94A3B8; font-size: 11px;">15 min chrono</span>
  </h4>
  <p id="notes-content">Notes pour l'orateur...</p>
</div>

<script>
  let currentSlide = 1;
  const totalSlides = 12;

  function updateSlide() {{
    document.querySelectorAll('.slide').forEach((slide, idx) => {{
      slide.classList.toggle('active', idx + 1 === currentSlide);
    }});
    
    document.getElementById('slide-nav').textContent = 
      String(currentSlide).padStart(2, '0') + ' / ' + String(totalSlides).padStart(2, '0');
    
    document.getElementById('progress-bar').style.width = 
      (currentSlide / totalSlides * 100) + '%';
    
    // Update speaker notes
    const activeSlide = document.getElementById('slide-' + currentSlide);
    const notes = activeSlide.getAttribute('data-notes') || "Pas de notes spécifiques.";
    document.getElementById('notes-content').textContent = notes;
  }}

  function nextSlide() {{
    if (currentSlide < totalSlides) {{
      currentSlide++;
      updateSlide();
    }}
  }}

  function prevSlide() {{
    if (currentSlide > 1) {{
      currentSlide--;
      updateSlide();
    }}
  }}

  function toggleNotes() {{
    const panel = document.getElementById('notes-panel');
    panel.classList.toggle('visible');
  }}

  function toggleFullscreen() {{
    if (!document.fullscreenElement) {{
      document.documentElement.requestFullscreen().catch(err => {{}});
    }} else {{
      document.exitFullscreen();
    }}
  }}

  document.addEventListener('keydown', (e) => {{
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
      nextSlide();
    }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
      prevSlide();
    }} else if (e.key === 'Home') {{
      currentSlide = 1;
      updateSlide();
    }} else if (e.key === 'End') {{
      currentSlide = totalSlides;
      updateSlide();
    }} else if (e.key.toLowerCase() === 's') {{
      toggleNotes();
    }} else if (e.key.toLowerCase() === 'f') {{
      toggleFullscreen();
    }} else if (e.key.toLowerCase() === 'p') {{
      window.print();
    }}
  }});

  // Initialisation
  updateSlide();
</script>

</body>
</html>
"""

    dest_html_1 = os.path.join(pres_dir, "Diaporama_ShopLoc_Soutenance.html")
    dest_html_2 = os.path.join(pres_dir, "GARIK_GLOP-2026-SOUTENANCE-R1.html")
    
    with open(dest_html_1, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(dest_html_2, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"[OK] Fichiers HTML générés :")
    print(f"  - {dest_html_1}")
    print(f"  - {dest_html_2}")
    
    # Export PDF via Chrome Headless
    chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    dest_pdf_1 = os.path.join(pres_dir, "Diaporama_ShopLoc_Soutenance.pdf")
    dest_pdf_2 = os.path.join(pres_dir, "GARIK_GLOP-2026-SOUTENANCE-R1.pdf")
    
    if os.path.exists(chrome_bin):
        args_chrome = [
            chrome_bin,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={dest_pdf_2}",
            dest_html_1
        ]
        try:
            print("[...] Impression vectorielle PDF 16:9 via Google Chrome...")
            subprocess.run(args_chrome, check=True)
            if os.path.exists(dest_pdf_2):
                import shutil
                shutil.copyfile(dest_pdf_2, dest_pdf_1)
                size_mb = os.path.getsize(dest_pdf_2) / (1024 * 1024)
                print(f"[SUCCÈS] PDF généré : {dest_pdf_2} ({size_mb:.2f} Mo)")
                print(f"[SUCCÈS] Copie synchronisée : {dest_pdf_1}")
        except Exception as e:
            print(f"[ERREUR] Erreur lors de la génération PDF : {e}")

if __name__ == "__main__":
    build_deck()

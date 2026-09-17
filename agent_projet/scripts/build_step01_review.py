#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de la page de revue visuelle de l'Étape 01 — Design Éditorial Épuré (Anti-Slop AI)
Master 2 MIAGE — Université de Lille — UE GLOP (2026-2027)

Règle permanente 8 : Zéro languette (aucune bordure gauche/supérieure asymétrique d'accent).
Conception UI sur-mesure, symétrique, sobre et inspirée des publications d'ingénierie haut de gamme.
"""
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))
agent_projet_dir = os.path.join(project_root, "agent_projet")
comp_dir = os.path.join(agent_projet_dir, "templates", "components")

with open(os.path.join(comp_dir, "bete_a_cornes.html"), "r", encoding="utf-8") as f:
    bete_html = f.read()

with open(os.path.join(comp_dir, "matrice_positionnement.html"), "r", encoding="utf-8") as f:
    matrice_html = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Revue Visuelle Étape 01 — Cadrage Stratégique &amp; Méthode APTE (ShopLoc)</title>
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
      max-width: 1040px;
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
      font-size: 27px;
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
      padding: 6px 14px;
      border-radius: 9999px;
      transition: all 0.18s ease;
    }}
    .toc-link:hover {{
      background: #243342;
      color: #FFFFFF;
      border-color: #243342;
    }}

    /* SECTIONS DE FIGURES */
    .figure-section {{
      margin-bottom: 56px;
    }}

    /* ENCARTS PÉDAGOGIQUES — DESIGN SUR-MESURE MONOCHROMATIQUE SANS BORDURE LATÉRALE */
    .pedagogy-card {{
      background: #FFFFFF;
      border: 1px solid #E8E6DF;
      border-radius: 14px;
      padding: 24px 28px;
      margin-bottom: 20px;
      box-shadow: 0 2px 10px rgba(36, 51, 66, 0.03);
    }}
    .pedagogy-header {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #FAF9F6;
      border: 1px solid #E2DDD5;
      padding: 4px 12px;
      border-radius: 9999px;
      margin-bottom: 12px;
      font-size: 11px;
      font-weight: 700;
      color: #243342;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }}
    .pedagogy-content {{
      font-size: 13.5px;
      color: #334155;
      line-height: 1.65;
    }}
    .pedagogy-content strong {{
      color: #243342;
    }}

    /* CARTE GRAPHIQUE CONTENEUR SVG */
    .figure-card {{
      background: #FFFFFF;
      border: 1px solid #E8E6DF;
      border-radius: 16px;
      padding: 32px 28px;
      margin-bottom: 20px;
      box-shadow: 0 4px 20px -2px rgba(36, 51, 66, 0.05);
    }}
    .figure-card svg {{
      display: block;
      width: 100%;
      height: auto;
    }}

    /* CARTE QUESTIONS DE VALIDATION — SYMÉTRIQUE & PROPRE */
    .questions-card {{
      background: #FFFFFF;
      border: 1px solid #E8E6DF;
      border-radius: 14px;
      padding: 24px 28px;
      box-shadow: 0 2px 10px rgba(36, 51, 66, 0.03);
    }}
    .questions-header {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #FAF9F6;
      border: 1px solid #E2DDD5;
      padding: 4px 12px;
      border-radius: 9999px;
      margin-bottom: 12px;
      font-size: 11px;
      font-weight: 700;
      color: #8E3D2A;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }}
    .questions-card ul {{
      padding-left: 20px;
      font-size: 13px;
      color: #475569;
      line-height: 1.65;
    }}
    .questions-card li {{
      margin-bottom: 6px;
    }}
  </style>
</head>
<body>

  <div class="container">
    
    <!-- EN-TÊTE ÉDITORIAL UNIFIÉ -->
    <header class="header-card">
      <div class="header-top">
        <div class="meta-tag">
          <span>Master 2 MIAGE · Université de Lille · UE GLOP</span>
        </div>
        <div class="meta-tag-pill">
          <span>Livrable R1 · Section 01</span>
        </div>
      </div>
      <h1>Revue des Modèles Stratégiques &amp; Méthodologiques</h1>
      <p class="subtitle">
        Plateforme ShopLoc · Validation Granulaire des Visuels de Cadrage · Norme AFNOR NF X 50-151 &amp; Différenciation Concurrentielle
      </p>
      <nav class="toc-bar">
        <span class="toc-label">Modèles de l'Étape 01 :</span>
        <a class="toc-link" href="#fig1">Figure 1.1 — Bête à Cornes APTE</a>
        <a class="toc-link" href="#fig2">Figure 1.2 — Matrice de Positionnement (2 Axes)</a>
      </nav>
    </header>

    <!-- SECTION FIGURE 1.1 : BÊTE À CORNES -->
    <div id="fig1" class="figure-section">
      <div class="pedagogy-card">
        <div class="pedagogy-header">
          <span>Cadre Méthodologique &amp; Rôle de l'Artefact (Figure 1.1)</span>
        </div>
        <div class="pedagogy-content">
          La Bête à Cornes constitue le pilier initial de la méthode APTE (norme AFNOR NF X 50-151). Elle formalise la raison d'être du système ShopLoc en apportant une réponse canonique et non négociable à trois interrogations fondatrices :
          <br>• <strong>À qui rend-il service ?</strong> Aux citoyens urbains (consommateurs, seniors) et aux artisans commerçants indépendants.
          <br>• <strong>Sur quoi agit-il ?</strong> Sur les flux marchands en boutique physique et sur les comportements de mobilité urbaine décarbonée.
          <br>• <strong>Dans quel but ?</strong> Revitaliser durablement le commerce de centre-ville sans prélèvement de commission prédatrice.
        </div>
      </div>
      
      {bete_html}

      <div class="questions-card">
        <div class="questions-header">
          <span>Critères d'Arbitrage &amp; Validation (Figure 1.1)</span>
        </div>
        <ul>
          <li><strong>Périmètre des bénéficiaires :</strong> Citoyens urbains et commerçants artisans indépendants constituent le cœur de la cible.</li>
          <li><strong>Matière d'œuvre :</strong> L'action porte exclusivement sur les flux physiques en boutique et la mobilité urbaine (aucune livraison à domicile).</li>
          <li><strong>Finalité fondamentale :</strong> Préservation intégrale de la valeur locale sans prélèvement de commission marchande.</li>
        </ul>
      </div>
    </div>

    <!-- SECTION FIGURE 1.2 : MATRICE DE POSITIONNEMENT -->
    <div id="fig2" class="figure-section">
      <div class="pedagogy-card">
        <div class="pedagogy-header">
          <span>Positionnement Stratégique &amp; Différenciation de Marché (Figure 1.2)</span>
        </div>
        <div class="pedagogy-content">
          Cette matrice à deux axes orthogonaux démontre la proposition de valeur de ShopLoc au sein de l'écosystème du commerce territorial :
          <br>• <strong>Axe horizontal (Modèle Économique) :</strong> Oppose le prélèvement lucratif marchand (commissions prédatrices de 15% à 30%) à la souveraineté territoriale et à la gratuité citoyenne intégrale (0% de commission).
          <br>• <strong>Axe vertical (Ancrage Spatial) :</strong> Oppose la délocalisation logistique pure (entrepôts, livraisons motorisées) à l'ancrage physique pédestre en boutique de centre-ville.
          <br>ShopLoc s'isole dans le quadrant d'excellence stratégique (Haut-Droit) comme l'unique solution alliant flux piétonnier obligatoire et gratuité marchande.
        </div>
      </div>
      
      {matrice_html}

      <div class="questions-card">
        <div class="questions-header">
          <span>Critères d'Arbitrage &amp; Validation (Figure 1.2)</span>
        </div>
        <ul>
          <li><strong>Quadrants de marché :</strong> Les 4 typologies d'acteurs (Ollca/Epicery, Amazon/Deliveroo, Proxity, ShopLoc) traduisent fidèlement l'état de l'art du commerce local et numérique.</li>
          <li><strong>Rupture de modèle :</strong> ShopLoc garantit un double engagement non négociable : ancrage physique piétonnier obligatoire et gratuité citoyenne / zéro commission marchande.</li>
        </ul>
      </div>
    </div>

  </div>

</body>
</html>
"""

out_path = os.path.join(agent_projet_dir, "docs", "01_Cadrage_Et_Cahier_Des_Charges_R1", "figures", "revue_visuels_etape_01.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Page generee avec succes : {out_path} ({len(html_content)} octets)")

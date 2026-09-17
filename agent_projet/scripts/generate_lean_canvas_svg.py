#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GÉNÉRATEUR DU LEAN CANVAS SHOPLOC (FIGURE 1.4)
Master 2 MIAGE — Université de Lille — UE GLOP (2026-2027)

Génère le schéma vectoriel SVG autonome et l'export PNG HD (2360 x 1400)
pour la synthèse panoramique du modèle économique et opérationnel (Ash Maurya).
Conformité stricte à la charte graphique pastel ShopLoc (ADR-014, ADR-015),
sans emoji, sans languette asymétrique.
"""

import os
import sys

COMMON_DEFS = """
  <defs>
    <filter id="shadow-card" x="-4%" y="-3%" width="108%" height="108%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#243342" flood-opacity="0.05"/>
    </filter>
    <filter id="shadow-box" x="-3%" y="-3%" width="106%" height="108%">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2" flood-color="#243342" flood-opacity="0.04"/>
    </filter>
  </defs>
"""

def generate_lean_canvas_svg():
    return f"""<svg viewBox="0 0 1180 700" width="1180" height="700" style="overflow:visible; font-family:'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
{COMMON_DEFS}

  <!-- CADRE GLOBAL EXTERIEUR -->
  <rect x="10" y="10" width="1160" height="680" rx="14" fill="#FAFAFA" stroke="#E2E8F0" stroke-width="1.2" />

  <!-- EN-TETE BANDEAU OFFICIEL -->
  <rect x="25" y="22" width="1130" height="42" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
  <rect x="35" y="32" width="22" height="22" rx="4" fill="#C26750" />
  <text x="46" y="47" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">LC</text>
  <text x="68" y="46" font-size="13" font-weight="700" fill="#243342">Figure 1.4 — Lean Canvas Synthétique ShopLoc (9 Blocs Stratégiques &amp; Modèle Économique)</text>
  <text x="1140" y="46" text-anchor="end" font-size="11" font-weight="500" fill="#5A6578">Méthodologie Ash Maurya · Synthèse Consolidée des Étapes 01 à 09 (Cadrage R1)</text>

  <!-- ======================================================================== -->
  <!-- RANGEE SUPERIEURE : 5 COLONNES (HAUTEUR = 410px, de y=75 a y=485)       -->
  <!-- ======================================================================== -->

  <!-- COLONNE 1 : 1. PROBLEME (x=25, w=218) -->
  <g filter="url(#shadow-box)">
    <rect x="25" y="75" width="218" height="410" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
    
    <!-- En-tete Bloc -->
    <rect x="25" y="75" width="218" height="32" rx="10" fill="#F8FAFC" />
    <circle cx="39" cy="91" r="4" fill="#8E3D2A" />
    <text x="50" y="95" font-size="10.5" font-weight="700" fill="#8E3D2A" letter-spacing="0.05em">1. PROBLÈME</text>

    <!-- Contenu Problemes Clés -->
    <text x="37" y="125" font-size="10" font-weight="700" fill="#243342">Désertification commerciale :</text>
    <text x="37" y="140" font-size="9.5" fill="#475569">Perte de flux piétonnier face</text>
    <text x="37" y="153" font-size="9.5" fill="#475569">aux grandes surfaces périphériques.</text>

    <text x="37" y="177" font-size="10" font-weight="700" fill="#243342">Commissions prédatrices :</text>
    <text x="37" y="192" font-size="9.5" fill="#475569">15% à 30% prélevés par les</text>
    <text x="37" y="205" font-size="9.5" fill="#475569">plateformes privées de livraison.</text>

    <text x="37" y="229" font-size="10" font-weight="700" fill="#243342">Fracture numérique seniors :</text>
    <text x="37" y="244" font-size="9.5" fill="#475569">Pierre (74 ans) exclu des apps</text>
    <text x="37" y="257" font-size="9.5" fill="#475569">mobiles et du tout-en-ligne.</text>

    <text x="37" y="281" font-size="10" font-weight="700" fill="#243342">Évasion de la valeur :</text>
    <text x="37" y="296" font-size="9.5" fill="#475569">Aucun retour vers l'intérêt public</text>
    <text x="37" y="309" font-size="9.5" fill="#475569">ni la mobilité décarbonée.</text>

    <!-- Separation Alternatives -->
    <line x1="37" y1="330" x2="231" y2="330" stroke="#E2E8F0" stroke-dasharray="3,3" />
    <rect x="37" y="342" width="194" height="130" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1" />
    <text x="47" y="359" font-size="9" font-weight="700" fill="#64748B" letter-spacing="0.04em">ALTERNATIVES EXISTANTES</text>
    <text x="47" y="377" font-size="9" fill="#475569">• Géants web (Amazon, Deliveroo) :</text>
    <text x="55" y="390" font-size="8.5" fill="#64748B">modèle centralisé, trafic routier.</text>
    <text x="47" y="407" font-size="9" fill="#475569">• Marketplaces (Ollca, Epicery) :</text>
    <text x="55" y="420" font-size="8.5" fill="#64748B">commissions élevées (8-15%).</text>
    <text x="47" y="437" font-size="9" fill="#475569">• Cartes papier tampons :</text>
    <text x="55" y="450" font-size="8.5" fill="#64748B">isolées, aucune mutualisation.</text>
  </g>

  <!-- COLONNE 2 : 4. SOLUTION (HAUT) & 8. METRIQUES CLES (BAS) (x=253, w=218) -->
  <!-- 4. SOLUTION -->
  <g filter="url(#shadow-box)">
    <rect x="253" y="75" width="218" height="200" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
    <rect x="253" y="75" width="218" height="32" rx="10" fill="#F8FAFC" />
    <circle cx="267" cy="91" r="4" fill="#0284C7" />
    <text x="278" y="95" font-size="10.5" font-weight="700" fill="#0284C7" letter-spacing="0.05em">4. SOLUTION</text>

    <text x="265" y="123" font-size="10" font-weight="700" fill="#243342">Click &amp; Collect mutualisé :</text>
    <text x="265" y="137" font-size="9.5" fill="#475569">Panier multi-commerces (2PC),</text>
    <text x="265" y="150" font-size="9.5" fill="#475569">retrait piéton ordonnancé &lt; 2h.</text>

    <text x="265" y="172" font-size="10" font-weight="700" fill="#243342">Fidélité double découplée :</text>
    <text x="265" y="186" font-size="9.5" fill="#475569">Cagnotte boutique dédiée (12m)</text>
    <text x="265" y="199" font-size="9.5" fill="#475569">+ statut VFP (10p / 15j) mobilité.</text>

    <text x="265" y="221" font-size="10" font-weight="700" fill="#243342">Pass Citoyen universel :</text>
    <text x="265" y="235" font-size="9.5" fill="#475569">Carte physique QR code / NFC,</text>
    <text x="265" y="248" font-size="9.5" fill="#475569">caisse tactile commerçant &lt; 3s.</text>
  </g>

  <!-- 8. METRIQUES CLES -->
  <g filter="url(#shadow-box)">
    <rect x="253" y="285" width="218" height="200" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
    <rect x="253" y="285" width="218" height="32" rx="10" fill="#F8FAFC" />
    <circle cx="267" cy="301" r="4" fill="#1E293B" />
    <text x="278" y="305" font-size="10.5" font-weight="700" fill="#1E293B" letter-spacing="0.05em">8. MÉTRIQUES CLÉS</text>

    <text x="265" y="333" font-size="9.5" font-weight="700" fill="#243342">• Adhésion commerçante :</text>
    <text x="273" y="347" font-size="9.5" fill="#475569">Taux actif cible &gt; 75% du centre.</text>

    <text x="265" y="369" font-size="9.5" font-weight="700" fill="#243342">• Taux d'usagers VFP :</text>
    <text x="273" y="383" font-size="9.5" fill="#475569">&ge; 10 passages sur 15 jours.</text>

    <text x="265" y="405" font-size="9.5" font-weight="700" fill="#243342">• Qualité de service C&amp;C :</text>
    <text x="273" y="419" font-size="9.5" fill="#475569">Mise à disposition &lt; 2h, no-show &lt; 2%.</text>

    <text x="265" y="441" font-size="9.5" font-weight="700" fill="#243342">• Accessibilité &amp; RGPD :</text>
    <text x="273" y="455" font-size="9.5" fill="#475569">100% RGAA AA, 0 fuite nominative.</text>
  </g>

  <!-- COLONNE 3 : 3. PROPOSITION DE VALEUR UNIQUE (CENTRE — TERRACOTTA) (x=481, w=218) -->
  <g filter="url(#shadow-card)">
    <rect x="481" y="75" width="218" height="410" rx="10" fill="#FBEEEA" stroke="#D88B77" stroke-width="1.5" />
    
    <!-- En-tete Bloc -->
    <rect x="481" y="75" width="218" height="32" rx="10" fill="#F6DFD8" />
    <circle cx="495" cy="91" r="4" fill="#C26750" />
    <text x="506" y="95" font-size="10.5" font-weight="700" fill="#C26750" letter-spacing="0.05em">3. VALEUR UNIQUE (UVP)</text>

    <!-- Citation Principale -->
    <rect x="491" y="116" width="198" height="74" rx="8" fill="#FFFFFF" stroke="#E8C5BC" stroke-width="1" />
    <text x="501" y="133" font-size="10" font-weight="700" fill="#243342">"La vitalité de vos</text>
    <text x="501" y="147" font-size="10" font-weight="700" fill="#243342">commerces de quartier</text>
    <text x="501" y="161" font-size="10" font-weight="700" fill="#243342">dans un panier unique,</text>
    <text x="501" y="175" font-size="10" font-weight="700" fill="#C26750">soutenu par votre ville."</text>

    <!-- Valeur Tripartite Détaillée -->
    <text x="493" y="210" font-size="9.5" font-weight="700" fill="#8E3D2A">Pour les Citoyens :</text>
    <text x="493" y="224" font-size="9" fill="#475569">Courses locales unifiées et gratuité</text>
    <text x="493" y="237" font-size="9" fill="#475569">mobilité (bus / 20 min parking).</text>

    <text x="493" y="259" font-size="9.5" font-weight="700" fill="#8E3D2A">Pour les Commerçants :</text>
    <text x="493" y="273" font-size="9" fill="#475569">0% de commission marchande et</text>
    <text x="493" y="286" font-size="9" fill="#475569">sanctuarisation du flux comptoir.</text>

    <text x="493" y="308" font-size="9.5" font-weight="700" fill="#8E3D2A">Pour la Ville :</text>
    <text x="493" y="322" font-size="9" fill="#475569">Revitalisation piétonne, report</text>
    <text x="493" y="335" font-size="9" fill="#475569">modal décarboné et observatoire RGPD.</text>

    <!-- Concept de Haut Niveau -->
    <rect x="491" y="358" width="198" height="114" rx="6" fill="#FFFFFF" stroke="#D88B77" stroke-width="1" />
    <text x="501" y="375" font-size="9" font-weight="700" fill="#C26750" letter-spacing="0.04em">CONCEPT DE HAUT NIVEAU</text>
    <text x="501" y="394" font-size="10" font-weight="700" fill="#243342">L'infrastructure souveraine</text>
    <text x="501" y="408" font-size="9.5" fill="#475569">de commerce territorial</text>
    <text x="501" y="422" font-size="9.5" fill="#475569">piétonnier, financée par</text>
    <text x="501" y="436" font-size="9.5" fill="#475569">subvention municipale et</text>
    <text x="501" y="450" font-size="9.5" font-weight="600" fill="#2E583D">100% gratuite au citoyen.</text>
  </g>

  <!-- COLONNE 4 : 9. AVANTAGE DETERMINANT (HAUT) & 5. CANAUX (BAS) (x=709, w=218) -->
  <!-- 9. AVANTAGE DETERMINANT -->
  <g filter="url(#shadow-box)">
    <rect x="709" y="75" width="218" height="200" rx="10" fill="#FEF7EB" stroke="#DCB162" stroke-width="1.2" />
    <rect x="709" y="75" width="218" height="32" rx="10" fill="#FDF0D5" />
    <circle cx="723" cy="91" r="4" fill="#845A11" />
    <text x="734" y="95" font-size="10.5" font-weight="700" fill="#845A11" letter-spacing="0.05em">9. AVANTAGE DÉTERMINANT</text>

    <text x="721" y="123" font-size="10" font-weight="700" fill="#243342">Convention publique tripartite :</text>
    <text x="721" y="137" font-size="9.5" fill="#475569">Légitimité municipale exclusive</text>
    <text x="721" y="150" font-size="9.5" fill="#475569">(Mairie + Ass. Commerçants).</text>

    <text x="721" y="172" font-size="10" font-weight="700" fill="#243342">Couplage direct voirie/bus :</text>
    <text x="721" y="186" font-size="9.5" fill="#475569">Interconnexion directe aux mocks</text>
    <text x="721" y="199" font-size="9.5" fill="#475569">transports sans intermédiaire bancaire.</text>

    <text x="721" y="221" font-size="10" font-weight="700" fill="#243342">Inclusion physique seniors :</text>
    <text x="721" y="235" font-size="9.5" fill="#475569">Pass carton QR distribué en mairie,</text>
    <text x="721" y="248" font-size="9.5" fill="#475569">zéro exclusion par l'écran.</text>
  </g>

  <!-- 5. CANAUX -->
  <g filter="url(#shadow-box)">
    <rect x="709" y="285" width="218" height="200" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
    <rect x="709" y="285" width="218" height="32" rx="10" fill="#F8FAFC" />
    <circle cx="723" cy="301" r="4" fill="#5A6578" />
    <text x="734" y="305" font-size="10.5" font-weight="700" fill="#5A6578" letter-spacing="0.05em">5. CANAUX</text>

    <text x="721" y="333" font-size="9.5" font-weight="700" fill="#243342">• Application Web PWA :</text>
    <text x="729" y="347" font-size="9.5" fill="#475569">Responsive, légère, sans store.</text>

    <text x="721" y="369" font-size="9.5" font-weight="700" fill="#243342">• Guichet Mairie &amp; CCAS :</text>
    <text x="729" y="383" font-size="9.5" fill="#475569">Remise physique du pass citoyen.</text>

    <text x="721" y="405" font-size="9.5" font-weight="700" fill="#243342">• Points de vente physiques :</text>
    <text x="729" y="419" font-size="9.5" fill="#475569">Vitrophanies et chevalets caisse.</text>

    <text x="721" y="441" font-size="9.5" font-weight="700" fill="#243342">• Médias municipaux :</text>
    <text x="729" y="455" font-size="9.5" fill="#475569">Bulletin communal, affichage urbain.</text>
  </g>

  <!-- COLONNE 5 : 2. SEGMENTS DE CLIENTELE (x=937, w=218) -->
  <g filter="url(#shadow-box)">
    <rect x="937" y="75" width="218" height="410" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
    
    <!-- En-tete Bloc -->
    <rect x="937" y="75" width="218" height="32" rx="10" fill="#F8FAFC" />
    <circle cx="951" cy="91" r="4" fill="#1C2D3D" />
    <text x="962" y="95" font-size="10.5" font-weight="700" fill="#1C2D3D" letter-spacing="0.05em">2. CLIENTS (PERSONAS)</text>

    <!-- 4 Personas Cibles -->
    <text x="949" y="125" font-size="10" font-weight="700" fill="#243342">Citoyens actifs pressés :</text>
    <text x="949" y="139" font-size="9.5" fill="#475569">Julie &amp; Arthur · Gain de temps,</text>
    <text x="949" y="152" font-size="9.5" fill="#475569">panier multi-boutiques pédestre.</text>

    <text x="949" y="176" font-size="10" font-weight="700" fill="#243342">Seniors &amp; non-connectés :</text>
    <text x="949" y="190" font-size="9.5" fill="#475569">Pierre (74 ans) · Lien social,</text>
    <text x="949" y="203" font-size="9.5" fill="#475569">pass QR physique, caisse directe.</text>

    <text x="949" y="227" font-size="10" font-weight="700" fill="#243342">Commerçants indépendants :</text>
    <text x="949" y="241" font-size="9.5" fill="#475569">Suzanne (22 ans) · 0% commission,</text>
    <text x="949" y="254" font-size="9.5" fill="#475569">caisse tactile instantanée (&lt; 3s).</text>

    <text x="949" y="278" font-size="10" font-weight="700" fill="#243342">Mairie &amp; Collectivité :</text>
    <text x="949" y="292" font-size="9.5" fill="#475569">Marius (48 ans) · Vitalité urbaine,</text>
    <text x="949" y="305" font-size="9.5" fill="#475569">mobilités douces, souveraineté.</text>

    <!-- Separation Early Adopters -->
    <line x1="949" y1="330" x2="1143" y2="330" stroke="#E2E8F0" stroke-dasharray="3,3" />
    <rect x="949" y="342" width="194" height="130" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1" />
    <text x="959" y="359" font-size="9" font-weight="700" fill="#64748B" letter-spacing="0.04em">EARLY ADOPTERS</text>
    <text x="959" y="377" font-size="9" font-weight="600" fill="#243342">• Quartier pilote Wazemmes :</text>
    <text x="967" y="390" font-size="8.5" fill="#64748B">25 artisans de bouche &amp; commerces.</text>
    <text x="959" y="407" font-size="9" font-weight="600" fill="#243342">• Usagers réseau de bus :</text>
    <text x="967" y="420" font-size="8.5" fill="#64748B">Piétons du centre et abonnés mobilités.</text>
    <text x="959" y="437" font-size="9" font-weight="600" fill="#243342">• Association locale :</text>
    <text x="967" y="450" font-size="8.5" fill="#64748B">Fédération commerçante Saint-Sauveur.</text>
  </g>

  <!-- ======================================================================== -->
  <!-- RANGEE INFERIEURE : 2 GRANDES COLONNES (HAUTEUR = 185px, de y=495 a 680)-->
  <!-- ======================================================================== -->

  <!-- COLONNE GAUCHE : 7. STRUCTURE DES COUTS (x=25, w=555) -->
  <g filter="url(#shadow-box)">
    <rect x="25" y="495" width="555" height="185" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
    <rect x="25" y="495" width="555" height="30" rx="10" fill="#F8FAFC" />
    <circle cx="39" cy="510" r="4" fill="#6E3946" />
    <text x="50" y="514" font-size="10.5" font-weight="700" fill="#6E3946" letter-spacing="0.05em">7. STRUCTURE DES COÛTS (MÉTHODE DES COÛTS COMPLETS — Y1 : 76 620 €)</text>

    <!-- Deux sous-colonnes internes -->
    <!-- Sous-colonne 1 : Répartition des charges -->
    <text x="37" y="542" font-size="9.5" font-weight="700" fill="#243342">Charges Directes (16 620 €) :</text>
    <text x="37" y="556" font-size="9" fill="#475569">• Déploiement sur site, signalétique physique &amp; kits QR caisse.</text>
    <text x="37" y="569" font-size="9" fill="#475569">• Formation commerçante personnalisée et accompagnement.</text>

    <text x="37" y="591" font-size="9.5" font-weight="700" fill="#243342">Charges Indirectes (60 000 € via 5 Centres d'Analyse) :</text>
    <text x="37" y="605" font-size="9" fill="#475569">• Auxiliaires : Administration (12k€) + Support/FinOps (6k€).</text>
    <text x="37" y="618" font-size="9" fill="#475569">• Principaux : Vente (9,2k€), Réalisation (16,7k€), Run (10,3k€).</text>

    <!-- Sous-colonne 2 : Unités d'Oeuvre & Seuil de rentabilité -->
    <line x1="330" y1="535" x2="330" y2="670" stroke="#E2E8F0" />

    <text x="342" y="542" font-size="9.5" font-weight="700" fill="#243342">Unités d'Œuvre (UO) &amp; Rentabilité :</text>
    <text x="342" y="556" font-size="9" fill="#475569">• UO Vente : 10,23 € / 100 € CA prospection.</text>
    <text x="342" y="569" font-size="9" fill="#475569">• UO Réalisation : 2,78 € / heure dev.</text>
    <text x="342" y="582" font-size="9" fill="#475569">• UO Maintenance : 1 716,67 € / ville / an.</text>

    <rect x="342" y="596" width="226" height="72" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1" />
    <text x="352" y="611" font-size="8.5" font-weight="700" fill="#64748B">SEUIL DE RENTABILITÉ COMMUNAL</text>
    <text x="352" y="626" font-size="9" fill="#243342">Charges Fixes : <tspan font-weight="700">68 000 €</tspan> · Taux MCV : <tspan font-weight="700">90,23%</tspan></text>
    <text x="352" y="640" font-size="9" fill="#0284C7">Point Mort : <tspan font-weight="700">75 365,24 €</tspan> (Jour 312)</text>
    <text x="352" y="654" font-size="8.5" fill="#2E583D">Marge de sécurité : <tspan font-weight="700">12 635 €</tspan> (14,36%)</text>
  </g>

  <!-- COLONNE DROITE : 6. FLUX DE REVENUS & FINANCEMENT (x=600, w=555) -->
  <g filter="url(#shadow-box)">
    <rect x="600" y="495" width="555" height="185" rx="10" fill="#EBF3ED" stroke="#7EA88D" stroke-width="1.2" />
    <rect x="600" y="495" width="555" height="30" rx="10" fill="#DFECE2" />
    <circle cx="614" cy="510" r="4" fill="#2E583D" />
    <text x="625" y="514" font-size="10.5" font-weight="700" fill="#2E583D" letter-spacing="0.05em">6. FLUX DE REVENUS &amp; FINANCEMENT (CONVENTION TRIPARTITE ADR-004)</text>

    <!-- Sous-colonne 1 : Sources contractuelles de revenus -->
    <text x="612" y="542" font-size="9.5" font-weight="700" fill="#243342">Convention Municipale Annuelle :</text>
    <text x="612" y="556" font-size="9" fill="#334155">• Petite Ville (&lt; 20k hab.) : 10 500 € Y1 (Setup 4,5k€ + Run 6k€).</text>
    <text x="612" y="569" font-size="9" fill="#334155">• Ville Moyenne (20k-100k) : 23 000 € Y1 (Setup 9k€ + Run 14k€).</text>
    <text x="612" y="582" font-size="9" fill="#334155">• Grande Ville (&gt; 100k) : 46 000 € Y1 (Setup 18k€ + Run 28k€).</text>

    <text x="612" y="604" font-size="9.5" font-weight="700" fill="#243342">Modèle Solidaire Sans Commission :</text>
    <text x="612" y="618" font-size="9" fill="#334155">• Cotisation commerçante symbolique : 50 € / an / commerce.</text>
    <text x="612" y="631" font-size="9" font-weight="700" fill="#2E583D">• 0% de prélèvement sur les ventes marchandes.</text>
    <text x="612" y="644" font-size="9" fill="#334155">• Compensation mobilité : prise en charge Mairie / Régie.</text>

    <!-- Sous-colonne 2 : Trajectoire P&L 3 ans -->
    <line x1="880" y1="535" x2="880" y2="670" stroke="#CBDDD1" />

    <text x="892" y="542" font-size="9.5" font-weight="700" fill="#243342">Trajectoire P&amp;L 3 Ans &amp; Ratios :</text>
    <text x="892" y="556" font-size="9" fill="#334155">• Y1 (6 villes) : CA 88k€ → R. Net <tspan font-weight="700">+3 277 €</tspan></text>
    <text x="892" y="569" font-size="9" fill="#334155">• Y2 (18 villes) : CA 236k€ → R. Net <tspan font-weight="700">+63 460 €</tspan></text>
    <text x="892" y="582" font-size="9" fill="#334155">• Y3 (33 villes) : CA 491k€ → R. Net <tspan font-weight="700">+159 410 €</tspan></text>

    <rect x="892" y="596" width="251" height="72" rx="6" fill="#FFFFFF" stroke="#7EA88D" stroke-width="1" />
    <text x="902" y="611" font-size="8.5" font-weight="700" fill="#2E583D">INDICATEURS DE RENTABILITÉ</text>
    <text x="902" y="626" font-size="9" fill="#243342">VAN (k=8%) : <tspan font-weight="700">170 482,30 €</tspan></text>
    <text x="902" y="640" font-size="9" fill="#0284C7">TRI : <tspan font-weight="700">101,50%</tspan> · Payback : <tspan font-weight="700">17,3 mois</tspan></text>
    <text x="902" y="654" font-size="8.5" fill="#475569">Plein emploi : <tspan font-weight="700">5 CDI confirmés en Y3</tspan></text>
  </g>

</svg>
"""

def export_png(svg_content, width, height, output_png):
    """Exporte le contenu SVG en image PNG haute résolution (2.0x) via PyMuPDF."""
    print(f"Exportation vectorielle HD vers : {output_png}...")
    try:
        import pymupdf
        doc = pymupdf.open(stream=svg_content.encode("utf-8"), filetype="svg")
        page = doc[0]
        mat = pymupdf.Matrix(2.0, 2.0)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        pix.save(output_png)
        print(f"Exporté avec succès (PyMuPDF HD) : {output_png} ({pix.width}x{pix.height})")
    except Exception as e:
        print(f"Erreur PyMuPDF : {e}")
        raise

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    figures_dir = os.path.join(repo_root, "agent_projet/docs/01_Cadrage_Et_Cahier_Des_Charges_R1/figures")
    components_dir = os.path.join(repo_root, "agent_projet/templates/components")
    previews_dir = os.path.join(repo_root, "agent_projet/docs/previews_composants")
    os.makedirs(figures_dir, exist_ok=True)
    os.makedirs(components_dir, exist_ok=True)
    os.makedirs(previews_dir, exist_ok=True)

    # 1. Génération SVG
    svg_canvas = generate_lean_canvas_svg()
    svg_path = os.path.join(figures_dir, "fig_1_4_lean_canvas_ash_maurya.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_canvas)
    print(f"SVG généré : {svg_path}")

    # 2. Export PNG HD (2360 x 1400)
    png_path = os.path.join(figures_dir, "fig_1_4_lean_canvas_ash_maurya.png")
    export_png(svg_canvas, 1180, 700, png_path)

    # 3. Sauvegarde composant HTML
    comp_html_path = os.path.join(components_dir, "lean_canvas.html")
    comp_content = f"""<!-- FIGURE 1.4 : LEAN CANVAS 9 BLOCS ASH MAURYA (CONSOLIDATION ÉTAPES 01 À 09) -->
<div class="figure-card" style="background:#FFFFFF; border:1px solid #E8E6DF; border-radius:16px; padding:24px; margin-bottom:28px; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px; border-bottom:1px solid #E8E6DF; padding-bottom:12px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#C26750;"></span>
        <span style="font-size:11px; font-weight:700; color:#C26750; text-transform:uppercase; letter-spacing:0.08em;">Synthèse Stratégique &amp; Modèle Économique</span>
      </div>
      <h3 style="font-size:17px; font-weight:700; color:#243342; margin:0;">Figure 1.4 — Lean Canvas Synthétique ShopLoc (9 Blocs d'Ash Maurya)</h3>
    </div>
    <span style="font-size:11px; background:#FAF9F6; border:1px solid #E8E6DF; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600;">Méthodologie Ash Maurya · Consolidation Globale R1</span>
  </div>
{svg_canvas}
</div>
"""
    with open(comp_html_path, "w", encoding="utf-8") as f:
        f.write(comp_content)
    print(f"Composant HTML écrit : {comp_html_path}")

    # 4. Génération de la page de prévisualisation autonome
    preview_html_path = os.path.join(previews_dir, "preview_lean_canvas.html")
    preview_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Prévisualisation — Lean Canvas ShopLoc (Figure 1.4)</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/latin-modern-web@1.0.0/style.css">
  <style>
    body {{
      font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: #F1F5F9;
      margin: 0;
      padding: 30px 20px;
    }}
    .preview-container {{
      max-width: 1220px;
      margin: 0 auto;
    }}
  </style>
</head>
<body>
  <div class="preview-container">
    {comp_content}
  </div>
</body>
</html>
"""
    with open(preview_html_path, "w", encoding="utf-8") as f:
        f.write(preview_content)
    print(f"Page de prévisualisation autonome générée : {preview_html_path}")
    print("Génération du Lean Canvas terminée avec succès !")

if __name__ == "__main__":
    main()

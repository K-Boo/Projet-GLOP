#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GÉNÉRATEUR DU SCHÉMA D'ARCHITECTURE LOGICIELLE SHOPLOC (FIGURE 4.1)
Master 2 MIAGE — Université de Lille — UE GLOP (2026-2027)

Génère le schéma d'architecture prévisionnel en conformité avec :
- Les tokens officiels de la charte ShopLoc (Lin doux #FAF9F6, Ardoise #243342, Terracotta #C26750, Sauge #4A7A5B, Miel #C48B28).
- Le format A4 Paysage haute résolution (vectoriel SVG + export PNG 300 DPI).
- Les 3 seuls profils usagers (Citoyens, Commerçants, Mairie/DSI).
- L'absence de Nginx et d'endpoints prématurés (structure globale épurée).
"""

import os
import pymupdf

def generate_tech_diagram_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 820" width="1440" height="820" style="font-family: 'Plus Jakarta Sans', 'Poppins', system-ui, -apple-system, sans-serif;">
  <defs>
    <filter id="shadow-soft" x="-2%" y="-2%" width="104%" height="106%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#243342" flood-opacity="0.06"/>
    </filter>
    <filter id="shadow-card" x="-4%" y="-6%" width="108%" height="116%">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2" flood-color="#243342" flood-opacity="0.05"/>
    </filter>
  </defs>

  <!-- FOND GLOBAL DE LA PAGE (LIN DOUX) -->
  <rect x="5" y="5" width="1430" height="810" rx="14" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1.2" filter="url(#shadow-soft)"/>

  <!-- ======================================================== -->
  <!-- EN-TÊTE OFFICIEL DU LIVRABLE                             -->
  <!-- ======================================================== -->
  <rect x="25" y="20" width="1390" height="52" rx="8" fill="#243342" />
  <rect x="38" y="32" width="28" height="28" rx="6" fill="#C26750" />
  <text x="52" y="51" text-anchor="middle" font-size="13" font-weight="800" fill="#FFFFFF">SL</text>
  <text x="78" y="44" font-size="14" font-weight="700" fill="#FFFFFF">Architecture Applicative Prévisionnelle &amp; Choix d'Outils Logiciels — ShopLoc</text>
  <text x="78" y="59" font-size="10" font-weight="400" fill="#EBF0F5">Proposition préliminaire de cadrage (Jalon R1) · Structure modulaire conteneurisée</text>
  <text x="1400" y="51" text-anchor="end" font-size="11" font-weight="600" fill="#DCD6CD">Master 2 MIAGE · Garik</text>

  <!-- ======================================================== -->
  <!-- TIER 1 : CLIENTS WEB & MOBILES (REACT + TYPESCRIPT)      -->
  <!-- ======================================================== -->
  <rect x="25" y="85" width="1390" height="175" rx="10" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1.2" filter="url(#shadow-card)"/>
  
  <!-- En-tête Tier 1 -->
  <rect x="25" y="85" width="1390" height="32" rx="10" fill="#EBF0F5" />
  <text x="45" y="106" font-size="11.5" font-weight="700" fill="#243342">TIER 1 — CLIENTS &amp; INTERFACES UTILISATEURS (Navigateurs Web &amp; Mobiles PWA · React 18 &amp; TypeScript)</text>
  <text x="1395" y="106" text-anchor="end" font-size="10" font-weight="600" fill="#5A6578">Application Web Réactive (PWA) · Aucun téléchargement requis</text>

  <!-- Carte 1.1 : Espace Citoyen -->
  <g transform="translate(45, 126)">
    <rect x="0" y="0" width="425" height="120" rx="8" fill="#FBEEEA" stroke="#D88B77" stroke-width="1" />
    <rect x="12" y="10" width="115" height="20" rx="4" fill="#C26750" />
    <text x="69" y="24" text-anchor="middle" font-size="9" font-weight="700" fill="#FFFFFF">ESPACE CITOYEN</text>
    <text x="140" y="24" font-size="9.5" font-weight="700" fill="#8E3D2A">Julie · Arthur · Pierre</text>
    <text x="12" y="48" font-size="9" font-weight="600" fill="#1E252D">Consultation &amp; Achats locaux :</text>
    <text x="12" y="64" font-size="8.5" font-weight="400" fill="#5A6578">• Recherche de boutiques et horaires du quartier</text>
    <text x="12" y="78" font-size="8.5" font-weight="400" fill="#5A6578">• Panier Click &amp; Collect groupé et calcul du trajet piéton</text>
    <text x="12" y="92" font-size="8.5" font-weight="400" fill="#5A6578">• Carte de fidélité numérique, statut VFP et avantages mobilité</text>
    <rect x="12" y="102" width="401" height="1" fill="#D88B77" opacity="0.4" />
  </g>

  <!-- Carte 1.2 : Espace Commerçant -->
  <g transform="translate(508, 126)">
    <rect x="0" y="0" width="425" height="120" rx="8" fill="#EBF3ED" stroke="#7EA88D" stroke-width="1" />
    <rect x="12" y="10" width="135" height="20" rx="4" fill="#4A7A5B" />
    <text x="79" y="24" text-anchor="middle" font-size="9" font-weight="700" fill="#FFFFFF">ESPACE COMMERÇANT</text>
    <text x="160" y="24" font-size="9.5" font-weight="700" fill="#2E583D">Suzanne (Boulangerie)</text>
    <text x="12" y="48" font-size="9" font-weight="600" fill="#1E252D">Gestion d'établissement &amp; Ventes :</text>
    <text x="12" y="64" font-size="8.5" font-weight="400" fill="#5A6578">• Gestion de la fiche boutique, créneaux et catalogue</text>
    <text x="12" y="78" font-size="8.5" font-weight="400" fill="#5A6578">• Synchronisation des stocks et validation des retraits</text>
    <text x="12" y="92" font-size="8.5" font-weight="400" fill="#5A6578">• Scan QR code en caisse et attribution des points boutique</text>
    <rect x="12" y="102" width="401" height="1" fill="#7EA88D" opacity="0.4" />
  </g>

  <!-- Carte 1.3 : Espace Mairie / DSI -->
  <g transform="translate(970, 126)">
    <rect x="0" y="0" width="425" height="120" rx="8" fill="#FEF7EB" stroke="#DCB162" stroke-width="1" />
    <rect x="12" y="10" width="135" height="20" rx="4" fill="#C48B28" />
    <text x="79" y="24" text-anchor="middle" font-size="9" font-weight="700" fill="#FFFFFF">PORTAIL DSI MAIRIE</text>
    <text x="160" y="24" font-size="9.5" font-weight="700" fill="#845A11">Marius (Gestionnaire Ville)</text>
    <text x="12" y="48" font-size="9" font-weight="600" fill="#1E252D">Supervision &amp; Animation locale :</text>
    <text x="12" y="64" font-size="8.5" font-weight="400" fill="#5A6578">• Suivi de l'activité économique et fréquentation centre-ville</text>
    <text x="12" y="78" font-size="8.5" font-weight="400" fill="#5A6578">• Comparatif volume des ventes vs coût avantages mobilité</text>
    <text x="12" y="92" font-size="8.5" font-weight="400" fill="#5A6578">• Diffusion d'actualités municipales et sondages QCM usagers</text>
    <rect x="12" y="102" width="401" height="1" fill="#DCB162" opacity="0.4" />
  </g>

  <!-- ======================================================== -->
  <!-- LIAISON FLUX TIER 1 -> TIER 2                            -->
  <!-- ======================================================== -->
  <line x1="720" y1="260" x2="720" y2="288" stroke="#243342" stroke-width="2" stroke-dasharray="4 3"/>
  <polygon points="720,293 715,283 725,283" fill="#243342"/>
  <rect x="610" y="266" width="220" height="18" rx="4" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
  <text x="720" y="279" text-anchor="middle" font-size="9" font-weight="600" fill="#243342">Requêtes HTTP / JSON (API REST)</text>

  <!-- ======================================================== -->
  <!-- TIER 2 : SERVEUR BACKEND APPLICATIF (JAVA SPRING BOOT 3) -->
  <!-- ======================================================== -->
  <rect x="25" y="295" width="910" height="240" rx="10" fill="#FFFFFF" stroke="#8B9EAF" stroke-width="1.4" filter="url(#shadow-card)"/>
  
  <!-- En-tête Tier 2 -->
  <rect x="25" y="295" width="910" height="34" rx="10" fill="#243342" />
  <rect x="38" y="303" width="18" height="18" rx="4" fill="#4A7A5B" />
  <text x="47" y="316" text-anchor="middle" font-size="10" font-weight="800" fill="#FFFFFF">B</text>
  <text x="65" y="317" font-size="11.5" font-weight="700" fill="#FFFFFF">TIER 2 — NOYAU APPLICATIF MÉTIER (Java 17 / Spring Boot 3 &amp; Maven)</text>
  <text x="915" y="317" text-anchor="end" font-size="10" font-weight="500" fill="#DCD6CD">Architecture en couches · Services Métier &amp; Contrôleurs REST</text>

  <!-- Module 2.1 : Comptes & Sécurité -->
  <g transform="translate(45, 342)">
    <rect x="0" y="0" width="415" height="82" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="12" y="18" font-size="10" font-weight="700" fill="#243342">1. Module Gestion des Comptes &amp; Sécurité</text>
    <text x="12" y="34" font-size="8.5" font-weight="400" fill="#5A6578">• Inscription et authentification des profils (citoyen, commerçant, DSI)</text>
    <text x="12" y="48" font-size="8.5" font-weight="400" fill="#5A6578">• Attribution d'un identifiant universel et gestion de la plaque auto</text>
    <text x="12" y="62" font-size="8.5" font-weight="400" fill="#5A6578">• Cloisonnement strict des accès par rôles (Spring Security)</text>
  </g>

  <!-- Module 2.2 : Marketplace & Click & Collect -->
  <g transform="translate(495, 342)">
    <rect x="0" y="0" width="415" height="82" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="12" y="18" font-size="10" font-weight="700" fill="#243342">2. Module Marketplace &amp; Click &amp; Collect</text>
    <text x="12" y="34" font-size="8.5" font-weight="400" fill="#5A6578">• Fiches commerces, catalogue d'articles et gestion des stocks</text>
    <text x="12" y="48" font-size="8.5" font-weight="400" fill="#5A6578">• Protocole de réservation en 2 phases (anti-rupture en boutique)</text>
    <text x="12" y="62" font-size="8.5" font-weight="400" fill="#5A6578">• Calcul du plus court chemin piéton pour commandes groupées</text>
  </g>

  <!-- Module 2.3 : Double Fidélité & Programme VFP -->
  <g transform="translate(45, 436)">
    <rect x="0" y="0" width="415" height="85" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="12" y="18" font-size="10" font-weight="700" fill="#243342">3. Module Double Fidélité &amp; Statut VFP</text>
    <text x="12" y="34" font-size="8.5" font-weight="400" fill="#5A6578">• Fidélité commerçante privée : cagnottage et catalogue de lots offerts</text>
    <text x="12" y="48" font-size="8.5" font-weight="400" fill="#5A6578">• Moteur VFP : calcul automatique de la fréquence (10 achats / 15 jours)</text>
    <text x="12" y="62" font-size="8.5" font-weight="400" fill="#5A6578">• Déblocage des avantages mobilité (1 ticket bus/jour ou 20 min parking)</text>
  </g>

  <!-- Module 2.4 : Statistiques & Animation -->
  <g transform="translate(495, 436)">
    <rect x="0" y="0" width="415" height="85" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="12" y="18" font-size="10" font-weight="700" fill="#243342">4. Module Statistiques &amp; Supervision Municipale</text>
    <text x="12" y="34" font-size="8.5" font-weight="400" fill="#5A6578">• Indicateurs de rentabilité commerçante et volume de ventes généré</text>
    <text x="12" y="48" font-size="8.5" font-weight="400" fill="#5A6578">• Suivi municipal de l'attractivité territoriale et des coûts transport</text>
    <text x="12" y="62" font-size="8.5" font-weight="400" fill="#5A6578">• Module de relance usagers et diffusion des questionnaires QCM</text>
  </g>

  <!-- ======================================================== -->
  <!-- TIER 3 : PERSISTANCE & DONNÉES (POSTGRESQL 16)           -->
  <!-- ======================================================== -->
  <rect x="965" y="295" width="450" height="240" rx="10" fill="#FFFFFF" stroke="#8B9EAF" stroke-width="1.4" filter="url(#shadow-card)"/>
  
  <!-- En-tête Tier 3 -->
  <rect x="965" y="295" width="450" height="34" rx="10" fill="#243342" />
  <rect x="978" y="303" width="18" height="18" rx="4" fill="#2B5270" />
  <text x="987" y="316" text-anchor="middle" font-size="10" font-weight="800" fill="#FFFFFF">D</text>
  <text x="1005" y="317" font-size="11.5" font-weight="700" fill="#FFFFFF">TIER 3 — PERSISTANCE &amp; DONNÉES (PostgreSQL 16)</text>

  <g transform="translate(985, 342)">
    <rect x="0" y="0" width="410" height="180" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="12" y="20" font-size="10" font-weight="700" fill="#243342">Base de Données Relationnelle ShopLoc</text>
    <text x="12" y="38" font-size="8.5" font-weight="600" fill="#2B5270">Entités &amp; Tables principales (Intégrité ACID) :</text>
    <text x="12" y="54" font-size="8.5" font-weight="400" fill="#5A6578">• `Utilisateurs` (citoyens, commerçants, gestionnaires DSI, plaques)</text>
    <text x="12" y="68" font-size="8.5" font-weight="400" fill="#5A6578">• `Commerces` &amp; `Horaires` (établissements partenaires conventionnés)</text>
    <text x="12" y="82" font-size="8.5" font-weight="400" fill="#5A6578">• `Articles` &amp; `Stocks` (produits, prix, disponibilités Click &amp; Collect)</text>
    <text x="12" y="96" font-size="8.5" font-weight="400" fill="#5A6578">• `Commandes` &amp; `LignesCommande` (réservations, retraits, statuts)</text>
    <text x="12" y="110" font-size="8.5" font-weight="400" fill="#5A6578">• `SoldesFidelite` &amp; `LotsOfferts` (points commerçant et règles cadeaux)</text>
    <text x="12" y="124" font-size="8.5" font-weight="400" fill="#5A6578">• `HistoriqueVFP` &amp; `AvantagesMobilite` (calcul fréquence et gratuités)</text>
    <rect x="12" y="136" width="386" height="34" rx="4" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="205" y="157" text-anchor="middle" font-size="8.5" font-weight="600" fill="#2E583D">Volume persistant Docker dédié (Sauvegardes &amp; Intégrité)</text>
  </g>

  <!-- LIAISON TIER 2 <-> TIER 3 -->
  <line x1="935" y1="415" x2="965" y2="415" stroke="#243342" stroke-width="2"/>
  <polygon points="965,415 957,411 957,419" fill="#243342"/>
  <polygon points="935,415 943,411 943,419" fill="#243342"/>

  <!-- ======================================================== -->
  <!-- TIER 4 : SIMULATEURS DE PARTENAIRES EXTERNES (MOCKS REST)-->
  <!-- ======================================================== -->
  <rect x="25" y="550" width="1390" height="135" rx="10" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1.2" stroke-dasharray="4 3" filter="url(#shadow-card)"/>
  
  <!-- En-tête Tier 4 -->
  <rect x="25" y="550" width="1390" height="30" rx="10" fill="#F5F2EB" />
  <text x="45" y="570" font-size="11" font-weight="700" fill="#243342">SIMULATEURS DE SERVICES PARTENAIRES (Bouchons / Mocks REST intégrés sous Docker pour tests autonomes)</text>
  <text x="1395" y="570" text-anchor="end" font-size="9.5" font-weight="500" fill="#5A6578">Simulation des infrastructures tierces inaccessibles en environnement étudiant</text>

  <!-- Mock 1 : Banque -->
  <g transform="translate(45, 590)">
    <rect x="0" y="0" width="425" height="82" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <rect x="10" y="8" width="110" height="18" rx="3" fill="#243342" />
    <text x="65" y="21" text-anchor="middle" font-size="8.5" font-weight="700" fill="#FFFFFF">MOCK BANCAIRE</text>
    <text x="130" y="21" font-size="9" font-weight="700" fill="#243342">Porte-monnaie type Izli</text>
    <text x="10" y="42" font-size="8.5" font-weight="400" fill="#5A6578">• Simulation du rechargement en ligne par carte bancaire</text>
    <text x="10" y="56" font-size="8.5" font-weight="400" fill="#5A6578">• Débit pour micro-achats chez les commerçants partenaires</text>
    <text x="10" y="70" font-size="8.5" font-weight="600" fill="#4A7A5B">Réponse HTTP 200 / Validation solde</text>
  </g>

  <!-- Mock 2 : Transports Ilévia -->
  <g transform="translate(508, 590)">
    <rect x="0" y="0" width="425" height="82" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <rect x="10" y="8" width="125" height="18" rx="3" fill="#243342" />
    <text x="72" y="21" text-anchor="middle" font-size="8.5" font-weight="700" fill="#FFFFFF">MOCK TRANSPORTS</text>
    <text x="145" y="21" font-size="9" font-weight="700" fill="#243342">Réseau Bus Urbain (Ilévia)</text>
    <text x="10" y="42" font-size="8.5" font-weight="400" fill="#5A6578">• Émission d'un titre de transport virtuel quotidien offert</text>
    <text x="10" y="56" font-size="8.5" font-weight="400" fill="#5A6578">• Validation du QR code lors de la montée dans le bus (Pierre)</text>
    <text x="10" y="70" font-size="8.5" font-weight="600" fill="#4A7A5B">Génération e-ticket / QR dynamique</text>
  </g>

  <!-- Mock 3 : Voirie Stationnement -->
  <g transform="translate(970, 590)">
    <rect x="0" y="0" width="425" height="82" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <rect x="10" y="8" width="115" height="18" rx="3" fill="#243342" />
    <text x="67" y="21" text-anchor="middle" font-size="8.5" font-weight="700" fill="#FFFFFF">MOCK VOIRIE</text>
    <text x="135" y="21" font-size="9" font-weight="700" fill="#243342">Système de Stationnement</text>
    <text x="10" y="42" font-size="8.5" font-weight="400" fill="#5A6578">• Activation du forfait de 20 minutes gratuites (Arthur)</text>
    <text x="10" y="56" font-size="8.5" font-weight="400" fill="#5A6578">• Synchronisation de la plaque d'immatriculation avec l'horodateur</text>
    <text x="10" y="70" font-size="8.5" font-weight="600" fill="#4A7A5B">Droit de stationnement validé 20 min</text>
  </g>

  <!-- LIAISONS TIER 2 <-> TIER 4 -->
  <line x1="480" y1="535" x2="480" y2="550" stroke="#8A9BAE" stroke-width="1.5" stroke-dasharray="3 2"/>

  <!-- ======================================================== -->
  <!-- BANDEAU BAS : SOCLE DE DÉPLOIEMENT & OUTILLAGE DEVOPS    -->
  <!-- ======================================================== -->
  <rect x="25" y="700" width="1390" height="98" rx="10" fill="#243342" filter="url(#shadow-card)"/>
  
  <rect x="45" y="715" width="28" height="28" rx="6" fill="#4A7A5B"/>
  <text x="59" y="734" text-anchor="middle" font-size="13" font-weight="800" fill="#FFFFFF">D</text>
  <text x="85" y="733" font-size="12" font-weight="700" fill="#FFFFFF">Socle de Déploiement Conteneurisé &amp; Intégration Continue (DevOps)</text>
  <text x="85" y="749" font-size="9.5" font-weight="400" fill="#DCD6CD">Environnement isolé, reproductible et exécutable en local sur les ordinateurs d'évaluation sans installation complexe.</text>

  <g transform="translate(45, 760)">
    <!-- Item 1 : Docker Compose -->
    <rect x="0" y="0" width="425" height="26" rx="5" fill="#FAF9F6" />
    <text x="10" y="17" font-size="9" font-weight="700" fill="#243342">Docker Compose :</text>
    <text x="120" y="17" font-size="8.5" font-weight="500" fill="#5A6578">Lancement complet du système en 1 commande (`docker compose up`)</text>

    <!-- Item 2 : GitLab Lille -->
    <rect x="463" y="0" width="425" height="26" rx="5" fill="#FAF9F6" />
    <text x="473" y="17" font-size="9" font-weight="700" fill="#243342">GitLab Université de Lille :</text>
    <text x="635" y="17" font-size="8.5" font-weight="500" fill="#5A6578">Gestion de version, traçabilité et visibilité équipe pédagogique</text>

    <!-- Item 3 : OpenAPI Swagger -->
    <rect x="925" y="0" width="425" height="26" rx="5" fill="#FAF9F6" />
    <text x="935" y="17" font-size="9" font-weight="700" fill="#243342">Spécification OpenAPI 3.1 :</text>
    <text x="1090" y="17" font-size="8.5" font-weight="500" fill="#5A6578">Contrat d'interface documenté liant le frontend et le backend</text>
  </g>
</svg>
"""

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    # 1. Sauvegarde du composant HTML
    html_path = os.path.join(repo_root, "agent_projet/templates/components/tech_choices_diagram.html")
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    
    svg_content = generate_tech_diagram_svg()
    
    component_content = f"""<!-- FIGURE 4.1 : SCHÉMA D'ARCHITECTURE LOGICIELLE SHOPLOC (CHARTE OFFICIELLE) -->
<div class="figure-card" style="background:#FAF9F6; border:1px solid #DCD6CD; border-radius:14px; padding:20px; margin-bottom:24px; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px; border-bottom:1px solid #DCD6CD; padding-bottom:10px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#243342;"></span>
        <span style="font-size:11px; font-weight:700; color:#243342; text-transform:uppercase; letter-spacing:0.08em;">Ingénierie Logicielle &amp; DevOps</span>
      </div>
      <h3 style="font-size:16px; font-weight:700; color:#243342; margin:0;">Figure 4.1 — Architecture Applicative Prévisionnelle &amp; Pile Technologique ShopLoc</h3>
    </div>
    <span style="font-size:11px; background:#FFFFFF; border:1px solid #DCD6CD; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600;">Proposition Jalon R1 · Modulaire Conteneurisée</span>
  </div>
{svg_content}
</div>
"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(component_content)
    print(f"HTML écrit : {html_path}")

    # 2. Export SVG et PNG haute résolution avec PyMuPDF
    output_dir = os.path.join(repo_root, "agent_projet/docs/01_Cadrage_Et_Cahier_Des_Charges_R1/figures")
    os.makedirs(output_dir, exist_ok=True)
    svg_path = os.path.join(output_dir, "fig_4_1_choix_techniques.svg")
    png_path = os.path.join(output_dir, "fig_4_1_choix_techniques.png")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"SVG écrit : {svg_path}")

    doc = pymupdf.open(svg_path)
    page = doc[0]
    pix = page.get_pixmap(dpi=300)
    pix.save(png_path)
    print(f"Exporté PNG : {png_path} ({pix.width}x{pix.height})")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GÉNÉRATEUR DE LA GRILLE DE USER STORY MAPPING SHOPLOC (FIGURE 3.3)
Master 2 MIAGE — Université de Lille — UE GLOP (2026-2027)

Génère la cartographie vectorielle SVG conforme au modèle aha.io / Jeff Patton :
- Niveau 1 (Activités / Goals) : Les 5 grands objectifs usagers
- Niveau 2 (User Steps) : Les étapes séquentielles du parcours
- Tranches horizontales (Releases) : Release 1 (MVP) et Release 2 (Évolutions)
- Cartes usagers (User Stories) : 100% fidèles au sujet officiel et aux personas (Pierre, Julie, Arthur, Suzanne, Marius).
- Charte graphique ShopLoc officielle : Lin doux #FAF9F6, Ardoise #243342, Terracotta #C26750, Sauge #4A7A5B, Miel #C48B28.
- STRICTEMENT AUCUN STORY POINT (SP) mentionné.
"""

import os
import pymupdf

def generate_story_mapping_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1520 860" width="1520" height="860" style="font-family: 'Plus Jakarta Sans', 'Poppins', system-ui, -apple-system, sans-serif;">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;display=swap');
    </style>
    <filter id="shadow-soft" x="-2%" y="-2%" width="104%" height="106%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#243342" flood-opacity="0.06"/>
    </filter>
    <filter id="shadow-card" x="-4%" y="-6%" width="108%" height="116%">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2" flood-color="#243342" flood-opacity="0.04"/>
    </filter>
  </defs>

  <!-- FOND GLOBAL DE LA CARTE (LIN DOUX) -->
  <rect x="5" y="5" width="1510" height="850" rx="14" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1.2" filter="url(#shadow-soft)"/>

  <!-- ======================================================== -->
  <!-- EN-TÊTE PRINCIPAL DU DIAGRAMME                           -->
  <!-- ======================================================== -->
  <rect x="25" y="20" width="1470" height="50" rx="8" fill="#243342" />
  <rect x="38" y="31" width="28" height="28" rx="6" fill="#C26750" />
  <text x="52" y="50" text-anchor="middle" font-size="12" font-weight="800" fill="#FFFFFF">USM</text>
  <text x="78" y="44" font-size="14" font-weight="700" fill="#FFFFFF">Cartographie des Récits Utilisateurs — User Story Mapping (Modèle aha.io / Jeff Patton)</text>
  <text x="78" y="59" font-size="9.5" font-weight="400" fill="#EBF0F5">Activités Métier (Backbone) &gt; Étapes du Parcours (Steps) &gt; Récits Utilisateurs par Release</text>
  <text x="1480" y="49" text-anchor="end" font-size="11" font-weight="600" fill="#DCD6CD">ShopLoc · Master 2 MIAGE · Garik</text>

  <!-- ======================================================== -->
  <!-- NIVEAU 1 : ACTIVITÉS UTILISATEURS (USER ACTIVITIES)       -->
  <!-- ======================================================== -->
  <!-- Col 0 : Axe -->
  <rect x="25" y="80" width="115" height="42" rx="6" fill="#F5F2EB" stroke="#DCD6CD" stroke-width="1" />
  <text x="82" y="98" text-anchor="middle" font-size="10" font-weight="700" fill="#243342">ACTIVITÉS</text>
  <text x="82" y="112" text-anchor="middle" font-size="8.5" font-weight="600" fill="#5A6578">BACKBONE</text>

  <!-- Act 1 : Compte & Profils -->
  <rect x="150" y="80" width="260" height="42" rx="6" fill="#C26750" />
  <text x="280" y="98" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">1. COMPTE &amp; IDENTITÉ</text>
  <text x="280" y="112" text-anchor="middle" font-size="8.5" font-weight="500" fill="#FBEEEA">Inscription, connexion et profils</text>

  <!-- Act 2 : Catalogue & Click & Collect -->
  <rect x="420" y="80" width="260" height="42" rx="6" fill="#4A7A5B" />
  <text x="550" y="98" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">2. CATALOGUE &amp; CLICK &amp; COLLECT</text>
  <text x="550" y="112" text-anchor="middle" font-size="8.5" font-weight="500" fill="#EBF3ED">Articles, stocks, panier et trajet piéton</text>

  <!-- Act 3 : Caisse & Fidélité Boutique -->
  <rect x="690" y="80" width="260" height="42" rx="6" fill="#4A7A5B" />
  <text x="820" y="98" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">3. CAISSE &amp; FIDÉLITÉ BOUTIQUE</text>
  <text x="820" y="112" text-anchor="middle" font-size="8.5" font-weight="500" fill="#EBF3ED">Scan QR caisse, points et cadeaux</text>

  <!-- Act 4 : Programme VFP & Mobilité -->
  <rect x="960" y="80" width="260" height="42" rx="6" fill="#C48B28" />
  <text x="1090" y="98" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">4. STATUT VFP &amp; MOBILITÉ</text>
  <text x="1090" y="112" text-anchor="middle" font-size="8.5" font-weight="500" fill="#FEF7EB">Fréquence, bus offert et parking 20 min</text>

  <!-- Act 5 : Pilotage & Mairie -->
  <rect x="1230" y="80" width="265" height="42" rx="6" fill="#243342" />
  <text x="1362" y="98" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">5. PILOTAGE &amp; SUPERVISION</text>
  <text x="1362" y="112" text-anchor="middle" font-size="8.5" font-weight="500" fill="#EBF0F5">Rentabilité Suzanne et métriques Marius</text>

  <!-- ======================================================== -->
  <!-- NIVEAU 2 : ÉTAPES UTILISATEURS (USER STEPS)               -->
  <!-- ======================================================== -->
  <!-- Col 0 : Axe -->
  <rect x="25" y="128" width="115" height="42" rx="6" fill="#F5F2EB" stroke="#DCD6CD" stroke-width="1" />
  <text x="82" y="146" text-anchor="middle" font-size="10" font-weight="700" fill="#243342">ÉTAPES</text>
  <text x="82" y="160" text-anchor="middle" font-size="8" font-weight="500" fill="#5A6578">PARCOURS</text>

  <!-- Steps Act 1 -->
  <rect x="150" y="128" width="125" height="42" rx="6" fill="#FBEEEA" stroke="#D88B77" stroke-width="1" />
  <text x="212" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#8E3D2A">1.1 Inscription &amp;</text>
  <text x="212" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#8E3D2A">Authentification</text>

  <rect x="285" y="128" width="125" height="42" rx="6" fill="#FBEEEA" stroke="#D88B77" stroke-width="1" />
  <text x="347" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#8E3D2A">1.2 Profil &amp;</text>
  <text x="347" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#8E3D2A">Immatriculation</text>

  <!-- Steps Act 2 -->
  <rect x="420" y="128" width="125" height="42" rx="6" fill="#EBF3ED" stroke="#7EA88D" stroke-width="1" />
  <text x="482" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">2.1 Fiche Boutique</text>
  <text x="482" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">&amp; Articles</text>

  <rect x="555" y="128" width="125" height="42" rx="6" fill="#EBF3ED" stroke="#7EA88D" stroke-width="1" />
  <text x="617" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">2.2 Commande C&amp;C</text>
  <text x="617" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">&amp; Trajet Piéton</text>

  <!-- Steps Act 3 -->
  <rect x="690" y="128" width="125" height="42" rx="6" fill="#EBF3ED" stroke="#7EA88D" stroke-width="1" />
  <text x="752" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">3.1 Scan Caisse &amp;</text>
  <text x="752" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">Crédit Points</text>

  <rect x="825" y="128" width="125" height="42" rx="6" fill="#EBF3ED" stroke="#7EA88D" stroke-width="1" />
  <text x="887" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">3.2 Déblocage</text>
  <text x="887" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">Cadeaux Boutique</text>

  <!-- Steps Act 4 -->
  <rect x="960" y="128" width="125" height="42" rx="6" fill="#FEF7EB" stroke="#DCB162" stroke-width="1" />
  <text x="1022" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#845A11">4.1 Fréquence &amp;</text>
  <text x="1022" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#845A11">Obtention VFP</text>

  <rect x="1095" y="128" width="125" height="42" rx="6" fill="#FEF7EB" stroke="#DCB162" stroke-width="1" />
  <text x="1157" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#845A11">4.2 Usage Bus &amp;</text>
  <text x="1157" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#845A11">Parking 20 min</text>

  <!-- Steps Act 5 -->
  <rect x="1230" y="128" width="128" height="42" rx="6" fill="#EBF0F5" stroke="#8B9EAF" stroke-width="1" />
  <text x="1294" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#1C2D3D">5.1 Statistiques</text>
  <text x="1294" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#1C2D3D">Commerçant</text>

  <rect x="1367" y="128" width="128" height="42" rx="6" fill="#EBF0F5" stroke="#8B9EAF" stroke-width="1" />
  <text x="1431" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#1C2D3D">5.2 Supervision DSI</text>
  <text x="1431" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#1C2D3D">&amp; Sondages</text>

  <!-- ======================================================== -->
  <!-- SWIMLANE 1 : RELEASE 1 (MVP R4/R5 - MUST HAVE)           -->
  <!-- ======================================================== -->
  <rect x="25" y="180" width="1470" height="445" rx="10" fill="#FFFFFF" stroke="#243342" stroke-width="1.6" filter="url(#shadow-soft)"/>
  
  <!-- Bandeau Latéral Release 1 -->
  <path d="M 25 190 A 10 10 0 0 1 35 180 L 140 180 L 140 625 L 35 625 A 10 10 0 0 1 25 615 Z" fill="#EBF0F5" />
  <rect x="35" y="195" width="95" height="24" rx="5" fill="#243342" />
  <text x="82" y="211" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">RELEASE 1</text>
  <text x="82" y="235" text-anchor="middle" font-size="11" font-weight="800" fill="#243342">MVP</text>
  <text x="82" y="252" text-anchor="middle" font-size="8.5" font-weight="600" fill="#4A7A5B">Cœur du sujet</text>
  <circle cx="82" cy="295" r="18" fill="#FFFFFF" stroke="#243342" stroke-width="1.5"/>
  <text x="82" y="301" text-anchor="middle" font-size="14" font-weight="800" fill="#243342">M</text>
  <text x="82" y="328" text-anchor="middle" font-size="8.5" font-weight="700" fill="#243342">MUST HAVE</text>
  <text x="82" y="344" text-anchor="middle" font-size="8" font-weight="500" fill="#5A6578">Évalué R4 / R5</text>
  <text x="82" y="585" text-anchor="middle" font-size="8.5" font-weight="700" fill="#243342">Socle Majeur</text>
  <text x="82" y="602" text-anchor="middle" font-size="10" font-weight="800" fill="#4A7A5B">Priorité 1</text>

  <!-- LIGNES SÉPARATRICES ACTIVITÉS MVP -->
  <line x1="415" y1="180" x2="415" y2="625" stroke="#EDE8E1" stroke-width="1" />
  <line x1="685" y1="180" x2="685" y2="625" stroke="#EDE8E1" stroke-width="1" />
  <line x1="955" y1="180" x2="955" y2="625" stroke="#EDE8E1" stroke-width="1" />
  <line x1="1225" y1="180" x2="1225" y2="625" stroke="#EDE8E1" stroke-width="1" />

  <!-- === CARTES RELEASE 1 (MVP) === -->
  
  <!-- Step 1.1 : Card US-01 (Inscription) -->
  <g transform="translate(150, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#C26750" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#FBEEEA" stroke="#D88B77" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#8E3D2A">US-01</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#F5F2EB"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Création Compte</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#C26750">Julie / Arthur</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que citoyen,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je crée mon compte avec</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">mes identifiants et j'obtiens</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">ma carte de fidélité.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Accès service garanti</text>
  </g>

  <!-- Step 1.1 : Card US-02 (Connexion) -->
  <g transform="translate(150, 405)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#C26750" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#FBEEEA" stroke="#D88B77" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#8E3D2A">US-02</text>
    <rect x="72" y="8" width="47" height="14" rx="3" fill="#F5F2EB"/>
    <text x="95" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Tous rôles</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Se Connecter</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#C26750">Tous profils</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant qu'utilisateur</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">(citoyen, commerçant,</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">admin mairie), je me</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">connecte à mon espace.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Authentification sécure</text>
  </g>

  <!-- Step 1.2 : Card US-04 (Plaque) -->
  <g transform="translate(285, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#C26750" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#FBEEEA" stroke="#D88B77" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#8E3D2A">US-04</text>
    <rect x="68" y="8" width="51" height="14" rx="3" fill="#F5F2EB"/>
    <text x="93" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Automobile</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Saisie Plaque Auto</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#C26750">Arthur (Automobiliste)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant qu'automobiliste,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je renseigne mon numéro</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">de plaque dans mon profil</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">pour le parking offert.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Lien véhicule &lt;&gt; profil</text>
  </g>

  <!-- Step 2.1 : Card US-06 (Fiche boutique) -->
  <g transform="translate(420, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#4A7A5B" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#2E583D">US-06</text>
    <rect x="62" y="8" width="57" height="14" rx="3" fill="#F5F2EB"/>
    <text x="90" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Commerçant</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Horaires &amp; Boutique</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#4A7A5B">Suzanne (Fournil)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que commerçante,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je configure les horaires</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">d'ouverture et l'adresse</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">de ma boulangerie.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Fiche magasin publique</text>
  </g>

  <!-- Step 2.1 : Card US-07 (Gestion articles & stocks) -->
  <g transform="translate(420, 405)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#4A7A5B" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#2E583D">US-07</text>
    <rect x="62" y="8" width="57" height="14" rx="3" fill="#F5F2EB"/>
    <text x="90" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Commerçant</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Articles &amp; Stocks</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#4A7A5B">Suzanne (Fournil)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que commerçante,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je saisis et modifie</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">facilement mes articles</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">et stocks Click &amp; Collect.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Stock en temps réel</text>
  </g>

  <!-- Step 2.2 : Card US-09 (Panier Julie) -->
  <g transform="translate(555, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#4A7A5B" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#2E583D">US-09</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#F5F2EB"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Commander en Ligne</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#4A7A5B">Julie (Citadine)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que cliente,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je consulte les magasins,</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">sélectionne mes articles et</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">valide ma commande C&amp;C.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Réservation 2 phases</text>
  </g>

  <!-- Step 2.2 : Card US-11 (Plus court chemin) -->
  <g transform="translate(555, 405)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#4A7A5B" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#2E583D">US-11</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#F5F2EB"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Trajet le Plus Court</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#4A7A5B">Julie (Citadine)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que cliente,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je demande au système le</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">plus court chemin pour</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">collecter mes achats.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Calcul itinéraire piéton</text>
  </g>

  <!-- Step 3.1 : Card US-13 (Scan caisse & points) -->
  <g transform="translate(690, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#4A7A5B" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#2E583D">US-13</text>
    <rect x="62" y="8" width="57" height="14" rx="3" fill="#F5F2EB"/>
    <text x="90" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Commerçant</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Scan Caisse &amp; Points</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#4A7A5B">Pierre / Suzanne</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que commerçante,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je scanne la carte client</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">pour créditer les points</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">liés au montant dépensé.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Gain de points boutique</text>
  </g>

  <!-- Step 3.2 : Card US-15 (Catalogue cadeaux) -->
  <g transform="translate(825, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#4A7A5B" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#2E583D">US-15</text>
    <rect x="62" y="8" width="57" height="14" rx="3" fill="#F5F2EB"/>
    <text x="90" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Commerçant</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Catalogue Cadeaux</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#4A7A5B">Suzanne (Fournil)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que commerçante,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je paramètre les lots</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">offerts (tarte maroilles,</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">mini-viennoiserie).</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Offres partenaires</text>
  </g>

  <!-- Step 3.2 : Card US-16 (Déblocage cadeau) -->
  <g transform="translate(825, 405)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#4A7A5B" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#2E583D">US-16</text>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#F5F2EB"/>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Débloquer Cadeau</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#4A7A5B">Julie (Cliente)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que cliente,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">j'obtiens mon cadeau lors</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">d'un achat si j'ai au moins</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">un achat antérieur.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Règle anti-abus validée</text>
  </g>

  <!-- Step 4.1 : Card US-17 (Attribution VFP) -->
  <g transform="translate(960, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#C48B28" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#FEF7EB" stroke="#DCB162" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#845A11">US-17</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#F5F2EB"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Obtention Statut VFP</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#C48B28">Pierre / Arthur / Julie</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que client fidèle,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">j'obtiens le statut VFP</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">grâce à la fréquence de mes</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">achats hebdomadaires.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Calcul de fréquence auto</text>
  </g>

  <!-- Step 4.2 : Card US-19 (Bus Pierre) -->
  <g transform="translate(1095, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#C48B28" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#FEF7EB" stroke="#DCB162" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#845A11">US-19</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#F5F2EB"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Mobilité</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Ticket Bus Offert</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#C48B28">Pierre (Senior)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que VFP,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je génère mon ticket de bus</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">gratuit quotidien avec QR code</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">à présenter au chauffeur.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Ticket mobilité actif</text>
  </g>

  <!-- Step 4.2 : Card US-20 (Parking Arthur) -->
  <g transform="translate(1095, 405)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#C48B28" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#FEF7EB" stroke="#DCB162" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#845A11">US-20</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#F5F2EB"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Mobilité</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">20 min Parking Offert</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#C48B28">Arthur (Automobiliste)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que VFP,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">j'active mon forfait de 20 min</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">gratuites et je suis le</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">décompte en temps réel.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Stationnement synchronisé</text>
  </g>

  <!-- Step 5.1 : Card US-22 (Stats Suzanne) -->
  <g transform="translate(1230, 190)">
    <rect x="0" y="0" width="128" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="128" height="4" rx="2" fill="#243342" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5" stroke="#8B9EAF" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#1C2D3D">US-22</text>
    <rect x="65" y="8" width="57" height="14" rx="3" fill="#F5F2EB"/>
    <text x="93" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Commerçant</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Ventes Boutique</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#243342">Suzanne (Fournil)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que commerçante,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je consulte le volume des</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">ventes et achats C&amp;C</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">généré par les clients.</text>
    <rect x="6" y="180" width="116" height="18" rx="3" fill="#EBF3ED"/>
    <text x="64" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Mesure rentabilité</text>
  </g>

  <!-- Step 5.2 : Card US-24 (Tableau DSI Marius) -->
  <g transform="translate(1367, 190)">
    <rect x="0" y="0" width="128" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="128" height="4" rx="2" fill="#243342" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5" stroke="#8B9EAF" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#1C2D3D">US-24</text>
    <rect x="80" y="8" width="42" height="14" rx="3" fill="#F5F2EB"/>
    <text x="101" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Mairie DSI</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Tableau DSI Mairie</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#243342">Marius (DSI Ville)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant qu'admin DSI,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je compare le coût des</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">avantages mobilité au</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">volume des ventes.</text>
    <rect x="6" y="180" width="116" height="18" rx="3" fill="#EBF3ED"/>
    <text x="64" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Rapport conseil municipal</text>
  </g>

  <!-- ======================================================== -->
  <!-- SWIMLANE 2 : RELEASE 2 (ÉVOLUTIONS & CONFORT - SHOULD HAVE) -->
  <!-- ======================================================== -->
  <rect x="25" y="635" width="1470" height="205" rx="10" fill="#FFFFFF" stroke="#8C96A5" stroke-width="1.2" stroke-dasharray="4 3" filter="url(#shadow-soft)"/>
  
  <!-- Bandeau Latéral Release 2 -->
  <path d="M 25 645 A 10 10 0 0 1 35 635 L 140 635 L 140 840 L 35 840 A 10 10 0 0 1 25 830 Z" fill="#F5F2EB" />
  <rect x="35" y="645" width="95" height="22" rx="5" fill="#5A6578" />
  <text x="82" y="660" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">RELEASE 2</text>
  <text x="82" y="680" text-anchor="middle" font-size="10" font-weight="700" fill="#243342">Évolutions</text>
  <text x="82" y="695" text-anchor="middle" font-size="8" font-weight="600" fill="#C48B28">Confort usagers</text>
  <circle cx="82" cy="728" r="15" fill="#FFFFFF" stroke="#8C96A5" stroke-width="1"/>
  <text x="82" y="733" text-anchor="middle" font-size="11" font-weight="700" fill="#5A6578">S</text>
  <text x="82" y="755" text-anchor="middle" font-size="8" font-weight="600" fill="#5A6578">SHOULD HAVE</text>
  <text x="82" y="818" text-anchor="middle" font-size="8.5" font-weight="700" fill="#5A6578">Post-MVP</text>

  <!-- LIGNES SÉPARATRICES ACTIVITÉS R2 -->
  <line x1="415" y1="635" x2="415" y2="840" stroke="#EDE8E1" stroke-width="1" />
  <line x1="685" y1="635" x2="685" y2="840" stroke="#EDE8E1" stroke-width="1" />
  <line x1="955" y1="635" x2="955" y2="840" stroke="#EDE8E1" stroke-width="1" />
  <line x1="1225" y1="635" x2="1225" y2="840" stroke="#EDE8E1" stroke-width="1" />

  <!-- === CARTES RELEASE 2 (Évolutions) === -->
  <!-- Step 1.2 : US-05 (Recharge Izli) -->
  <g transform="translate(285, 645)">
    <rect x="0" y="0" width="125" height="185" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#5A6578">US-05</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#FFFFFF"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Recharge Carte Izli</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#5A6578">Julie (Citadine)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">Chargement en ligne</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">d'une somme d'argent par</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">carte bleue pour petits</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">achats partenaires.</text>
    <rect x="6" y="160" width="113" height="18" rx="3" fill="#EBF0F5"/>
    <text x="62" y="172" text-anchor="middle" font-size="7" font-weight="600" fill="#243342">Porte-monnaie Izli</text>
  </g>

  <!-- Step 2.1 : US-08 (Alerte rupture stock) -->
  <g transform="translate(420, 645)">
    <rect x="0" y="0" width="125" height="185" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#5A6578">US-08</text>
    <rect x="62" y="8" width="57" height="14" rx="3" fill="#FFFFFF"/>
    <text x="90" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Commerçant</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Alerte Rupture Stock</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#5A6578">Suzanne (Fournil)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">Notification automatique</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">à la commerçante dès</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">qu'un article est épuisé.</text>
    <rect x="6" y="160" width="113" height="18" rx="3" fill="#EBF0F5"/>
    <text x="62" y="172" text-anchor="middle" font-size="7" font-weight="600" fill="#243342">Alerte commerçant</text>
  </g>

  <!-- Step 2.2 : US-12 (Notification horaires Julie) -->
  <g transform="translate(555, 645)">
    <rect x="0" y="0" width="125" height="185" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#5A6578">US-12</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#FFFFFF"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Alerte Horaires</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#5A6578">Julie (Citadine)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">Notification courriel aux</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">clients quand les horaires</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">des magasins favoris</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">sont modifiés.</text>
    <rect x="6" y="160" width="113" height="18" rx="3" fill="#EBF0F5"/>
    <text x="62" y="172" text-anchor="middle" font-size="7" font-weight="600" fill="#243342">Suivi des commerces</text>
  </g>

  <!-- Step 4.1 : US-18 (Perte VFP Vacances Arthur) -->
  <g transform="translate(960, 645)">
    <rect x="0" y="0" width="125" height="185" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#5A6578">US-18</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#FFFFFF"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Gestion Perte VFP</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#5A6578">Arthur (Vacances)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">Suspension temporaire</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">du statut VFP si la</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">fréquence d'achats baisse</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">(vacances scolaires).</text>
    <rect x="6" y="160" width="113" height="18" rx="3" fill="#EBF0F5"/>
    <text x="62" y="172" text-anchor="middle" font-size="7" font-weight="600" fill="#243342">Règle d'inactivité</text>
  </g>

  <!-- Step 5.1 : US-23 (Comparatif Suzanne) -->
  <g transform="translate(1230, 645)">
    <rect x="0" y="0" width="128" height="185" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#5A6578">US-23</text>
    <rect x="65" y="8" width="57" height="14" rx="3" fill="#FFFFFF"/>
    <text x="93" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Commerçant</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Comparatif Ventes</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#5A6578">Suzanne (Fournil)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">Indicateurs comparatifs</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">auprès des autres magasins</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">pour vérifier le gain</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">de participation.</text>
    <rect x="6" y="160" width="116" height="18" rx="3" fill="#EBF0F5"/>
    <text x="64" y="172" text-anchor="middle" font-size="7" font-weight="600" fill="#243342">Benchmark interne</text>
  </g>

  <!-- Step 5.2 : US-25 (Marius Relance & Sondages) -->
  <g transform="translate(1367, 645)">
    <rect x="0" y="0" width="128" height="185" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#5A6578">US-25</text>
    <rect x="80" y="8" width="42" height="14" rx="3" fill="#FFFFFF"/>
    <text x="101" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Mairie DSI</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Sondages &amp; Relances</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#5A6578">Marius (DSI)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">Envoi de questionnaires</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">QCM de satisfaction et</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">relance des usagers lors</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">de la perte du statut VFP.</text>
    <rect x="6" y="160" width="116" height="18" rx="3" fill="#EBF0F5"/>
    <text x="64" y="172" text-anchor="middle" font-size="7" font-weight="600" fill="#243342">Animation &amp; Rétention</text>
  </g>
</svg>
"""

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    # 1. Sauvegarde du composant HTML
    html_path = os.path.join(repo_root, "agent_projet/templates/components/story_mapping_grid.html")
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    
    svg_content = generate_story_mapping_svg()
    
    component_content = f"""<!-- FIGURE 3.3 : GRILLE DE USER STORY MAPPING (CHARTE OFFICIELLE SHOPLOC) -->
<div class="figure-card" style="background:#FAF9F6; border:1px solid #DCD6CD; border-radius:14px; padding:20px; margin-bottom:24px; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px; border-bottom:1px solid #DCD6CD; padding-bottom:10px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#C26750;"></span>
        <span style="font-size:11px; font-weight:700; color:#C26750; text-transform:uppercase; letter-spacing:0.08em;">Ingénierie des Exigences</span>
      </div>
      <h3 style="font-size:16px; font-weight:700; color:#243342; margin:0;">Figure 3.3 — Cartographie des Récits Utilisateurs (User Story Mapping)</h3>
    </div>
    <span style="font-size:11px; background:#FFFFFF; border:1px solid #DCD6CD; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600;">Modèle aha.io · Release 1 (MVP) &amp; Release 2</span>
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
    svg_path = os.path.join(output_dir, "fig_3_3_user_story_mapping.svg")
    png_path = os.path.join(output_dir, "fig_3_3_user_story_mapping.png")
    png_compat_path = os.path.join(output_dir, "fig_6_1_user_story_mapping.png")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"SVG écrit : {svg_path}")

    doc = pymupdf.open(svg_path)
    page = doc[0]
    pix = page.get_pixmap(dpi=300)
    pix.save(png_path)
    pix.save(png_compat_path)
    print(f"Exporté PNG : {png_path} et {png_compat_path} ({pix.width}x{pix.height})")

if __name__ == "__main__":
    main()

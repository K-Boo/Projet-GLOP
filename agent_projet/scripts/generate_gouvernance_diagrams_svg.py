#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GÉNÉRATEUR DE SCHÉMAS DE GOUVERNANCE AGILE SHOPLOC (FIGURES 8.1, 8.2 ET 8.3)
Master 2 MIAGE — Université de Lille — UE GLOP (2026-2027)

Génère trois schémas vectoriels pour la Section 08 :
- Figure 8.1 : Organigramme des Tâches WBS par lots (Work Breakdown Structure)
- Figure 8.2 : Matrice des Responsabilités RACI (6 pôles + MOA)
- Figure 8.3 : Diagramme de Gantt Annuel & Jalons Contractuels R1 à R5 (Sept 2026 - Mars 2027)

Conformité stricte à la charte graphique pastel ShopLoc (ADR-014, ADR-015), sans emoji, sans languette asymétrique.
"""

import os
import subprocess

BROWSER = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

COMMON_DEFS = """
  <defs>
    <filter id="shadow-card" x="-5%" y="-5%" width="110%" height="114%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#243342" flood-opacity="0.06"/>
    </filter>
    <filter id="shadow-box" x="-3%" y="-4%" width="106%" height="110%">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-color="#243342" flood-opacity="0.05"/>
    </filter>
    <marker id="arrow-slate" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#334155" />
    </marker>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0284C7" />
    </marker>
    <marker id="arrow-red" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#DC2626" />
    </marker>
  </defs>
"""

# ==============================================================================
# FIGURE 8.1 : ORGANIGRAMME DES TÂCHES WBS PAR LOTS (1180 x 680)
# ==============================================================================
def generate_wbs_svg():
    return f"""<svg viewBox="0 0 1180 680" width="1180" height="680" style="overflow:visible; font-family:'Poppins', sans-serif;">
{COMMON_DEFS}

  <!-- CADRE GLOBAL -->
  <rect x="10" y="10" width="1160" height="660" rx="14" fill="#FAFAFA" stroke="#E2E8F0" stroke-width="1.2" />

  <!-- EN-TETE BANDEAU -->
  <rect x="25" y="22" width="1130" height="42" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
  <rect x="35" y="32" width="22" height="22" rx="4" fill="#0284C7" />
  <text x="46" y="47" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">WBS</text>
  <text x="68" y="46" font-size="13" font-weight="700" fill="#1E293B">Organigramme des Tâches Projet (Work Breakdown Structure)</text>
  <text x="1140" y="46" text-anchor="end" font-size="11" font-weight="500" fill="#64748B">Décomposition Hiérarchique en 6 Lots de Travaux (WP1 à WP6) · Traçabilité R1-R5</text>

  <!-- NOEUD RACINE DU WBS -->
  <g filter="url(#shadow-card)">
    <rect x="420" y="80" width="340" height="44" rx="8" fill="#243342" stroke="#1E293B" stroke-width="1" />
    <text x="590" y="98" text-anchor="middle" font-size="12" font-weight="700" fill="#FFFFFF">PROJET SHOPLOC — SYSTÈME SAAS TERRITORIAL</text>
    <text x="590" y="113" text-anchor="middle" font-size="10" font-weight="400" fill="#CBD5E1">Plateforme Bimodale : Cockpit Gouvernance &amp; Monolithe Métier</text>
  </g>

  <!-- LIGNE MAITRESSE HORIZONTALE DU WBS -->
  <path d="M 590 124 L 590 148 M 115 148 L 1065 148" stroke="#94A3B8" stroke-width="1.5" fill="none" />
  <!-- CONNECTEURS VERTICAUX VERS LES 6 LOTS -->
  <path d="M 115 148 L 115 170" stroke="#94A3B8" stroke-width="1.5" fill="none" />
  <path d="M 305 148 L 305 170" stroke="#94A3B8" stroke-width="1.5" fill="none" />
  <path d="M 495 148 L 495 170" stroke="#94A3B8" stroke-width="1.5" fill="none" />
  <path d="M 685 148 L 685 170" stroke="#94A3B8" stroke-width="1.5" fill="none" />
  <path d="M 875 148 L 875 170" stroke="#94A3B8" stroke-width="1.5" fill="none" />
  <path d="M 1065 148 L 1065 170" stroke="#94A3B8" stroke-width="1.5" fill="none" />

  <!-- ======================================================== -->
  <!-- LOT 1 : WP1 - CADRAGE STRATÉGIQUE (R1)                   -->
  <!-- ======================================================== -->
  <g filter="url(#shadow-box)">
    <rect x="25" y="170" width="180" height="475" rx="10" fill="#FFFFFF" stroke="#BAE6FD" stroke-width="1.2" />
    <!-- Tete du lot -->
    <rect x="25" y="170" width="180" height="40" rx="10" fill="#E0F2FE" />
    <rect x="25" y="195" width="180" height="15" fill="#E0F2FE" />
    <text x="115" y="187" text-anchor="middle" font-size="11" font-weight="700" fill="#0369A1">LOT 1 · WP1</text>
    <text x="115" y="202" text-anchor="middle" font-size="10" font-weight="600" fill="#0C4A6E">Cadrage &amp; CDC (R1)</text>

    <!-- Sous-taches WP1 -->
    <rect x="35" y="222" width="160" height="48" rx="6" fill="#F0F9FF" stroke="#E0F2FE" stroke-width="1" />
    <text x="43" y="238" font-size="9.5" font-weight="700" fill="#0369A1">1.1 Analyse APTE &amp; Pyramide</text>
    <text x="43" y="253" font-size="8.5" fill="#475569">Bête à cornes &amp; pieuvre (FP/FC)</text>
    <text x="43" y="264" font-size="8" fill="#64748B">Positionnement concurrentiel</text>

    <rect x="35" y="278" width="160" height="48" rx="6" fill="#F0F9FF" stroke="#E0F2FE" stroke-width="1" />
    <text x="43" y="294" font-size="9.5" font-weight="700" fill="#0369A1">1.2 Personas &amp; Journeys</text>
    <text x="43" y="309" font-size="8.5" fill="#475569">Pierre, Suzanne, Marius, Julie</text>
    <text x="43" y="320" font-size="8" fill="#64748B">Cartes d'expérience utilisateur</text>

    <rect x="35" y="334" width="160" height="48" rx="6" fill="#F0F9FF" stroke="#E0F2FE" stroke-width="1" />
    <text x="43" y="350" font-size="9.5" font-weight="700" fill="#0369A1">1.3 Processus BPMN 2.0</text>
    <text x="43" y="365" font-size="8.5" fill="#475569">P1 à P5 : C&amp;C, VFP, Mobilité</text>
    <text x="43" y="376" font-size="8" fill="#64748B">Flux nominaux &amp; exceptions</text>

    <rect x="35" y="390" width="160" height="48" rx="6" fill="#F0F9FF" stroke="#E0F2FE" stroke-width="1" />
    <text x="43" y="406" font-size="9.5" font-weight="700" fill="#0369A1">1.4 Modélisation MCD Merise</text>
    <text x="43" y="421" font-size="8.5" fill="#475569">Schéma entités-associations</text>
    <text x="43" y="432" font-size="8" fill="#64748B">Dictionnaire formel des données</text>

    <rect x="35" y="446" width="160" height="48" rx="6" fill="#F0F9FF" stroke="#E0F2FE" stroke-width="1" />
    <text x="43" y="462" font-size="9.5" font-weight="700" fill="#0369A1">1.5 Story Mapping &amp; MoSCoW</text>
    <text x="43" y="477" font-size="8.5" fill="#475569">10 US Must Have (MVP V1)</text>
    <text x="43" y="488" font-size="8" fill="#64748B">Critères d'acceptation Gherkin</text>

    <rect x="35" y="502" width="160" height="48" rx="6" fill="#F0F9FF" stroke="#E0F2FE" stroke-width="1" />
    <text x="43" y="518" font-size="9.5" font-weight="700" fill="#0369A1">1.6 Cadrage Technique C4</text>
    <text x="43" y="533" font-size="8.5" fill="#475569">C4 Contexte &amp; Conteneurs</text>
    <text x="43" y="544" font-size="8" fill="#64748B">Spécifications OpenAPI 3.1</text>

    <!-- Livrable jalon -->
    <rect x="35" y="575" width="160" height="56" rx="6" fill="#0284C7" />
    <text x="115" y="595" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">LIVRABLE R1</text>
    <text x="115" y="609" text-anchor="middle" font-size="8.5" fill="#E0F2FE">Cahier des Charges &amp; Cadrage</text>
    <text x="115" y="621" text-anchor="middle" font-size="8" font-weight="600" fill="#BAE6FD">Rendu 18/09 · Oral 21/09</text>
  </g>

  <!-- ======================================================== -->
  <!-- LOT 2 : WP2 - OUTILLAGE & DEVOPS (R2)                    -->
  <!-- ======================================================== -->
  <g filter="url(#shadow-box)">
    <rect x="215" y="170" width="180" height="475" rx="10" fill="#FFFFFF" stroke="#FED7AA" stroke-width="1.2" />
    <rect x="215" y="170" width="180" height="40" rx="10" fill="#FFEDD5" />
    <rect x="215" y="195" width="180" height="15" fill="#FFEDD5" />
    <text x="305" y="187" text-anchor="middle" font-size="11" font-weight="700" fill="#C2410C">LOT 2 · WP2</text>
    <text x="305" y="202" text-anchor="middle" font-size="10" font-weight="600" fill="#7C2D12">Outillage &amp; DevOps (R2)</text>

    <rect x="225" y="222" width="160" height="48" rx="6" fill="#FFF7ED" stroke="#FFEDD5" stroke-width="1" />
    <text x="233" y="238" font-size="9.5" font-weight="700" fill="#C2410C">2.1 Forge GitLab &amp; Gitflow</text>
    <text x="233" y="253" font-size="8.5" fill="#475569">Protection main/develop</text>
    <text x="233" y="264" font-size="8" fill="#64748B">Convention Conventional Commits</text>

    <rect x="225" y="278" width="160" height="48" rx="6" fill="#FFF7ED" stroke="#FFEDD5" stroke-width="1" />
    <text x="233" y="294" font-size="9.5" font-weight="700" fill="#C2410C">2.2 CI/CD &amp; Qualimétrie</text>
    <text x="233" y="309" font-size="8.5" fill="#475569">Pipeline GitLab CI automatisé</text>
    <text x="233" y="320" font-size="8" fill="#64748B">Intégration SonarQube (seuil 80%)</text>

    <rect x="225" y="334" width="160" height="48" rx="6" fill="#FFF7ED" stroke="#FFEDD5" stroke-width="1" />
    <text x="233" y="350" font-size="9.5" font-weight="700" fill="#C2410C">2.3 Socle Docker Multi-Stage</text>
    <text x="233" y="365" font-size="8.5" fill="#475569">Docker Compose unifié</text>
    <text x="233" y="376" font-size="8" fill="#64748B">PostgreSQL 16 &amp; Redis 7</text>

    <rect x="225" y="390" width="160" height="48" rx="6" fill="#FFF7ED" stroke="#FFEDD5" stroke-width="1" />
    <text x="233" y="406" font-size="9.5" font-weight="700" fill="#C2410C">2.4 Serveurs Mocks REST</text>
    <text x="233" y="421" font-size="8.5" fill="#475569">Mocks Banque 2PC, Ilévia, POS</text>
    <text x="233" y="432" font-size="8" fill="#64748B">Contrats OpenAPI 3.1 simulés</text>

    <!-- Espace d'alignement -->
    <rect x="225" y="446" width="160" height="104" rx="6" fill="#FAFAFA" stroke="#E2E8F0" stroke-dasharray="3,3" />
    <text x="305" y="500" text-anchor="middle" font-size="9" fill="#94A3B8">Socle outillage &amp; validation</text>
    <text x="305" y="514" text-anchor="middle" font-size="8" fill="#CBD5E1">Préalable strict au dev R4</text>

    <!-- Livrable jalon -->
    <rect x="225" y="575" width="160" height="56" rx="6" fill="#EA580C" />
    <text x="305" y="595" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">LIVRABLE R2</text>
    <text x="305" y="609" text-anchor="middle" font-size="8.5" fill="#FFEDD5">Choix &amp; Setup Outils Logiciels</text>
    <text x="305" y="621" text-anchor="middle" font-size="8" font-weight="600" fill="#FED7AA">Rendu 12/10/2026</text>
  </g>

  <!-- ======================================================== -->
  <!-- LOT 3 : WP3 - ÉCONOMIE & COÛTS COMPLETS (R3)             -->
  <!-- ======================================================== -->
  <g filter="url(#shadow-box)">
    <rect x="405" y="170" width="180" height="475" rx="10" fill="#FFFFFF" stroke="#FEF08A" stroke-width="1.2" />
    <rect x="405" y="170" width="180" height="40" rx="10" fill="#FEF9C3" />
    <rect x="405" y="195" width="180" height="15" fill="#FEF9C3" />
    <text x="495" y="187" text-anchor="middle" font-size="11" font-weight="700" fill="#A16207">LOT 3 · WP3</text>
    <text x="495" y="202" text-anchor="middle" font-size="10" font-weight="600" fill="#713F12">Économie &amp; ROI (R3)</text>

    <rect x="415" y="222" width="160" height="48" rx="6" fill="#FEFCE8" stroke="#FEF9C3" stroke-width="1" />
    <text x="423" y="238" font-size="9.5" font-weight="700" fill="#A16207">3.1 Méthode Coûts Complets</text>
    <text x="423" y="253" font-size="8.5" fill="#475569">Charges directes &amp; indirectes</text>
    <text x="423" y="264" font-size="8" fill="#64748B">Centres Build, Run, Support</text>

    <rect x="415" y="278" width="160" height="48" rx="6" fill="#FEFCE8" stroke="#FEF9C3" stroke-width="1" />
    <text x="423" y="294" font-size="9.5" font-weight="700" fill="#A16207">3.2 Unités d'Œuvre (UO)</text>
    <text x="423" y="309" font-size="8.5" fill="#475569">Clés de répartition analytique</text>
    <text x="423" y="320" font-size="8" fill="#64748B">Coût par habitant &amp; commerce</text>

    <rect x="415" y="334" width="160" height="48" rx="6" fill="#FEFCE8" stroke="#FEF9C3" stroke-width="1" />
    <text x="423" y="350" font-size="9.5" font-weight="700" fill="#A16207">3.3 P&amp;L Prévisionnel 3 Ans</text>
    <text x="423" y="365" font-size="8.5" fill="#475569">Investissement initial &amp; Run</text>
    <text x="423" y="376" font-size="8" fill="#64748B">Amortissement matériel/logiciel</text>

    <rect x="415" y="390" width="160" height="48" rx="6" fill="#FEFCE8" stroke="#FEF9C3" stroke-width="1" />
    <text x="423" y="406" font-size="9.5" font-weight="700" fill="#A16207">3.4 Calcul ROI &amp; VAN</text>
    <text x="423" y="421" font-size="8.5" fill="#475569">Actualisation flux de trésorerie</text>
    <text x="423" y="432" font-size="8" fill="#64748B">Seuils par strates de communes</text>

    <!-- Espace alignement -->
    <rect x="415" y="446" width="160" height="104" rx="6" fill="#FAFAFA" stroke="#E2E8F0" stroke-dasharray="3,3" />
    <text x="495" y="500" text-anchor="middle" font-size="9" fill="#94A3B8">Arbitrage financier</text>
    <text x="495" y="514" text-anchor="middle" font-size="8" fill="#CBD5E1">Modèle convention tripartite</text>

    <!-- Livrable jalon -->
    <rect x="415" y="575" width="160" height="56" rx="6" fill="#CA8A04" />
    <text x="495" y="595" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">LIVRABLE R3</text>
    <text x="495" y="609" text-anchor="middle" font-size="8.5" fill="#FEF9C3">Étude Financière &amp; Coûts</text>
    <text x="495" y="621" text-anchor="middle" font-size="8" font-weight="600" fill="#FEF08A">Rendu 30/11/2026</text>
  </g>

  <!-- ======================================================== -->
  <!-- LOT 4 : WP4 - ARCHITECTURE & 1ER COMPOSANT (R4)          -->
  <!-- ======================================================== -->
  <g filter="url(#shadow-box)">
    <rect x="595" y="170" width="180" height="475" rx="10" fill="#FFFFFF" stroke="#DDD6FE" stroke-width="1.2" />
    <rect x="595" y="170" width="180" height="40" rx="10" fill="#EDE9FE" />
    <rect x="595" y="195" width="180" height="15" fill="#EDE9FE" />
    <text x="685" y="187" text-anchor="middle" font-size="11" font-weight="700" fill="#6D28D9">LOT 4 · WP4</text>
    <text x="685" y="202" text-anchor="middle" font-size="10" font-weight="600" fill="#4C1D95">Archi &amp; Prototype (R4)</text>

    <rect x="605" y="222" width="160" height="48" rx="6" fill="#F5F3FF" stroke="#EDE9FE" stroke-width="1" />
    <text x="613" y="238" font-size="9.5" font-weight="700" fill="#6D28D9">4.1 Vues 4+1 C4 Détaillées</text>
    <text x="613" y="253" font-size="8.5" fill="#475569">Vue fonctionnelle &amp; composants</text>
    <text x="613" y="264" font-size="8" fill="#64748B">Vue développement &amp; déploiement</text>

    <rect x="605" y="278" width="160" height="48" rx="6" fill="#F5F3FF" stroke="#EDE9FE" stroke-width="1" />
    <text x="613" y="294" font-size="9.5" font-weight="700" fill="#6D28D9">4.2 Schéma SQL &amp; Mapping</text>
    <text x="613" y="309" font-size="8.5" fill="#475569">DDL PostgreSQL 16 normalisé</text>
    <text x="613" y="320" font-size="8" fill="#64748B">Mapping objet-relationnel ORM</text>

    <rect x="605" y="334" width="160" height="48" rx="6" fill="#F5F3FF" stroke="#EDE9FE" stroke-width="1" />
    <text x="613" y="350" font-size="9.5" font-weight="700" fill="#6D28D9">4.3 1er Composant Logiciel</text>
    <text x="613" y="365" font-size="8.5" fill="#475569">Implémentation Panier 2PC</text>
    <text x="613" y="376" font-size="8" fill="#64748B">Conteneurisé &amp; testé TDD</text>

    <rect x="605" y="390" width="160" height="48" rx="6" fill="#F5F3FF" stroke="#EDE9FE" stroke-width="1" />
    <text x="613" y="406" font-size="9.5" font-weight="700" fill="#6D28D9">4.4 Justification Propriétés</text>
    <text x="613" y="421" font-size="8.5" fill="#475569">Performance, Frugalité Green IT</text>
    <text x="613" y="432" font-size="8" fill="#64748B">Maintenabilité &amp; Réutilisabilité</text>

    <!-- Espace alignement -->
    <rect x="605" y="446" width="160" height="104" rx="6" fill="#FAFAFA" stroke="#E2E8F0" stroke-dasharray="3,3" />
    <text x="685" y="500" text-anchor="middle" font-size="9" fill="#94A3B8">Pitch projet &amp; démo</text>
    <text x="685" y="514" text-anchor="middle" font-size="8" fill="#CBD5E1">Proposition de valeur &amp; RSE</text>

    <!-- Livrable jalon -->
    <rect x="605" y="575" width="160" height="56" rx="6" fill="#7C3AED" />
    <text x="685" y="595" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">LIVRABLE R4</text>
    <text x="685" y="609" text-anchor="middle" font-size="8.5" fill="#EDE9FE">Archi Vues 4+1 &amp; Démo V1</text>
    <text x="685" y="621" text-anchor="middle" font-size="8" font-weight="600" fill="#DDD6FE">Rendu 18/12 · Oral 04/01</text>
  </g>

  <!-- ======================================================== -->
  <!-- LOT 5 : WP5 - DÉVELOPPEMENT & LIVRABLE FINAL (R5)        -->
  <!-- ======================================================== -->
  <g filter="url(#shadow-box)">
    <rect x="785" y="170" width="180" height="475" rx="10" fill="#FFFFFF" stroke="#A7F3D0" stroke-width="1.2" />
    <rect x="785" y="170" width="180" height="40" rx="10" fill="#D1FAE5" />
    <rect x="785" y="195" width="180" height="15" fill="#D1FAE5" />
    <text x="875" y="187" text-anchor="middle" font-size="11" font-weight="700" fill="#047857">LOT 5 · WP5</text>
    <text x="875" y="202" text-anchor="middle" font-size="10" font-weight="600" fill="#064E3B">Dév &amp; Release Finale (R5)</text>

    <rect x="795" y="222" width="160" height="48" rx="6" fill="#ECFDF5" stroke="#D1FAE5" stroke-width="1" />
    <text x="803" y="238" font-size="9.5" font-weight="700" fill="#047857">5.1 Implémentation MVP V1</text>
    <text x="803" y="253" font-size="8.5" fill="#475569">10 US Must Have complètes</text>
    <text x="803" y="264" font-size="8" fill="#64748B">Front-office &amp; Back-office</text>

    <rect x="795" y="278" width="160" height="48" rx="6" fill="#ECFDF5" stroke="#D1FAE5" stroke-width="1" />
    <text x="803" y="294" font-size="9.5" font-weight="700" fill="#047857">5.2 Double Moteur Fidélité</text>
    <text x="803" y="309" font-size="8.5" fill="#475569">Points commerçants &amp; VFP 15j</text>
    <text x="803" y="320" font-size="8" fill="#64748B">Scan express &lt; 3s &amp; Pass papier</text>

    <rect x="795" y="334" width="160" height="48" rx="6" fill="#ECFDF5" stroke="#D1FAE5" stroke-width="1" />
    <text x="803" y="350" font-size="9.5" font-weight="700" fill="#047857">5.3 Mocks &amp; Intégration</text>
    <text x="803" y="365" font-size="8.5" fill="#475569">Titres transport &amp; parking</text>
    <text x="803" y="376" font-size="8" fill="#64748B">Simulation passerelle bancaire</text>

    <rect x="795" y="390" width="160" height="48" rx="6" fill="#ECFDF5" stroke="#D1FAE5" stroke-width="1" />
    <text x="803" y="406" font-size="9.5" font-weight="700" fill="#047857">5.4 Campagne Tests &amp; Homolog.</text>
    <text x="803" y="421" font-size="8.5" fill="#475569">Tests charge, non-régression</text>
    <text x="803" y="432" font-size="8" fill="#64748B">Audit accessibilité RGAA AA</text>

    <!-- Espace alignement -->
    <rect x="795" y="446" width="160" height="104" rx="6" fill="#FAFAFA" stroke="#E2E8F0" stroke-dasharray="3,3" />
    <text x="875" y="500" text-anchor="middle" font-size="9" fill="#94A3B8">Déploiement clé en main</text>
    <text x="875" y="514" text-anchor="middle" font-size="8" fill="#CBD5E1">docker compose up -d</text>

    <!-- Livrable jalon -->
    <rect x="795" y="575" width="160" height="56" rx="6" fill="#059669" />
    <text x="875" y="595" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">LIVRABLE R5</text>
    <text x="875" y="609" text-anchor="middle" font-size="8.5" fill="#D1FAE5">Solution Déployée &amp; Validée</text>
    <text x="875" y="621" text-anchor="middle" font-size="8" font-weight="600" fill="#A7F3D0">Rendu 19/03 · Oral 22/03</text>
  </g>

  <!-- ======================================================== -->
  <!-- LOT 6 : WP6 - EXPLOITATION, RSE & CLÔTURE                -->
  <!-- ======================================================== -->
  <g filter="url(#shadow-box)">
    <rect x="975" y="170" width="180" height="475" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2" />
    <rect x="975" y="170" width="180" height="40" rx="10" fill="#F1F5F9" />
    <rect x="975" y="195" width="180" height="15" fill="#F1F5F9" />
    <text x="1065" y="187" text-anchor="middle" font-size="11" font-weight="700" fill="#334155">LOT 6 · WP6</text>
    <text x="1065" y="202" text-anchor="middle" font-size="10" font-weight="600" fill="#0F172A">RSE &amp; Clôture</text>

    <rect x="985" y="222" width="160" height="48" rx="6" fill="#F8FAFC" stroke="#F1F5F9" stroke-width="1" />
    <text x="993" y="238" font-size="9.5" font-weight="700" fill="#334155">6.1 Bilan Frugalité &amp; Green IT</text>
    <text x="993" y="253" font-size="8.5" fill="#475569">Sobriété requêtes SQL &amp; réseau</text>
    <text x="993" y="264" font-size="8" fill="#64748B">Éco-conception logicielle</text>

    <rect x="985" y="278" width="160" height="48" rx="6" fill="#F8FAFC" stroke="#F1F5F9" stroke-width="1" />
    <text x="993" y="294" font-size="9.5" font-weight="700" fill="#334155">6.2 Manuel Exploitation</text>
    <text x="993" y="309" font-size="8.5" fill="#475569">Guide déploiement Docker</text>
    <text x="993" y="320" font-size="8" fill="#64748B">Notice support commerçants</text>

    <rect x="985" y="334" width="160" height="48" rx="6" fill="#F8FAFC" stroke="#F1F5F9" stroke-width="1" />
    <text x="993" y="350" font-size="9.5" font-weight="700" fill="#334155">6.3 Registre RGPD &amp; Clôture</text>
    <text x="993" y="365" font-size="8.5" fill="#475569">Pseudonymisation salée SHA-256</text>
    <text x="993" y="376" font-size="8" fill="#64748B">Conformité CNIL territoriale</text>

    <rect x="985" y="390" width="160" height="48" rx="6" fill="#F8FAFC" stroke="#F1F5F9" stroke-width="1" />
    <text x="993" y="406" font-size="9.5" font-weight="700" fill="#334155">6.4 Rétrospective Globale</text>
    <text x="993" y="421" font-size="8.5" fill="#475569">Bilan agile sur l'année</text>
    <text x="993" y="432" font-size="8" fill="#64748B">Capitalisation des apprentissages</text>

    <!-- Espace alignement -->
    <rect x="985" y="446" width="160" height="104" rx="6" fill="#FAFAFA" stroke="#E2E8F0" stroke-dasharray="3,3" />
    <text x="1065" y="500" text-anchor="middle" font-size="9" fill="#94A3B8">Pérénnité &amp; Passation</text>
    <text x="1065" y="514" text-anchor="middle" font-size="8" fill="#CBD5E1">Documentation ouverte</text>

    <!-- Livrable jalon -->
    <rect x="985" y="575" width="160" height="56" rx="6" fill="#475569" />
    <text x="1065" y="595" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">ARCHIVAGE &amp; BILAN</text>
    <text x="1065" y="609" text-anchor="middle" font-size="8.5" fill="#F1F5F9">Notice Exploitation &amp; RSE</text>
    <text x="1065" y="621" text-anchor="middle" font-size="8" font-weight="600" fill="#CBD5E1">Clôture Session S4</text>
  </g>

</svg>"""

# ==============================================================================
# FIGURE 8.2 : MATRICE DES RESPONSABILITÉS RACI (1180 x 640)
# ==============================================================================
def generate_raci_svg():
    return f"""<svg viewBox="0 0 1180 640" width="1180" height="640" style="overflow:visible; font-family:'Poppins', sans-serif;">
{COMMON_DEFS}

  <!-- CADRE GLOBAL -->
  <rect x="10" y="10" width="1160" height="620" rx="14" fill="#FAFAFA" stroke="#E2E8F0" stroke-width="1.2" />

  <!-- EN-TETE BANDEAU -->
  <rect x="25" y="22" width="1130" height="42" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
  <rect x="35" y="32" width="22" height="22" rx="4" fill="#7C3AED" />
  <text x="46" y="47" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">RACI</text>
  <text x="68" y="46" font-size="13" font-weight="700" fill="#1E293B">Matrice des Responsabilités RACI &amp; Répartition des 6 Pôles d'Équipe</text>
  <text x="1140" y="46" text-anchor="end" font-size="11" font-weight="500" fill="#64748B">Gouvernance Agile sans Chef de Projet · 5 Étudiants-Ingénieurs · R1 à R5</text>

  <!-- LEGENDE RACI HORIZONTALE -->
  <g transform="translate(25, 76)">
    <rect x="0" y="0" width="1130" height="34" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
    <text x="18" y="22" font-size="10.5" font-weight="700" fill="#334155">Légende RACI :</text>
    
    <!-- R -->
    <rect x="135" y="7" width="20" height="20" rx="4" fill="#059669" />
    <text x="145" y="21" text-anchor="middle" font-size="10.5" font-weight="700" fill="#FFFFFF">R</text>
    <text x="162" y="21" font-size="10" font-weight="600" fill="#065F46">Réalisateur (Responsible)</text>

    <!-- A -->
    <rect x="345" y="7" width="20" height="20" rx="4" fill="#0284C7" />
    <text x="355" y="21" text-anchor="middle" font-size="10.5" font-weight="700" fill="#FFFFFF">A</text>
    <text x="372" y="21" font-size="10" font-weight="600" fill="#075985">Approbateur / Décideur (Accountable)</text>

    <!-- C -->
    <rect x="635" y="7" width="20" height="20" rx="4" fill="#D97706" />
    <text x="645" y="21" text-anchor="middle" font-size="10.5" font-weight="700" fill="#FFFFFF">C</text>
    <text x="662" y="21" font-size="10" font-weight="600" fill="#92400E">Consulté (Consulted)</text>

    <!-- I -->
    <rect x="835" y="7" width="20" height="20" rx="4" fill="#64748B" />
    <text x="845" y="21" text-anchor="middle" font-size="10.5" font-weight="700" fill="#FFFFFF">I</text>
    <text x="862" y="21" font-size="10" font-weight="600" fill="#334155">Informé (Informed)</text>
  </g>

  <!-- TABLEAU MATRICE RACI -->
  <g transform="translate(25, 122)" filter="url(#shadow-box)">
    <!-- FOND TABLEAU -->
    <rect x="0" y="0" width="1130" height="490" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2" />

    <!-- EN-TETE COLONNES -->
    <rect x="0" y="0" width="1130" height="46" rx="8" fill="#243342" />
    <rect x="0" y="20" width="1130" height="26" fill="#243342" />

    <text x="20" y="28" font-size="10.5" font-weight="700" fill="#FFFFFF">ACTIVITÉS MAJEURES &amp; LIVRABLES</text>
    <text x="445" y="21" text-anchor="middle" font-size="9.5" font-weight="700" fill="#93C5FD">MOA</text>
    <text x="445" y="34" text-anchor="middle" font-size="8" fill="#BFDBFE">Enseignants</text>

    <text x="545" y="21" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">SM</text>
    <text x="545" y="34" text-anchor="middle" font-size="8" fill="#CBD5E1">Scrum Tournant</text>

    <text x="645" y="21" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">QA</text>
    <text x="645" y="34" text-anchor="middle" font-size="8" fill="#CBD5E1">Qualité &amp; DoD</text>

    <text x="745" y="21" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">COM</text>
    <text x="745" y="34" text-anchor="middle" font-size="8" fill="#CBD5E1">Communication</text>

    <text x="845" y="21" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">DEVOPS</text>
    <text x="845" y="34" text-anchor="middle" font-size="8" fill="#CBD5E1">CI/CD &amp; Docker</text>

    <text x="955" y="21" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">ARC-BACK</text>
    <text x="955" y="34" text-anchor="middle" font-size="8" fill="#CBD5E1">Archi &amp; SQL</text>

    <text x="1065" y="21" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">ARC-FRONT</text>
    <text x="1065" y="34" text-anchor="middle" font-size="8" fill="#CBD5E1">UX &amp; Accessib.</text>

    <!-- LIGNES DE LA MATRICE (10 LIGNES) -->
    <!-- Ligne 1 : WP1 Cadrage & CDC R1 -->
    <rect x="0" y="46" width="1130" height="44" fill="#F8FAFC" />
    <line x1="0" y1="90" x2="1130" y2="90" stroke="#E2E8F0" stroke-width="1" />
    <text x="20" y="66" font-size="10" font-weight="700" fill="#1E293B">WP1 · Cadrage Stratégique &amp; Cahier des Charges (R1)</text>
    <text x="20" y="79" font-size="8.5" fill="#64748B">Expression des besoins, APTE, personas, BPMN, MCD Merise, C4, MoSCoW</text>
    <circle cx="445" cy="68" r="11" fill="#0284C7" /><text x="445" y="72" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">A</text>
    <circle cx="545" cy="68" r="11" fill="#059669" /><text x="545" y="72" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="645" cy="68" r="11" fill="#D97706" /><text x="645" y="72" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="745" cy="68" r="11" fill="#D97706" /><text x="745" y="72" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="845" cy="68" r="11" fill="#64748B" /><text x="845" y="72" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>
    <circle cx="955" cy="68" r="11" fill="#059669" /><text x="955" y="72" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="1065" cy="68" r="11" fill="#059669" /><text x="1065" y="72" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>

    <!-- Ligne 2 : WP2 Outils & Socle CI/CD R2 -->
    <rect x="0" y="90" width="1130" height="44" fill="#FFFFFF" />
    <line x1="0" y1="134" x2="1130" y2="134" stroke="#E2E8F0" stroke-width="1" />
    <text x="20" y="110" font-size="10" font-weight="700" fill="#1E293B">WP2 · Choix, Setup Outils &amp; Déploiement CI/CD (R2)</text>
    <text x="20" y="123" font-size="8.5" fill="#64748B">GitLab, branches protégées, GitLab CI, SonarQube, Docker multi-stage</text>
    <circle cx="445" cy="112" r="11" fill="#64748B" /><text x="445" y="116" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>
    <circle cx="545" cy="112" r="11" fill="#D97706" /><text x="545" y="116" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="645" cy="112" r="11" fill="#0284C7" /><text x="645" y="116" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">A</text>
    <circle cx="745" cy="112" r="11" fill="#64748B" /><text x="745" y="116" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>
    <circle cx="845" cy="112" r="11" fill="#059669" /><text x="845" y="116" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="955" cy="112" r="11" fill="#D97706" /><text x="955" y="116" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="1065" cy="112" r="11" fill="#64748B" /><text x="1065" y="116" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>

    <!-- Ligne 3 : WP3 Étude Économique R3 -->
    <rect x="0" y="134" width="1130" height="44" fill="#F8FAFC" />
    <line x1="0" y1="178" x2="1130" y2="178" stroke="#E2E8F0" stroke-width="1" />
    <text x="20" y="154" font-size="10" font-weight="700" fill="#1E293B">WP3 · Analyse Économique par Coûts Complets &amp; Rentabilité (R3)</text>
    <text x="20" y="167" font-size="8.5" fill="#64748B">Centres d'analyse Build/Run, Unités d'Œuvre, P&amp;L 3 ans, calcul ROI &amp; VAN</text>
    <circle cx="445" cy="156" r="11" fill="#0284C7" /><text x="445" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">A</text>
    <circle cx="545" cy="156" r="11" fill="#059669" /><text x="545" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="645" cy="156" r="11" fill="#D97706" /><text x="645" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="745" cy="156" r="11" fill="#D97706" /><text x="745" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="845" cy="156" r="11" fill="#64748B" /><text x="845" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>
    <circle cx="955" cy="156" r="11" fill="#D97706" /><text x="955" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="1065" cy="156" r="11" fill="#64748B" /><text x="1065" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>

    <!-- Ligne 4 : Conception Vues 4+1 R4 -->
    <rect x="0" y="178" width="1130" height="44" fill="#FFFFFF" />
    <line x1="0" y1="222" x2="1130" y2="222" stroke="#E2E8F0" stroke-width="1" />
    <text x="20" y="198" font-size="10" font-weight="700" fill="#1E293B">WP4.1 · Conception Détaillée des Vues 4+1 C4 (R4)</text>
    <text x="20" y="211" font-size="8.5" fill="#64748B">Diagrammes composants, classes métiers, modèle relationnel 3NF, déploiement</text>
    <circle cx="445" cy="200" r="11" fill="#D97706" /><text x="445" y="204" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="545" cy="200" r="11" fill="#64748B" /><text x="545" y="204" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>
    <circle cx="645" cy="200" r="11" fill="#D97706" /><text x="645" y="204" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="745" cy="200" r="11" fill="#64748B" /><text x="745" y="204" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>
    <circle cx="845" cy="200" r="11" fill="#D97706" /><text x="845" y="204" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="955" cy="200" r="11" fill="#0284C7" /><text x="955" y="204" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">A</text>
    <circle cx="1065" cy="200" r="11" fill="#059669" /><text x="1065" y="204" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>

    <!-- Ligne 5 : 1er Composant Logiciel R4 -->
    <rect x="0" y="222" width="1130" height="44" fill="#F8FAFC" />
    <line x1="0" y1="266" x2="1130" y2="266" stroke="#E2E8F0" stroke-width="1" />
    <text x="20" y="242" font-size="10" font-weight="700" fill="#1E293B">WP4.2 · Développement &amp; Test du 1er Composant Déployé (R4)</text>
    <text x="20" y="255" font-size="8.5" fill="#64748B">Panier mutualisé 2PC, persistance PostgreSQL, tests TDD, démo Docker</text>
    <circle cx="445" cy="244" r="11" fill="#0284C7" /><text x="445" y="248" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">A</text>
    <circle cx="545" cy="244" r="11" fill="#D97706" /><text x="545" y="248" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="645" cy="244" r="11" fill="#0284C7" /><text x="645" y="248" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">A</text>
    <circle cx="745" cy="244" r="11" fill="#64748B" /><text x="745" y="248" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>
    <circle cx="845" cy="244" r="11" fill="#059669" /><text x="845" y="248" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="955" cy="244" r="11" fill="#059669" /><text x="955" y="248" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="1065" cy="244" r="11" fill="#059669" /><text x="1065" y="248" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>

    <!-- Ligne 6 : Dév MVP V1 R5 -->
    <rect x="0" y="266" width="1130" height="44" fill="#FFFFFF" />
    <line x1="0" y1="310" x2="1130" y2="310" stroke="#E2E8F0" stroke-width="1" />
    <text x="20" y="286" font-size="10" font-weight="700" fill="#1E293B">WP5.1 · Implémentation du Backlog MVP V1 (10 US Must Have)</text>
    <text x="20" y="299" font-size="8.5" fill="#64748B">Vitrines, stocks V1, caisse express &lt; 3s, moteur VFP 15j, vouchers mobilité</text>
    <circle cx="445" cy="288" r="11" fill="#64748B" /><text x="445" y="292" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>
    <circle cx="545" cy="288" r="11" fill="#0284C7" /><text x="545" y="292" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">A</text>
    <circle cx="645" cy="288" r="11" fill="#D97706" /><text x="645" y="292" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="745" cy="288" r="11" fill="#64748B" /><text x="745" y="292" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>
    <circle cx="845" cy="288" r="11" fill="#D97706" /><text x="845" y="292" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="955" cy="288" r="11" fill="#059669" /><text x="955" y="292" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="1065" cy="288" r="11" fill="#059669" /><text x="1065" y="292" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>

    <!-- Ligne 7 : Intégration Mocks & APIs Partenaires -->
    <rect x="0" y="310" width="1130" height="44" fill="#F8FAFC" />
    <line x1="0" y1="354" x2="1130" y2="354" stroke="#E2E8F0" stroke-width="1" />
    <text x="20" y="330" font-size="10" font-weight="700" fill="#1E293B">WP5.2 · Intégration des Services Partenaires &amp; Mocks REST</text>
    <text x="20" y="343" font-size="8.5" fill="#64748B">Passerelle bancaire CB, API Ilévia Pass Pass, simulation voirie parking</text>
    <circle cx="445" cy="332" r="11" fill="#64748B" /><text x="445" y="336" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>
    <circle cx="545" cy="332" r="11" fill="#64748B" /><text x="545" y="336" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>
    <circle cx="645" cy="332" r="11" fill="#D97706" /><text x="645" y="336" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="745" cy="332" r="11" fill="#64748B" /><text x="745" y="336" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>
    <circle cx="845" cy="332" r="11" fill="#059669" /><text x="845" y="336" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="955" cy="332" r="11" fill="#059669" /><text x="955" y="336" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="1065" cy="332" r="11" fill="#D97706" /><text x="1065" y="336" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>

    <!-- Ligne 8 : Validation Qualité & DoD -->
    <rect x="0" y="354" width="1130" height="44" fill="#FFFFFF" />
    <line x1="0" y1="398" x2="1130" y2="398" stroke="#E2E8F0" stroke-width="1" />
    <text x="20" y="374" font-size="10" font-weight="700" fill="#1E293B">WP5.3 · Validation DoD, Qualité &amp; Non-Régression</text>
    <text x="20" y="387" font-size="8.5" fill="#64748B">Tests unitaires (couverture &gt;= 80%), SonarQube, verify_deliverables.py, zéro emoji</text>
    <circle cx="445" cy="376" r="11" fill="#64748B" /><text x="445" y="380" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>
    <circle cx="545" cy="376" r="11" fill="#D97706" /><text x="545" y="380" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="645" cy="376" r="11" fill="#0284C7" /><text x="645" y="380" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">A</text>
    <circle cx="745" cy="376" r="11" fill="#64748B" /><text x="745" y="380" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">I</text>
    <circle cx="845" cy="376" r="11" fill="#059669" /><text x="845" y="380" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="955" cy="376" r="11" fill="#059669" /><text x="955" y="380" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="1065" cy="376" r="11" fill="#059669" /><text x="1065" y="380" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>

    <!-- Ligne 9 : Déploiement & Solution Finale R5 -->
    <rect x="0" y="398" width="1130" height="44" fill="#F8FAFC" />
    <line x1="0" y1="442" x2="1130" y2="442" stroke="#E2E8F0" stroke-width="1" />
    <text x="20" y="418" font-size="10" font-weight="700" fill="#1E293B">WP5.4 · Packaging Démonstrateur Docker &amp; Solution Finale (R5)</text>
    <text x="20" y="431" font-size="8.5" fill="#64748B">Orchestration docker compose up -d, jeu d'essai Lille, notice d'installation</text>
    <circle cx="445" cy="420" r="11" fill="#0284C7" /><text x="445" y="424" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">A</text>
    <circle cx="545" cy="420" r="11" fill="#D97706" /><text x="545" y="424" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="645" cy="420" r="11" fill="#0284C7" /><text x="645" y="424" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">A</text>
    <circle cx="745" cy="420" r="11" fill="#D97706" /><text x="745" y="424" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="845" cy="420" r="11" fill="#059669" /><text x="845" y="424" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="955" cy="420" r="11" fill="#059669" /><text x="955" y="424" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="1065" cy="420" r="11" fill="#059669" /><text x="1065" y="424" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>

    <!-- Ligne 10 : Soutenances Orales & Clôture -->
    <rect x="0" y="442" width="1130" height="48" fill="#FFFFFF" />
    <text x="20" y="462" font-size="10" font-weight="700" fill="#1E293B">WP6 · Soutenances Orales, Support Client &amp; Bilan RSE</text>
    <text x="20" y="475" font-size="8.5" fill="#64748B">Présentations amphi Turing (R1, R4, R5), documentation projet, site web</text>
    <circle cx="445" cy="466" r="11" fill="#0284C7" /><text x="445" y="470" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">A</text>
    <circle cx="545" cy="466" r="11" fill="#059669" /><text x="545" y="470" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="645" cy="466" r="11" fill="#D97706" /><text x="645" y="470" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="745" cy="466" r="11" fill="#059669" /><text x="745" y="470" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">R</text>
    <circle cx="845" cy="466" r="11" fill="#D97706" /><text x="845" y="470" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="955" cy="466" r="11" fill="#D97706" /><text x="955" y="470" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
    <circle cx="1065" cy="466" r="11" fill="#D97706" /><text x="1065" y="470" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">C</text>
  </g>

</svg>"""

# ==============================================================================
# FIGURE 8.3 : DIAGRAMME DE GANTT ANNUEL & JALONS CONTRACTUELS (1180 x 720)
# ==============================================================================
def generate_gantt_svg():
    return f"""<svg viewBox="0 0 1180 720" width="1180" height="720" style="overflow:visible; font-family:'Poppins', sans-serif;">
{COMMON_DEFS}

  <!-- CADRE GLOBAL -->
  <rect x="10" y="10" width="1160" height="700" rx="14" fill="#FAFAFA" stroke="#E2E8F0" stroke-width="1.2" />

  <!-- EN-TETE BANDEAU -->
  <rect x="25" y="22" width="1130" height="42" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
  <rect x="35" y="32" width="22" height="22" rx="4" fill="#059669" />
  <text x="46" y="47" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">GNT</text>
  <text x="68" y="46" font-size="13" font-weight="700" fill="#1E293B">Diagramme de Gantt Annuel &amp; Jalons Contractuels R1 à R5 (2026-2027)</text>
  <text x="1140" y="46" text-anchor="end" font-size="11" font-weight="500" fill="#64748B">Master 2 MIAGE · Chemin Critique &amp; Rendu des Livrables · Semestres S3 &amp; S4</text>

  <!-- ZONE DE CHRONOLOGIE (GANTT CHART) -->
  <g transform="translate(25, 78)" filter="url(#shadow-box)">
    <rect x="0" y="0" width="1130" height="616" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2" />

    <!-- EN-TETE CALENDRIER : MOIS DE L'ANNÉE (7 MOIS) -->
    <!-- Largeur dispo pour le planning = 860px (de x=270 à x=1130) -->
    
    <!-- Colonne des tâches (gauche) -->
    <rect x="0" y="0" width="270" height="50" rx="8" fill="#243342" />
    <rect x="0" y="25" width="270" height="25" fill="#243342" />
    <text x="20" y="30" font-size="11" font-weight="700" fill="#FFFFFF">SPRINTS &amp; TÂCHES CRITIQUES</text>

    <!-- Mois 1 : Septembre 2026 (x=270 à 392) -->
    <rect x="270" y="0" width="123" height="50" fill="#1E293B" stroke="#334155" stroke-width="0.8" />
    <text x="331" y="24" text-anchor="middle" font-size="10.5" font-weight="700" fill="#FFFFFF">SEPT. 2026</text>
    <text x="331" y="38" text-anchor="middle" font-size="8" fill="#94A3B8">S01 - S04 (R1)</text>

    <!-- Mois 2 : Octobre 2026 (x=393 à 516) -->
    <rect x="393" y="0" width="123" height="50" fill="#1E293B" stroke="#334155" stroke-width="0.8" />
    <text x="454" y="24" text-anchor="middle" font-size="10.5" font-weight="700" fill="#FFFFFF">OCT. 2026</text>
    <text x="454" y="38" text-anchor="middle" font-size="8" fill="#94A3B8">S05 - S08 (R2)</text>

    <!-- Mois 3 : Novembre 2026 (x=516 à 639) -->
    <rect x="516" y="0" width="123" height="50" fill="#1E293B" stroke="#334155" stroke-width="0.8" />
    <text x="577" y="24" text-anchor="middle" font-size="10.5" font-weight="700" fill="#FFFFFF">NOV. 2026</text>
    <text x="577" y="38" text-anchor="middle" font-size="8" fill="#94A3B8">S09 - S13 (R3)</text>

    <!-- Mois 4 : Décembre 2026 (x=639 à 762) -->
    <rect x="639" y="0" width="123" height="50" fill="#1E293B" stroke="#334155" stroke-width="0.8" />
    <text x="700" y="24" text-anchor="middle" font-size="10.5" font-weight="700" fill="#FFFFFF">DÉC. 2026</text>
    <text x="700" y="38" text-anchor="middle" font-size="8" fill="#94A3B8">S14 - S16 (R4)</text>

    <!-- Mois 5 : Janvier 2027 (x=762 à 885) -->
    <rect x="762" y="0" width="123" height="50" fill="#1E293B" stroke="#334155" stroke-width="0.8" />
    <text x="823" y="24" text-anchor="middle" font-size="10.5" font-weight="700" fill="#FFFFFF">JANV. 2027</text>
    <text x="823" y="38" text-anchor="middle" font-size="8" fill="#94A3B8">S17 - S20</text>

    <!-- Mois 6 : Février 2027 (x=885 à 1008) -->
    <rect x="885" y="0" width="123" height="50" fill="#1E293B" stroke="#334155" stroke-width="0.8" />
    <text x="946" y="24" text-anchor="middle" font-size="10.5" font-weight="700" fill="#FFFFFF">FÉVR. 2027</text>
    <text x="946" y="38" text-anchor="middle" font-size="8" fill="#94A3B8">S21 - S24</text>

    <!-- Mois 7 : Mars 2027 (x=1008 à 1130) -->
    <rect x="1008" y="0" width="122" height="50" rx="8" fill="#1E293B" />
    <rect x="1008" y="0" width="20" height="50" fill="#1E293B" />
    <text x="1069" y="24" text-anchor="middle" font-size="10.5" font-weight="700" fill="#FFFFFF">MARS 2027</text>
    <text x="1069" y="38" text-anchor="middle" font-size="8" fill="#94A3B8">S25 - S27 (R5)</text>

    <!-- LIGNES VERTICALES DE MOIS -->
    <line x1="270" y1="50" x2="270" y2="616" stroke="#E2E8F0" stroke-width="1.5" />
    <line x1="393" y1="50" x2="393" y2="616" stroke="#E2E8F0" stroke-width="1" />
    <line x1="516" y1="50" x2="516" y2="616" stroke="#E2E8F0" stroke-width="1" />
    <line x1="639" y1="50" x2="639" y2="616" stroke="#E2E8F0" stroke-width="1" />
    <line x1="762" y1="50" x2="762" y2="616" stroke="#E2E8F0" stroke-width="1" />
    <line x1="885" y1="50" x2="885" y2="616" stroke="#E2E8F0" stroke-width="1" />
    <line x1="1008" y1="50" x2="1008" y2="616" stroke="#E2E8F0" stroke-width="1" />

    <!-- ZONES BANALISÉES / VACANCES (Hachures douces limitées au graphique) -->
    <!-- Semaine IA : 19/10 - 25/10 -->
    <rect x="468" y="50" width="25" height="386" fill="#FEF3C7" opacity="0.4" />

    <!-- Vacances Toussaint : 26/10 - 01/11 -->
    <rect x="495" y="50" width="25" height="386" fill="#F1F5F9" opacity="0.7" />

    <!-- Vacances Noël : 21/12 - 03/01 -->
    <rect x="722" y="50" width="48" height="386" fill="#F1F5F9" opacity="0.7" />

    <!-- Vacances Hiver : 01/03 - 07/03 -->
    <rect x="1008" y="50" width="28" height="386" fill="#F1F5F9" opacity="0.7" />

    <!-- ======================================================== -->
    <!-- BARRES DE TÂCHES / SPRINTS GANTT                         -->
    <!-- ======================================================== -->

    <!-- TÂCHE 1 : SPRINT 0 - CADRAGE STRATÉGIQUE & CDC R1 -->
    <rect x="0" y="55" width="270" height="42" fill="#F8FAFC" />
    <text x="15" y="73" font-size="9.5" font-weight="700" fill="#0369A1">Sprint 0 · Cadrage &amp; CDC (R1)</text>
    <text x="15" y="86" font-size="8" fill="#64748B">Analyse APTE, BPMN, MCD, MoSCoW</text>
    <rect x="278" y="63" width="66" height="24" rx="4" fill="#0284C7" stroke="#0369A1" stroke-width="1.2" />
    <text x="311" y="79" text-anchor="middle" font-size="8.5" font-weight="700" fill="#FFFFFF">Sprint 0 (3 sem.)</text>
    <path d="M 344 60 L 350 75 L 344 90 L 338 75 Z" fill="#DC2626" />
    <text x="356" y="73" font-size="8" font-weight="700" fill="#DC2626">R1 (18/09)</text>
    <text x="356" y="83" font-size="7.5" fill="#475569">Oral 21/09</text>

    <!-- TÂCHE 2 : SPRINT 1 - SOCLE OUTILLAGE & CI/CD R2 -->
    <rect x="0" y="102" width="270" height="42" fill="#FFFFFF" />
    <text x="15" y="120" font-size="9.5" font-weight="700" fill="#C2410C">Sprint 1 · Outils &amp; DevOps (R2)</text>
    <text x="15" y="133" font-size="8" fill="#64748B">GitLab CI, SonarQube, Docker</text>
    <rect x="358" y="110" width="82" height="24" rx="4" fill="#EA580C" stroke="#C2410C" stroke-width="1.2" />
    <text x="399" y="126" text-anchor="middle" font-size="8.5" font-weight="700" fill="#FFFFFF">Sprint 1 (3 sem.)</text>
    <path d="M 440 107 L 446 122 L 440 137 L 434 122 Z" fill="#EA580C" />
    <text x="452" y="124" font-size="8" font-weight="700" fill="#EA580C">R2 (12/10)</text>

    <!-- TÂCHE 3 : SPRINT 2 - ANALYSE FINANCIÈRE R3 -->
    <rect x="0" y="149" width="270" height="42" fill="#F8FAFC" />
    <text x="15" y="167" font-size="9.5" font-weight="700" fill="#A16207">Sprint 2 · Économie &amp; ROI (R3)</text>
    <text x="15" y="180" font-size="8" fill="#64748B">Coûts complets, P&amp;L 3 ans, VAN</text>
    <rect x="444" y="157" width="191" height="24" rx="4" fill="#CA8A04" stroke="#A16207" stroke-width="1.2" />
    <text x="539" y="173" text-anchor="middle" font-size="8.5" font-weight="700" fill="#FFFFFF">Sprint 2 · Étude Financière R3 (7 sem.)</text>
    <path d="M 635 154 L 641 169 L 635 184 L 629 169 Z" fill="#CA8A04" />
    <text x="647" y="171" font-size="8" font-weight="700" fill="#CA8A04">R3 (30/11)</text>

    <!-- TÂCHE 4 : SPRINT 3 - ARCHITECTURE C4 & 1ER COMPOSANT R4 -->
    <rect x="0" y="196" width="270" height="42" fill="#FFFFFF" />
    <text x="15" y="214" font-size="9.5" font-weight="700" fill="#6D28D9">Sprint 3 · Archi C4 &amp; Proto (R4)</text>
    <text x="15" y="227" font-size="8" fill="#64748B">Vues 4+1, SQL 3NF, Panier 2PC</text>
    <rect x="444" y="204" width="266" height="24" rx="4" fill="#7C3AED" stroke="#6D28D9" stroke-width="1.2" />
    <text x="577" y="220" text-anchor="middle" font-size="8.5" font-weight="700" fill="#FFFFFF">Sprint 3 · Archi Détaillée &amp; 1er Composant 2PC (9 sem.)</text>
    <path d="M 710 201 L 716 216 L 710 231 L 704 216 Z" fill="#DC2626" />
    <text x="722" y="214" font-size="8" font-weight="700" fill="#DC2626">R4 (18/12)</text>
    <text x="722" y="224" font-size="7.5" fill="#475569">Oral 04/01</text>

    <!-- TÂCHE 5 : SPRINT 4 - DÉVELOPPEMENT CŒUR MVP & FIDÉLITÉ -->
    <rect x="0" y="243" width="270" height="42" fill="#F8FAFC" />
    <text x="15" y="261" font-size="9.5" font-weight="700" fill="#047857">Sprint 4 · Cœur MVP &amp; Caisse</text>
    <text x="15" y="274" font-size="8" fill="#64748B">US Must Have, Scan &lt; 3s, VFP 15j</text>
    <rect x="780" y="251" width="102" height="24" rx="4" fill="#059669" stroke="#047857" stroke-width="1.2" />
    <text x="831" y="267" text-anchor="middle" font-size="8.5" font-weight="700" fill="#FFFFFF">Sprint 4 (4 sem.)</text>

    <!-- TÂCHE 6 : SPRINT 5 - FRONTEND, MOCKS & MOBILITÉ -->
    <rect x="0" y="290" width="270" height="42" fill="#FFFFFF" />
    <text x="15" y="308" font-size="9.5" font-weight="700" fill="#047857">Sprint 5 · Front, Mocks &amp; Titres</text>
    <text x="15" y="321" font-size="8" fill="#64748B">SPA responsive, Bus/Parking PassPass</text>
    <rect x="885" y="298" width="80" height="24" rx="4" fill="#059669" stroke="#047857" stroke-width="1.2" />
    <text x="925" y="314" text-anchor="middle" font-size="8.5" font-weight="700" fill="#FFFFFF">Sprint 5 (3 sem.)</text>

    <!-- TÂCHE 7 : SPRINT 6 - TESTS CHARGE & DÉPLOIEMENT R5 -->
    <rect x="0" y="337" width="270" height="42" fill="#F8FAFC" />
    <text x="15" y="355" font-size="9.5" font-weight="700" fill="#047857">Sprint 6 · Tests &amp; Release R5</text>
    <text x="15" y="368" font-size="8" fill="#64748B">Homologation, Docker clé en main</text>
    <rect x="965" y="345" width="115" height="24" rx="4" fill="#059669" stroke="#047857" stroke-width="1.2" />
    <text x="1022" y="361" text-anchor="middle" font-size="8.5" font-weight="700" fill="#FFFFFF">Sprint 6 (4 sem.)</text>
    <path d="M 1080 342 L 1086 357 L 1080 372 L 1074 357 Z" fill="#DC2626" />
    <text x="1035" y="335" font-size="8" font-weight="700" fill="#DC2626">R5 (19/03)</text>
    <text x="1035" y="344" font-size="7.5" fill="#475569">Oral 22/03</text>

    <!-- TÂCHE 8 : ASSURANCE QUALITÉ & AUDITS TRANSVERSES -->
    <rect x="0" y="384" width="270" height="42" fill="#FFFFFF" />
    <text x="15" y="402" font-size="9.5" font-weight="700" fill="#334155">QA Transverse &amp; Audit DoD</text>
    <text x="15" y="415" font-size="8" fill="#64748B">SonarQube, verify_deliverables, RGAA</text>
    <rect x="278" y="392" width="802" height="20" rx="4" fill="#F1F5F9" stroke="#94A3B8" stroke-dasharray="4,4" />
    <text x="679" y="406" text-anchor="middle" font-size="8.5" font-weight="600" fill="#475569">Supervision Qualité Continue &amp; Contrôles de Sécurité Permanents (DoD)</text>

    <!-- TRACÉ DU CHEMIN CRITIQUE -->
    <path d="M 344 75 L 358 122" stroke="#DC2626" stroke-width="1.8" stroke-dasharray="3,2" fill="none" marker-end="url(#arrow-red)" />
    <path d="M 440 122 L 444 216" stroke="#DC2626" stroke-width="1.8" stroke-dasharray="3,2" fill="none" marker-end="url(#arrow-red)" />
    <path d="M 710 216 L 780 263" stroke="#DC2626" stroke-width="1.8" stroke-dasharray="3,2" fill="none" marker-end="url(#arrow-red)" />
    <path d="M 882 263 L 885 310" stroke="#DC2626" stroke-width="1.8" stroke-dasharray="3,2" fill="none" marker-end="url(#arrow-red)" />
    <path d="M 965 310 L 965 357" stroke="#DC2626" stroke-width="1.8" stroke-dasharray="3,2" fill="none" marker-end="url(#arrow-red)" />

    <!-- ENCART INFORMATIF : TABLEAU DES 5 JALONS ACADÉMIQUES -->
    <g transform="translate(15, 436)">
      <rect x="0" y="0" width="1100" height="168" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1" />
      <rect x="0" y="0" width="1100" height="28" rx="8" fill="#334155" />
      <rect x="0" y="15" width="1100" height="13" fill="#334155" />
      <text x="15" y="19" font-size="9.5" font-weight="700" fill="#FFFFFF">RÉCAPITULATIF DES JALONS CONTRACTUELS DE L'ANNÉE UNIVERSITAIRE (CONSIGNES ÉVALUÉES)</text>
      
      <!-- R1 -->
      <rect x="12" y="36" width="206" height="120" rx="6" fill="#FFFFFF" stroke="#BAE6FD" stroke-width="1" />
      <rect x="12" y="36" width="206" height="24" rx="6" fill="#E0F2FE" />
      <text x="22" y="52" font-size="9.5" font-weight="700" fill="#0369A1">JALON R1 · CADRAGE</text>
      <text x="22" y="72" font-size="8.5" font-weight="700" fill="#1E293B">Rendu : 18/09/2026 (18h)</text>
      <text x="22" y="85" font-size="8" font-weight="600" fill="#0284C7">Soutenance : 21/09 (Amphi)</text>
      <text x="22" y="100" font-size="8" fill="#475569">Cahier des Charges complet</text>
      <text x="22" y="112" font-size="8" fill="#475569">Grille MoSCoW, BPMN, MCD</text>
      <text x="22" y="124" font-size="8" fill="#475569">Matrice RACI, WBS &amp; Gantt</text>
      <text x="22" y="142" font-size="7.5" font-weight="600" fill="#DC2626">Chemin critique : OUI</text>

      <!-- R2 -->
      <rect x="230" y="36" width="206" height="120" rx="6" fill="#FFFFFF" stroke="#FED7AA" stroke-width="1" />
      <rect x="230" y="36" width="206" height="24" rx="6" fill="#FFEDD5" />
      <text x="240" y="52" font-size="9.5" font-weight="700" fill="#C2410C">JALON R2 · OUTILLAGE</text>
      <text x="240" y="72" font-size="8.5" font-weight="700" fill="#1E293B">Rendu : 12/10/2026</text>
      <text x="240" y="85" font-size="8" font-weight="600" fill="#EA580C">Pas de soutenance orale</text>
      <text x="240" y="100" font-size="8" fill="#475569">Dépôt GitLab &amp; branches</text>
      <text x="240" y="112" font-size="8" fill="#475569">Pipeline CI/CD SonarQube</text>
      <text x="240" y="124" font-size="8" fill="#475569">Socle Docker Compose</text>
      <text x="240" y="142" font-size="7.5" font-weight="600" fill="#DC2626">Chemin critique : OUI</text>

      <!-- R3 -->
      <rect x="448" y="36" width="206" height="120" rx="6" fill="#FFFFFF" stroke="#FEF08A" stroke-width="1" />
      <rect x="448" y="36" width="206" height="24" rx="6" fill="#FEF9C3" />
      <text x="458" y="52" font-size="9.5" font-weight="700" fill="#A16207">JALON R3 · ÉCONOMIE</text>
      <text x="458" y="72" font-size="8.5" font-weight="700" fill="#1E293B">Rendu : 30/11/2026</text>
      <text x="458" y="85" font-size="8" font-weight="600" fill="#CA8A04">Pas de soutenance orale</text>
      <text x="458" y="100" font-size="8" fill="#475569">Méthode Coûts Complets</text>
      <text x="458" y="112" font-size="8" fill="#475569">Unités d'Œuvre &amp; P&amp;L 3 ans</text>
      <text x="458" y="124" font-size="8" fill="#475569">Calcul ROI &amp; VAN actualisée</text>
      <text x="458" y="142" font-size="7.5" font-weight="600" fill="#64748B">Chemin critique : Non (marge 3j)</text>

      <!-- R4 -->
      <rect x="666" y="36" width="206" height="120" rx="6" fill="#FFFFFF" stroke="#DDD6FE" stroke-width="1" />
      <rect x="666" y="36" width="206" height="24" rx="6" fill="#EDE9FE" />
      <text x="676" y="52" font-size="9.5" font-weight="700" fill="#6D28D9">JALON R4 · ARCHITECTURE</text>
      <text x="676" y="72" font-size="8.5" font-weight="700" fill="#1E293B">Rendu : 18/12/2026 (18h)</text>
      <text x="676" y="85" font-size="8" font-weight="600" fill="#7C3AED">Soutenance : 04/01/2027</text>
      <text x="676" y="100" font-size="8" fill="#475569">Vues 4+1 C4 complètes</text>
      <text x="676" y="112" font-size="8" fill="#475569">1er composant déployé (2PC)</text>
      <text x="676" y="124" font-size="8" fill="#475569">Pitch valeur &amp; posture RSE</text>
      <text x="676" y="142" font-size="7.5" font-weight="600" fill="#DC2626">Chemin critique : OUI</text>

      <!-- R5 -->
      <rect x="884" y="36" width="204" height="120" rx="6" fill="#FFFFFF" stroke="#A7F3D0" stroke-width="1" />
      <rect x="884" y="36" width="204" height="24" rx="6" fill="#D1FAE5" />
      <text x="894" y="52" font-size="9.5" font-weight="700" fill="#047857">JALON R5 · FINAL</text>
      <text x="894" y="72" font-size="8.5" font-weight="700" fill="#1E293B">Rendu : 19/03/2027 (18h)</text>
      <text x="894" y="85" font-size="8" font-weight="600" fill="#059669">Soutenance : 22/03/2027</text>
      <text x="894" y="100" font-size="8" fill="#475569">Solution intégrale déployée</text>
      <text x="894" y="112" font-size="8" fill="#475569">Démonstrateur opérationnel</text>
      <text x="894" y="124" font-size="8" fill="#475569">Audit accessibilité &amp; RGPD</text>
      <text x="894" y="142" font-size="7.5" font-weight="600" fill="#DC2626">Chemin critique : OUI</text>
    </g>

  </g>

</svg>"""

def export_png(svg_content, width, height, output_png):
    # Sauvegarde du fichier SVG source
    svg_path = output_png.replace(".png", ".svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    try:
        import pymupdf
        doc = pymupdf.open(stream=svg_content.encode("utf-8"), filetype="svg")
        page = doc[0]
        # Rendu haute définition (facteur d'échelle 2.0 pour netteté d'impression)
        mat = pymupdf.Matrix(2.0, 2.0)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        pix.save(output_png)
        print(f"Exporté avec succès (PyMuPDF HD) : {output_png} ({pix.width}x{pix.height})")
    except Exception as e:
        print(f"Erreur PyMuPDF : {e}, tentative de fallback...")
        raise

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    figures_dir = os.path.join(repo_root, "agent_projet/docs/01_Cadrage_Et_Cahier_Des_Charges_R1/figures")
    components_dir = os.path.join(repo_root, "agent_projet/templates/components")
    os.makedirs(figures_dir, exist_ok=True)
    os.makedirs(components_dir, exist_ok=True)

    # 1. Génération WBS (Figure 8.1)
    svg_wbs = generate_wbs_svg()
    png_wbs = os.path.join(figures_dir, "fig_8_1_wbs_lots_travaux.png")
    export_png(svg_wbs, 1180, 680, png_wbs)

    # 2. Génération RACI (Figure 8.2)
    svg_raci = generate_raci_svg()
    png_raci = os.path.join(figures_dir, "fig_8_2_matrice_raci.png")
    export_png(svg_raci, 1180, 640, png_raci)

    # 3. Génération Gantt (Figure 8.3)
    svg_gantt = generate_gantt_svg()
    png_gantt = os.path.join(figures_dir, "fig_8_3_gantt_jalons_r1_r5.png")
    export_png(svg_gantt, 1180, 720, png_gantt)

    # 4. Sauvegarde composant HTML unifié
    comp_html_path = os.path.join(components_dir, "gouvernance_views.html")
    comp_content = f"""<!-- FIGURE 8.1, 8.2 & 8.3 : SCHÉMAS DE GOUVERNANCE ET PLANNING SHOPLOC -->
<div class="figure-card" style="background:#FFFFFF; border:1px solid #E8E6DF; border-radius:16px; padding:24px; margin-bottom:28px; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px; border-bottom:1px solid #E8E6DF; padding-bottom:12px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#0284C7;"></span>
        <span style="font-size:11px; font-weight:700; color:#0284C7; text-transform:uppercase; letter-spacing:0.08em;">Work Breakdown Structure</span>
      </div>
      <h3 style="font-size:17px; font-weight:700; color:#243342; margin:0;">Figure 8.1 — Organigramme des Tâches Projet (WBS par Lots de Travaux)</h3>
    </div>
    <span style="font-size:11px; background:#FAF9F6; border:1px solid #E8E6DF; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600;">Lots WP1 à WP6 · Démarche Arborescence Inversée</span>
  </div>
{svg_wbs}
</div>

<div class="figure-card" style="background:#FFFFFF; border:1px solid #E8E6DF; border-radius:16px; padding:24px; margin-bottom:28px; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px; border-bottom:1px solid #E8E6DF; padding-bottom:12px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#7C3AED;"></span>
        <span style="font-size:11px; font-weight:700; color:#7C3AED; text-transform:uppercase; letter-spacing:0.08em;">Matrice des Responsabilités</span>
      </div>
      <h3 style="font-size:17px; font-weight:700; color:#243342; margin:0;">Figure 8.2 — Matrice des Responsabilités RACI (6 Pôles d'Équipe &amp; MOA)</h3>
    </div>
    <span style="font-size:11px; background:#FAF9F6; border:1px solid #E8E6DF; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600;">Scrum Master Tournant · Aucun Chef de Projet Unique</span>
  </div>
{svg_raci}
</div>

<div class="figure-card" style="background:#FFFFFF; border:1px solid #E8E6DF; border-radius:16px; padding:24px; margin-bottom:28px; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px; border-bottom:1px solid #E8E6DF; padding-bottom:12px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#059669;"></span>
        <span style="font-size:11px; font-weight:700; color:#059669; text-transform:uppercase; letter-spacing:0.08em;">Chronogramme Annuel</span>
      </div>
      <h3 style="font-size:17px; font-weight:700; color:#243342; margin:0;">Figure 8.3 — Diagramme de Gantt Annuel &amp; Jalons Contractuels R1 à R5</h3>
    </div>
    <span style="font-size:11px; background:#FAF9F6; border:1px solid #E8E6DF; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600;">Chemin Critique · Septembre 2026 à Mars 2027</span>
  </div>
{svg_gantt}
</div>
"""
    with open(comp_html_path, "w", encoding="utf-8") as f:
        f.write(comp_content)
    print(f"Composant HTML écrit : {comp_html_path}")
    print("Génération de la gouvernance terminée avec succès !")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GÉNÉRATEUR DE SCHÉMAS D'ARCHITECTURE C4 SHOPLOC (FIGURES 7.1 ET 7.2)
Master 2 MIAGE — Université de Lille — UE GLOP (2026-2027)

Génère deux schémas d'architecture vectoriels conformes au standard C4 Model :
- Figure 7.1 : Diagramme C4 Niveau 1 — Contexte Système (C4 Context)
- Figure 7.2 : Diagramme C4 Niveau 2 — Conteneurs & Monolithe Modulaire Docker (C4 Container)
Conformité stricte à la charte graphique pastel ShopLoc (ADR-014, ADR-015), sans emoji.
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
    <marker id="arrow-purple" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#7C3AED" />
    </marker>
    <marker id="arrow-emerald" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#059669" />
    </marker>
  </defs>
"""

# ==============================================================================
# FIGURE 7.1 : DIAGRAMME C4 NIVEAU 1 — CONTEXTE SYSTÈME
# ==============================================================================
def generate_c4_context_svg():
    return f"""<svg viewBox="0 0 1180 700" width="100%" height="auto" style="overflow:visible; font-family:'Poppins', sans-serif;">
{COMMON_DEFS}

  <!-- CADRE GLOBAL CONTEXTE -->
  <rect x="10" y="10" width="1160" height="680" rx="14" fill="#FAFAFA" stroke="#E2E8F0" stroke-width="1.2" />

  <!-- EN-TETE BANDEAU -->
  <rect x="25" y="22" width="1130" height="42" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
  <rect x="35" y="32" width="22" height="22" rx="4" fill="#0284C7" />
  <text x="46" y="47" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">C4</text>
  <text x="68" y="46" font-size="13" font-weight="700" fill="#1E293B">Système ShopLoc — Diagramme de Contexte (Niveau 1)</text>
  <text x="1140" y="46" text-anchor="end" font-size="11" font-weight="500" fill="#64748B">Frontière Métier &amp; Écosystème Partenaires · ADR-004, ADR-012</text>

  <!-- ======================================================== -->
  <!-- 1. ACTEURS (PERSONAS SHOPLOC) - GAUCHE                   -->
  <!-- ======================================================== -->
  
  <!-- Cadre groupement Acteurs -->
  <rect x="25" y="80" width="250" height="590" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-dasharray="4,3" stroke-width="1.2" />
  <text x="40" y="104" font-size="11" font-weight="700" fill="#475569" letter-spacing="0.05em">UTILISATEURS CIBLES</text>

  <!-- Acteur 1 : Pierre (Senior) -->
  <g filter="url(#shadow-card)">
    <rect x="38" y="118" width="224" height="118" rx="8" fill="#FFFFFF" stroke="#BAE6FD" stroke-width="1.3" />
    <rect x="48" y="128" width="56" height="18" rx="4" fill="#E0F2FE" />
    <text x="76" y="141" text-anchor="middle" font-size="9" font-weight="700" fill="#0369A1">PERSONA</text>
    <text x="112" y="141" font-size="12" font-weight="700" fill="#0F172A">Pierre (74 ans)</text>
    <text x="48" y="162" font-size="9.5" font-weight="600" fill="#0284C7">Citoyen &amp; Retraité local</text>
    <text x="48" y="180" font-size="8.5" font-weight="400" fill="#475569">Consulte les vitrines, présente</text>
    <text x="48" y="194" font-size="8.5" font-weight="400" fill="#475569">son pass QR papier en caisse et</text>
    <text x="48" y="208" font-size="8.5" font-weight="400" fill="#475569">obtient des tickets de bus offerts.</text>
  </g>

  <!-- Acteur 2 : Julie & Arthur (Actifs) -->
  <g filter="url(#shadow-card)">
    <rect x="38" y="252" width="224" height="122" rx="8" fill="#FFFFFF" stroke="#DDD6FE" stroke-width="1.3" />
    <rect x="48" y="262" width="56" height="18" rx="4" fill="#EDE9FE" />
    <text x="76" y="275" text-anchor="middle" font-size="9" font-weight="700" fill="#6D28D9">PERSONA</text>
    <text x="112" y="275" font-size="12" font-weight="700" fill="#0F172A">Julie &amp; Arthur</text>
    <text x="48" y="296" font-size="9.5" font-weight="600" fill="#7C3AED">Consommateurs actifs</text>
    <text x="48" y="314" font-size="8.5" font-weight="400" fill="#475569">Commandent en Click &amp; Collect</text>
    <text x="48" y="328" font-size="8.5" font-weight="400" fill="#475569">avec panier mutualisé 2PC, et</text>
    <text x="48" y="342" font-size="8.5" font-weight="400" fill="#475569">activent le parking gratuit 20 min.</text>
  </g>

  <!-- Acteur 3 : Suzanne (Commerçante) -->
  <g filter="url(#shadow-card)">
    <rect x="38" y="390" width="224" height="122" rx="8" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1.3" />
    <rect x="48" y="400" width="56" height="18" rx="4" fill="#DCFCE7" />
    <text x="76" y="413" text-anchor="middle" font-size="9" font-weight="700" fill="#15803D">PERSONA</text>
    <text x="112" y="413" font-size="12" font-weight="700" fill="#0F172A">Suzanne (22 ans)</text>
    <text x="48" y="434" font-size="9.5" font-weight="600" fill="#16A34A">Commerçante &amp; Artisan</text>
    <text x="48" y="452" font-size="8.5" font-weight="400" fill="#475569">Gère son stock en ligne, scanne</text>
    <text x="48" y="466" font-size="8.5" font-weight="400" fill="#475569">les pass caisse en moins de 3s et</text>
    <text x="48" y="480" font-size="8.5" font-weight="400" fill="#475569">valide les retraits de commandes.</text>
  </g>

  <!-- Acteur 4 : Marius & Super-Admin (Collectivité) -->
  <g filter="url(#shadow-card)">
    <rect x="38" y="528" width="224" height="124" rx="8" fill="#FFFFFF" stroke="#FED7AA" stroke-width="1.3" />
    <rect x="48" y="538" width="56" height="18" rx="4" fill="#FFEDD5" />
    <text x="76" y="551" text-anchor="middle" font-size="9" font-weight="700" fill="#C2410C">PERSONA</text>
    <text x="112" y="551" font-size="12" font-weight="700" fill="#0F172A">Marius &amp; DSI Mairie</text>
    <text x="48" y="572" font-size="9.5" font-weight="600" fill="#EA580C">Collectivité Territoriale</text>
    <text x="48" y="590" font-size="8.5" font-weight="400" fill="#475569">Supervise les KPIs communaux,</text>
    <text x="48" y="604" font-size="8.5" font-weight="400" fill="#475569">compense le budget mobilité et</text>
    <text x="48" y="618" font-size="8.5" font-weight="400" fill="#475569">administre les conventions locales.</text>
  </g>

  <!-- ======================================================== -->
  <!-- 2. SYSTEME CENTRAL : SHOPLOC CORE (C4 CONTEXT)          -->
  <!-- ======================================================== -->
  
  <g filter="url(#shadow-card)">
    <!-- Conteneur Système Principal -->
    <rect x="345" y="118" width="460" height="534" rx="12" fill="#FFFFFF" stroke="#0284C7" stroke-width="2" />
    
    <!-- Bandeau titre Système -->
    <rect x="345" y="118" width="460" height="52" rx="12" fill="#F0F9FF" />
    <rect x="345" y="156" width="460" height="14" fill="#F0F9FF" />
    <text x="575" y="142" text-anchor="middle" font-size="14" font-weight="700" fill="#0369A1">SYSTÈME SHOPLOC CORE</text>
    <text x="575" y="159" text-anchor="middle" font-size="10" font-weight="600" fill="#0284C7">[Logiciel SaaS Multi-Tenant Mutualisé — ADR-004 / ADR-012]</text>

    <!-- Description Système -->
    <rect x="365" y="182" width="420" height="74" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1" />
    <text x="375" y="202" font-size="9.5" font-weight="600" fill="#334155">Plateforme territoriale de revitalisation commerciale &amp; civique</text>
    <text x="375" y="220" font-size="8.5" font-weight="400" fill="#64748B">Centralise les catalogues marchands de centre-ville, orchestre les commandes</text>
    <text x="375" y="234" font-size="8.5" font-weight="400" fill="#64748B">multi-boutiques sous protocole Two-Phase Commit (2PC), gère le double moteur</text>
    <text x="375" y="248" font-size="8.5" font-weight="400" fill="#64748B">de fidélité (points artisans + VFP glissant 15j) et génère les titres de mobilité.</text>

    <!-- Blocs Fonctionnels Internes Découpés -->
    <!-- Bloc F1 : Marketplace & C&C 2PC -->
    <rect x="365" y="270" width="200" height="85" rx="6" fill="#FAF5FF" stroke="#DDD6FE" stroke-width="1" />
    <text x="375" y="288" font-size="10" font-weight="700" fill="#6D28D9">Marketplace Click &amp; Collect</text>
    <text x="375" y="304" font-size="8" font-weight="400" fill="#475569">Panier multi-commerces</text>
    <text x="375" y="318" font-size="8" font-weight="400" fill="#475569">Validation 2PC &amp; Retrait &lt; 3s</text>
    <text x="375" y="332" font-size="7.5" font-weight="600" fill="#7C3AED">Flux P2 · Snapshot des prix</text>

    <!-- Bloc F2 : Double Fidélité & VFP -->
    <rect x="585" y="270" width="200" height="85" rx="6" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1" />
    <text x="595" y="288" font-size="10" font-weight="700" fill="#15803D">Double Moteur Fidélité</text>
    <text x="595" y="304" font-size="8" font-weight="400" fill="#475569">Points marchands autonomes</text>
    <text x="595" y="318" font-size="8" font-weight="400" fill="#475569">Batch nocturne VFP (15 jours)</text>
    <text x="595" y="332" font-size="7.5" font-weight="600" fill="#16A34A">Flux P3 · ADR-005 découplé</text>

    <!-- Bloc F3 : Enrôlement & Multi-Tenancy -->
    <rect x="365" y="368" width="200" height="85" rx="6" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1" />
    <text x="375" y="386" font-size="10" font-weight="700" fill="#0369A1">Conventionnement &amp; Tenants</text>
    <text x="375" y="402" font-size="8" font-weight="400" fill="#475569">Validation tripartite Mairie/Asso</text>
    <text x="375" y="416" font-size="8" font-weight="400" fill="#475569">Partitionnement strict par ville</text>
    <text x="375" y="430" font-size="7.5" font-weight="600" fill="#0284C7">Flux P1 · tenant_id = ville_id</text>

    <!-- Bloc F4 : Mobilité Urbaine & Reporting -->
    <rect x="585" y="368" width="200" height="85" rx="6" fill="#FEFCE8" stroke="#FDE047" stroke-width="1" />
    <text x="595" y="386" font-size="10" font-weight="700" fill="#A16207">Mobilité &amp; Tableaux de Bord</text>
    <text x="595" y="402" font-size="8" font-weight="400" fill="#475569">Vouchers bus &amp; parking 20 min</text>
    <text x="595" y="416" font-size="8" font-weight="400" fill="#475569">Statistiques DSI anonymisées</text>
    <text x="595" y="430" font-size="7.5" font-weight="600" fill="#CA8A04">Flux P4 · RGPD &amp; Privacy</text>

    <!-- Bandeau Propriétés Clés -->
    <rect x="365" y="468" width="420" height="74" rx="8" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1" />
    <text x="375" y="488" font-size="9.5" font-weight="700" fill="#1E293B">Propriétés Non-Négociables du Système :</text>
    <text x="375" y="505" font-size="8.5" font-weight="500" fill="#334155">• Monolithe Modulaire Dockerisé (ADR-012) avec PostgreSQL 16 3NF.</text>
    <text x="375" y="519" font-size="8.5" font-weight="500" fill="#334155">• Zéro livraison motorisée : retrait physique pédestre en boutique obligatoire.</text>
    <text x="375" y="533" font-size="8.5" font-weight="500" fill="#334155">• Étanchéité absolue inter-commerces (secret des affaires) et zéro commission vente.</text>

    <!-- Footer Sécurité & Pass bi-média -->
    <rect x="365" y="555" width="420" height="42" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
    <text x="575" y="573" text-anchor="middle" font-size="8.5" font-weight="600" fill="#0F172A">Sécurité &amp; Accessibilité Bi-Média : Pass Citoyen Haché SHA-256</text>
    <text x="575" y="587" text-anchor="middle" font-size="8.5" font-weight="400" fill="#64748B">Identifiant scannable sur écran smartphone ou carte papier QR pour inclusion seniors.</text>
  </g>

  <!-- ======================================================== -->
  <!-- 3. SYSTEMES TIERS EXTERNES (MOCKS REST OPENAPI) - DROITE -->
  <!-- ======================================================== -->

  <!-- Cadre groupement Partenaires Externes -->
  <rect x="880" y="80" width="275" height="590" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-dasharray="4,3" stroke-width="1.2" />
  <text x="895" y="104" font-size="11" font-weight="700" fill="#475569" letter-spacing="0.05em">SERVICES TIERS (MOCKS REST)</text>

  <!-- Partenaire 1 : Passerelle Bancaire -->
  <g filter="url(#shadow-card)">
    <rect x="895" y="128" width="245" height="135" rx="8" fill="#FFFFFF" stroke="#FED7AA" stroke-width="1.3" />
    <rect x="905" y="138" width="80" height="18" rx="4" fill="#FFEDD5" />
    <text x="945" y="151" text-anchor="middle" font-size="9" font-weight="700" fill="#C2410C">MOCK EXT-01</text>
    <text x="895" y="174" font-size="11.5" font-weight="700" fill="#0F172A" dx="10">Passerelle Bancaire</text>
    <text x="905" y="192" font-size="9" font-weight="600" fill="#EA580C">Paiement CB &amp; Protocole 2PC</text>
    <text x="905" y="208" font-size="8.5" font-weight="400" fill="#475569">Simule l'autorisation bancaire,</text>
    <text x="905" y="222" font-size="8.5" font-weight="400" fill="#475569">le débit unique du panier mutualisé</text>
    <text x="905" y="236" font-size="8.5" font-weight="400" fill="#475569">et le rollback en cas de rupture.</text>
    <text x="905" y="252" font-size="8" font-weight="600" fill="#9A3412">[OpenAPI 3.1 · Simulation Q8.2]</text>
  </g>

  <!-- Partenaire 2 : SI Mobilité Municipale -->
  <g filter="url(#shadow-card)">
    <rect x="895" y="295" width="245" height="145" rx="8" fill="#FFFFFF" stroke="#BAE6FD" stroke-width="1.3" />
    <rect x="905" y="305" width="80" height="18" rx="4" fill="#E0F2FE" />
    <text x="945" y="318" text-anchor="middle" font-size="9" font-weight="700" fill="#0369A1">MOCK EXT-02</text>
    <text x="895" y="341" font-size="11.5" font-weight="700" fill="#0F172A" dx="10">Services Mobilité Mairie</text>
    <text x="905" y="359" font-size="9" font-weight="600" fill="#0284C7">Réseau Bus Ilévia &amp; Horodateurs</text>
    <text x="905" y="375" font-size="8.5" font-weight="400" fill="#475569">Valide les recharges de cartes Pass Pass</text>
    <text x="905" y="389" font-size="8.5" font-weight="400" fill="#475569">et déclenche les 20 min de parking</text>
    <text x="905" y="403" font-size="8.5" font-weight="400" fill="#475569">gratuit associées à la plaque usager.</text>
    <text x="905" y="420" font-size="8" font-weight="600" fill="#075985">[OpenAPI 3.1 · Simulation Q7.3 / Q8.2]</text>
  </g>

  <!-- Partenaire 3 : Systèmes de Caisse POS Marchands -->
  <g filter="url(#shadow-card)">
    <rect x="895" y="472" width="245" height="145" rx="8" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1.3" />
    <rect x="905" y="482" width="80" height="18" rx="4" fill="#DCFCE7" />
    <text x="945" y="495" text-anchor="middle" font-size="9" font-weight="700" fill="#15803D">MOCK EXT-03</text>
    <text x="895" y="518" font-size="11.5" font-weight="700" fill="#0F172A" dx="10">Logiciels de Caisse (POS)</text>
    <text x="905" y="536" font-size="9" font-weight="600" fill="#16A34A">Terminaux Marchands (Pilote V3)</text>
    <text x="905" y="552" font-size="8.5" font-weight="400" fill="#475569">Simule l'exportation des stocks</text>
    <text x="905" y="566" font-size="8.5" font-weight="400" fill="#475569">et la synchronisation des passages</text>
    <text x="905" y="580" font-size="8.5" font-weight="400" fill="#475569">caisse pour les grandes boutiques.</text>
    <text x="905" y="597" font-size="8" font-weight="600" fill="#166534">[OpenAPI 3.1 · Simulation US-C16]</text>
  </g>

  <!-- ======================================================== -->
  <!-- 4. CONNECTEURS / FLUX RELATIONNELS                       -->
  <!-- ======================================================== -->

  <!-- Flux Utilisateurs -> ShopLoc Core -->
  <line x1="262" y1="177" x2="345" y2="210" stroke="#0284C7" stroke-width="1.6" marker-end="url(#arrow-blue)" />
  <line x1="262" y1="313" x2="345" y2="313" stroke="#7C3AED" stroke-width="1.6" marker-end="url(#arrow-purple)" />
  <line x1="262" y1="451" x2="345" y2="410" stroke="#16A34A" stroke-width="1.6" marker-end="url(#arrow-emerald)" />
  <line x1="262" y1="590" x2="345" y2="500" stroke="#EA580C" stroke-width="1.6" marker-end="url(#arrow-slate)" />

  <!-- Labels Flux Entrants -->
  <rect x="270" y="215" width="70" height="18" rx="3" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.8" />
  <text x="305" y="227" text-anchor="middle" font-size="7.5" font-weight="600" fill="#0369A1">HTTPS / Web</text>

  <rect x="270" y="325" width="70" height="18" rx="3" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.8" />
  <text x="305" y="337" text-anchor="middle" font-size="7.5" font-weight="600" fill="#6D28D9">Panier 2PC</text>

  <rect x="270" y="425" width="70" height="18" rx="3" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.8" />
  <text x="305" y="437" text-anchor="middle" font-size="7.5" font-weight="600" fill="#15803D">Scan Caisse</text>

  <rect x="270" y="525" width="70" height="18" rx="3" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.8" />
  <text x="305" y="537" text-anchor="middle" font-size="7.5" font-weight="600" fill="#C2410C">Tableau DSI</text>

  <!-- Flux ShopLoc Core -> Partenaires Externes -->
  <line x1="805" y1="210" x2="895" y2="195" stroke="#EA580C" stroke-width="1.6" marker-end="url(#arrow-slate)" />
  <line x1="805" y1="367" x2="895" y2="367" stroke="#0284C7" stroke-width="1.6" marker-end="url(#arrow-blue)" />
  <line x1="805" y1="500" x2="895" y2="545" stroke="#16A34A" stroke-width="1.6" marker-end="url(#arrow-emerald)" />

  <!-- Labels Flux Sortants -->
  <rect x="815" y="190" width="72" height="18" rx="3" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.8" />
  <text x="851" y="202" text-anchor="middle" font-size="7.5" font-weight="600" fill="#C2410C">REST / JSON</text>

  <rect x="815" y="355" width="72" height="18" rx="3" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.8" />
  <text x="851" y="367" text-anchor="middle" font-size="7.5" font-weight="600" fill="#0369A1">REST / OAuth</text>

  <rect x="815" y="515" width="72" height="18" rx="3" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.8" />
  <text x="851" y="527" text-anchor="middle" font-size="7.5" font-weight="600" fill="#15803D">Sync Mocks</text>

</svg>
"""

# ==============================================================================
# FIGURE 7.2 : DIAGRAMME C4 NIVEAU 2 — CONTENEURS & MONOLITHE MODULAIRE DOCKER
# ==============================================================================
def generate_c4_containers_svg():
    return f"""<svg viewBox="0 0 1180 750" width="100%" height="auto" style="overflow:visible; font-family:'Poppins', sans-serif;">
{COMMON_DEFS}

  <!-- CADRE GLOBAL C4 CONTENEURS -->
  <rect x="10" y="10" width="1160" height="730" rx="14" fill="#FAFAFA" stroke="#E2E8F0" stroke-width="1.2" />

  <!-- EN-TETE BANDEAU -->
  <rect x="25" y="22" width="1130" height="42" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
  <rect x="35" y="32" width="22" height="22" rx="4" fill="#7C3AED" />
  <text x="46" y="47" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">C4</text>
  <text x="68" y="46" font-size="13" font-weight="700" fill="#1E293B">Système ShopLoc — Diagramme des Conteneurs &amp; Monolithe Modulaire (Niveau 2)</text>
  <text x="1140" y="46" text-anchor="end" font-size="11" font-weight="500" fill="#64748B">Orchestration Docker &amp; Découpage Bounded Contexts DDD · ADR-012</text>

  <!-- ======================================================== -->
  <!-- 1. COUCHE CLIENTS & FRONTEND (HAUT)                      -->
  <!-- ======================================================== -->

  <!-- Conteneur SPA Unique Responsive -->
  <g filter="url(#shadow-card)">
    <rect x="280" y="80" width="620" height="85" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.6" />
    <rect x="295" y="92" width="110" height="20" rx="4" fill="#E0F2FE" />
    <text x="350" y="106" text-anchor="middle" font-size="9" font-weight="700" fill="#0369A1">CONTENEUR WEB</text>
    <text x="420" y="106" font-size="12" font-weight="700" fill="#0F172A">Single Page Application Responsive (SPA)</text>
    <text x="790" y="106" font-size="10" font-weight="600" fill="#64748B">[TypeScript / React &amp; Vue.js]</text>
    
    <!-- 3 vues spécialisées au sein de la SPA -->
    <rect x="295" y="122" width="180" height="32" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="0.8" />
    <text x="385" y="138" text-anchor="middle" font-size="9" font-weight="700" fill="#0369A1">Vue Pierre (Senior)</text>
    <text x="385" y="149" text-anchor="middle" font-size="7.5" font-weight="400" fill="#475569">Gros contrastes, RGAA AA</text>

    <rect x="495" y="122" width="190" height="32" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="0.8" />
    <text x="590" y="138" text-anchor="middle" font-size="9" font-weight="700" fill="#15803D">Vue Suzanne (Artisan)</text>
    <text x="590" y="149" text-anchor="middle" font-size="7.5" font-weight="400" fill="#475569">Scan caisse &lt; 3s, stocks</text>

    <rect x="705" y="122" width="180" height="32" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="0.8" />
    <text x="795" y="138" text-anchor="middle" font-size="9" font-weight="700" fill="#C2410C">Vue Marius (DSI Mairie)</text>
    <text x="795" y="149" text-anchor="middle" font-size="7.5" font-weight="400" fill="#475569">Tableaux bord anonymisés</text>
  </g>

  <!-- Pass Bi-Média Papier (A côté) -->
  <g filter="url(#shadow-box)">
    <rect x="930" y="80" width="220" height="85" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2" />
    <rect x="942" y="92" width="80" height="18" rx="4" fill="#F1F5F9" />
    <text x="982" y="105" text-anchor="middle" font-size="8.5" font-weight="700" fill="#475569">BI-MÉDIA</text>
    <text x="942" y="126" font-size="10.5" font-weight="700" fill="#1E293B">Pass Papier QR Citoyen</text>
    <text x="942" y="142" font-size="8" font-weight="400" fill="#64748B">Empreinte SHA-256 salée</text>
    <text x="942" y="154" font-size="8" font-weight="400" fill="#64748B">Inclusion seniors sans mobile</text>
  </g>

  <!-- Utilisateurs Externes (Gauche) -->
  <g filter="url(#shadow-box)">
    <rect x="30" y="80" width="220" height="85" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2" />
    <text x="42" y="105" font-size="11" font-weight="700" fill="#1E293B">Navigateurs &amp; Mobiles</text>
    <text x="42" y="125" font-size="8.5" font-weight="500" fill="#475569">Clients finaux, Commerçants,</text>
    <text x="42" y="139" font-size="8.5" font-weight="500" fill="#475569">Élus et Administrateurs</text>
    <text x="42" y="153" font-size="8" font-weight="600" fill="#0284C7">HTTPS / Protocole TLS 1.3</text>
  </g>

  <line x1="250" y1="122" x2="280" y2="122" stroke="#0284C7" stroke-width="1.8" marker-end="url(#arrow-blue)" />

  <!-- ======================================================== -->
  <!-- 2. REVERSE PROXY & GATEWAY (MILIEU HAUT)                 -->
  <!-- ======================================================== -->

  <g filter="url(#shadow-box)">
    <rect x="380" y="195" width="420" height="52" rx="8" fill="#FFFFFF" stroke="#64748B" stroke-width="1.4" />
    <rect x="392" y="205" width="100" height="18" rx="4" fill="#F1F5F9" />
    <text x="442" y="218" text-anchor="middle" font-size="8.5" font-weight="700" fill="#334155">EDGE GATEWAY</text>
    <text x="502" y="218" font-size="11" font-weight="700" fill="#0F172A">Conteneur Nginx / Traefik (Docker)</text>
    <text x="392" y="238" font-size="8.5" font-weight="400" fill="#475569">Terminaison SSL, Routage API REST `/api/v1/...`, Rate Limiting et CORS</text>
  </g>

  <!-- Ligne SPA -> Gateway -->
  <line x1="590" y1="165" x2="590" y2="195" stroke="#334155" stroke-width="1.8" marker-end="url(#arrow-slate)" />
  <text x="600" y="184" font-size="8" font-weight="600" fill="#64748B">JSON / HTTPS</text>

  <!-- ======================================================== -->
  <!-- 3. CŒUR : MONOLITHE MODULAIRE BACKEND (CENTRE)           -->
  <!-- ======================================================== -->

  <g filter="url(#shadow-card)">
    <!-- Cadre Englobant Backend Monolithique -->
    <rect x="30" y="275" width="810" height="325" rx="12" fill="#FFFFFF" stroke="#7C3AED" stroke-width="2" />
    
    <!-- En-tête Backend -->
    <rect x="30" y="275" width="810" height="42" rx="12" fill="#FAF5FF" />
    <rect x="30" y="303" width="810" height="14" fill="#FAF5FF" />
    <text x="435" y="296" text-anchor="middle" font-size="13" font-weight="700" fill="#6D28D9">CONTENEUR BACKEND : MONOLITHE MODULAIRE MULTI-TENANT</text>
    <text x="435" y="311" text-anchor="middle" font-size="9.5" font-weight="600" fill="#7C3AED">[Java Spring Boot / TypeScript NestJS — Clean Architecture &amp; In-Process DDD — ADR-012]</text>

    <!-- MODULE 1 : Conventionnement & Onboarding -->
    <g filter="url(#shadow-box)">
      <rect x="48" y="332" width="235" height="120" rx="8" fill="#F8FAFC" stroke="#BAE6FD" stroke-width="1.2" />
      <rect x="58" y="342" width="65" height="18" rx="4" fill="#E0F2FE" />
      <text x="90" y="355" text-anchor="middle" font-size="8" font-weight="700" fill="#0369A1">MODULE 01</text>
      <text x="130" y="355" font-size="10" font-weight="700" fill="#0F172A">Onboarding &amp; Tenants</text>
      <text x="58" y="378" font-size="8.5" font-weight="600" fill="#0284C7">Conventionnement Tripartite</text>
      <text x="58" y="394" font-size="8" font-weight="400" fill="#475569">• Enrôlement Mairie &amp; Association</text>
      <text x="58" y="408" font-size="8" font-weight="400" fill="#475569">• Adhésion commerçants sans commission</text>
      <text x="58" y="422" font-size="8" font-weight="400" fill="#475569">• Cloisonnement tenant_id par commune</text>
      <text x="58" y="440" font-size="7.5" font-weight="600" fill="#0369A1">Contrat : /api/v1/tenants/...</text>
    </g>

    <!-- MODULE 2 : Catalogue & Gestion Stocks -->
    <g filter="url(#shadow-box)">
      <rect x="318" y="332" width="235" height="120" rx="8" fill="#F8FAFC" stroke="#BBF7D0" stroke-width="1.2" />
      <rect x="328" y="342" width="65" height="18" rx="4" fill="#DCFCE7" />
      <text x="360" y="355" text-anchor="middle" font-size="8" font-weight="700" fill="#15803D">MODULE 02</text>
      <text x="400" y="355" font-size="10" font-weight="700" fill="#0F172A">Catalogue &amp; Stocks V1</text>
      <text x="328" y="378" font-size="8.5" font-weight="600" fill="#16A34A">Offre Marchande Locale</text>
      <text x="328" y="394" font-size="8" font-weight="400" fill="#475569">• Saisie manuelle simplifiée (Suzanne)</text>
      <text x="328" y="408" font-size="8" font-weight="400" fill="#475569">• Masquage immédiat si stock = 0</text>
      <text x="328" y="422" font-size="8" font-weight="400" fill="#475569">• Recherche géolocalisée de proximité</text>
      <text x="328" y="440" font-size="7.5" font-weight="600" fill="#15803D">Contrat : /api/v1/catalog/...</text>
    </g>

    <!-- MODULE 3 : Commande 2PC & Click & Collect -->
    <g filter="url(#shadow-box)">
      <rect x="588" y="332" width="235" height="120" rx="8" fill="#F8FAFC" stroke="#DDD6FE" stroke-width="1.2" />
      <rect x="598" y="342" width="65" height="18" rx="4" fill="#EDE9FE" />
      <text x="630" y="355" text-anchor="middle" font-size="8" font-weight="700" fill="#6D28D9">MODULE 03</text>
      <text x="670" y="355" font-size="10" font-weight="700" fill="#0F172A">Commande &amp; 2PC</text>
      <text x="598" y="378" font-size="8.5" font-weight="600" fill="#7C3AED">Orchestrateur Two-Phase Commit</text>
      <text x="598" y="394" font-size="8" font-weight="400" fill="#475569">• Panier mutualisé multi-boutiques</text>
      <text x="598" y="408" font-size="8" font-weight="400" fill="#475569">• Verrouillage ACID &amp; rollback unitaire</text>
      <text x="598" y="422" font-size="8" font-weight="400" fill="#475569">• Snapshot tarifaire &amp; No-Show 24h</text>
      <text x="598" y="440" font-size="7.5" font-weight="600" fill="#6D28D9">Contrat : /api/v1/orders/...</text>
    </g>

    <!-- MODULE 4 : Double Fidélité & Moteur VFP -->
    <g filter="url(#shadow-box)">
      <rect x="48" y="468" width="235" height="118" rx="8" fill="#F8FAFC" stroke="#FBCFE8" stroke-width="1.2" />
      <rect x="58" y="478" width="65" height="18" rx="4" fill="#FCE7F3" />
      <text x="90" y="491" text-anchor="middle" font-size="8" font-weight="700" fill="#BE185D">MODULE 04</text>
      <text x="130" y="491" font-size="10" font-weight="700" fill="#0F172A">Double Fidélité &amp; VFP</text>
      <text x="58" y="513" font-size="8.5" font-weight="600" fill="#DB2777">Moteurs Découplés (ADR-005)</text>
      <text x="58" y="528" font-size="8" font-weight="400" fill="#475569">• Système 1 : Points marchands libres</text>
      <text x="58" y="542" font-size="8" font-weight="400" fill="#475569">• Système 2 : Batch VFP (>=10 vis/15j)</text>
      <text x="58" y="556" font-size="8" font-weight="400" fill="#475569">• Scan caisse ultra-rapide (&lt; 3s)</text>
      <text x="58" y="574" font-size="7.5" font-weight="600" fill="#BE185D">Contrat : /api/v1/loyalty/...</text>
    </g>

    <!-- MODULE 5 : Mobilité Municipale -->
    <g filter="url(#shadow-box)">
      <rect x="318" y="468" width="235" height="118" rx="8" fill="#F8FAFC" stroke="#FEF08A" stroke-width="1.2" />
      <rect x="328" y="478" width="65" height="18" rx="4" fill="#FEF9C3" />
      <text x="360" y="491" text-anchor="middle" font-size="8" font-weight="700" fill="#A16207">MODULE 05</text>
      <text x="400" y="491" font-size="10" font-weight="700" fill="#0F172A">Mobilité Municipale</text>
      <text x="328" y="513" font-size="8.5" font-weight="600" fill="#CA8A04">Conversion Avantages VFP</text>
      <text x="328" y="528" font-size="8" font-weight="400" fill="#475569">• Vouchers titres de transport (Bus)</text>
      <text x="328" y="542" font-size="8" font-weight="400" fill="#475569">• Décompte stationnement 20 min</text>
      <text x="328" y="556" font-size="8" font-weight="400" fill="#475569">• Quotas journaliers &amp; compensation</text>
      <text x="328" y="574" font-size="7.5" font-weight="600" fill="#A16207">Contrat : /api/v1/mobility/...</text>
    </g>

    <!-- MODULE 6 : Reporting & Audit RGPD -->
    <g filter="url(#shadow-box)">
      <rect x="588" y="468" width="235" height="118" rx="8" fill="#F8FAFC" stroke="#FED7AA" stroke-width="1.2" />
      <rect x="598" y="478" width="65" height="18" rx="4" fill="#FFEDD5" />
      <text x="630" y="491" text-anchor="middle" font-size="8" font-weight="700" fill="#C2410C">MODULE 06</text>
      <text x="670" y="491" font-size="10" font-weight="700" fill="#0F172A">Reporting &amp; RGPD</text>
      <text x="598" y="513" font-size="8.5" font-weight="600" fill="#EA580C">Agrégats &amp; Étanchéité</text>
      <text x="598" y="528" font-size="8" font-weight="400" fill="#475569">• KPIs Mairie anonymisés (Marius)</text>
      <text x="598" y="542" font-size="8" font-weight="400" fill="#475569">• Secret des affaires entre commerces</text>
      <text x="598" y="556" font-size="8" font-weight="400" fill="#475569">• Hachage des empreintes citoyennes</text>
      <text x="598" y="574" font-size="7.5" font-weight="600" fill="#C2410C">Contrat : /api/v1/reporting/...</text>
    </g>
  </g>

  <!-- Ligne Gateway -> Monolithe Modulaire -->
  <line x1="590" y1="247" x2="590" y2="275" stroke="#7C3AED" stroke-width="1.8" marker-end="url(#arrow-purple)" />

  <!-- ======================================================== -->
  <!-- 4. PERSISTANCE & CACHE (BAS DROITE)                      -->
  <!-- ======================================================== -->

  <!-- Conteneur PostgreSQL 16 -->
  <g filter="url(#shadow-card)">
    <rect x="880" y="275" width="270" height="180" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="1.6" />
    <rect x="892" y="287" width="130" height="20" rx="4" fill="#D1FAE5" />
    <text x="957" y="301" text-anchor="middle" font-size="8.5" font-weight="700" fill="#065F46">PERSISTANCE PRINCIPALE</text>
    <text x="892" y="326" font-size="11.5" font-weight="700" fill="#0F172A">PostgreSQL 16 (Docker)</text>
    <text x="892" y="344" font-size="9" font-weight="600" fill="#059669">Schéma Relationnel Normalisé 3NF</text>
    <text x="892" y="362" font-size="8" font-weight="400" fill="#475569">• Partitionnement logique par tenant_id</text>
    <text x="892" y="376" font-size="8" font-weight="400" fill="#475569">• Intégrité référentielle &amp; contraintes ACID</text>
    <text x="892" y="390" font-size="8" font-weight="400" fill="#475569">• Transactions 2PC avec verrous SELECT FOR UPDATE</text>
    <text x="892" y="404" font-size="8" font-weight="400" fill="#475569">• Index partiels pour calcul nocturne VFP</text>
    <text x="892" y="424" font-size="8" font-weight="600" fill="#065F46">Pilote : JDBC / PostgreSQL Driver</text>
  </g>

  <!-- Conteneur Redis Cache -->
  <g filter="url(#shadow-card)">
    <rect x="880" y="475" width="270" height="125" rx="10" fill="#FFFFFF" stroke="#DC2626" stroke-width="1.4" />
    <rect x="892" y="487" width="90" height="20" rx="4" fill="#FEE2E2" />
    <text x="937" y="501" text-anchor="middle" font-size="8.5" font-weight="700" fill="#991B1B">CACHE &amp; SESSIONS</text>
    <text x="892" y="526" font-size="11.5" font-weight="700" fill="#0F172A">Redis 7 (Docker)</text>
    <text x="892" y="544" font-size="8" font-weight="400" fill="#475569">• Cache des sessions et tokens JWT</text>
    <text x="892" y="558" font-size="8" font-weight="400" fill="#475569">• Verrous distribués temporaires 2PC</text>
    <text x="892" y="572" font-size="8" font-weight="400" fill="#475569">• Rate Limiting des scans caisse</text>
  </g>

  <!-- Lignes Backend -> Persistance -->
  <line x1="840" y1="365" x2="880" y2="365" stroke="#059669" stroke-width="1.8" marker-end="url(#arrow-emerald)" />
  <text x="846" y="355" font-size="7.5" font-weight="600" fill="#065F46">SQL / ACID</text>

  <line x1="840" y1="535" x2="880" y2="535" stroke="#DC2626" stroke-width="1.8" marker-end="url(#arrow-slate)" />
  <text x="846" y="525" font-size="7.5" font-weight="600" fill="#991B1B">RESP / TCP</text>

  <!-- ======================================================== -->
  <!-- 5. SERVICES TIERS MOCKÉS (BAS)                           -->
  <!-- ======================================================== -->

  <g filter="url(#shadow-box)">
    <rect x="30" y="625" width="1120" height="95" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2" />
    <rect x="42" y="635" width="140" height="18" rx="4" fill="#F1F5F9" />
    <text x="112" y="648" text-anchor="middle" font-size="8.5" font-weight="700" fill="#334155">MOCKS CONTENEURISÉS</text>
    <text x="195" y="648" font-size="11" font-weight="700" fill="#0F172A">Services Externes Simulés (Docker Compose — Mocks REST OpenAPI 3.1)</text>

    <!-- Mock 1 : Banque -->
    <rect x="45" y="662" width="345" height="45" rx="6" fill="#FFF7ED" stroke="#FDBA74" stroke-width="0.8" />
    <text x="55" y="679" font-size="9" font-weight="700" fill="#C2410C">Mock Passerelle Bancaire :</text>
    <text x="55" y="695" font-size="8" font-weight="400" fill="#7C2D12">Simulation validation CB, encaissement global et rollback 2PC.</text>

    <!-- Mock 2 : Mobilité -->
    <rect x="415" y="662" width="350" height="45" rx="6" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="0.8" />
    <text x="425" y="679" font-size="9" font-weight="700" fill="#0369A1">Mock Mobilité Urbaine :</text>
    <text x="425" y="695" font-size="8" font-weight="400" fill="#0C4A6E">Simulation validation pass bus Ilévia et compteur parking 20 min.</text>

    <!-- Mock 3 : POS Marchand -->
    <rect x="790" y="662" width="345" height="45" rx="6" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="0.8" />
    <text x="800" y="679" font-size="9" font-weight="700" fill="#15803D">Mock Caisses POS (V3) :</text>
    <text x="800" y="695" font-size="8" font-weight="400" fill="#14532D">Simulation synchronisation inventaires et exports caisse.</text>
  </g>

  <!-- Ligne Monolithe -> Mocks -->
  <line x1="435" y1="600" x2="435" y2="625" stroke="#64748B" stroke-width="1.8" stroke-dasharray="4,3" marker-end="url(#arrow-slate)" />
  <text x="445" y="616" font-size="8" font-weight="600" fill="#64748B">REST / JSON Mocks</text>

</svg>
"""

# ==============================================================================
# EXPORTATION PNG VIA HEADLESS BROWSER
# ==============================================================================
def export_png(svg_content, width, height, output_png):
    temp_html = output_png.replace(".png", "_temp.html")
    html_wrapper = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    width: {width}px;
    height: {height}px;
    background: transparent;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }}
</style>
</head>
<body>
{svg_content}
</body>
</html>
"""
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_wrapper)

    cmd = [
        BROWSER,
        "--headless",
        "--disable-gpu",
        f"--window-size={width},{height}",
        f"--screenshot={output_png}",
        f"file://{os.path.abspath(temp_html)}"
    ]
    subprocess.run(cmd, check=True, stderr=subprocess.DEVNULL)
    if os.path.exists(temp_html):
        os.remove(temp_html)
    print(f"Exporté avec succès : {output_png} ({width}x{height})")

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    figures_dir = os.path.join(repo_root, "agent_projet/docs/01_Cadrage_Et_Cahier_Des_Charges_R1/figures")
    components_dir = os.path.join(repo_root, "agent_projet/templates/components")
    os.makedirs(figures_dir, exist_ok=True)
    os.makedirs(components_dir, exist_ok=True)

    # 1. Génération C4 Contexte (Figure 7.1)
    svg_context = generate_c4_context_svg()
    png_context = os.path.join(figures_dir, "fig_7_1_c4_contexte.png")
    export_png(svg_context, 1180, 700, png_context)

    # 2. Génération C4 Conteneurs (Figure 7.2)
    svg_containers = generate_c4_containers_svg()
    png_containers = os.path.join(figures_dir, "fig_7_2_c4_conteneurs.png")
    export_png(svg_containers, 1180, 750, png_containers)

    # 3. Sauvegarde composant HTML unifié
    comp_html_path = os.path.join(components_dir, "c4_architecture_views.html")
    comp_content = f"""<!-- FIGURE 7.1 & FIGURE 7.2 : SCHÉMAS D'ARCHITECTURE C4 SHOPLOC -->
<div class="figure-card" style="background:#FFFFFF; border:1px solid #E8E6DF; border-radius:16px; padding:24px; margin-bottom:28px; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px; border-bottom:1px solid #E8E6DF; padding-bottom:12px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#0284C7;"></span>
        <span style="font-size:11px; font-weight:700; color:#0284C7; text-transform:uppercase; letter-spacing:0.08em;">Architecture C4 Model</span>
      </div>
      <h3 style="font-size:17px; font-weight:700; color:#243342; margin:0;">Figure 7.1 — Diagramme C4 Niveau 1 : Contexte Système ShopLoc</h3>
    </div>
    <span style="font-size:11px; background:#FAF9F6; border:1px solid #E8E6DF; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600;">SaaS Multi-Tenant · Écosystème Partenaires</span>
  </div>
{svg_context}
</div>

<div class="figure-card" style="background:#FFFFFF; border:1px solid #E8E6DF; border-radius:16px; padding:24px; margin-bottom:28px; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px; border-bottom:1px solid #E8E6DF; padding-bottom:12px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#7C3AED;"></span>
        <span style="font-size:11px; font-weight:700; color:#7C3AED; text-transform:uppercase; letter-spacing:0.08em;">Architecture Conteneurs &amp; Docker</span>
      </div>
      <h3 style="font-size:17px; font-weight:700; color:#243342; margin:0;">Figure 7.2 — Diagramme C4 Niveau 2 : Conteneurs &amp; Monolithe Modulaire Docker</h3>
    </div>
    <span style="font-size:11px; background:#FAF9F6; border:1px solid #E8E6DF; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600;">Monolithe Modulaire · 6 Bounded Contexts DDD</span>
  </div>
{svg_containers}
</div>
"""
    with open(comp_html_path, "w", encoding="utf-8") as f:
        f.write(comp_content)
    print(f"Composant HTML écrit : {comp_html_path}")
    print("Génération C4 terminée avec succès !")

if __name__ == "__main__":
    main()

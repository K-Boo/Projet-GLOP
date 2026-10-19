#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERATE R2 FIGURES - Generation des 3 Schemas Techniques Officiels pour le Livrable R2
Projet ShopLoc (MiageShopLoc) - M2 MIAGE GLOP 2026-2027

Trois diagrammes d'architecture hautement visuels conformes au bareme de Jeremy Woirhaye :
1. fig_1_contexte_systeme_shoploc.svg : Schema de Contexte (5 Types d'Acteurs, Systeme ShopLoc, 3 Partenaires Simules - C4 Niveau 1)
2. fig_2_services_et_liaisons.svg : Schema des Services & Liaisons (Gateway, 4 Microservices, 4 BDD dediees, 2PC RestClient, Stubs - C4 Niveau 2)
3. fig_3_chaine_outils_devops.svg : Schema de la Chaine d'Outils (Dev Local H2, GitLab CI multi-depots, Deploiement VPS Linux OVHcloud)
"""

import os
from pathlib import Path


def generate_fig1_context(output_path: Path):
    """Schema 1 : Contexte Systeme (5 types d'utilisateurs, Systeme ShopLoc, 3 Partenaires simules - C4 Niveau 1)."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1140 760" width="100%" height="100%" style="background-color: #F8FAFC; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <filter id="shadow1" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#0F172A" flood-opacity="0.08" />
    </filter>
    <marker id="arrow-blue1" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#0284C7" />
    </marker>
    <marker id="arrow-amber1" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#D97706" />
    </marker>
  </defs>

  <!-- En-tete du schema -->
  <rect x="30" y="20" width="1080" height="64" rx="8" fill="#0F172A" filter="url(#shadow1)" />
  <text x="50" y="48" fill="#F8FAFC" font-size="18" font-weight="700">SCHEMA 1 : CONTEXTE SYSTEME SHOPLOC (C4 NIVEAU 1)</text>
  <text x="50" y="68" fill="#94A3B8" font-size="12">5 Canaux d'Usage, Plateforme Territoriale ShopLoc et Services Partenaires Simules</text>
  <rect x="910" y="36" width="180" height="30" rx="6" fill="#1E293B" stroke="#334155" />
  <text x="930" y="56" fill="#38BDF8" font-size="11" font-weight="600">Notation : C4 Contexte</text>

  <!-- ==================== COLONNE 1 : LES 5 TYPES D'UTILISATEURS ==================== -->
  <rect x="30" y="105" width="280" height="535" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow1)" />
  <rect x="30" y="105" width="280" height="38" rx="10" fill="#F1F5F9" />
  <text x="45" y="130" fill="#1E293B" font-size="13" font-weight="700">1. LES 5 TYPES D'UTILISATEURS</text>

  <!-- Acteur 1 : Citoyen Web -->
  <rect x="45" y="155" width="250" height="78" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 172)">
    <rect width="36" height="36" rx="8" fill="#E0F2FE" />
    <path d="M 8 11 L 28 11 C 29 11 30 12 30 13 L 30 23 C 30 24 29 25 28 25 L 8 25 C 7 25 6 24 6 23 L 6 13 C 6 12 7 11 8 11 Z" fill="none" stroke="#0284C7" stroke-width="2" />
    <line x1="18" y1="25" x2="18" y2="29" stroke="#0284C7" stroke-width="2" />
    <line x1="13" y1="29" x2="23" y2="29" stroke="#0284C7" stroke-width="2" stroke-linecap="round" />
  </g>
  <text x="102" y="180" fill="#0F172A" font-size="12.5" font-weight="700">Client Web Citoyen</text>
  <text x="102" y="197" fill="#64748B" font-size="11">Consommateur local (Julie)</text>
  <text x="102" y="213" fill="#0284C7" font-size="10" font-weight="600">Achat C&amp;C &amp; Cagnotte VFP</text>

  <!-- Acteur 2 : Commercant Web -->
  <rect x="45" y="245" width="250" height="78" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 262)">
    <rect width="36" height="36" rx="8" fill="#DCFCE7" />
    <path d="M 8 15 L 28 15 L 26 27 C 26 28 25 29 24 29 L 12 29 C 11 29 10 28 10 27 Z" fill="none" stroke="#16A34A" stroke-width="2" />
    <path d="M 6 15 L 18 9 L 30 15 Z" fill="none" stroke="#16A34A" stroke-width="2" />
    <rect x="15" y="21" width="6" height="8" fill="#16A34A" />
  </g>
  <text x="102" y="270" fill="#0F172A" font-size="12.5" font-weight="700">Portail Commercant</text>
  <text x="102" y="287" fill="#64748B" font-size="11">Gestionnaire boutique (Suzanne)</text>
  <text x="102" y="303" fill="#16A34A" font-size="10" font-weight="600">Gestion fiches &amp; stocks</text>

  <!-- Acteur 3 : Terminal Mobile Caisse -->
  <rect x="45" y="335" width="250" height="78" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 352)">
    <rect width="36" height="36" rx="8" fill="#F1F5F9" />
    <rect x="11" y="8" width="14" height="22" rx="3" fill="none" stroke="#475569" stroke-width="2" />
    <circle cx="18" cy="25" r="1.5" fill="#475569" />
    <line x1="15" y1="11" x2="21" y2="11" stroke="#475569" stroke-width="1.5" stroke-linecap="round" />
  </g>
  <text x="102" y="360" fill="#0F172A" font-size="12.5" font-weight="700">Terminal Caisse (PWA)</text>
  <text x="102" y="377" fill="#64748B" font-size="11">Vendeur en boutique</text>
  <text x="102" y="393" fill="#475569" font-size="10" font-weight="600">Scan QR Code &amp; Remise</text>

  <!-- Acteur 4 : Console Mairie -->
  <rect x="45" y="425" width="250" height="78" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 442)">
    <rect width="36" height="36" rx="8" fill="#F3E8FF" />
    <path d="M 8 28 L 28 28 M 10 28 L 10 16 L 18 10 L 26 16 L 26 28" fill="none" stroke="#9333EA" stroke-width="2" />
    <rect x="13" y="19" width="3" height="4" fill="#9333EA" />
    <rect x="20" y="19" width="3" height="4" fill="#9333EA" />
  </g>
  <text x="102" y="450" fill="#0F172A" font-size="12.5" font-weight="700">Console Mairie</text>
  <text x="102" y="467" fill="#64748B" font-size="11">Decideurs municipaux (Marius)</text>
  <text x="102" y="483" fill="#9333EA" font-size="10" font-weight="600">Statistiques Anonymisees</text>

  <!-- Acteur 5 : Console Exploitation -->
  <rect x="45" y="515" width="250" height="78" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 532)">
    <rect width="36" height="36" rx="8" fill="#FEF3C7" />
    <circle cx="18" cy="18" r="4" fill="none" stroke="#D97706" stroke-width="2" />
    <path d="M 18 9 L 18 12 M 18 24 L 18 27 M 9 18 L 12 18 M 24 18 L 27 18" stroke="#D97706" stroke-width="2" stroke-linecap="round" />
  </g>
  <text x="102" y="540" fill="#0F172A" font-size="12.5" font-weight="700">Console Exploitation</text>
  <text x="102" y="557" fill="#64748B" font-size="11">Equipe technique Garik (SRE)</text>
  <text x="102" y="573" fill="#D97706" font-size="10" font-weight="600">Supervision /actuator</text>

  <!-- LIAISON CLIENTS -> SYSTEME -->
  <line x1="310" y1="370" x2="358" y2="370" stroke="#0284C7" stroke-width="3" marker-end="url(#arrow-blue1)" />
  <text x="334" y="358" fill="#0284C7" font-size="10" font-weight="700" text-anchor="middle">HTTPS</text>
  <text x="334" y="386" fill="#64748B" font-size="9" text-anchor="middle">REST</text>

  <!-- ==================== COLONNE 2 : SYSTEME SHOPLOC ==================== -->
  <rect x="360" y="105" width="420" height="535" rx="12" fill="#F0F9FF" stroke="#0284C7" stroke-width="2" filter="url(#shadow1)" />
  <rect x="360" y="105" width="420" height="42" rx="12" fill="#0284C7" />
  <text x="570" y="132" fill="#F8FAFC" font-size="15" font-weight="800" text-anchor="middle">SYSTEME CENTRAL SHOPLOC</text>

  <rect x="380" y="165" width="380" height="95" rx="8" fill="#FFFFFF" stroke="#BAE6FD" />
  <text x="400" y="192" fill="#0369A1" font-size="13" font-weight="700">Passerelle d'Entree Unique (API Gateway)</text>
  <text x="400" y="212" fill="#64748B" font-size="11.5">• Spring Cloud Gateway (Port 8080)</text>
  <text x="400" y="230" fill="#64748B" font-size="11.5">• Routage URL, Securite JWT, CORS, X-Correlation-ID</text>
  <text x="400" y="248" fill="#0284C7" font-size="10.5" font-weight="600">Unique point de contact externe du cluster</text>

  <rect x="380" y="275" width="380" height="235" rx="8" fill="#FFFFFF" stroke="#BAE6FD" />
  <text x="400" y="302" fill="#0369A1" font-size="13" font-weight="700">Cluster des 4 Microservices Metiers</text>
  <text x="400" y="325" fill="#1E293B" font-size="11.5">• <tspan font-weight="700">shoploc-auth-service</tspan> (:8081) — Securite, RBAC &amp; JWT</text>
  <text x="400" y="350" fill="#1E293B" font-size="11.5">• <tspan font-weight="700">shoploc-merchant-catalog-service</tspan> (:8082) — Fiches &amp; Stocks</text>
  <text x="400" y="375" fill="#1E293B" font-size="11.5">• <tspan font-weight="700">shoploc-cart-order-service</tspan> (:8083) — Commandes &amp; 2PC</text>
  <text x="400" y="400" fill="#1E293B" font-size="11.5">• <tspan font-weight="700">shoploc-loyalty-service</tspan> (:8084) — Fidelite VFP 15 jours</text>
  <line x1="400" y1="418" x2="740" y2="418" stroke="#E2E8F0" stroke-width="1" />
  <text x="400" y="440" fill="#166534" font-size="11" font-weight="700">Persistance Database-per-Service :</text>
  <text x="400" y="460" fill="#64748B" font-size="10.5">4 bases PostgreSQL 16 physiques isolees (5432 a 5435)</text>
  <text x="400" y="478" fill="#64748B" font-size="10.5">Zero jointure SQL partagee — Coherence applicative 2PC</text>
  <text x="400" y="496" fill="#0284C7" font-size="10" font-weight="600">Deploiement conteneurise Docker Compose (shoploc-net)</text>

  <rect x="380" y="525" width="380" height="95" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
  <text x="400" y="550" fill="#0F172A" font-size="12" font-weight="700">Garanties Architecturales de la Societe Garik</text>
  <text x="400" y="570" fill="#475569" font-size="11">• Format d'erreur normalise RFC 7807 (Problem Details)</text>
  <text x="400" y="588" fill="#475569" font-size="11">• Echanges synchrones Spring 6 RestClient brides par timeouts</text>
  <text x="400" y="606" fill="#15803D" font-size="10.5" font-weight="600">• Eco-conception RGESN (Rejet motive de Kubernetes)</text>

  <!-- LIAISON SYSTEME -> PARTENAIRES -->
  <line x1="780" y1="370" x2="828" y2="370" stroke="#D97706" stroke-width="3" marker-end="url(#arrow-amber1)" />
  <text x="804" y="358" fill="#D97706" font-size="10" font-weight="700" text-anchor="middle">REST</text>
  <text x="804" y="386" fill="#64748B" font-size="9" text-anchor="middle">JSON</text>

  <!-- ==================== COLONNE 3 : SERVICES PARTENAIRES ==================== -->
  <rect x="830" y="105" width="280" height="535" rx="10" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1.5" filter="url(#shadow1)" />
  <rect x="830" y="105" width="280" height="38" rx="10" fill="#FEF3C7" />
  <text x="845" y="130" fill="#92400E" font-size="13" font-weight="700">3. PARTENAIRES SIMULES (STUBS)</text>

  <!-- Partenaire 1 : Banque -->
  <rect x="845" y="155" width="250" height="115" rx="8" fill="#FFFBEB" stroke="#FDE68A" />
  <g transform="translate(856, 172)">
    <rect width="34" height="34" rx="7" fill="#FDE68A" />
    <rect x="6" y="10" width="22" height="15" rx="2" fill="none" stroke="#B45309" stroke-width="1.8" />
    <line x1="6" y1="14" x2="28" y2="14" stroke="#B45309" stroke-width="2" />
    <rect x="9" y="18" width="4" height="3" fill="#B45309" />
  </g>
  <text x="900" y="180" fill="#92400E" font-size="12.5" font-weight="700">Simulateur Banque</text>
  <text x="900" y="197" fill="#64748B" font-size="11">Stub REST HTTP (:8090)</text>
  <text x="900" y="215" fill="#B45309" font-size="10.5" font-weight="600">POST /api/bank/authorize</text>
  <text x="856" y="240" fill="#475569" font-size="10">Debit carte &amp; scenarios de rejet</text>
  <text x="856" y="256" fill="#166534" font-size="10" font-weight="600">Eprouve le Rollback 2PC ShopLoc</text>

  <!-- Partenaire 2 : Ilevia -->
  <rect x="845" y="290" width="250" height="115" rx="8" fill="#FFFBEB" stroke="#FDE68A" />
  <g transform="translate(856, 307)">
    <rect width="34" height="34" rx="7" fill="#FDE68A" />
    <rect x="9" y="8" width="16" height="18" rx="3" fill="none" stroke="#B45309" stroke-width="1.8" />
    <circle cx="12" cy="23" r="1.5" fill="#B45309" />
    <circle cx="22" cy="23" r="1.5" fill="#B45309" />
  </g>
  <text x="900" y="315" fill="#92400E" font-size="12.5" font-weight="700">Simulateur Ilevia</text>
  <text x="900" y="332" fill="#64748B" font-size="11">Stub Transports (:8091)</text>
  <text x="900" y="350" fill="#B45309" font-size="10.5" font-weight="600">POST /api/ilevia/ticket</text>
  <text x="856" y="375" fill="#475569" font-size="10">Emission de tickets bus &amp; tramway</text>
  <text x="856" y="391" fill="#475569" font-size="10">Convertit la cagnotte VFP citoyenne</text>

  <!-- Partenaire 3 : Voirie Parking -->
  <rect x="845" y="425" width="250" height="115" rx="8" fill="#FFFBEB" stroke="#FDE68A" />
  <g transform="translate(856, 442)">
    <rect width="34" height="34" rx="7" fill="#FDE68A" />
    <rect x="8" y="8" width="18" height="18" rx="3" fill="none" stroke="#B45309" stroke-width="1.8" />
    <path d="M 14 20 L 14 12 L 18 12 C 19.5 12 20.5 13 20.5 14.5 C 20.5 16 19.5 17 18 17 L 14 17" fill="none" stroke="#B45309" stroke-width="1.8" />
  </g>
  <text x="900" y="450" fill="#92400E" font-size="12.5" font-weight="700">Simulateur Parking</text>
  <text x="900" y="467" fill="#64748B" font-size="11">Stub Voirie (:8092)</text>
  <text x="900" y="485" fill="#B45309" font-size="10.5" font-weight="600">POST /api/parking/voucher</text>
  <text x="856" y="510" fill="#475569" font-size="10">Franchise de 20 min stationnement</text>
  <text x="856" y="526" fill="#475569" font-size="10">Delivrance sur immatriculation</text>

  <!-- LEGENDE DU BAS -->
  <rect x="30" y="660" width="1080" height="75" rx="8" fill="#1E293B" />
  <text x="50" y="682" fill="#F8FAFC" font-size="12" font-weight="700">LEGENDE DU SCHEMA DE CONTEXTE (C4 NIVEAU 1) :</text>
  <text x="50" y="702" fill="#CBD5E1" font-size="11">• <tspan font-weight="700">Acteurs Externes :</tspan> Les 5 profils clients interagissent avec la plateforme via des canaux dedies (Web, PWA, Consoles).</text>
  <text x="50" y="720" fill="#CBD5E1" font-size="11">• <tspan font-weight="700">Testabilite Autonome :</tspan> Les 3 partenaires tiers sont entierement simules par des stubs conteneurises, sans dependance externe.</text>
</svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[OK] Figure 1 Contexte generee : {output_path}")


def generate_fig2_services(output_path: Path):
    """Schema 2 : Architecture des Services & Liaisons (Gateway, 4 Microservices, 4 BDD, 2PC, Stubs - C4 Niveau 2)."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1140 760" width="100%" height="100%" style="background-color: #F8FAFC; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <filter id="shadow2" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#0F172A" flood-opacity="0.08" />
    </filter>
    <marker id="arrow-blue2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#0284C7" />
    </marker>
    <marker id="arrow-green2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#16A34A" />
    </marker>
    <marker id="arrow-amber2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#D97706" />
    </marker>
  </defs>

  <!-- En-tete du schema -->
  <rect x="30" y="20" width="1080" height="64" rx="8" fill="#0F172A" filter="url(#shadow2)" />
  <text x="50" y="48" fill="#F8FAFC" font-size="18" font-weight="700">SCHEMA 2 : ARCHITECTURE DES SERVICES &amp; LIAISONS (C4 NIVEAU 2)</text>
  <text x="50" y="68" fill="#94A3B8" font-size="12">Gateway Unique, 4 Microservices Metiers, Database-per-Service et Protocole 2PC RestClient</text>
  <rect x="910" y="36" width="180" height="30" rx="6" fill="#1E293B" stroke="#334155" />
  <text x="930" y="56" fill="#38BDF8" font-size="11" font-weight="600">Notation : C4 Conteneurs</text>

  <!-- ==================== BLOC GAUCHE : PASSERELLE EDGE ==================== -->
  <rect x="30" y="105" width="220" height="535" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="2" filter="url(#shadow2)" />
  <rect x="30" y="105" width="220" height="38" rx="10" fill="#E0F2FE" />
  <text x="45" y="130" fill="#0369A1" font-size="13" font-weight="700">POINT D'ENTREE UNIQUE</text>

  <rect x="42" y="160" width="196" height="130" rx="8" fill="#F0F9FF" stroke="#BAE6FD" />
  <g transform="translate(54, 175)">
    <rect width="36" height="36" rx="8" fill="#0284C7" />
    <path d="M 18 9 L 27 13 L 27 20 C 27 25 18 29 18 29 C 18 29 9 25 9 20 L 9 13 Z" fill="none" stroke="#FFFFFF" stroke-width="2" />
    <path d="M 15 19 L 17 21 L 22 16" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" />
  </g>
  <text x="98" y="184" fill="#0369A1" font-size="12" font-weight="700">shoploc-api-gateway</text>
  <text x="98" y="201" fill="#64748B" font-size="11">Port externe : 8080</text>
  <text x="54" y="228" fill="#1E293B" font-size="10.5">• Terminaison JWT &amp; RBAC</text>
  <text x="54" y="246" fill="#1E293B" font-size="10.5">• Routage vers microservices</text>
  <text x="54" y="264" fill="#1E293B" font-size="10.5">• En-tete X-Correlation-ID</text>
  <text x="54" y="282" fill="#0284C7" font-size="10" font-weight="600">• Protection CORS globale</text>

  <rect x="42" y="310" width="196" height="310" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <text x="54" y="335" fill="#0F172A" font-size="11.5" font-weight="700">Routage Public vers Prive :</text>
  <text x="54" y="360" fill="#475569" font-size="10.5">/api/v1/auth/** -&gt; :8081</text>
  <text x="54" y="385" fill="#475569" font-size="10.5">/api/v1/catalog/** -&gt; :8082</text>
  <text x="54" y="410" fill="#475569" font-size="10.5">/api/v1/orders/** -&gt; :8083</text>
  <text x="54" y="435" fill="#475569" font-size="10.5">/api/v1/loyalty/** -&gt; :8084</text>
  <line x1="54" y1="455" x2="226" y2="455" stroke="#CBD5E1" stroke-width="1" />
  <text x="54" y="480" fill="#166534" font-size="10.5" font-weight="700">Reseau Docker Isole :</text>
  <text x="54" y="500" fill="#64748B" font-size="10">Aucun port microservice (8081-8084) ni BDD n'est ouvert sur Internet.</text>
  <text x="54" y="535" fill="#64748B" font-size="10">Seul Nginx reverse proxy achemine le trafic vers :8080.</text>

  <!-- LIAISON GATEWAY -> SERVICES -->
  <line x1="250" y1="370" x2="288" y2="370" stroke="#0284C7" stroke-width="3" marker-end="url(#arrow-blue2)" />
  <text x="269" y="358" fill="#0284C7" font-size="10" font-weight="700" text-anchor="middle">HTTP</text>
  <text x="269" y="386" fill="#64748B" font-size="9" text-anchor="middle">prive</text>

  <!-- ==================== ZONE CENTRALE : LES 4 MICROSERVICES & BDD ==================== -->
  <rect x="290" y="105" width="560" height="535" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow2)" />
  <rect x="290" y="105" width="560" height="38" rx="10" fill="#F1F5F9" />
  <text x="310" y="130" fill="#1E293B" font-size="13" font-weight="700">2. LES 4 MICROSERVICES AUTONOMES &amp; PERSISTANCE ISOLEE</text>

  <!-- Service 1 : Auth -->
  <rect x="310" y="155" width="360" height="85" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
  <text x="325" y="180" fill="#0F172A" font-size="12" font-weight="700">shoploc-auth-service (Port 8081)</text>
  <text x="325" y="198" fill="#64748B" font-size="11">Securite Spring Security 6, hashing BCrypt, emission JWT</text>
  <text x="325" y="215" fill="#0284C7" font-size="10.5">Roles : ROLE_CITOYEN, ROLE_COMMERCANT, ROLE_MAIRIE</text>

  <!-- BDD 1 : auth_db -->
  <rect x="685" y="155" width="145" height="85" rx="8" fill="#F1F5F9" stroke="#CBD5E1" />
  <text x="700" y="180" fill="#1E293B" font-size="11.5" font-weight="700">auth_db (:5432)</text>
  <text x="700" y="198" fill="#64748B" font-size="10.5">PostgreSQL 16</text>
  <text x="700" y="215" fill="#0284C7" font-size="10">Comptes &amp; roles</text>

  <!-- Service 2 : Catalog -->
  <rect x="310" y="255" width="360" height="105" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5" />
  <text x="325" y="280" fill="#166534" font-size="12.5" font-weight="800">shoploc-merchant-catalog-service (Port 8082)</text>
  <text x="325" y="298" fill="#64748B" font-size="11">Referentiel boutiques, categories, articles et inventaires</text>
  <text x="325" y="316" fill="#15803D" font-size="10.5" font-weight="700">Phase 1 2PC : Verrous pessimistes SQL (SELECT FOR UPDATE)</text>
  <text x="325" y="333" fill="#15803D" font-size="10">Statut STOCK_HOLD temporaire (TTL 5 min) -&gt; COMMIT ou RELEASED</text>

  <!-- BDD 2 : catalog_db -->
  <rect x="685" y="255" width="145" height="105" rx="8" fill="#F0FDF4" stroke="#86EFAC" />
  <text x="700" y="280" fill="#166534" font-size="11.5" font-weight="700">catalog_db (:5433)</text>
  <text x="700" y="298" fill="#64748B" font-size="10.5">PostgreSQL 16</text>
  <text x="700" y="316" fill="#15803D" font-size="10">Stocks physiques</text>
  <text x="700" y="333" fill="#15803D" font-size="10">&amp; reservations</text>

  <!-- FLUX 2PC ENTRE CATALOG ET ORDER -->
  <line x1="490" y1="360" x2="490" y2="378" stroke="#16A34A" stroke-width="3" marker-end="url(#arrow-green2)" />
  <text x="500" y="372" fill="#166534" font-size="10" font-weight="700">RestClient 2PC (Prepare / Commit)</text>

  <!-- Service 3 : Cart Order (Coordinateur 2PC) -->
  <rect x="310" y="380" width="360" height="110" rx="8" fill="#EFF6FF" stroke="#38BDF8" stroke-width="1.8" />
  <text x="325" y="405" fill="#0369A1" font-size="12.5" font-weight="800">shoploc-cart-order-service (Port 8083) [COORDINATEUR 2PC]</text>
  <text x="325" y="423" fill="#64748B" font-size="11">Panier multi-boutiques, orchestration de la commande Click &amp; Collect</text>
  <text x="325" y="441" fill="#0284C7" font-size="10.5" font-weight="700">Orchestrateur Two-Phase Commit :</text>
  <text x="325" y="458" fill="#475569" font-size="10">1. Prepare reservation catalogue -&gt; 2. Appel Bancaire -&gt; 3. Commit / Rollback</text>
  <text x="325" y="474" fill="#0284C7" font-size="10">Generation du QR Code de retrait signe HMAC-SHA256</text>

  <!-- BDD 3 : order_db -->
  <rect x="685" y="380" width="145" height="110" rx="8" fill="#EFF6FF" stroke="#BAE6FD" />
  <text x="700" y="405" fill="#0369A1" font-size="11.5" font-weight="700">order_db (:5434)</text>
  <text x="700" y="423" fill="#64748B" font-size="10.5">PostgreSQL 16</text>
  <text x="700" y="441" fill="#0284C7" font-size="10">Paniers, commandes</text>
  <text x="700" y="458" fill="#0284C7" font-size="10">statuts &amp; tokens</text>

  <!-- Service 4 : Loyalty -->
  <rect x="310" y="505" width="360" height="85" rx="8" fill="#FAF5FF" stroke="#D8B4FE" />
  <text x="325" y="530" fill="#6B21A8" font-size="12" font-weight="700">shoploc-loyalty-service (Port 8084)</text>
  <text x="325" y="548" fill="#64748B" font-size="11">Moteur VFP 15 jours glissants, conversion en tickets bus et parking</text>
  <text x="325" y="565" fill="#9333EA" font-size="10.5">Scheduled job nocturne d'expiration &amp; restitution k-anonymisee mairie</text>

  <!-- BDD 4 : loyalty_db -->
  <rect x="685" y="505" width="145" height="85" rx="8" fill="#FAF5FF" stroke="#D8B4FE" />
  <text x="700" y="530" fill="#6B21A8" font-size="11.5" font-weight="700">loyalty_db (:5435)</text>
  <text x="700" y="548" fill="#64748B" font-size="10.5">PostgreSQL 16</text>
  <text x="700" y="565" fill="#9333EA" font-size="10">Points &amp; titres</text>

  <!-- LIAISON SERVICES -> STUBS EXTERNES -->
  <line x1="850" y1="370" x2="878" y2="370" stroke="#D97706" stroke-width="3" marker-end="url(#arrow-amber2)" />

  <!-- ==================== COLONNE DROITE : STUBS EXTERNES ==================== -->
  <rect x="880" y="105" width="230" height="535" rx="10" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1.5" filter="url(#shadow2)" />
  <rect x="880" y="105" width="230" height="38" rx="10" fill="#FEF3C7" />
  <text x="895" y="130" fill="#92400E" font-size="12.5" font-weight="700">3. PARTENAIRES SIMULES</text>

  <rect x="895" y="165" width="200" height="120" rx="8" fill="#FFFBEB" stroke="#FDE68A" />
  <text x="908" y="190" fill="#92400E" font-size="12" font-weight="700">Mock Banque (:8090)</text>
  <text x="908" y="210" fill="#64748B" font-size="10.5">Appele par Cart-Order</text>
  <text x="908" y="228" fill="#B45309" font-size="10">HTTP 200 -&gt; Commit 2PC</text>
  <text x="908" y="246" fill="#DC2626" font-size="10">HTTP 402 -&gt; Rollback 2PC</text>
  <text x="908" y="264" fill="#475569" font-size="9.5">Simulation de refus</text>

  <rect x="895" y="310" width="200" height="120" rx="8" fill="#FFFBEB" stroke="#FDE68A" />
  <text x="908" y="335" fill="#92400E" font-size="12" font-weight="700">Mock Ilevia (:8091)</text>
  <text x="908" y="355" fill="#64748B" font-size="10.5">Appele par Loyalty</text>
  <text x="908" y="373" fill="#B45309" font-size="10">POST /api/ilevia/ticket</text>
  <text x="908" y="391" fill="#475569" font-size="9.5">Delivrance de titres bus</text>
  <text x="908" y="409" fill="#475569" font-size="9.5">pour usagers reguliers</text>

  <rect x="895" y="455" width="200" height="120" rx="8" fill="#FFFBEB" stroke="#FDE68A" />
  <text x="908" y="480" fill="#92400E" font-size="12" font-weight="700">Mock Parking (:8092)</text>
  <text x="908" y="500" fill="#64748B" font-size="10.5">Appele par Loyalty</text>
  <text x="908" y="518" fill="#B45309" font-size="10">POST /api/parking/voucher</text>
  <text x="908" y="536" fill="#475569" font-size="9.5">20 min franchise stationnement</text>
  <text x="908" y="554" fill="#475569" font-size="9.5">horodateurs de voirie</text>

  <!-- LEGENDE DU BAS -->
  <rect x="30" y="660" width="1080" height="75" rx="8" fill="#1E293B" />
  <text x="50" y="682" fill="#F8FAFC" font-size="12" font-weight="700">LEGENDE DU SCHEMA DES SERVICES ET LIAISONS (C4 NIVEAU 2) :</text>
  <text x="50" y="702" fill="#CBD5E1" font-size="11">• <tspan font-weight="700">Database-per-Service :</tspan> Chaque microservice est proprietaire de sa persistance PostgreSQL dediee, garantissant le couplage lache.</text>
  <text x="50" y="720" fill="#CBD5E1" font-size="11">• <tspan font-weight="700">Coherence 2PC :</tspan> RestClient coordonne la reservation PENDING sur le catalogue avant confirmation bancaire et COMMIT definitif.</text>
</svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[OK] Figure 2 Services & Liaisons generee : {output_path}")


def generate_fig3_devops(output_path: Path):
    """Schema 3 : Chaine DevOps, CI/CD GitLab et Hebergement VPS Linux (Pipeline DevOps)."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1140 760" width="100%" height="100%" style="background-color: #F8FAFC; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <filter id="shadow3" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#0F172A" flood-opacity="0.08" />
    </filter>
    <marker id="arrow-blue3" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#0284C7" />
    </marker>
  </defs>

  <!-- En-tete du schema -->
  <rect x="30" y="20" width="1080" height="64" rx="8" fill="#0F172A" filter="url(#shadow3)" />
  <text x="50" y="48" fill="#F8FAFC" font-size="18" font-weight="700">SCHEMA 3 : CHAINE DEVOPS, CI/CD ET HEBERGEMENT EN PRODUCTION REELLE</text>
  <text x="50" y="68" fill="#94A3B8" font-size="12">Developpement Local H2, Integration Continue GitLab Univ-Lille et Deploiement VPS Linux</text>
  <rect x="880" y="36" width="210" height="30" rx="6" fill="#1E293B" stroke="#334155" />
  <text x="900" y="56" fill="#38BDF8" font-size="11" font-weight="600">Notation : DevOps Pipeline</text>

  <!-- ==================== COLONNE 1 : DEVELOPPEMENT LOCAL ==================== -->
  <rect x="30" y="105" width="330" height="535" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow3)" />
  <rect x="30" y="105" width="330" height="38" rx="10" fill="#F1F5F9" />
  <text x="45" y="130" fill="#1E293B" font-size="13" font-weight="700">1. DEVELOPPEMENT LOCAL ETUDIANT</text>

  <!-- Boite 1 : Poste & IDE -->
  <rect x="45" y="155" width="300" height="85" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 172)">
    <rect width="36" height="36" rx="8" fill="#E0F2FE" />
    <path d="M 8 13 L 28 13 L 28 23 L 8 23 Z" fill="none" stroke="#0284C7" stroke-width="1.8" />
    <path d="M 5 26 L 31 26 C 31 26 29 23 28 23 L 8 23 C 7 23 5 26 5 26 Z" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.8" />
  </g>
  <text x="104" y="177" fill="#0F172A" font-size="12" font-weight="700">Poste Developpeur (Windows/WSL2/macOS)</text>
  <text x="104" y="195" fill="#64748B" font-size="11">IntelliJ IDEA / VS Code</text>
  <text x="104" y="211" fill="#64748B" font-size="11">Java 17 (OpenJDK) + Maven 3.9 (mvnw)</text>
  <text x="104" y="227" fill="#0284C7" font-size="10" font-weight="600">Base memoire H2 (Tests unitaires ultra-rapides)</text>

  <!-- Boite 2 : Qualite Statique -->
  <rect x="45" y="255" width="300" height="80" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 272)">
    <rect width="36" height="36" rx="8" fill="#DCFCE7" />
    <circle cx="16" cy="16" r="6" fill="none" stroke="#16A34A" stroke-width="2" />
    <line x1="21" y1="21" x2="27" y2="27" stroke="#16A34A" stroke-width="2" stroke-linecap="round" />
  </g>
  <text x="104" y="277" fill="#0F172A" font-size="12" font-weight="700">Analyse de Qualite Locale</text>
  <text x="104" y="295" fill="#64748B" font-size="11">Plugin SonarLint en temps reel dans l'IDE</text>
  <text x="104" y="311" fill="#15803D" font-size="10.5" font-weight="600">Regles Clean Code &amp; zero anomalie</text>

  <!-- Boite 3 : Git Workflow -->
  <rect x="45" y="350" width="300" height="85" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 368)">
    <rect width="36" height="36" rx="8" fill="#F3E8FF" />
    <circle cx="12" cy="12" r="3" fill="#9333EA" />
    <circle cx="12" cy="24" r="3" fill="#9333EA" />
    <circle cx="24" cy="12" r="3" fill="#9333EA" />
    <line x1="12" y1="15" x2="12" y2="21" stroke="#9333EA" stroke-width="2" />
    <path d="M 12 21 C 12 16 24 18 24 15" fill="none" stroke="#9333EA" stroke-width="2" />
  </g>
  <text x="104" y="372" fill="#0F172A" font-size="12" font-weight="700">Gestion de Versions Git</text>
  <text x="104" y="390" fill="#64748B" font-size="11">Branches feature/&lt;us-id&gt; isolees</text>
  <text x="104" y="406" fill="#64748B" font-size="11">Conventional Commits (feat:, fix:, test:)</text>
  <text x="104" y="422" fill="#9333EA" font-size="10" font-weight="600">Merge Requests &amp; Revue par les pairs</text>

  <!-- Boite 4 : Commande Push -->
  <rect x="45" y="450" width="300" height="60" rx="8" fill="#EFF6FF" stroke="#BFDBFE" />
  <g transform="translate(56, 460)">
    <rect width="28" height="28" rx="6" fill="#1E40AF" />
    <path d="M 8 11 L 13 14 L 8 17 M 14 18 L 19 18" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" />
  </g>
  <text x="96" y="475" fill="#1E40AF" font-size="11" font-weight="700">Declenchement CI</text>
  <text x="96" y="493" fill="#1D4ED8" font-size="10.5" font-weight="600">git push origin main (sur GitLab Univ-Lille)</text>

  <!-- Boite 5 : Validation Pre-Commit -->
  <rect x="45" y="525" width="300" height="95" rx="8" fill="#F0FDF4" stroke="#86EFAC" />
  <text x="56" y="548" fill="#166534" font-size="12" font-weight="700">Validation Locale Pre-Commit</text>
  <text x="56" y="567" fill="#15803D" font-size="11">• Commande : ./mvnw clean test</text>
  <text x="56" y="585" fill="#15803D" font-size="11">• Tests JUnit 5 : 0 echec, 0 erreur</text>
  <text x="56" y="603" fill="#166534" font-size="11" font-weight="700">• Couverture Jacoco >= 80%</text>

  <!-- FLECHE 1 -> 2 -->
  <line x1="360" y1="370" x2="398" y2="370" stroke="#0284C7" stroke-width="2.5" marker-end="url(#arrow-blue3)" />
  <text x="379" y="358" fill="#0284C7" font-size="9.5" font-weight="700" text-anchor="middle">Push</text>

  <!-- ==================== COLONNE 2 : GITLAB CI ==================== -->
  <rect x="405" y="105" width="330" height="535" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="2" filter="url(#shadow3)" />
  <rect x="405" y="105" width="330" height="38" rx="10" fill="#E0F2FE" />
  <text x="420" y="130" fill="#0369A1" font-size="13" font-weight="700">2. INTEGRATION CONTINUE (GITLAB CI)</text>

  <!-- Boite Forge Univ-Lille -->
  <rect x="420" y="155" width="300" height="85" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(432, 172)">
    <rect width="36" height="36" rx="8" fill="#FEF3C7" />
    <path d="M 18 29 L 10 11 L 14 11 L 18 21 L 22 11 L 26 11 Z" fill="#D97706" />
    <path d="M 18 29 L 10 11 L 7 19 C 6.5 21 7.2 23 9 24 Z" fill="#B45309" />
    <path d="M 18 29 L 26 11 L 29 19 C 29.5 21 28.8 23 27 24 Z" fill="#B45309" />
  </g>
  <text x="480" y="177" fill="#0F172A" font-size="12" font-weight="700">Forge GitLab Univ-Lille</text>
  <text x="480" y="195" fill="#64748B" font-size="11">Groupe : glop-garik-2026</text>
  <text x="480" y="211" fill="#64748B" font-size="11">4 depots de code independants (Polyrepo)</text>
  <text x="480" y="227" fill="#0284C7" font-size="10" font-weight="600">Runners mutualises campus</text>

  <!-- Boite Job CI Tests -->
  <rect x="420" y="255" width="300" height="95" rx="8" fill="#F0FDF4" stroke="#86EFAC" />
  <g transform="translate(432, 272)">
    <rect width="36" height="36" rx="8" fill="#DCFCE7" />
    <circle cx="18" cy="18" r="9" fill="none" stroke="#16A34A" stroke-width="2" />
    <path d="M 13 18 L 16 21 L 23 14" fill="none" stroke="#16A34A" stroke-width="2" stroke-linecap="round" />
  </g>
  <text x="480" y="275" fill="#166534" font-size="12" font-weight="700">Job CI : maven-tests</text>
  <text x="480" y="293" fill="#15803D" font-size="11">• Image : maven:3.9-eclipse-temurin-17</text>
  <text x="480" y="309" fill="#15803D" font-size="11">• Commande : mvn clean test jacoco:report</text>
  <text x="480" y="325" fill="#15803D" font-size="11">• Template autograding universitaire</text>
  <text x="480" y="341" fill="#166534" font-size="11" font-weight="700">Statut : SUCCESS (100% au vert)</text>

  <!-- Boite Docker Multi-Stage -->
  <rect x="420" y="365" width="300" height="95" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(432, 382)">
    <rect width="36" height="36" rx="8" fill="#E0F2FE" />
    <path d="M 8 19 L 26 19 C 27 19 28 17 27 15 C 25 12 21 12 20 14 C 18 11 12 12 11 15 C 9 15 8 17 8 19 Z" fill="#0284C7" />
    <rect x="11" y="13" width="2" height="2" fill="#FFFFFF" />
    <rect x="14" y="13" width="2" height="2" fill="#FFFFFF" />
    <rect x="17" y="13" width="2" height="2" fill="#FFFFFF" />
    <rect x="14" y="10" width="2" height="2" fill="#FFFFFF" />
  </g>
  <text x="480" y="385" fill="#0F172A" font-size="12" font-weight="700">Packaging Image Docker</text>
  <text x="480" y="403" fill="#64748B" font-size="11">• Multi-stage : Builder Maven + Runtime</text>
  <text x="480" y="419" fill="#15803D" font-size="10.5" font-weight="600">• Image legere Alpine JRE 17 (150 Mo)</text>
  <text x="480" y="435" fill="#64748B" font-size="10.5">• Gain de 75% d'empreinte disque</text>
  <text x="480" y="451" fill="#0284C7" font-size="10">Push sur Container Registry Univ</text>

  <!-- Boite Declencheur CD Deploiement -->
  <rect x="420" y="475" width="300" height="65" rx="8" fill="#FFFBEB" stroke="#FDE68A" />
  <text x="435" y="498" fill="#92400E" font-size="11.5" font-weight="700">Declenchement Deploiement CD</text>
  <text x="435" y="516" fill="#B45309" font-size="11">SSH Deploy securise vers VPS</text>
  <text x="435" y="532" fill="#92400E" font-size="10">Declenche apres succes des tests sur main</text>

  <!-- FLECHE 2 -> 3 -->
  <line x1="735" y1="370" x2="773" y2="370" stroke="#0284C7" stroke-width="2.5" marker-end="url(#arrow-blue3)" />
  <text x="754" y="358" fill="#0284C7" font-size="9.5" font-weight="700" text-anchor="middle">Deploy</text>

  <!-- ==================== COLONNE 3 : HEBERGEMENT VPS ==================== -->
  <rect x="780" y="105" width="330" height="535" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow3)" />
  <rect x="780" y="105" width="330" height="38" rx="10" fill="#FEF3C7" />
  <text x="795" y="130" fill="#92400E" font-size="13" font-weight="700">3. HEBERGEMENT PRODUCTION (VPS LINUX)</text>

  <!-- Boite Serveur VPS -->
  <rect x="795" y="155" width="300" height="85" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(806, 172)">
    <rect width="36" height="36" rx="8" fill="#F1F5F9" />
    <rect x="8" y="10" width="20" height="6" rx="1.5" fill="none" stroke="#475569" stroke-width="1.8" />
    <circle cx="12" cy="13" r="1" fill="#16A34A" />
    <rect x="8" y="19" width="20" height="6" rx="1.5" fill="none" stroke="#475569" stroke-width="1.8" />
    <circle cx="12" cy="22" r="1" fill="#16A34A" />
  </g>
  <text x="854" y="177" fill="#0F172A" font-size="12" font-weight="700">Serveur VPS Linux OVHcloud</text>
  <text x="854" y="195" fill="#64748B" font-size="11">Ubuntu Server 24.04 LTS (France / Roubaix)</text>
  <text x="854" y="211" fill="#15803D" font-size="10.5" font-weight="600">4 vCPU, 8 Go RAM, 50 Go NVMe</text>
  <text x="854" y="227" fill="#64748B" font-size="10">Cout fixe maitrise (~10-15 €/mois)</text>

  <!-- Boite Reverse Proxy Nginx & Cadenas SSL -->
  <rect x="795" y="255" width="300" height="95" rx="8" fill="#F0FDF4" stroke="#86EFAC" />
  <g transform="translate(806, 272)">
    <rect width="36" height="36" rx="8" fill="#DCFCE7" />
    <rect x="10" y="15" width="16" height="12" rx="2" fill="none" stroke="#16A34A" stroke-width="2" />
    <path d="M 13 15 L 13 11 C 13 8.5 15 7 18 7 C 21 7 23 8.5 23 11 L 23 15" fill="none" stroke="#16A34A" stroke-width="2" />
  </g>
  <text x="854" y="275" fill="#166534" font-size="12" font-weight="700">Reverse Proxy Nginx + SSL TLS</text>
  <text x="854" y="293" fill="#15803D" font-size="10.5">• Certificat Let's Encrypt automatique</text>
  <text x="854" y="309" fill="#475569" font-size="10.5">https://shoploc.garik.fr/ -&gt; Web UI (:3000)</text>
  <text x="854" y="325" fill="#475569" font-size="10.5">https://shoploc.garik.fr/api/ -&gt; Gateway (:8080)</text>
  <text x="854" y="341" fill="#166534" font-size="10" font-weight="600">Seuls les ports 80 et 443 sont publics</text>

  <!-- Boite Docker Compose & Reseau Isole -->
  <rect x="795" y="365" width="300" height="95" rx="8" fill="#EFF6FF" stroke="#BFDBFE" />
  <g transform="translate(806, 382)">
    <rect width="36" height="36" rx="8" fill="#E0F2FE" />
    <circle cx="18" cy="18" r="8" fill="none" stroke="#0284C7" stroke-width="1.8" />
    <line x1="18" y1="10" x2="18" y2="26" stroke="#0284C7" stroke-width="1.5" />
    <line x1="10" y1="18" x2="26" y2="18" stroke="#0284C7" stroke-width="1.5" />
  </g>
  <text x="854" y="385" fill="#1E40AF" font-size="12" font-weight="700">Docker Compose &amp; Reseau Isole</text>
  <text x="854" y="403" fill="#1D4ED8" font-size="10.5">• docker compose pull &amp;&amp; up -d</text>
  <text x="854" y="419" fill="#1D4ED8" font-size="10.5">• Reseau prive etanche : shoploc-net</text>
  <text x="854" y="435" fill="#475569" font-size="10">Microservices (8081-8084) cloisonnes</text>
  <text x="854" y="451" fill="#475569" font-size="10">BDD PostgreSQL (5432-5435) cloisonnees</text>

  <!-- Boite Persistance & Sante -->
  <rect x="795" y="475" width="300" height="85" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
  <text x="806" y="497" fill="#0F172A" font-size="11.5" font-weight="700">Persistance &amp; Sauvegardes</text>
  <text x="806" y="515" fill="#475569" font-size="10.5">• Volumes nommes persistants sur disque hote</text>
  <text x="806" y="531" fill="#0284C7" font-size="10.5">• Tache cron quotidienne : pg_dump (7 jours)</text>
  <text x="806" y="547" fill="#15803D" font-size="10.5" font-weight="600">• Healthchecks automatiques /actuator/health</text>

  <!-- LEGENDE DU BAS -->
  <rect x="30" y="660" width="1080" height="75" rx="8" fill="#1E293B" />
  <text x="50" y="682" fill="#F8FAFC" font-size="12" font-weight="700">ENGAGEMENT DEVOPS DE L'EQUIPE GARIK :</text>
  <text x="50" y="702" fill="#CBD5E1" font-size="11">• <tspan font-weight="700">Testabilite en Conditions Reelles :</tspan> Le code compile en local sous Java 17, passe la CI GitLab de l'universite et se deploie sur VPS Linux sous reverse proxy HTTPS.</text>
  <text x="50" y="720" fill="#CBD5E1" font-size="11">• <tspan font-weight="700">Pragmatisme Etudiant :</tspan> Rejet de Kubernetes pour privilegier une architecture Docker Compose simple, securisee et parfaitement maitrisee.</text>
</svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[OK] Figure 3 DevOps generee : {output_path}")


def main():
    project_root = Path(__file__).resolve().parent.parent.parent
    figures_dir = project_root / "agent_projet" / "docs" / "02_Architecture_Et_Outils_R2" / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    fig1 = figures_dir / "fig_1_contexte_systeme_shoploc.svg"
    fig2 = figures_dir / "fig_2_services_et_liaisons.svg"
    fig3 = figures_dir / "fig_3_chaine_outils_devops.svg"

    generate_fig1_context(fig1)
    generate_fig2_services(fig2)
    generate_fig3_devops(fig3)
    print(f"[SUCCES] Les 3 figures techniques officielles R2 ont ete generees dans : {figures_dir}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERATE R2 FIGURES - Generation des 2 Schemas Techniques Officiels pour le Livrable R2
Projet ShopLoc (MiageShopLoc) - M2 MIAGE GLOP 2026-2027

Deux diagrammes d'architecture hautement visuels enrichis d'icones vectorielles pures :
1. fig_1_contexte_systeme_shoploc.svg : Contexte C4 & Architecture Globale des Services (Clients, Gateway, 4 Microservices, 4 BDD, 3 Stubs)
2. fig_2_chaine_outils_devops.svg : Chaine DevOps, CI/CD GitLab et Hebergement Production Reelle sur VPS Linux
"""

import os
from pathlib import Path


def generate_fig1_context(output_path: Path):
    """Schema 1 : Contexte Technique & Architecture des Microservices (C4 Niveau 1/2)."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1140 760" width="100%" height="100%" style="background-color: #F8FAFC; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#0F172A" flood-opacity="0.08" />
    </filter>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#0284C7" />
    </marker>
    <marker id="arrow-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#D97706" />
    </marker>
  </defs>

  <!-- En-tete du schema -->
  <rect x="30" y="20" width="1080" height="64" rx="8" fill="#0F172A" filter="url(#shadow)" />
  <text x="50" y="48" fill="#F8FAFC" font-size="18" font-weight="700">SCHEMA 1 : CONTEXTE TECHNIQUE &amp; ARCHITECTURE DES MICROSERVICES</text>
  <text x="50" y="68" fill="#94A3B8" font-size="12">ShopLoc - Architecture Microservices Distribuee | M2 MIAGE GLOP / Cours ALOM Universite de Lille</text>
  <rect x="910" y="36" width="180" height="30" rx="6" fill="#1E293B" stroke="#334155" />
  <text x="930" y="56" fill="#38BDF8" font-size="11" font-weight="600">Notation : C4 Architecture</text>

  <!-- ==================== COLONNE 1 : CANAUX CLIENTS ==================== -->
  <rect x="30" y="105" width="260" height="535" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow)" />
  <rect x="30" y="105" width="260" height="38" rx="10" fill="#F1F5F9" />
  <text x="45" y="130" fill="#1E293B" font-size="13" font-weight="700">CANAUX CLIENTS (FRONT-END)</text>

  <!-- Client 1 : Citoyen Web (Icone Ecran / Web) -->
  <rect x="45" y="155" width="230" height="78" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 172)">
    <rect width="36" height="36" rx="8" fill="#E0F2FE" />
    <!-- Icone Ecran Ordinateur -->
    <path d="M 8 11 L 28 11 C 29 11 30 12 30 13 L 30 23 C 30 24 29 25 28 25 L 8 25 C 7 25 6 24 6 23 L 6 13 C 6 12 7 11 8 11 Z" fill="none" stroke="#0284C7" stroke-width="2" />
    <line x1="18" y1="25" x2="18" y2="29" stroke="#0284C7" stroke-width="2" />
    <line x1="13" y1="29" x2="23" y2="29" stroke="#0284C7" stroke-width="2" stroke-linecap="round" />
  </g>
  <text x="102" y="180" fill="#0F172A" font-size="12.5" font-weight="700">Client Web Citoyen</text>
  <text x="102" y="197" fill="#64748B" font-size="11">React 18 / TypeScript (:3000)</text>
  <text x="102" y="213" fill="#0284C7" font-size="10" font-weight="600">HTTPS / REST JSON</text>

  <!-- Client 2 : Commercant Web (Icone Boutique) -->
  <rect x="45" y="245" width="230" height="78" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 262)">
    <rect width="36" height="36" rx="8" fill="#DCFCE7" />
    <!-- Icone Magasin / Store -->
    <path d="M 8 15 L 28 15 L 26 27 C 26 28 25 29 24 29 L 12 29 C 11 29 10 28 10 27 Z" fill="none" stroke="#16A34A" stroke-width="2" />
    <path d="M 6 15 L 18 9 L 30 15 Z" fill="none" stroke="#16A34A" stroke-width="2" />
    <rect x="15" y="21" width="6" height="8" fill="#16A34A" />
  </g>
  <text x="102" y="270" fill="#0F172A" font-size="12.5" font-weight="700">Portail Commercant</text>
  <text x="102" y="287" fill="#64748B" font-size="11">React 18 Back-Office</text>
  <text x="102" y="303" fill="#16A34A" font-size="10" font-weight="600">Stocks &amp; Validation VFP</text>

  <!-- Client 3 : Terminal Mobile (Icone Smartphone) -->
  <rect x="45" y="335" width="230" height="78" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 352)">
    <rect width="36" height="36" rx="8" fill="#F1F5F9" />
    <!-- Icone Smartphone -->
    <rect x="11" y="8" width="14" height="22" rx="3" fill="none" stroke="#475569" stroke-width="2" />
    <circle cx="18" cy="25" r="1.5" fill="#475569" />
    <line x1="15" y1="11" x2="21" y2="11" stroke="#475569" stroke-width="1.5" stroke-linecap="round" />
  </g>
  <text x="102" y="360" fill="#0F172A" font-size="12.5" font-weight="700">Terminal Caisse (PWA)</text>
  <text x="102" y="377" fill="#64748B" font-size="11">Scanner Mobile Commercant</text>
  <text x="102" y="393" fill="#475569" font-size="10" font-weight="600">Scan QR Code &amp; Retrait</text>

  <!-- Client 4 : Console Mairie (Icone Batiment) -->
  <rect x="45" y="425" width="230" height="78" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 442)">
    <rect width="36" height="36" rx="8" fill="#F3E8FF" />
    <!-- Icone Batiment Mairie -->
    <path d="M 8 28 L 28 28 M 10 28 L 10 16 L 18 10 L 26 16 L 26 28" fill="none" stroke="#9333EA" stroke-width="2" />
    <rect x="13" y="19" width="3" height="4" fill="#9333EA" />
    <rect x="20" y="19" width="3" height="4" fill="#9333EA" />
  </g>
  <text x="102" y="450" fill="#0F172A" font-size="12.5" font-weight="700">Console Mairie</text>
  <text x="102" y="467" fill="#64748B" font-size="11">Tableau de Bord Territorial</text>
  <text x="102" y="483" fill="#9333EA" font-size="10" font-weight="600">Statistiques Anonymisees</text>

  <!-- Client 5 : Console Exploitation (Icone Rouages) -->
  <rect x="45" y="515" width="230" height="78" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 532)">
    <rect width="36" height="36" rx="8" fill="#FEF3C7" />
    <!-- Icone Rouages / Maintenance -->
    <circle cx="18" cy="18" r="4" fill="none" stroke="#D97706" stroke-width="2" />
    <path d="M 18 9 L 18 12 M 18 24 L 18 27 M 9 18 L 12 18 M 24 18 L 27 18 M 12 12 L 14 14 M 22 22 L 24 24 M 12 24 L 14 22 M 22 14 L 24 12" stroke="#D97706" stroke-width="2" stroke-linecap="round" />
  </g>
  <text x="102" y="540" fill="#0F172A" font-size="12.5" font-weight="700">Console Exploitation</text>
  <text x="102" y="557" fill="#64748B" font-size="11">Administration &amp; Sante</text>
  <text x="102" y="573" fill="#D97706" font-size="10" font-weight="600">Endpoints /actuator</text>


  <!-- FLECHE CLIENTS -> GATEWAY -->
  <line x1="290" y1="370" x2="338" y2="370" stroke="#0284C7" stroke-width="2.5" marker-end="url(#arrow-blue)" />
  <text x="314" y="358" fill="#0284C7" font-size="9.5" font-weight="700" text-anchor="middle">HTTPS</text>
  <text x="314" y="386" fill="#64748B" font-size="8.5" text-anchor="middle">:8080</text>


  <!-- ==================== COLONNE 2 : SYSTEME SHOPLOC ==================== -->
  <rect x="340" y="105" width="460" height="535" rx="12" fill="#F0F9FF" stroke="#0284C7" stroke-width="2" filter="url(#shadow)" />
  <rect x="340" y="105" width="460" height="38" rx="12" fill="#0284C7" />
  <text x="570" y="130" fill="#F8FAFC" font-size="14" font-weight="800" text-anchor="middle">SYSTEME MICROSERVICES SHOPLOC</text>

  <!-- Point d'entree : API Gateway -->
  <rect x="358" y="155" width="424" height="60" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5" />
  <g transform="translate(370, 168)">
    <rect width="34" height="34" rx="7" fill="#E0F2FE" />
    <!-- Icone Bouclier / Passerelle -->
    <path d="M 17 8 L 26 12 L 26 19 C 26 24 17 28 17 28 C 17 28 8 24 8 19 L 8 12 Z" fill="none" stroke="#0284C7" stroke-width="2" />
    <path d="M 14 18 L 16 20 L 21 15" fill="none" stroke="#0284C7" stroke-width="2" stroke-linecap="round" />
  </g>
  <text x="415" y="180" fill="#0F172A" font-size="13" font-weight="700">shoploc-api-gateway (Spring Cloud Gateway : 8080)</text>
  <text x="415" y="198" fill="#0369A1" font-size="11">Routage dynamique, validation des jetons JWT, gestion unifiee CORS</text>

  <!-- Microservice 1 : Auth Service -->
  <rect x="358" y="230" width="270" height="80" rx="8" fill="#FFFFFF" stroke="#CBD5E1" />
  <g transform="translate(370, 245)">
    <rect width="32" height="32" rx="6" fill="#F1F5F9" />
    <!-- Icone Cle / Auth -->
    <circle cx="14" cy="15" r="4" fill="none" stroke="#475569" stroke-width="2" />
    <path d="M 17 17 L 24 24 M 21 21 L 23 19" stroke="#475569" stroke-width="2" stroke-linecap="round" />
  </g>
  <text x="412" y="254" fill="#0F172A" font-size="12" font-weight="700">shoploc-auth-service (:8081)</text>
  <text x="412" y="271" fill="#64748B" font-size="11">Spring Boot 3.3 / Spring Security</text>
  <text x="412" y="287" fill="#0284C7" font-size="10">Authentification, RBAC &amp; JWT</text>

  <!-- BDD 1 : auth_db (Cylindre) -->
  <rect x="640" y="230" width="142" height="80" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
  <g transform="translate(650, 248)">
    <path d="M 2 6 C 2 3.8 7.4 2 14 2 C 20.6 2 26 3.8 26 6 L 26 18 C 26 20.2 20.6 22 14 22 C 7.4 22 2 20.2 2 18 Z" fill="#E2E8F0" stroke="#475569" stroke-width="1.5" />
    <path d="M 2 6 C 2 8.2 7.4 10 14 10 C 20.6 10 26 8.2 26 6" fill="none" stroke="#475569" stroke-width="1.5" />
    <path d="M 2 12 C 2 14.2 7.4 16 14 16 C 20.6 16 26 14.2 26 12" fill="none" stroke="#475569" stroke-width="1.5" />
  </g>
  <text x="686" y="256" fill="#1E293B" font-size="11" font-weight="700">auth_db</text>
  <text x="686" y="272" fill="#64748B" font-size="10">PostgreSQL 16</text>
  <text x="686" y="288" fill="#0284C7" font-size="9.5">Port 5432</text>

  <!-- Microservice 2 : Merchant Catalog Service -->
  <rect x="358" y="325" width="270" height="85" rx="8" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.5" />
  <g transform="translate(370, 342)">
    <rect width="32" height="32" rx="6" fill="#DCFCE7" />
    <!-- Icone Boite / Produit -->
    <path d="M 6 11 L 16 6 L 26 11 L 16 16 Z" fill="none" stroke="#16A34A" stroke-width="1.8" />
    <path d="M 6 11 L 6 22 L 16 27 L 16 16" fill="none" stroke="#16A34A" stroke-width="1.8" />
    <path d="M 26 11 L 26 22 L 16 27" fill="none" stroke="#16A34A" stroke-width="1.8" />
  </g>
  <text x="412" y="348" fill="#166534" font-size="12" font-weight="800">shoploc-merchant-catalog-service</text>
  <text x="412" y="365" fill="#64748B" font-size="11">Port 8082 | Produits, boutiques, stocks</text>
  <text x="412" y="381" fill="#15803D" font-size="10" font-weight="600">Verrou temporaire stock (2PC)</text>

  <!-- BDD 2 : catalog_db (Cylindre Vert) -->
  <rect x="640" y="325" width="142" height="85" rx="8" fill="#F0FDF4" stroke="#86EFAC" />
  <g transform="translate(650, 345)">
    <path d="M 2 6 C 2 3.8 7.4 2 14 2 C 20.6 2 26 3.8 26 6 L 26 18 C 26 20.2 20.6 22 14 22 C 7.4 22 2 20.2 2 18 Z" fill="#BBF7D0" stroke="#16A34A" stroke-width="1.5" />
    <path d="M 2 6 C 2 8.2 7.4 10 14 10 C 20.6 10 26 8.2 26 6" fill="none" stroke="#16A34A" stroke-width="1.5" />
    <path d="M 2 12 C 2 14.2 7.4 16 14 16 C 20.6 16 26 14.2 26 12" fill="none" stroke="#16A34A" stroke-width="1.5" />
  </g>
  <text x="686" y="352" fill="#166534" font-size="11" font-weight="700">catalog_db</text>
  <text x="686" y="368" fill="#64748B" font-size="10">PostgreSQL 16</text>
  <text x="686" y="384" fill="#15803D" font-size="9.5">Port 5433</text>

  <!-- Microservice 3 : Cart Order Service -->
  <rect x="358" y="425" width="270" height="85" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5" />
  <g transform="translate(370, 442)">
    <rect width="32" height="32" rx="6" fill="#E0F2FE" />
    <!-- Icone Panier -->
    <path d="M 7 9 L 10 9 L 13 22 L 25 22 L 27 12 L 11 12" fill="none" stroke="#0284C7" stroke-width="1.8" />
    <circle cx="14" cy="25" r="1.8" fill="#0284C7" />
    <circle cx="23" cy="25" r="1.8" fill="#0284C7" />
  </g>
  <text x="412" y="448" fill="#0369A1" font-size="12" font-weight="800">shoploc-cart-order-service</text>
  <text x="412" y="465" fill="#64748B" font-size="11">Port 8083 | Panier Click &amp; Collect</text>
  <text x="412" y="481" fill="#0284C7" font-size="10" font-weight="600">Coordinateur 2PC (RestClient)</text>

  <!-- BDD 3 : order_db (Cylindre Bleu) -->
  <rect x="640" y="425" width="142" height="85" rx="8" fill="#F0F9FF" stroke="#BAE6FD" />
  <g transform="translate(650, 445)">
    <path d="M 2 6 C 2 3.8 7.4 2 14 2 C 20.6 2 26 3.8 26 6 L 26 18 C 26 20.2 20.6 22 14 22 C 7.4 22 2 20.2 2 18 Z" fill="#BAE6FD" stroke="#0284C7" stroke-width="1.5" />
    <path d="M 2 6 C 2 8.2 7.4 10 14 10 C 20.6 10 26 8.2 26 6" fill="none" stroke="#0284C7" stroke-width="1.5" />
    <path d="M 2 12 C 2 14.2 7.4 16 14 16 C 20.6 16 26 14.2 26 12" fill="none" stroke="#0284C7" stroke-width="1.5" />
  </g>
  <text x="686" y="452" fill="#0369A1" font-size="11" font-weight="700">order_db</text>
  <text x="686" y="468" fill="#64748B" font-size="10">PostgreSQL 16</text>
  <text x="686" y="484" fill="#0284C7" font-size="9.5">Port 5434</text>

  <!-- Microservice 4 : Loyalty Service -->
  <rect x="358" y="525" width="270" height="80" rx="8" fill="#FFFFFF" stroke="#CBD5E1" />
  <g transform="translate(370, 540)">
    <rect width="32" height="32" rx="6" fill="#F3E8FF" />
    <!-- Icone Etoile / Fidelite -->
    <path d="M 16 8 L 18.5 13.5 L 24.5 14 L 20 18 L 21.5 24 L 16 21 L 10.5 24 L 12 18 L 7.5 14 L 13.5 13.5 Z" fill="none" stroke="#9333EA" stroke-width="1.8" />
  </g>
  <text x="412" y="548" fill="#0F172A" font-size="12" font-weight="700">shoploc-loyalty-service (:8084)</text>
  <text x="412" y="565" fill="#64748B" font-size="11">Cagnotte VFP (15 jours glissants)</text>
  <text x="412" y="581" fill="#9333EA" font-size="10">Bons bus &amp; stationnement</text>

  <!-- BDD 4 : loyalty_db (Cylindre Violet) -->
  <rect x="640" y="525" width="142" height="80" rx="8" fill="#FAF5FF" stroke="#E9D5FF" />
  <g transform="translate(650, 543)">
    <path d="M 2 6 C 2 3.8 7.4 2 14 2 C 20.6 2 26 3.8 26 6 L 26 18 C 26 20.2 20.6 22 14 22 C 7.4 22 2 20.2 2 18 Z" fill="#E9D5FF" stroke="#9333EA" stroke-width="1.5" />
    <path d="M 2 6 C 2 8.2 7.4 10 14 10 C 20.6 10 26 8.2 26 6" fill="none" stroke="#9333EA" stroke-width="1.5" />
    <path d="M 2 12 C 2 14.2 7.4 16 14 16 C 20.6 16 26 14.2 26 12" fill="none" stroke="#9333EA" stroke-width="1.5" />
  </g>
  <text x="686" y="550" fill="#6B21A8" font-size="11" font-weight="700">loyalty_db</text>
  <text x="686" y="566" fill="#64748B" font-size="10">PostgreSQL 16</text>
  <text x="686" y="582" fill="#9333EA" font-size="9.5">Port 5435</text>

  <!-- Liaison synchrone 2PC entre commande et catalogue -->
  <path d="M 490 425 L 490 412" fill="none" stroke="#16A34A" stroke-width="2.5" marker-end="url(#arrow-blue)" />


  <!-- FLECHE GATEWAY -> STUBS EXTERNES -->
  <line x1="800" y1="370" x2="848" y2="370" stroke="#D97706" stroke-width="2.5" marker-end="url(#arrow-amber)" />
  <text x="824" y="358" fill="#D97706" font-size="9.5" font-weight="700" text-anchor="middle">REST</text>
  <text x="824" y="386" fill="#64748B" font-size="8.5" text-anchor="middle">Stubs</text>


  <!-- ==================== COLONNE 3 : SERVICES PARTENAIRES (STUBS) ==================== -->
  <rect x="850" y="105" width="260" height="535" rx="10" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1.5" filter="url(#shadow)" />
  <rect x="850" y="105" width="260" height="38" rx="10" fill="#FEF3C7" />
  <text x="865" y="130" fill="#92400E" font-size="13" font-weight="700">SERVICES PARTENAIRES (STUBS)</text>

  <!-- Stub 1 : Simulateur Bancaire -->
  <rect x="865" y="175" width="230" height="95" rx="8" fill="#FFFBEB" stroke="#FDE68A" />
  <g transform="translate(876, 192)">
    <rect width="34" height="34" rx="7" fill="#FDE68A" />
    <!-- Icone Carte Bancaire -->
    <rect x="6" y="10" width="22" height="15" rx="2" fill="none" stroke="#B45309" stroke-width="1.8" />
    <line x1="6" y1="14" x2="28" y2="14" stroke="#B45309" stroke-width="2" />
    <rect x="9" y="18" width="4" height="3" fill="#B45309" />
  </g>
  <text x="920" y="200" fill="#92400E" font-size="12" font-weight="700">Simulateur Banque</text>
  <text x="920" y="217" fill="#64748B" font-size="11">Stub REST HTTP (:8090)</text>
  <text x="920" y="233" fill="#B45309" font-size="10">POST /api/bank/authorize</text>
  <text x="920" y="249" fill="#475569" font-size="9.5">Debit carte simule</text>

  <!-- Stub 2 : Transports Ilevia -->
  <rect x="865" y="315" width="230" height="95" rx="8" fill="#FFFBEB" stroke="#FDE68A" />
  <g transform="translate(876, 332)">
    <rect width="34" height="34" rx="7" fill="#FDE68A" />
    <!-- Icone Bus / Tram -->
    <rect x="9" y="8" width="16" height="18" rx="3" fill="none" stroke="#B45309" stroke-width="1.8" />
    <circle cx="12" cy="23" r="1.5" fill="#B45309" />
    <circle cx="22" cy="23" r="1.5" fill="#B45309" />
    <line x1="11" y1="13" x2="23" y2="13" stroke="#B45309" stroke-width="1.5" />
  </g>
  <text x="920" y="340" fill="#92400E" font-size="12" font-weight="700">Simulateur Ilevia</text>
  <text x="920" y="357" fill="#64748B" font-size="11">Stub Transports (:8091)</text>
  <text x="920" y="373" fill="#B45309" font-size="10">POST /api/ilevia/ticket</text>
  <text x="920" y="389" fill="#475569" font-size="9.5">Titres bus &amp; tramway</text>

  <!-- Stub 3 : Voirie Parking -->
  <rect x="865" y="455" width="230" height="95" rx="8" fill="#FFFBEB" stroke="#FDE68A" />
  <g transform="translate(876, 472)">
    <rect width="34" height="34" rx="7" fill="#FDE68A" />
    <!-- Icone Parking (P) -->
    <rect x="8" y="8" width="18" height="18" rx="3" fill="none" stroke="#B45309" stroke-width="1.8" />
    <path d="M 14 20 L 14 12 L 18 12 C 19.5 12 20.5 13 20.5 14.5 C 20.5 16 19.5 17 18 17 L 14 17" fill="none" stroke="#B45309" stroke-width="1.8" />
  </g>
  <text x="920" y="480" fill="#92400E" font-size="12" font-weight="700">Simulateur Parking</text>
  <text x="920" y="497" fill="#64748B" font-size="11">Stub Voirie (:8092)</text>
  <text x="920" y="513" fill="#B45309" font-size="10">POST /api/parking/voucher</text>
  <text x="920" y="529" fill="#475569" font-size="9.5">Franchise stationnement</text>


  <!-- ==================== LEGENDE DU BAS ==================== -->
  <rect x="30" y="660" width="1080" height="75" rx="8" fill="#1E293B" />
  <text x="50" y="682" fill="#F8FAFC" font-size="12" font-weight="700">LEGENDE DES CHOIX D'ARCHITECTURE ALOM :</text>
  <text x="50" y="702" fill="#CBD5E1" font-size="11">• <tspan font-weight="700">Database-per-Service Stricte :</tspan> 4 bases PostgreSQL autonomes sur 4 ports distincts (5432 a 5435). Aucune jointure SQL inter-services.</text>
  <text x="50" y="720" fill="#CBD5E1" font-size="11">• <tspan font-weight="700">Point d'Entree Unique :</tspan> Seule l'API Gateway (8080) est exposee, garantissant l'isolation des microservices et la centralisation JWT.</text>
</svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[OK] Figure 1 technique generee : {output_path}")


def generate_fig2_devops(output_path: Path):
    """Schema 2 : Chaine DevOps, CI/CD GitLab et Hebergement Production Reelle sur VPS Linux."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1140 760" width="100%" height="100%" style="background-color: #F8FAFC; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#0F172A" flood-opacity="0.08" />
    </filter>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#0284C7" />
    </marker>
  </defs>

  <!-- En-tete du schema -->
  <rect x="30" y="20" width="1080" height="64" rx="8" fill="#0F172A" filter="url(#shadow)" />
  <text x="50" y="48" fill="#F8FAFC" font-size="18" font-weight="700">SCHEMA 2 : CHAINE DEVOPS, CI/CD ET HEBERGEMENT EN PRODUCTION REELLE</text>
  <text x="50" y="68" fill="#94A3B8" font-size="12">Developpement Local, Integration Continue GitLab Univ-Lille et Deploiement VPS Linux</text>
  <rect x="880" y="36" width="210" height="30" rx="6" fill="#1E293B" stroke="#334155" />
  <text x="900" y="56" fill="#38BDF8" font-size="11" font-weight="600">Notation : DevOps Pipeline</text>

  <!-- ==================== COLONNE 1 : DEVELOPPEMENT LOCAL ==================== -->
  <rect x="30" y="105" width="330" height="535" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow)" />
  <rect x="30" y="105" width="330" height="38" rx="10" fill="#F1F5F9" />
  <text x="45" y="130" fill="#1E293B" font-size="13" font-weight="700">1. DEVELOPPEMENT LOCAL ETUDIANT</text>

  <!-- Boite 1 : Poste & IDE (Icone Laptop) -->
  <rect x="45" y="155" width="300" height="85" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 172)">
    <rect width="36" height="36" rx="8" fill="#E0F2FE" />
    <!-- Icone Ordinateur Portable -->
    <path d="M 8 13 L 28 13 L 28 23 L 8 23 Z" fill="none" stroke="#0284C7" stroke-width="1.8" />
    <path d="M 5 26 L 31 26 C 31 26 29 23 28 23 L 8 23 C 7 23 5 26 5 26 Z" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.8" />
  </g>
  <text x="104" y="177" fill="#0F172A" font-size="12" font-weight="700">Poste Developpeur</text>
  <text x="104" y="195" fill="#64748B" font-size="11">IntelliJ IDEA / VS Code</text>
  <text x="104" y="211" fill="#64748B" font-size="11">Java 17 (OpenJDK) + Maven 3.9</text>
  <text x="104" y="227" fill="#0284C7" font-size="10" font-weight="600">Base memoire H2 (Tests ultra-rapides)</text>

  <!-- Boite 2 : Qualite Statique (Icone Verification / Scan) -->
  <rect x="45" y="255" width="300" height="80" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 272)">
    <rect width="36" height="36" rx="8" fill="#DCFCE7" />
    <!-- Icone Loupe Qualite -->
    <circle cx="16" cy="16" r="6" fill="none" stroke="#16A34A" stroke-width="2" />
    <line x1="21" y1="21" x2="27" y2="27" stroke="#16A34A" stroke-width="2" stroke-linecap="round" />
  </g>
  <text x="104" y="277" fill="#0F172A" font-size="12" font-weight="700">Analyse de Qualite Locale</text>
  <text x="104" y="295" fill="#64748B" font-size="11">Plugin SonarLint en temps reel</text>
  <text x="104" y="311" fill="#15803D" font-size="10.5" font-weight="600">Zero serveur distant lourd (Sobriete)</text>

  <!-- Boite 3 : Git Workflow (Icone Branches Git) -->
  <rect x="45" y="350" width="300" height="85" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(56, 368)">
    <rect width="36" height="36" rx="8" fill="#F3E8FF" />
    <!-- Icone Branches Git -->
    <circle cx="12" cy="12" r="3" fill="#9333EA" />
    <circle cx="12" cy="24" r="3" fill="#9333EA" />
    <circle cx="24" cy="12" r="3" fill="#9333EA" />
    <line x1="12" y1="15" x2="12" y2="21" stroke="#9333EA" stroke-width="2" />
    <path d="M 12 21 C 12 16 24 18 24 15" fill="none" stroke="#9333EA" stroke-width="2" />
  </g>
  <text x="104" y="372" fill="#0F172A" font-size="12" font-weight="700">Gestion de Versions Git</text>
  <text x="104" y="390" fill="#64748B" font-size="11">Branches feature/&lt;nom&gt;</text>
  <text x="104" y="406" fill="#64748B" font-size="11">Conventional Commits (feat:, fix:)</text>
  <text x="104" y="422" fill="#9333EA" font-size="10" font-weight="600">Revue de code par les pairs</text>

  <!-- Boite 4 : Commande Push (Icone Terminal) -->
  <rect x="45" y="450" width="300" height="60" rx="8" fill="#EFF6FF" stroke="#BFDBFE" />
  <g transform="translate(56, 460)">
    <rect width="28" height="28" rx="6" fill="#1E40AF" />
    <path d="M 8 11 L 13 14 L 8 17 M 14 18 L 19 18" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" />
  </g>
  <text x="96" y="475" fill="#1E40AF" font-size="11" font-weight="700">Declenchement CI</text>
  <text x="96" y="493" fill="#1D4ED8" font-size="10.5" font-weight="600">git push origin main (sur GitLab)</text>

  <!-- Boite 5 : Validation Pre-Commit -->
  <rect x="45" y="525" width="300" height="95" rx="8" fill="#F0FDF4" stroke="#86EFAC" />
  <text x="56" y="548" fill="#166534" font-size="12" font-weight="700">Validation Locale Pre-Commit</text>
  <text x="56" y="567" fill="#15803D" font-size="11">• Commande : mvn clean test</text>
  <text x="56" y="585" fill="#15803D" font-size="11">• Tests JUnit 5 : 0 echec, 0 erreur</text>
  <text x="56" y="603" fill="#166534" font-size="11" font-weight="700">• Couverture Jacoco >= 80%</text>


  <!-- FLECHE 1 -> 2 -->
  <line x1="360" y1="370" x2="398" y2="370" stroke="#0284C7" stroke-width="2.5" marker-end="url(#arrow-blue)" />
  <text x="379" y="358" fill="#0284C7" font-size="9.5" font-weight="700" text-anchor="middle">Push</text>


  <!-- ==================== COLONNE 2 : GITLAB CI ==================== -->
  <rect x="405" y="105" width="330" height="535" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="2" filter="url(#shadow)" />
  <rect x="405" y="105" width="330" height="38" rx="10" fill="#E0F2FE" />
  <text x="420" y="130" fill="#0369A1" font-size="13" font-weight="700">2. INTEGRATION CONTINUE (GITLAB CI)</text>

  <!-- Boite Forge Univ-Lille (Icone Renard GitLab) -->
  <rect x="420" y="155" width="300" height="85" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(432, 172)">
    <rect width="36" height="36" rx="8" fill="#FEF3C7" />
    <!-- Icone Renard GitLab -->
    <path d="M 18 29 L 10 11 L 14 11 L 18 21 L 22 11 L 26 11 Z" fill="#D97706" />
    <path d="M 18 29 L 10 11 L 7 19 C 6.5 21 7.2 23 9 24 Z" fill="#B45309" />
    <path d="M 18 29 L 26 11 L 29 19 C 29.5 21 28.8 23 27 24 Z" fill="#B45309" />
  </g>
  <text x="480" y="177" fill="#0F172A" font-size="12" font-weight="700">Forge GitLab Univ-Lille</text>
  <text x="480" y="195" fill="#64748B" font-size="11">Groupe : glop-garik-2026</text>
  <text x="480" y="211" fill="#64748B" font-size="11">4 depots de code independants</text>
  <text x="480" y="227" fill="#0284C7" font-size="10" font-weight="600">Runners mutualises campus</text>

  <!-- Boite Job CI Tests (Icone Validation Verte) -->
  <rect x="420" y="255" width="300" height="95" rx="8" fill="#F0FDF4" stroke="#86EFAC" />
  <g transform="translate(432, 272)">
    <rect width="36" height="36" rx="8" fill="#DCFCE7" />
    <!-- Icone Check / Succes -->
    <circle cx="18" cy="18" r="9" fill="none" stroke="#16A34A" stroke-width="2" />
    <path d="M 13 18 L 16 21 L 23 14" fill="none" stroke="#16A34A" stroke-width="2" stroke-linecap="round" />
  </g>
  <text x="480" y="275" fill="#166534" font-size="12" font-weight="700">Job CI : maven-tests</text>
  <text x="480" y="293" fill="#15803D" font-size="11">• Image : maven:3.9-eclipse-temurin-17</text>
  <text x="480" y="309" fill="#15803D" font-size="11">• Commande : mvn clean test</text>
  <text x="480" y="325" fill="#15803D" font-size="11">• Template autograding universitaire</text>
  <text x="480" y="341" fill="#166534" font-size="11" font-weight="700">Statut : SUCCESS (100% au vert)</text>

  <!-- Boite Docker Multi-Stage (Icone Baleine Docker) -->
  <rect x="420" y="365" width="300" height="95" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(432, 382)">
    <rect width="36" height="36" rx="8" fill="#E0F2FE" />
    <!-- Icone Baleine Docker -->
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
  <text x="435" y="516" fill="#B45309" font-size="11">Webhook / SSH Deploy securise vers VPS</text>
  <text x="435" y="532" fill="#92400E" font-size="10">Declenche apres succes des tests sur main</text>


  <!-- FLECHE 2 -> 3 -->
  <line x1="735" y1="370" x2="773" y2="370" stroke="#0284C7" stroke-width="2.5" marker-end="url(#arrow-blue)" />
  <text x="754" y="358" fill="#0284C7" font-size="9.5" font-weight="700" text-anchor="middle">Deploy</text>


  <!-- ==================== COLONNE 3 : HEBERGEMENT VPS ==================== -->
  <rect x="780" y="105" width="330" height="535" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow)" />
  <rect x="780" y="105" width="330" height="38" rx="10" fill="#FEF3C7" />
  <text x="795" y="130" fill="#92400E" font-size="13" font-weight="700">3. HEBERGEMENT PRODUCTION (VPS LINUX)</text>

  <!-- Boite Serveur VPS (Icone Rack Serveur) -->
  <rect x="795" y="155" width="300" height="85" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <g transform="translate(806, 172)">
    <rect width="36" height="36" rx="8" fill="#F1F5F9" />
    <!-- Icone Rack Serveur -->
    <rect x="8" y="10" width="20" height="6" rx="1.5" fill="none" stroke="#475569" stroke-width="1.8" />
    <circle cx="12" cy="13" r="1" fill="#16A34A" />
    <rect x="8" y="19" width="20" height="6" rx="1.5" fill="none" stroke="#475569" stroke-width="1.8" />
    <circle cx="12" cy="22" r="1" fill="#16A34A" />
  </g>
  <text x="854" y="177" fill="#0F172A" font-size="12" font-weight="700">Serveur VPS Linux Dedie</text>
  <text x="854" y="195" fill="#64748B" font-size="11">Ubuntu Server 24.04 LTS (France)</text>
  <text x="854" y="211" fill="#15803D" font-size="10.5" font-weight="600">4 vCPU, 8 Go RAM, 50 Go NVMe</text>
  <text x="854" y="227" fill="#64748B" font-size="10">Cout fixe maitrise (~10-15 €/mois)</text>

  <!-- Boite Reverse Proxy Nginx & Cadenas SSL -->
  <rect x="795" y="255" width="300" height="95" rx="8" fill="#F0FDF4" stroke="#86EFAC" />
  <g transform="translate(806, 272)">
    <rect width="36" height="36" rx="8" fill="#DCFCE7" />
    <!-- Icone Cadenas SSL / Securite -->
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
    <!-- Icone Reseau Interne -->
    <circle cx="18" cy="18" r="8" fill="none" stroke="#0284C7" stroke-width="1.8" />
    <line x1="18" y1="10" x2="18" y2="26" stroke="#0284C7" stroke-width="1.5" />
    <line x1="10" y1="18" x2="26" y2="18" stroke="#0284C7" stroke-width="1.5" />
  </g>
  <text x="854" y="385" fill="#1E40AF" font-size="12" font-weight="700">Docker Compose &amp; Reseau Isole</text>
  <text x="854" y="403" fill="#1D4ED8" font-size="10.5">• docker compose pull &amp;&amp; up -d</text>
  <text x="854" y="419" fill="#1D4ED8" font-size="10.5">• Reseau prive : shoploc-net</text>
  <text x="854" y="435" fill="#475569" font-size="10">Microservices (8081-8084) cloisonnes</text>
  <text x="854" y="451" fill="#475569" font-size="10">BDD PostgreSQL (5432-5435) cloisonnees</text>

  <!-- Boite Persistance & Sante -->
  <rect x="795" y="475" width="300" height="85" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
  <text x="806" y="497" fill="#0F172A" font-size="11.5" font-weight="700">Persistance &amp; Sauvegardes</text>
  <text x="806" y="515" fill="#475569" font-size="10.5">• Volumes nommes persistants sur disque hote</text>
  <text x="806" y="531" fill="#0284C7" font-size="10.5">• Tache cron quotidienne : pg_dump (7 jours)</text>
  <text x="806" y="547" fill="#15803D" font-size="10.5" font-weight="600">• Healthchecks automatiques /actuator/health</text>


  <!-- ==================== LEGENDE DU BAS ==================== -->
  <rect x="30" y="660" width="1080" height="75" rx="8" fill="#1E293B" />
  <text x="50" y="682" fill="#F8FAFC" font-size="12" font-weight="700">ENGAGEMENT DEVOPS DE L'EQUIPE GARIK :</text>
  <text x="50" y="702" fill="#CBD5E1" font-size="11">• <tspan font-weight="700">Testabilite en Conditions Reelles :</tspan> Le code compile en local sous Java 17, passe la CI GitLab de l'universite et se deploie sur VPS Linux sous reverse proxy HTTPS.</text>
  <text x="50" y="720" fill="#CBD5E1" font-size="11">• <tspan font-weight="700">Pragmatisme Etudiant :</tspan> Rejet de Kubernetes pour privilegier une architecture Docker Compose simple, securisee et parfaitement maitrisee.</text>
</svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[OK] Figure 2 DevOps generee : {output_path}")


def main():
    root_dir = Path(__file__).resolve().parent.parent.parent.parent
    figures_dir = root_dir / "ShopLoc" / "agent_projet" / "docs" / "02_Architecture_Et_Outils_R2" / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    # Nettoyage des anciennes figures superflues
    old_fig2 = figures_dir / "fig_2_services_et_liaisons.svg"
    old_fig3 = figures_dir / "fig_3_chaine_outils_devops.svg"
    if old_fig2.exists():
        old_fig2.unlink()
        print(f"[SUPPRIME] Ancienne Figure 2 retiree : {old_fig2}")
    if old_fig3.exists():
        old_fig3.unlink()
        print(f"[SUPPRIME] Ancienne Figure 3 retiree : {old_fig3}")

    generate_fig1_context(figures_dir / "fig_1_contexte_systeme_shoploc.svg")
    generate_fig2_devops(figures_dir / "fig_2_chaine_outils_devops.svg")
    print(f"[SUCCES] Les 2 figures techniques R2 ont ete generees dans : {figures_dir}")

if __name__ == "__main__":
    main()

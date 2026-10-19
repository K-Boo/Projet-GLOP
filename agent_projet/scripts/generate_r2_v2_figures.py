#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERATEUR DES FIGURES D'ARCHITECTURE STYLE EPURE (V2)
Livrable R2 — Master 2 MIAGE GLOP — Universite de Lille
Societe Garik

Genere 3 schemas vectoriels SVG epures et lisibles :
1. fig_1_contexte_global_shoploc.svg      : Vue de contexte (acteurs, systeme ShopLoc, simulateurs tiers)
2. fig_2_architecture_services_donnees.svg : Architecture applicative en zones (Acces, Metier, Donnees)
3. fig_3_chaine_devops_deploiement.svg    : Chaine DevOps et hebergement VPS
"""

import os

def build_fig_1():
    """Figure 1 : Vue de ShopLoc dans son environnement (Contexte C4 Niveau 1)"""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 560" width="100%" height="auto" style="background:#FAF9F6; font-family:'Helvetica Neue', Arial, sans-serif;">
  <defs>
    <filter id="shadow" x="-3%" y="-3%" width="106%" height="106%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.06"/>
    </filter>
    <marker id="arr-blue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#1D4ED8"/>
    </marker>
    <marker id="arr-orange" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#C2410C"/>
    </marker>
  </defs>

  <!-- Titre de la figure -->
  <text x="475" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#0F172A">FIG. 1 – Vue de la plateforme ShopLoc dans son environnement (Contexte global)</text>

  <!-- 1. ZONE USAGERS ET CANAUX (Gauche) -->
  <rect x="40" y="60" width="220" height="420" rx="8" fill="#F1F5F9" stroke="#94A3B8" stroke-width="1.5" filter="url(#shadow)"/>
  <rect x="40" y="60" width="220" height="36" rx="8" fill="#E2E8F0" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="150" y="83" text-anchor="middle" font-size="13" font-weight="bold" fill="#334155">Acteurs &amp; Canaux d'Usage</text>

  <!-- Acteur 1 -->
  <rect x="55" y="115" width="190" height="60" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="150" y="140" text-anchor="middle" font-size="12" font-weight="bold" fill="#1E293B">Citoyens Acheteurs</text>
  <text x="150" y="158" text-anchor="middle" font-size="10.5" fill="#64748B">Application Web (React SPA)</text>

  <!-- Acteur 2 -->
  <rect x="55" y="190" width="190" height="60" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="150" y="215" text-anchor="middle" font-size="12" font-weight="bold" fill="#1E293B">Commercants Adherents</text>
  <text x="150" y="233" text-anchor="middle" font-size="10.5" fill="#64748B">Portail de Gestion Back-Office</text>

  <!-- Acteur 3 -->
  <rect x="55" y="265" width="190" height="60" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="150" y="290" text-anchor="middle" font-size="12" font-weight="bold" fill="#1E293B">Vendeurs en Boutique</text>
  <text x="150" y="308" text-anchor="middle" font-size="10.5" fill="#64748B">Terminal Scanner de Retrait (PWA)</text>

  <!-- Acteur 4 -->
  <rect x="55" y="340" width="190" height="60" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="150" y="365" text-anchor="middle" font-size="12" font-weight="bold" fill="#1E293B">Collectivite Municipale</text>
  <text x="150" y="383" text-anchor="middle" font-size="10.5" fill="#64748B">Console Mairie (Statistiques)</text>

  <!-- Acteur 5 -->
  <rect x="55" y="415" width="190" height="50" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="150" y="438" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#1E293B">Equipe d'Exploitation</text>
  <text x="150" y="454" text-anchor="middle" font-size="10" fill="#64748B">Supervision Actuator &amp; Grafana</text>

  <!-- 2. SYSTEME CENTRAL SHOPLOC (Centre) -->
  <rect x="330" y="60" width="300" height="420" rx="8" fill="#F8FAFC" stroke="#0284C7" stroke-width="2" filter="url(#shadow)"/>
  <rect x="330" y="60" width="300" height="36" rx="8" fill="#E0F2FE" stroke="#0284C7" stroke-width="2"/>
  <text x="480" y="83" text-anchor="middle" font-size="14" font-weight="bold" fill="#0369A1">Plateforme Logicielle ShopLoc</text>

  <!-- Bloc Passerelle -->
  <rect x="350" y="115" width="260" height="55" rx="6" fill="#FFFFFF" stroke="#38BDF8" stroke-width="1.2"/>
  <text x="480" y="138" text-anchor="middle" font-size="12" font-weight="bold" fill="#0369A1">Passerelle d'Acces (API Gateway)</text>
  <text x="480" y="156" text-anchor="middle" font-size="10.5" fill="#0284C7">Routage public, Securite JWT, Tracage</text>

  <!-- Bloc Microservices -->
  <rect x="350" y="185" width="260" height="215" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="480" y="208" text-anchor="middle" font-size="12" font-weight="bold" fill="#1E293B">Services Metiers Distribues</text>

  <rect x="365" y="222" width="230" height="34" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="480" y="243" text-anchor="middle" font-size="11" fill="#334155">Authentification &amp; Comptes (Auth)</text>

  <rect x="365" y="264" width="230" height="34" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="480" y="285" text-anchor="middle" font-size="11" fill="#334155">Catalogue &amp; Stocks Magasins</text>

  <rect x="365" y="306" width="230" height="34" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="480" y="327" text-anchor="middle" font-size="11" fill="#334155">Paniers &amp; Commandes (Coordinateur 2PC)</text>

  <rect x="365" y="348" width="230" height="34" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="480" y="369" text-anchor="middle" font-size="11" fill="#334155">Fidelite VFP &amp; Titres de Mobilite</text>

  <!-- Bloc Persistance isolee -->
  <rect x="350" y="415" width="260" height="50" rx="6" fill="#F1F5F9" stroke="#94A3B8" stroke-width="1"/>
  <text x="480" y="436" text-anchor="middle" font-size="11" font-weight="bold" fill="#334155">Bases de Donnees Isolees</text>
  <text x="480" y="453" text-anchor="middle" font-size="10" fill="#64748B">Une base PostgreSQL 16 distincte par service</text>

  <!-- 3. SERVICES PARTENAIRES SIMULES (Droite) -->
  <rect x="700" y="115" width="210" height="310" rx="8" fill="#FFFBEB" stroke="#F59E0B" stroke-width="1.5" filter="url(#shadow)"/>
  <rect x="700" y="115" width="210" height="36" rx="8" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5"/>
  <text x="805" y="138" text-anchor="middle" font-size="13" font-weight="bold" fill="#B45309">Services Tiers Simules</text>

  <!-- Partenaire 1 -->
  <rect x="715" y="170" width="180" height="65" rx="6" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1"/>
  <text x="805" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400E">Simulateur Banque</text>
  <text x="805" y="213" text-anchor="middle" font-size="10.5" fill="#78350F">Debit carte &amp; pannes 402</text>
  <text x="805" y="227" text-anchor="middle" font-size="9.5" fill="#A16207">(Validation du 2PC)</text>

  <!-- Partenaire 2 -->
  <rect x="715" y="250" width="180" height="65" rx="6" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1"/>
  <text x="805" y="275" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400E">Simulateur Transports</text>
  <text x="805" y="293" text-anchor="middle" font-size="10.5" fill="#78350F">Emission de titres bus / tram</text>
  <text x="805" y="307" text-anchor="middle" font-size="9.5" fill="#A16207">(Conversion VFP Ilevia)</text>

  <!-- Partenaire 3 -->
  <rect x="715" y="330" width="180" height="65" rx="6" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1"/>
  <text x="805" y="355" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400E">Simulateur Voirie</text>
  <text x="805" y="373" text-anchor="middle" font-size="10.5" fill="#78350F">Franchise de 20 min parking</text>
  <text x="805" y="387" text-anchor="middle" font-size="9.5" fill="#A16207">(Gestion par immatriculation)</text>

  <!-- FLECHES DE LIAISON -->
  <line x1="260" y1="145" x2="340" y2="145" stroke="#1D4ED8" stroke-width="2" marker-end="url(#arr-blue)"/>
  <text x="300" y="137" text-anchor="middle" font-size="9.5" fill="#1E40AF">HTTPS</text>

  <line x1="260" y1="220" x2="340" y2="155" stroke="#1D4ED8" stroke-width="1.5" marker-end="url(#arr-blue)"/>
  <line x1="260" y1="295" x2="340" y2="162" stroke="#1D4ED8" stroke-width="1.5" marker-end="url(#arr-blue)"/>
  <line x1="260" y1="370" x2="340" y2="168" stroke="#1D4ED8" stroke-width="1.5" marker-end="url(#arr-blue)"/>
  <line x1="260" y1="440" x2="340" y2="175" stroke="#1D4ED8" stroke-width="1.5" marker-end="url(#arr-blue)"/>

  <!-- ShopLoc -> Partenaires -->
  <line x1="630" y1="322" x2="690" y2="205" stroke="#C2410C" stroke-width="1.5" marker-end="url(#arr-orange)"/>
  <text x="668" y="245" font-size="9.5" fill="#9A3412">Paiement</text>

  <line x1="630" y1="365" x2="690" y2="282" stroke="#C2410C" stroke-width="1.5" marker-end="url(#arr-orange)"/>
  <line x1="630" y1="365" x2="690" y2="362" stroke="#C2410C" stroke-width="1.5" marker-end="url(#arr-orange)"/>
  <text x="668" y="325" font-size="9.5" fill="#9A3412">Mobilite</text>

  <!-- LEGENDE DU SCHEMA -->
  <rect x="180" y="505" width="590" height="38" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <line x1="200" y1="524" x2="230" y2="524" stroke="#1D4ED8" stroke-width="2" marker-end="url(#arr-blue)"/>
  <text x="240" y="528" font-size="11" fill="#334155">Flux d'appels clients (HTTPS)</text>

  <line x1="420" y1="524" x2="450" y2="524" stroke="#C2410C" stroke-width="2" marker-end="url(#arr-orange)"/>
  <text x="460" y="528" font-size="11" fill="#334155">Flux d'echange inter-services (REST synchrone)</text>

  <rect x="680" y="517" width="14" height="14" rx="2" fill="#E0F2FE" stroke="#0284C7"/>
  <text x="702" y="528" font-size="11" fill="#334155">Frontiere de securite</text>
</svg>'''
    return svg

def build_fig_2():
    """Figure 2 : Architecture applicative et liaisons de donnees (Zones d'isolation)"""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 620" width="100%" height="auto" style="background:#FAF9F6; font-family:'Helvetica Neue', Arial, sans-serif;">
  <defs>
    <filter id="shadow2" x="-3%" y="-3%" width="106%" height="106%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.06"/>
    </filter>
    <marker id="arr-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0D9488"/>
    </marker>
    <marker id="arr-red" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#DC2626"/>
    </marker>
  </defs>

  <!-- Titre -->
  <text x="475" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#0F172A">FIG. 2 – Architecture applicative interne et flux de persistance (Zones d'isolation)</text>

  <!-- ZONE 1 : ZONE ACCES (Haut) -->
  <rect x="40" y="55" width="870" height="90" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.5" filter="url(#shadow2)"/>
  <text x="60" y="78" font-size="12" font-weight="bold" fill="#15803D" text-transform="uppercase">Zone 1 : Acces &amp; Exposition Publique</text>

  <!-- Nginx -->
  <rect x="180" y="85" width="230" height="45" rx="6" fill="#FFFFFF" stroke="#86EFAC" stroke-width="1.2"/>
  <text x="295" y="105" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">Reverse Proxy Nginx</text>
  <text x="295" y="121" text-anchor="middle" font-size="10" fill="#4B5563">Port 443 HTTPS &amp; Certificat SSL Let's Encrypt</text>

  <!-- Gateway -->
  <rect x="520" y="85" width="250" height="45" rx="6" fill="#FFFFFF" stroke="#86EFAC" stroke-width="1.2"/>
  <text x="645" y="105" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">API Gateway (Spring Cloud)</text>
  <text x="645" y="121" text-anchor="middle" font-size="10" fill="#4B5563">Verification JWT, Routage interne, Correlation ID</text>

  <line x1="410" y1="107" x2="510" y2="107" stroke="#16A34A" stroke-width="2" marker-end="url(#arr-green)"/>
  <text x="460" y="100" text-anchor="middle" font-size="9.5" fill="#15803D">Routage</text>

  <!-- ZONE 2 : ZONE APPLICATIVE METIER (Milieu) -->
  <rect x="40" y="170" width="870" height="260" rx="8" fill="#F8FAFC" stroke="#0284C7" stroke-width="1.5" filter="url(#shadow2)"/>
  <text x="60" y="195" font-size="12" font-weight="bold" fill="#0369A1" text-transform="uppercase">Zone 2 : Services Metiers (Spring Boot 3.3 / Java 17)</text>

  <!-- Service 1 : Auth -->
  <rect x="65" y="215" width="180" height="180" rx="6" fill="#FFFFFF" stroke="#BAE6FD" stroke-width="1.2"/>
  <rect x="65" y="215" width="180" height="28" rx="6" fill="#E0F2FE"/>
  <text x="155" y="234" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#0369A1">shoploc-auth-service</text>
  <text x="155" y="262" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#334155">Gestion des Comptes</text>
  <text x="75" y="285" font-size="10" fill="#475569">• Inscription &amp; Profils</text>
  <text x="75" y="303" font-size="10" fill="#475569">• Authentification BCrypt</text>
  <text x="75" y="321" font-size="10" fill="#475569">• Habilitations RBAC</text>
  <text x="75" y="339" font-size="10" fill="#475569">• Emission des jetons JWT</text>
  <text x="155" y="380" text-anchor="middle" font-size="9.5" fill="#0369A1">Port interne 8081</text>

  <!-- Service 2 : Catalogue -->
  <rect x="275" y="215" width="185" height="180" rx="6" fill="#FFFFFF" stroke="#BAE6FD" stroke-width="1.2"/>
  <rect x="275" y="215" width="185" height="28" rx="6" fill="#E0F2FE"/>
  <text x="367" y="234" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#0369A1">merchant-catalog-service</text>
  <text x="367" y="262" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#334155">Catalogue &amp; Stocks</text>
  <text x="285" y="285" font-size="10" fill="#475569">• Fiches magasins &amp; horaires</text>
  <text x="285" y="303" font-size="10" fill="#475569">• Produits &amp; prix en centimes</text>
  <text x="285" y="321" font-size="10" fill="#475569">• Inventaires en temps reel</text>
  <text x="285" y="339" font-size="10" fill="#475569">• Verrous de stock (2PC)</text>
  <text x="367" y="380" text-anchor="middle" font-size="9.5" fill="#0369A1">Port interne 8082</text>

  <!-- Service 3 : Commande -->
  <rect x="490" y="215" width="185" height="180" rx="6" fill="#FFFFFF" stroke="#0284C7" stroke-width="2"/>
  <rect x="490" y="215" width="185" height="28" rx="6" fill="#BAE6FD"/>
  <text x="582" y="234" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#0C4A6E">cart-order-service</text>
  <text x="582" y="262" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#0369A1">Coordinateur 2PC</text>
  <text x="500" y="285" font-size="10" fill="#475569">• Panier multi-boutiques</text>
  <text x="500" y="303" font-size="10" fill="#475569">• Phase 1 : Prepare stock</text>
  <text x="500" y="321" font-size="10" fill="#475569">• Phase 2 : Commit / Rollback</text>
  <text x="500" y="339" font-size="10" fill="#475569">• QR code de retrait</text>
  <text x="582" y="380" text-anchor="middle" font-size="9.5" fill="#0369A1">Port interne 8083</text>

  <!-- Service 4 : Fidelite -->
  <rect x="705" y="215" width="180" height="180" rx="6" fill="#FFFFFF" stroke="#BAE6FD" stroke-width="1.2"/>
  <rect x="705" y="215" width="180" height="28" rx="6" fill="#E0F2FE"/>
  <text x="795" y="234" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#0369A1">shoploc-loyalty-service</text>
  <text x="795" y="262" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#334155">Programme Fidelite VFP</text>
  <text x="715" y="285" font-size="10" fill="#475569">• Points d'achat marchands</text>
  <text x="715" y="303" font-size="10" fill="#475569">• Regularite 10 pass / 15j</text>
  <text x="715" y="321" font-size="10" fill="#475569">• Vouchers bus &amp; parking</text>
  <text x="715" y="339" font-size="10" fill="#475569">• Statistiques mairie anonymes</text>
  <text x="795" y="380" text-anchor="middle" font-size="9.5" fill="#0369A1">Port interne 8084</text>

  <!-- LIAISON 2PC RestClient entre Commande et Catalogue -->
  <path d="M 490 280 L 465 280" stroke="#DC2626" stroke-width="2" marker-end="url(#arr-red)"/>
  <text x="477" y="272" text-anchor="middle" font-size="9" font-weight="bold" fill="#DC2626">2PC</text>

  <!-- ZONE 3 : PERSISTANCE & DONNEES (Bas) -->
  <rect x="40" y="450" width="870" height="110" rx="8" fill="#FDF4FF" stroke="#A855F7" stroke-width="1.5" filter="url(#shadow2)"/>
  <text x="60" y="475" font-size="12" font-weight="bold" fill="#7E22CE" text-transform="uppercase">Zone 3 : Persistance Database-per-Service (PostgreSQL 16)</text>

  <!-- DB 1 -->
  <rect x="75" y="490" width="160" height="50" rx="6" fill="#FFFFFF" stroke="#E9D5FF" stroke-width="1"/>
  <text x="155" y="512" text-anchor="middle" font-size="11" font-weight="bold" fill="#581C87">auth_db</text>
  <text x="155" y="528" text-anchor="middle" font-size="9.5" fill="#6B7280">Port 5432 / Comptes</text>
  <line x1="155" y1="395" x2="155" y2="485" stroke="#9333EA" stroke-width="1.5" stroke-dasharray="3,3"/>

  <!-- DB 2 -->
  <rect x="287" y="490" width="160" height="50" rx="6" fill="#FFFFFF" stroke="#E9D5FF" stroke-width="1"/>
  <text x="367" y="512" text-anchor="middle" font-size="11" font-weight="bold" fill="#581C87">catalog_db</text>
  <text x="367" y="528" text-anchor="middle" font-size="9.5" fill="#6B7280">Port 5433 / Articles</text>
  <line x1="367" y1="395" x2="367" y2="485" stroke="#9333EA" stroke-width="1.5" stroke-dasharray="3,3"/>

  <!-- DB 3 -->
  <rect x="502" y="490" width="160" height="50" rx="6" fill="#FFFFFF" stroke="#E9D5FF" stroke-width="1"/>
  <text x="582" y="512" text-anchor="middle" font-size="11" font-weight="bold" fill="#581C87">order_db</text>
  <text x="582" y="528" text-anchor="middle" font-size="9.5" fill="#6B7280">Port 5434 / Commandes</text>
  <line x1="582" y1="395" x2="582" y2="485" stroke="#9333EA" stroke-width="1.5" stroke-dasharray="3,3"/>

  <!-- DB 4 -->
  <rect x="715" y="490" width="160" height="50" rx="6" fill="#FFFFFF" stroke="#E9D5FF" stroke-width="1"/>
  <text x="795" y="512" text-anchor="middle" font-size="11" font-weight="bold" fill="#581C87">loyalty_db</text>
  <text x="795" y="528" text-anchor="middle" font-size="9.5" fill="#6B7280">Port 5435 / Points</text>
  <line x1="795" y1="395" x2="795" y2="485" stroke="#9333EA" stroke-width="1.5" stroke-dasharray="3,3"/>

  <!-- LEGENDE DES FLUX ET COMPOSANTS -->
  <rect x="180" y="575" width="590" height="32" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <line x1="200" y1="591" x2="230" y2="591" stroke="#16A34A" stroke-width="2" marker-end="url(#arr-green)"/>
  <text x="240" y="595" font-size="10.5" fill="#334155">Point d'entree public (Nginx)</text>

  <line x1="420" y1="591" x2="450" y2="591" stroke="#DC2626" stroke-width="2" marker-end="url(#arr-red)"/>
  <text x="460" y="595" font-size="10.5" fill="#334155">Echange transactionnel 2PC</text>

  <line x1="640" y1="591" x2="670" y2="591" stroke="#9333EA" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="680" y="595" font-size="10.5" fill="#334155">Liaison BDD privee</text>
</svg>'''
    return svg

def build_fig_3():
    """Figure 3 : Chaine DevOps, CI/CD et Deploiement VPS"""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 560" width="100%" height="auto" style="background:#FAF9F6; font-family:'Helvetica Neue', Arial, sans-serif;">
  <defs>
    <filter id="shadow3" x="-3%" y="-3%" width="106%" height="106%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.06"/>
    </filter>
    <marker id="arr-gray" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- Titre -->
  <text x="475" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#0F172A">FIG. 3 – Chaine d'ingenierie DevOps : de l'environnement local au deploiement VPS</text>

  <!-- ETAPE 1 : POSTE LOCAL (Gauche) -->
  <rect x="40" y="65" width="260" height="415" rx="8" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5" filter="url(#shadow3)"/>
  <rect x="40" y="65" width="260" height="36" rx="8" fill="#E2E8F0" stroke="#64748B" stroke-width="1.5"/>
  <text x="170" y="88" text-anchor="middle" font-size="13" font-weight="bold" fill="#1E293B">1. Developpement Local</text>

  <rect x="55" y="120" width="230" height="65" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="170" y="145" text-anchor="middle" font-size="12" font-weight="bold" fill="#0F172A">Environnement &amp; Outils</text>
  <text x="170" y="163" text-anchor="middle" font-size="10.5" fill="#475569">Java 17 OpenJDK, Maven Wrapper (mvnw)</text>
  <text x="170" y="177" text-anchor="middle" font-size="10" fill="#64748B">IntelliJ IDEA / VS Code sous Windows &amp; WSL</text>

  <rect x="55" y="200" width="230" height="65" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="170" y="225" text-anchor="middle" font-size="12" font-weight="bold" fill="#0F172A">Tests Unitaires Rapides</text>
  <text x="170" y="243" text-anchor="middle" font-size="10.5" fill="#475569">Base H2 en memoire (h2:mem)</text>
  <text x="170" y="257" text-anchor="middle" font-size="10" fill="#64748B">Execution instantanee sans conteneur</text>

  <rect x="55" y="280" width="230" height="65" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="170" y="305" text-anchor="middle" font-size="12" font-weight="bold" fill="#0F172A">Qualite &amp; Clean Code</text>
  <text x="170" y="323" text-anchor="middle" font-size="10.5" fill="#475569">SonarLint integre a la saisie</text>
  <text x="170" y="337" text-anchor="middle" font-size="10" fill="#64748B">Zero anomalie critique avant commit</text>

  <rect x="55" y="360" width="230" height="60" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="170" y="385" text-anchor="middle" font-size="12" font-weight="bold" fill="#0F172A">Gestion Git &amp; MR</text>
  <text x="170" y="403" text-anchor="middle" font-size="10.5" fill="#475569">Branches feature/ &amp; Revue de code</text>

  <!-- ETAPE 2 : FORGE GITLAB CI (Milieu) -->
  <rect x="345" y="65" width="260" height="415" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.5" filter="url(#shadow3)"/>
  <rect x="345" y="65" width="260" height="36" rx="8" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5"/>
  <text x="475" y="88" text-anchor="middle" font-size="13" font-weight="bold" fill="#15803D">2. Integration Continue (GitLab)</text>

  <rect x="360" y="120" width="230" height="75" rx="6" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1"/>
  <text x="475" y="145" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">Forge Univ-Lille</text>
  <text x="475" y="163" text-anchor="middle" font-size="10.5" fill="#15803D">Groupe glop-garik-2026</text>
  <text x="475" y="177" text-anchor="middle" font-size="10" fill="#4B5563">4 depots independants (Polyrepo)</text>
  <text x="475" y="190" text-anchor="middle" font-size="9.5" fill="#16A34A">Acces Reporter+ accorde aux enseignants</text>

  <rect x="360" y="210" width="230" height="75" rx="6" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1"/>
  <text x="475" y="235" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">Pipeline CI Automatique</text>
  <text x="475" y="253" text-anchor="middle" font-size="10.5" fill="#15803D">Job maven-tests sur runner</text>
  <text x="475" y="267" text-anchor="middle" font-size="10" fill="#4B5563">mvn test jacoco:report</text>
  <text x="475" y="280" text-anchor="middle" font-size="9.5" fill="#15803D">Verification du seuil Jacoco &gt;= 80%</text>

  <rect x="360" y="300" width="230" height="75" rx="6" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1"/>
  <text x="475" y="325" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">Construction d'Images</text>
  <text x="475" y="343" text-anchor="middle" font-size="10.5" fill="#15803D">Dockerfile Multi-Stage</text>
  <text x="475" y="357" text-anchor="middle" font-size="10" fill="#4B5563">Base allegee Alpine JRE (148 Mo)</text>
  <text x="475" y="370" text-anchor="middle" font-size="9.5" fill="#166534">Registre prive universitaire</text>

  <rect x="360" y="390" width="230" height="40" rx="6" fill="#E2E8F0" stroke="#CBD5E1" stroke-width="1"/>
  <text x="475" y="415" text-anchor="middle" font-size="11" font-weight="bold" fill="#334155">Declencheur CD post-succes</text>

  <!-- ETAPE 3 : HEBERGEMENT VPS (Droite) -->
  <rect x="650" y="65" width="260" height="415" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5" filter="url(#shadow3)"/>
  <rect x="650" y="65" width="260" height="36" rx="8" fill="#DBEAFE" stroke="#2563EB" stroke-width="1.5"/>
  <text x="780" y="88" text-anchor="middle" font-size="13" font-weight="bold" fill="#1E40AF">3. Exploitation en Production</text>

  <rect x="665" y="120" width="230" height="65" rx="6" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1"/>
  <text x="780" y="145" text-anchor="middle" font-size="12" font-weight="bold" fill="#1E40AF">Serveur VPS OVHcloud</text>
  <text x="780" y="163" text-anchor="middle" font-size="10.5" fill="#2563EB">Linux Ubuntu Server 24.04 LTS</text>
  <text x="780" y="177" text-anchor="middle" font-size="10" fill="#64748B">Datacenter Roubaix / Gravelines (France)</text>

  <rect x="665" y="200" width="230" height="65" rx="6" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1"/>
  <text x="780" y="225" text-anchor="middle" font-size="12" font-weight="bold" fill="#1E40AF">Frontal Securise</text>
  <text x="780" y="243" text-anchor="middle" font-size="10.5" fill="#2563EB">Nginx Reverse Proxy &amp; HTTPS</text>
  <text x="780" y="257" text-anchor="middle" font-size="10" fill="#64748B">Certificats SSL Let's Encrypt (Certbot)</text>

  <rect x="665" y="280" width="230" height="75" rx="6" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1"/>
  <text x="780" y="305" text-anchor="middle" font-size="12" font-weight="bold" fill="#1E40AF">Docker Compose</text>
  <text x="780" y="323" text-anchor="middle" font-size="10.5" fill="#2563EB">Reseau prive etanche (shoploc-net)</text>
  <text x="780" y="337" text-anchor="middle" font-size="10" fill="#4B5563">Microservices &amp; BDD non exposes</text>
  <text x="780" y="350" text-anchor="middle" font-size="9.5" fill="#64748B">Volumes persistants sur disque hote</text>

  <rect x="665" y="370" width="230" height="65" rx="6" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1"/>
  <text x="780" y="395" text-anchor="middle" font-size="12" font-weight="bold" fill="#1E40AF">Maintenance &amp; Sauvegardes</text>
  <text x="780" y="413" text-anchor="middle" font-size="10" fill="#4B5563">Tache cron nocturne pg_dump (7 jours)</text>
  <text x="780" y="427" text-anchor="middle" font-size="9.5" fill="#64748B">Supervision Actuator (/health, /metrics)</text>

  <!-- FLECHES INTER-ZONES -->
  <line x1="300" y1="230" x2="340" y2="230" stroke="#475569" stroke-width="2" marker-end="url(#arr-gray)"/>
  <text x="320" y="220" text-anchor="middle" font-size="9.5" fill="#475569">git push</text>

  <line x1="605" y1="230" x2="645" y2="230" stroke="#475569" stroke-width="2" marker-end="url(#arr-gray)"/>
  <text x="625" y="220" text-anchor="middle" font-size="9.5" fill="#475569">deploy</text>

  <!-- LEGENDE DU PIPELINE -->
  <rect x="250" y="500" width="450" height="34" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <circle cx="270" cy="517" r="5" fill="#64748B"/>
  <text x="282" y="521" font-size="11" fill="#334155">Code source local</text>

  <circle cx="410" cy="517" r="5" fill="#16A34A"/>
  <text x="422" y="521" font-size="11" fill="#334155">Validation continue CI</text>

  <circle cx="560" cy="517" r="5" fill="#2563EB"/>
  <text x="572" y="521" font-size="11" fill="#334155">Production conteneurisee VPS</text>
</svg>'''
    return svg

def build_fig_4():
    """Figure 4 : Diagramme de sequence du Walking Skeleton (validation inter-services)"""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 510" width="100%" height="auto" style="background:#FAF9F6; font-family:'Helvetica Neue', Arial, sans-serif;">
  <defs>
    <filter id="shadow4" x="-3%" y="-3%" width="106%" height="106%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.06"/>
    </filter>
    <marker id="arr-req" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#1E293B"/>
    </marker>
    <marker id="arr-resp" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#059669"/>
    </marker>
    <marker id="arr-sql" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#D97706"/>
    </marker>
  </defs>

  <!-- Titre -->
  <text x="475" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#0F172A">FIG. 4 – Diagramme de sequence du Walking Skeleton (validation de disponibilite inter-services)</text>

  <!-- LIGNES DE VIE (LIFELINES) -->
  <!-- 1. Client / Evaluateur (x = 110) -->
  <rect x="25" y="55" width="170" height="50" rx="6" fill="#F1F5F9" stroke="#94A3B8" stroke-width="1.2" filter="url(#shadow4)"/>
  <text x="110" y="77" text-anchor="middle" font-size="12" font-weight="bold" fill="#1E293B">Client / Evaluateur</text>
  <text x="110" y="93" text-anchor="middle" font-size="10" fill="#64748B">Navigateur / cURL</text>
  <line x1="110" y1="105" x2="110" y2="435" stroke="#CBD5E1" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- 2. Cart-Order Service (x = 380) -->
  <rect x="290" y="55" width="180" height="50" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.2" filter="url(#shadow4)"/>
  <text x="380" y="77" text-anchor="middle" font-size="12" font-weight="bold" fill="#1E40AF">cart-order-service</text>
  <text x="380" y="93" text-anchor="middle" font-size="10" fill="#3B82F6">Port 8083 (Spring Boot 3.3)</text>
  <line x1="380" y1="105" x2="380" y2="435" stroke="#93C5FD" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- 3. Merchant-Catalog Service (x = 670) -->
  <rect x="575" y="55" width="190" height="50" rx="6" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.2" filter="url(#shadow4)"/>
  <text x="670" y="77" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400E">merchant-catalog-service</text>
  <text x="670" y="93" text-anchor="middle" font-size="10" fill="#D97706">Port 8082 (Spring Boot 3.3)</text>
  <line x1="670" y1="105" x2="670" y2="435" stroke="#FCD34D" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- 4. PostgreSQL 16 (x = 880) -->
  <rect x="805" y="55" width="150" height="50" rx="6" fill="#ECFDF5" stroke="#10B981" stroke-width="1.2" filter="url(#shadow4)"/>
  <text x="880" y="77" text-anchor="middle" font-size="12" font-weight="bold" fill="#065F46">PostgreSQL 16</text>
  <text x="880" y="93" text-anchor="middle" font-size="10" fill="#059669">catalog_db (Port 5432)</text>
  <line x1="880" y1="105" x2="880" y2="435" stroke="#A7F3D0" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- BARRES D'ACTIVATION -->
  <rect x="105" y="130" width="10" height="295" fill="#E2E8F0" stroke="#94A3B8" stroke-width="1"/>
  <rect x="375" y="140" width="10" height="275" fill="#DBEAFE" stroke="#3B82F6" stroke-width="1"/>
  <rect x="665" y="185" width="10" height="175" fill="#FDE68A" stroke="#F59E0B" stroke-width="1"/>
  <rect x="875" y="230" width="10" height="75" fill="#A7F3D0" stroke="#10B981" stroke-width="1"/>

  <!-- ETAPE 1 : Client -> Cart-Order -->
  <line x1="115" y1="150" x2="375" y2="150" stroke="#1E293B" stroke-width="1.8" marker-end="url(#arr-req)"/>
  <circle cx="140" cy="138" r="9" fill="#1E293B"/>
  <text x="140" y="142" text-anchor="middle" font-size="10" font-weight="bold" fill="#FFFFFF">1</text>
  <text x="245" y="142" text-anchor="middle" font-size="11" font-weight="bold" fill="#1E293B">GET /api/v1/cart/check-item/1/1</text>
  <text x="245" y="164" text-anchor="middle" font-size="9.5" fill="#64748B">Verification disponibilite &amp; stock</text>

  <!-- ETAPE 2 : Cart-Order -> Merchant-Catalog -->
  <line x1="385" y1="195" x2="665" y2="195" stroke="#1E293B" stroke-width="1.8" marker-end="url(#arr-req)"/>
  <circle cx="410" cy="183" r="9" fill="#1E293B"/>
  <text x="410" y="187" text-anchor="middle" font-size="10" font-weight="bold" fill="#FFFFFF">2</text>
  <text x="525" y="187" text-anchor="middle" font-size="11" font-weight="bold" fill="#1E293B">GET /api/v1/merchants/1/products/1</text>
  <text x="525" y="209" text-anchor="middle" font-size="9.5" fill="#64748B">Appel synchrone Spring RestClient</text>

  <!-- ETAPE 3 : Merchant-Catalog -> PostgreSQL -->
  <line x1="675" y1="240" x2="875" y2="240" stroke="#D97706" stroke-width="1.8" marker-end="url(#arr-sql)"/>
  <circle cx="700" cy="228" r="9" fill="#D97706"/>
  <text x="700" y="232" text-anchor="middle" font-size="10" font-weight="bold" fill="#FFFFFF">3</text>
  <text x="775" y="232" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#92400E">SELECT * FROM products</text>
  <text x="775" y="254" text-anchor="middle" font-size="9.5" fill="#B45309">WHERE id=1 AND merchant_id=1</text>

  <!-- ETAPE 4 : PostgreSQL -> Merchant-Catalog -->
  <line x1="875" y1="290" x2="675" y2="290" stroke="#059669" stroke-width="1.6" stroke-dasharray="5,4" marker-end="url(#arr-resp)"/>
  <circle cx="850" cy="278" r="9" fill="#059669"/>
  <text x="850" y="282" text-anchor="middle" font-size="10" font-weight="bold" fill="#FFFFFF">4</text>
  <text x="775" y="282" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#065F46">Tuple SQL (stock = 25)</text>
  <text x="775" y="304" text-anchor="middle" font-size="9.5" fill="#047857">Entity Product JPA hydratee</text>

  <!-- ETAPE 5 : Merchant-Catalog -> Cart-Order -->
  <line x1="665" y1="345" x2="385" y2="345" stroke="#059669" stroke-width="1.6" stroke-dasharray="5,4" marker-end="url(#arr-resp)"/>
  <circle cx="635" cy="333" r="9" fill="#059669"/>
  <text x="635" y="337" text-anchor="middle" font-size="10" font-weight="bold" fill="#FFFFFF">5</text>
  <text x="525" y="337" text-anchor="middle" font-size="11" font-weight="bold" fill="#065F46">200 OK (ProductDto JSON)</text>
  <text x="525" y="359" text-anchor="middle" font-size="9.5" fill="#047857">Deserialisation du stock disponible</text>

  <!-- ETAPE 6 : Cart-Order -> Client -->
  <line x1="375" y1="400" x2="115" y2="400" stroke="#059669" stroke-width="1.6" stroke-dasharray="5,4" marker-end="url(#arr-resp)"/>
  <circle cx="345" cy="388" r="9" fill="#059669"/>
  <text x="345" y="392" text-anchor="middle" font-size="10" font-weight="bold" fill="#FFFFFF">6</text>
  <text x="245" y="392" text-anchor="middle" font-size="11" font-weight="bold" fill="#065F46">200 OK {"status": "AVAILABLE"}</text>
  <text x="245" y="414" text-anchor="middle" font-size="9.5" fill="#047857">Reponse consolidee retournee</text>

  <!-- LEGENDE DU SCHEMA -->
  <rect x="180" y="455" width="590" height="36" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <line x1="200" y1="473" x2="235" y2="473" stroke="#1E293B" stroke-width="2" marker-end="url(#arr-req)"/>
  <text x="245" y="477" font-size="11" fill="#334155">Appel synchrone HTTP REST</text>

  <line x1="420" y1="473" x2="455" y2="473" stroke="#D97706" stroke-width="2" marker-end="url(#arr-sql)"/>
  <text x="465" y="477" font-size="11" fill="#334155">Requete SQL Spring Data JPA</text>

  <line x1="630" y1="473" x2="665" y2="473" stroke="#059669" stroke-width="1.8" stroke-dasharray="4,3" marker-end="url(#arr-resp)"/>
  <text x="675" y="477" font-size="11" fill="#334155">Reponse JSON (200 OK)</text>
</svg>'''
    return svg

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    figures_dir = os.path.join(os.path.dirname(script_dir), "docs", "02_Architecture_Et_Outils_R2", "figures")
    os.makedirs(figures_dir, exist_ok=True)

    fig1_path = os.path.join(figures_dir, "fig_1_contexte_global_shoploc.svg")
    with open(fig1_path, "w", encoding="utf-8") as f:
        f.write(build_fig_1())
    print(f"SUCCESS: Generated {fig1_path}")

    fig2_path = os.path.join(figures_dir, "fig_2_architecture_services_donnees.svg")
    with open(fig2_path, "w", encoding="utf-8") as f:
        f.write(build_fig_2())
    print(f"SUCCESS: Generated {fig2_path}")

    fig3_path = os.path.join(figures_dir, "fig_3_chaine_devops_deploiement.svg")
    with open(fig3_path, "w", encoding="utf-8") as f:
        f.write(build_fig_3())
    print(f"SUCCESS: Generated {fig3_path}")

    fig4_path = os.path.join(figures_dir, "fig_4_sequence_walking_skeleton.svg")
    with open(fig4_path, "w", encoding="utf-8") as f:
        f.write(build_fig_4())
    print(f"SUCCESS: Generated {fig4_path}")

if __name__ == "__main__":
    main()

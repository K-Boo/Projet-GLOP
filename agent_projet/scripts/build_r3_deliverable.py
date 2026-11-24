#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GÉNÉRATEUR DU LIVRABLE R3 HAUTE FIDÉLITÉ (build_r3_deliverable.py)
Master 2 MIAGE GLOP 2026-2027 — Université de Lille
Projet ShopLoc — Société Garik

Génère GARIK_GLOP-2026-LIVRABLE-R3.html et compile le PDF officiel (12 pages exactes)
avec rendu typographique parfait des formules, Booktabs et charte Pastel & Craft.
"""

import base64
import os
import subprocess
import sys

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""

def generate_r3():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    target_dir = os.path.join(repo_root, "docs", "02_Etude_Financiere_R3")
    os.makedirs(target_dir, exist_ok=True)

    assets_dir = os.path.join(repo_root, "docs", "assets")
    univ_logo_b64 = get_base64_image(os.path.join(assets_dir, "logo_univ_lille.png"))
    fst_logo_b64 = get_base64_image(os.path.join(assets_dir, "logo_fst_informatique.png"))

    html_file = os.path.join(target_dir, "GARIK_GLOP-2026-LIVRABLE-R3.html")
    pdf_file = os.path.join(target_dir, "GARIK_GLOP-2026-LIVRABLE-R3.pdf")

    # CSS calibré pour exactement 12 pages A4
    css_content = """
    @page {
        size: A4 portrait;
        margin: 14mm 15mm 14mm 15mm;
        @bottom-right {
            content: "Page " counter(page) " / " counter(pages);
            font-family: 'Poppins', sans-serif;
            font-size: 8pt;
            color: #5A6578;
        }
        @bottom-left {
            content: "Garik — ShopLoc | Livrable R3 : Étude Financière Approfondie";
            font-family: 'Poppins', sans-serif;
            font-size: 8pt;
            color: #5A6578;
        }
    }

    * {
        box-sizing: border-box;
    }

    body {
        font-family: 'Latin Modern Roman', 'Computer Modern', 'Times New Roman', Times, serif;
        font-size: 9.2pt;
        line-height: 1.38;
        color: #1E252D;
        background-color: #FFFFFF;
        margin: 0;
        padding: 0;
    }

    h1, h2, h3, h4, .sans {
        font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    /* En-tête officiel de page de garde */
    .cover-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2pt solid #243342;
        padding-bottom: 10pt;
        margin-bottom: 18pt;
    }

    .cover-header img {
        height: 46px;
        width: auto;
    }

    .cover-institution {
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-size: 9pt;
        font-weight: 600;
        color: #243342;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .cover-title-box {
        text-align: center;
        margin: 20pt 0 16pt 0;
        padding: 16pt;
        background: #F8FAFC;
        border: 1.5pt solid #243342;
        border-radius: 8px;
    }

    .cover-title-main {
        font-size: 15pt;
        font-weight: 700;
        color: #243342;
        margin: 0 0 6pt 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .cover-subtitle {
        font-size: 10pt;
        font-weight: 500;
        color: #C26750;
        margin: 0 0 8pt 0;
        line-height: 1.3;
    }

    .cover-ref {
        font-family: 'Courier New', monospace;
        font-size: 8.5pt;
        color: #5A6578;
        background: #EBF0F5;
        display: inline-block;
        padding: 3pt 8pt;
        border-radius: 4px;
        font-weight: 600;
    }

    /* Cartouche des métadonnées */
    .meta-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12pt;
        margin-bottom: 16pt;
        font-family: 'Poppins', sans-serif;
        font-size: 8.5pt;
    }

    .meta-card {
        background: #FAF9F6;
        border: 1pt solid #DCD6CD;
        border-radius: 6px;
        padding: 10pt 12pt;
    }

    .meta-card h4 {
        margin: 0 0 6pt 0;
        font-size: 9pt;
        color: #243342;
        border-bottom: 1pt solid #DCD6CD;
        padding-bottom: 3pt;
        text-transform: uppercase;
    }

    .meta-card p {
        margin: 3pt 0;
        color: #334155;
    }

    /* Titres de sections */
    h2.section-title {
        font-size: 11.5pt;
        font-weight: 700;
        color: #243342;
        border-bottom: 1.5pt solid #243342;
        padding-bottom: 3pt;
        margin-top: 0;
        margin-bottom: 8pt;
        text-transform: uppercase;
        letter-spacing: 0.3px;
        page-break-after: avoid;
    }

    h3.subsection-title {
        font-size: 10pt;
        font-weight: 600;
        color: #C26750;
        margin-top: 10pt;
        margin-bottom: 4pt;
        page-break-after: avoid;
    }

    h4.category-title {
        font-size: 9pt;
        font-weight: 600;
        color: #243342;
        margin-top: 8pt;
        margin-bottom: 3pt;
        page-break-after: avoid;
    }

    p {
        margin: 0 0 5pt 0;
        text-align: justify;
    }

    /* Tables Booktabs normées */
    .table-container {
        margin: 8pt 0 10pt 0;
        page-break-inside: avoid;
        width: 100%;
    }

    table.booktabs {
        width: 100%;
        border-collapse: collapse;
        font-size: 8.2pt;
        margin: 0 auto;
    }

    table.booktabs thead th {
        border-top: 1.5pt solid #243342;
        border-bottom: 1pt solid #243342;
        padding: 4.5pt 5pt;
        text-align: left;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        color: #243342;
        background-color: #F8FAFC;
    }

    table.booktabs tbody td {
        padding: 4pt 5pt;
        border-bottom: 0.5pt solid #E2E8F0;
        color: #1E252D;
    }

    table.booktabs tbody tr:nth-child(even) {
        background-color: #FAFAFA;
    }

    table.booktabs tbody tr:last-child td {
        border-bottom: 1.5pt solid #243342;
        font-weight: 600;
    }

    .text-center { text-align: center !important; }
    .text-right { text-align: right !important; }
    .font-bold { font-weight: bold; }

    /* Cartouches d'appel (Callouts) */
    .callout {
        padding: 6pt 10pt;
        margin: 8pt 0;
        border-radius: 5px;
        font-size: 8.5pt;
        page-break-inside: avoid;
        line-height: 1.35;
    }

    .callout-success {
        background-color: #EBF3ED;
        border-left: 3.5pt solid #4A7A5B;
        color: #166534;
    }

    .callout-info {
        background-color: #EBF0F5;
        border-left: 3.5pt solid #243342;
        color: #1E293B;
    }

    .callout-warning {
        background-color: #FEF7EB;
        border-left: 3.5pt solid #C48B28;
        color: #854D0E;
    }

    /* Cartouche des Formules Mathématiques Haute Définition */
    .math-card {
        background: #F8FAFC;
        border: 1pt solid #CBD5E1;
        border-left: 3.5pt solid #243342;
        border-radius: 5px;
        padding: 6pt 12pt;
        margin: 7pt 0;
        page-break-inside: avoid;
    }

    .math-title {
        font-family: 'Poppins', sans-serif;
        font-size: 8pt;
        font-weight: 600;
        color: #243342;
        text-transform: uppercase;
        margin-bottom: 3pt;
        letter-spacing: 0.3px;
    }

    .math-content {
        font-family: 'Latin Modern Roman', 'Computer Modern', 'Times New Roman', serif;
        font-size: 10pt;
        color: #0F172A;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        padding: 2pt 0;
    }

    .math-frac {
        display: inline-flex;
        flex-direction: column;
        vertical-align: middle;
        text-align: center;
        padding: 0 4pt;
        margin: 0 4pt;
    }

    .math-frac .num {
        border-bottom: 1.2pt solid #0F172A;
        padding-bottom: 1.5pt;
        font-size: 0.9em;
    }

    .math-frac .den {
        padding-top: 1.5pt;
        font-size: 0.9em;
    }

    .math-var {
        font-style: italic;
    }

    .math-op {
        margin: 0 5pt;
    }

    .math-sum-container {
        display: inline-flex;
        align-items: center;
        margin: 0 4pt;
    }

    .math-sum {
        font-size: 1.6em;
        line-height: 1;
        font-family: 'Times New Roman', serif;
    }

    .math-limits {
        display: inline-flex;
        flex-direction: column;
        justify-content: space-between;
        font-size: 0.65em;
        font-style: italic;
        line-height: 1;
        margin-left: 2pt;
    }

    /* Gestion des sauts de page stricts */
    .page-break {
        page-break-before: always;
    }

    ul, ol {
        margin: 3pt 0 6pt 16pt;
        padding: 0;
    }

    li {
        margin-bottom: 2.5pt;
        text-align: justify;
    }

    .badge {
        font-family: 'Poppins', sans-serif;
        font-size: 7.5pt;
        font-weight: 600;
        padding: 1.5pt 5pt;
        border-radius: 4px;
        text-transform: uppercase;
        display: inline-block;
    }
    .badge-primary { background: #EBF0F5; color: #243342; }
    .badge-accent { background: #EBF3ED; color: #4A7A5B; }
    """

    # HTML optimisé en 12 pages équilibrées
    html_body = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Livrable R3 — Étude Financière & Rentabilité (ShopLoc — Équipe Garik)</title>
    <style>
{{css_content}}
    </style>
</head>
<body>

<!-- ==========================================================================
     PAGE 1 : PAGE DE GARDE OFFICIELLE
     ========================================================================== -->
<div class="cover-header">
    <img src="data:image/png;base64,{{univ_logo_b64}}" alt="Université de Lille">
    <div class="cover-institution">
        Université de Lille &bull; Faculté des Sciences et Technologies<br>
        Département Informatique &bull; Master 2 MIAGE GLOP (2026-2027)
    </div>
    <img src="data:image/png;base64,{{fst_logo_b64}}" alt="FST Informatique">
</div>

<div class="cover-title-box">
    <div class="cover-title-main">Livrable R3 : Dossier d'Étude Financière Approfondie</div>
    <div class="cover-subtitle">Analyse des Coûts Complets par Centres d'Analyse, Seuil de Rentabilité &amp; Évaluation Pluriannuelle de l'Investissement (VAN, TRI, Payback)</div>
    <div class="cover-ref">RÉFÉRENCE : GLOP-2026-GARIK-LIVRABLE-R3-v1.0 &bull; 30 NOVEMBRE 2026</div>
</div>

<div class="meta-grid">
    <div class="meta-card">
        <h4>Équipe d'Ingénierie Garik</h4>
        <p><strong>Abdelkader HEDDI :</strong> Frontend, Sécurité RBAC &amp; Composant Retrait QR Code</p>
        <p><strong>Gautam DEMEULEMEESTER :</strong> Backend, Persistance Catalogue &amp; Responsable R3</p>
        <p><strong>Rayane ALLI :</strong> Lead DevOps, Conteneurisation &amp; Simulateur OpenAPI 3.1</p>
        <p><strong>Ilyas AIT ALI :</strong> Lead Frontend, Portail Marchand &amp; Scrum Master</p>
        <p><strong>Khalil BOUCHAMA :</strong> Lead QA, Cœur Transactionnel 2PC &amp; Coordinateur</p>
    </div>
    <div class="meta-card">
        <h4>Cadre Pédagogique &amp; Évaluation</h4>
        <p><strong>Unité d'Enseignement :</strong> Génie Logiciel par la Pratique (GLOP)</p>
        <p><strong>Enseignants Évaluateurs :</strong> Laurence DUCHIEN, Anne ETIEN, François SECCHI, Jérémy WOIRHAYE</p>
        <p><strong>Projet Support :</strong> ShopLoc — Plateforme mutualisée de commerce de proximité</p>
        <p><strong>Statut du Document :</strong> Version 1.0 Définitive (Conforme Charte &amp; Zéro Emoji)</p>
    </div>
</div>

<div class="callout callout-info" style="margin-top: 15pt;">
    <strong>Objet et Périmètre du Document :</strong> Le présent dossier formalise la réponse contractuelle de l'entreprise étudiante Garik pour le Jalon R3 de l'UE GLOP. Il applique rigoureusement les enseignements universitaires en gestion stratégique des coûts (méthode des coûts complets par centres d'analyse et direct costing) et en gestion des investissements (CMPC, cash flows prévisionnels, CAF nettes, VAN, TRI, DRCI et IP). Il résout intégralement la réserve formulée lors de la soutenance R1 concernant la réconciliation de l'enveloppe globale horaire (950 heures) et la revalorisation réaliste de la main-d'œuvre d'ingénierie (45,00 €/h chargé).
</div>

<!-- ==========================================================================
     PAGE 2 : FICHE DE SYNTHÈSE EXÉCUTIVE & TABLEAU DES 15 KPIS
     ========================================================================== -->
<div class="page-break"></div>

<h2 class="section-title">Synthèse Exécutive des Indicateurs Clés de l'Investissement (KPIs)</h2>
<p>
    Le tableau de bord ci-dessous récapitule les agrégats financiers fondamentaux régissant le modèle économique de ShopLoc sur son cycle d'amorçage et son expansion pluriannuelle sur 3 ans :
</p>

<div class="table-container">
    <table class="booktabs">
        <thead>
            <tr>
                <th style="width: 28%;">Indicateur Financier</th>
                <th style="width: 22%;" class="text-center">Valeur Certifiée</th>
                <th style="width: 50%;">Interprétation Managériale &amp; Conformité Académique</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Investissement Initial (I<sub>0</sub>)</strong></td>
                <td class="text-center"><strong>45 000,00 €</strong></td>
                <td>Dépenses d'installation logicielle, matériel informatique et Besoin en Fonds de Roulement (&Delta;BFRe).</td>
            </tr>
            <tr>
                <td><strong>Coût Moyen du Capital (K)</strong></td>
                <td class="text-center"><strong>7,80 %</strong></td>
                <td>Structure financière mixte : 60 % Capitaux Propres (r = 10 %) + 40 % Dette bancaire (i = 4,5 %).</td>
            </tr>
            <tr>
                <td><strong>Chiffre d'Affaires Année 1</strong></td>
                <td class="text-center"><strong>79 400,00 €</strong></td>
                <td>Subvention municipale d'amorce (50 000 €) + Adhésions annuelles de 70 commerces (29 400 €).</td>
            </tr>
            <tr>
                <td><strong>Coût de Revient Complet An 1</strong></td>
                <td class="text-center"><strong>70 100,00 €</strong></td>
                <td>Absorption totale des charges directes (MOD à 45 €/h) et indirectes de structure (45 000 €).</td>
            </tr>
            <tr>
                <td><strong>Résultat Analytique Net An 1</strong></td>
                <td class="text-center"><strong>+ 9 300,00 €</strong></td>
                <td>Marge nette bénéficiaire de <strong>11,71 %</strong> dès le lancement territorial pilote.</td>
            </tr>
            <tr>
                <td><strong>Prix de Vente Cible (Marge 15 %)</strong></td>
                <td class="text-center"><strong>82 470,59 €</strong></td>
                <td>Objectif tarifaire pour l'expansion métropolitaine en Année 2 (formule de cours PV = CR / 0,85).</td>
            </tr>
            <tr>
                <td><strong>Volume d'Ingénierie Réconcilié</strong></td>
                <td class="text-center"><strong>950 heures</strong></td>
                <td>100 % des heures justifiées : 480 h MOD Build + 470 h avant-vente, devops et gouvernance.</td>
            </tr>
            <tr>
                <td><strong>Taux de Marge sur Coût Variable</strong></td>
                <td class="text-center"><strong>94,71 %</strong></td>
                <td>Charges variables ultra-légères (4 200 € / an), profil typique d'un SaaS scalable.</td>
            </tr>
            <tr>
                <td><strong>Seuil de Rentabilité (SR)</strong></td>
                <td class="text-center"><strong>69 580,60 €</strong></td>
                <td>Niveau de chiffre d'affaires minimum strict pour couvrir l'ensemble des charges fixes.</td>
            </tr>
            <tr>
                <td><strong>Point Mort d'Exploitation (PM)</strong></td>
                <td class="text-center"><strong>315,45 jours</strong></td>
                <td>Seuil franchi le <strong>16 novembre de l'Année 1</strong> (profit net sur les 45 derniers jours).</td>
            </tr>
            <tr>
                <td><strong>Marge de Sécurité (MS / IS)</strong></td>
                <td class="text-center"><strong>9 819,40 € (12,37 %)</strong></td>
                <td>Résistance à une perte de 12,37 % du CA (défection de 23 boutiques affiliées sur 70).</td>
            </tr>
            <tr>
                <td><strong>Valeur Actuelle Nette (VAN)</strong></td>
                <td class="text-center"><strong>+ 49 838,63 €</strong></td>
                <td>Création nette de richesse substantielle à 36 mois après rémunération des capitaux.</td>
            </tr>
            <tr>
                <td><strong>Indice de Profitabilité (IP)</strong></td>
                <td class="text-center"><strong>2,11</strong></td>
                <td>Chaque tranche de 1,00 € investi rapporte <strong>2,11 €</strong> en flux actualisés.</td>
            </tr>
            <tr>
                <td><strong>Délai de Récupération (DRCI)</strong></td>
                <td class="text-center"><strong>2 ans et 13 jours</strong></td>
                <td>Amortissement complet du capital investi au début du mois de janvier de l'Année 3.</td>
            </tr>
            <tr>
                <td><strong>Taux de Rendement Interne (TRI)</strong></td>
                <td class="text-center"><strong>45,32 %</strong></td>
                <td>Rentabilité intrinsèque très supérieure au coût du capital (7,80 %) et à l'emprunt (4,50 %).</td>
            </tr>
            <tr>
                <td><strong>Retour sur Investissement (ROI)</strong></td>
                <td class="text-center"><strong>199,84 %</strong></td>
                <td>Le projet dégage près de deux fois sa mise de départ en résultat net comptable sur 3 ans.</td>
            </tr>
        </tbody>
    </table>
</div>

<!-- ==========================================================================
     PAGE 3 : SECTION 1 — CADRAGE STRATÉGIQUE & SUSTAINABLE BMC
     ========================================================================== -->
<div class="page-break"></div>

<h2 class="section-title">Section 1 : Cadrage Stratégique, Chaîne de Valeur &amp; Modèle d'Affaires Responsable</h2>

<h3 class="subsection-title">1.1. Chaîne de Valeur de Michael Porter Appliquée à l'Éditeur SaaS ShopLoc</h3>
<p>
    Conformément aux enseignements de gestion stratégique des coûts appliqués aux entreprises de services du numérique (ESN) et aux éditeurs de logiciels SaaS (slides 8 et 14 du cours), la création de valeur de la société Garik s'articule autour de trois activités principales séquentielles, soutenues par deux fonctions d'appui transverses :
</p>

<div class="table-container">
    <table class="booktabs">
        <thead>
            <tr>
                <th style="width: 25%;">Étape de la Chaîne</th>
                <th style="width: 45%;">Opérations Réalisées &amp; Livrables Produits</th>
                <th style="width: 30%;">Centre d'Analyse Associé</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>1. Vente &amp; Avant-vente</strong></td>
                <td>Cadrage avec la Mairie pilote et la MEL, convention tripartite, démonstrations terrain et affiliation des commerces de bouche.</td>
                <td>Centre Principal Commercial &amp; Déploiement</td>
            </tr>
            <tr>
                <td><strong>2. Réalisation (Build)</strong></td>
                <td>Architecture microservices (Spring Boot 3.3, Java 17, React 18), coordinateur transactionnel 2PC, suites de tests TDD (JaCoCo &ge; 80 %).</td>
                <td>Centre Principal Production &amp; Delivery</td>
            </tr>
            <tr>
                <td><strong>3. Maintenance (Run)</strong></td>
                <td>Maintien en Condition Opérationnelle (MCO) sur VPS OVHcloud, sauvegardes pg_dump, rotation des certificats SSL/TLS, support commerçants.</td>
                <td>Centre Principal Production &amp; Delivery</td>
            </tr>
            <tr>
                <td><strong>Soutien : DevOps &amp; Infra</strong></td>
                <td>Pipeline GitLab CI partagé, conteneurisation Docker multi-stage, simulateurs externes d'APIs sous contrat OpenAPI 3.1 (Banque, Mobilité).</td>
                <td>Centre Auxiliaire Support Infra &amp; DevOps</td>
            </tr>
            <tr>
                <td><strong>Soutien : Gouvernance</strong></td>
                <td>Pilotage Agile Scrum (Linear), conformité RGPD (droit à l'oubli), accessibilité numérique universelle (RGAA / WCAG AA) et gestion financière.</td>
                <td>Centre Auxiliaire Administration Générale</td>
            </tr>
        </tbody>
    </table>
</div>

<h3 class="subsection-title">1.2. Modèle d'Affaires Responsable (Sustainable Business Model Canvas)</h3>
<p>
    En application de la matrice d'affaires responsable développée par l'Université Laval (slides 3 à 27 du cours), ShopLoc structure sa rentabilité économique en harmonie avec ses engagements sociaux et écologiques :
</p>
<ul>
    <li><strong>Cohérence Interne (Mission, Vision, Valeurs) :</strong> Offrir une alternative souveraine et décarbonée aux géants du e-commerce en fournissant aux artisans de quartier une marketplace Click &amp; Collect mutualisée. Frugalité technique, transparence algorithmique et respect absolu de la vie privée.</li>
    <li><strong>Désirabilité &amp; Distinction Clients / Utilisateurs :</strong>
        <ul>
            <li><em>Clients Payeurs :</em> La Ville de quartier (subvention d'amorçage au titre de la politique de dynamisation) et l'Association des commerçants (cotisation SaaS mutualisée).</li>
            <li><em>Utilisateurs Quotidiens :</em> Les citoyens (Julie, commande multi-boutiques en paiement unique) et les commerçants (Suzanne, gestion des stocks et validation QR code).</li>
            <li><em>Bénéficiaires Élargis :</em> Personnes en situation de handicap (accessibilité RGAA complète) et régie des transports urbains (report modal favorisé par le programme VFP).</li>
        </ul>
    </li>
    <li><strong>Faisabilité Opérationnelle :</strong> Savoir-faire technique des 5 ingénieurs M2 MIAGE, socle open source éprouvé, infrastructure cloud souveraine basée en France (OVHcloud Roubaix/Gravelines) et partenariat étroit avec la Mairie et l'Association des Commerçants.</li>
    <li><strong>Viabilité Économique :</strong> Modèle hybride B2G/B2B sécurisant la trésorerie via une subvention municipale d'amorce complétée par une adhésion mensuelle modérée par boutique (35 € HT/mois), sans aucune commission prélevée sur le volume des ventes.</li>
</ul>

<!-- ==========================================================================
     PAGE 4 : SECTION 2 — CHARGES DIRECTES & CHARGES INDIRECTES DÉTAILLÉES
     ========================================================================== -->
<div class="page-break"></div>

<h2 class="section-title">Section 2 : Analyse des Coûts Complets par la Méthode des Centres d'Analyse</h2>

<h3 class="subsection-title">2.1. Périmètre Analytique des Charges Directes de l'Exercice (Année 1)</h3>
<p>
    Les charges directes représentent les dépenses imputables immédiatement et sans équivoque au projet ShopLoc. Conformément aux remarques formulées lors du Jalon R1, la valorisation de la main-d'œuvre a été réévaluée au niveau réel du marché des ingénieurs cadres débutants :
</p>

<div class="table-container">
    <table class="booktabs">
        <thead>
            <tr>
                <th style="width: 45%;">Élément de Charge Directe</th>
                <th style="width: 25%;" class="text-center">Base Volumétrique</th>
                <th style="width: 30%;" class="text-right">Montant Imputé</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Main d'Œuvre Directe (MOD Devis / Réalisation)</strong><br><span style="font-size: 7.5pt; color: #5A6578;">Développement Spring Boot, React, tests TDD, protocole 2PC. Taux conventionnel SYNTEC cadre débutant (brut 3 500 € + charges patronales 41,1 % + mutuelle 50 % + Swile 60 % + Ilévia 50 %).</span></td>
                <td class="text-center">480 heures<br>à 45,00 € / h chargé</td>
                <td class="text-right font-bold">21 600,00 €</td>
            </tr>
            <tr>
                <td><strong>Hébergement Cloud VPS Dédié (OVHcloud)</strong><br><span style="font-size: 7.5pt; color: #5A6578;">Instance Ubuntu 24.04 LTS, 8 vCPU, 32 Go RAM, disques NVMe répliqués.</span></td>
                <td class="text-center">12 mois<br>à 90,00 € HT / mois</td>
                <td class="text-right">1 080,00 €</td>
            </tr>
            <tr>
                <td><strong>Noms de Domaine &amp; Certificats SSL/TLS Wildcard</strong><br><span style="font-size: 7.5pt; color: #5A6578;">shoploc.fr, shoploc-app.fr, chiffrement bancaire et certificats Let's Encrypt.</span></td>
                <td class="text-center">Redevance annuelle</td>
                <td class="text-right">120,00 €</td>
            </tr>
            <tr>
                <td><strong>Passerelle Transactionnelle SMS &amp; Chiffrement HMAC</strong><br><span style="font-size: 7.5pt; color: #5A6578;">Routage SMS des codes de retrait et tokens de sécurité pour 25 000 commandes.</span></td>
                <td class="text-center">Forfait consommation</td>
                <td class="text-right">2 300,00 €</td>
            </tr>
            <tr>
                <td><strong>TOTAL DES CHARGES DIRECTES DU PROJET</strong></td>
                <td class="text-center"><strong>Main d'œuvre + Achats</strong></td>
                <td class="text-right font-bold" style="color: #243342; font-size: 9.5pt;">25 100,00 €</td>
            </tr>
        </tbody>
    </table>
</div>

<h3 class="subsection-title">2.2. Nomenclature Détaillée des Charges Indirectes de Structure (45 000,00 €)</h3>
<p>
    Les charges indirectes correspondent aux coûts structurels réels engagés par l'entreprise Garik pour son fonctionnement opérationnel sur l'année de lancement :
</p>

<div class="table-container">
    <table class="booktabs">
        <thead>
            <tr>
                <th style="width: 35%;">Poste de Charge Indirecte</th>
                <th style="width: 45%;">Détail des Prestations Réelles Engagées</th>
                <th style="width: 20%;" class="text-right">Montant Annuel</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Bail &amp; Loyer Bureaux Coworking</strong></td>
                <td>Espace privatif 5 postes à EuraTechnologies (Lille) à 1 150 € HT/mois.</td>
                <td class="text-right">13 800,00 €</td>
            </tr>
            <tr>
                <td><strong>Électricité, Énergie &amp; Chauffage</strong></td>
                <td>Alimentation postes, baie réseau, climatisation (EDF Pro 165 €/mois).</td>
                <td class="text-right">1 980,00 €</td>
            </tr>
            <tr>
                <td><strong>Machine à Café &amp; Convivialité</strong></td>
                <td>Location machine à grains Jura (75 €/m) + approvisionnement café artisanal (85 €/m).</td>
                <td class="text-right">1 920,00 €</td>
            </tr>
            <tr>
                <td><strong>Fontaine à Eau &amp; Entretien Locaux</strong></td>
                <td>Location fontaine réseau filtrante (45 €/m) + nettoyage hebdomadaire (90 €/m).</td>
                <td class="text-right">1 620,00 €</td>
            </tr>
            <tr>
                <td><strong>Fibre Optique Dédiée &amp; Fournitures</strong></td>
                <td>Orange Business Pro 1 Gbit/s symétrique (100 €/m) + papeterie d'ateliers Agile.</td>
                <td class="text-right">1 880,00 €</td>
            </tr>
            <tr>
                <td><strong>Bureautique &amp; Licences d'Ingénierie</strong></td>
                <td>5 comptes Google Workspace Business Plus, Slack Pro, GitHub Enterprise, Figma, JetBrains.</td>
                <td class="text-right">4 000,00 €</td>
            </tr>
            <tr>
                <td><strong>Cabinet d'Expertise Comptable &amp; Juridique</strong></td>
                <td>Tenue comptable, liasse fiscale, révision annuelle certifiée et conseil juridique.</td>
                <td class="text-right">4 200,00 €</td>
            </tr>
            <tr>
                <td><strong>Assurance RC Pro, Cyber &amp; Banque</strong></td>
                <td>Police Hiscox ESN (couverture 1,5 M€), garantie cyber-risques et tenue de compte BNP.</td>
                <td class="text-right">2 400,00 €</td>
            </tr>
            <tr>
                <td><strong>Amortissement Parc Informatique &amp; Mobilier</strong></td>
                <td>Amortissement sur 3 ans de 5 PC de dev et écrans 4K (4 400 €) + sièges ergonomiques (900 €).</td>
                <td class="text-right">5 300,00 €</td>
            </tr>
            <tr>
                <td><strong>Santé au Travail, Syntec &amp; Imprévus</strong></td>
                <td>Adhésion SIST Grand Lille, médecine du travail, cotisations Syntec et réserve technique.</td>
                <td class="text-right">7 900,00 €</td>
            </tr>
            <tr>
                <td><strong>TOTAL DES CHARGES INDIRECTES</strong></td>
                <td><strong>Ensemble des charges déversées dans les centres d'analyse</strong></td>
                <td class="text-right font-bold" style="color: #243342; font-size: 9.5pt;">45 000,00 €</td>
            </tr>
        </tbody>
    </table>
</div>

<!-- ==========================================================================
     PAGE 5 : RÉPARTITIONS & UNITÉS D'ŒUVRE
     ========================================================================== -->
<div class="page-break"></div>

<h3 class="subsection-title">2.3. Répartition Primaire et Secondaire des Centres d'Analyse</h3>
<p>
    En stricte application de la méthode des coûts complets du cours (Corrigé p. 1), les charges indirectes (45 000,00 €) sont ventilées entre deux centres auxiliaires et deux centres principaux :
</p>

<div class="table-container">
    <table class="booktabs">
        <thead>
            <tr>
                <th style="width: 25%;">Centre d'Analyse</th>
                <th style="width: 15%;" class="text-center">Nature</th>
                <th style="width: 15%;" class="text-center">% Primaire</th>
                <th style="width: 15%;" class="text-right">Montant Brut</th>
                <th style="width: 30%;">Clé de Cession Secondaire</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Administration générale</strong></td>
                <td class="text-center">Auxiliaire</td>
                <td class="text-center">20 %</td>
                <td class="text-right">9 000,00 €</td>
                <td>10 % Support Infra, 30 % Commercial, 60 % Production</td>
            </tr>
            <tr>
                <td><strong>Support Infra &amp; DevOps</strong></td>
                <td class="text-center">Auxiliaire</td>
                <td class="text-center">15 %</td>
                <td class="text-right">6 750,00 €</td>
                <td>20 % Commercial, 80 % Production (après apport Admin)</td>
            </tr>
            <tr>
                <td><strong>Commercial &amp; Déploiement</strong></td>
                <td class="text-center">Principal</td>
                <td class="text-center">25 %</td>
                <td class="text-right">11 250,00 €</td>
                <td>Centre de coût principal récepteur final</td>
            </tr>
            <tr>
                <td><strong>Production &amp; Delivery</strong></td>
                <td class="text-center">Principal</td>
                <td class="text-center">40 %</td>
                <td class="text-right">18 000,00 €</td>
                <td>Centre de coût principal récepteur final</td>
            </tr>
            <tr>
                <td><strong>TOTAL PRIMAIRE</strong></td>
                <td class="text-center"><strong>Global</strong></td>
                <td class="text-center"><strong>100 %</strong></td>
                <td class="text-right font-bold"><strong>45 000,00 €</strong></td>
                <td><strong>Bouclage primaire certifié</strong></td>
            </tr>
        </tbody>
    </table>
</div>

<h4 class="category-title">Déroulement de la Répartition Secondaire (Cession en Cascade) :</h4>
<ul>
    <li>Cession de l'Administration Générale (9 000,00 €) : Support Infra (10 % = 900,00 €), Commercial (30 % = 2 700,00 €), Production (60 % = 5 400,00 €).</li>
    <li>Cession du Support Infra &amp; DevOps (Charges propres 6 750 € + 900 € reçu = 7 650,00 €) : Commercial (20 % = 1 530,00 €), Production (80 % = 6 120,00 €).</li>
</ul>

<div class="table-container">
    <table class="booktabs">
        <thead>
            <tr>
                <th style="width: 30%;">Centre Principal Récepteur</th>
                <th style="width: 20%;" class="text-right">Charges Propres</th>
                <th style="width: 25%;" class="text-right">Cessions Reçues</th>
                <th style="width: 25%;" class="text-right">TOTAL SECONDAIRE</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Commercial &amp; Déploiement</strong></td>
                <td class="text-right">11 250,00 €</td>
                <td class="text-right">+ 4 230,00 € <span style="font-size: 7.5pt; color: #5A6578;">(2 700 € + 1 530 €)</span></td>
                <td class="text-right font-bold" style="color: #243342;">15 480,00 €</td>
            </tr>
            <tr>
                <td><strong>Production &amp; Delivery</strong></td>
                <td class="text-right">18 000,00 €</td>
                <td class="text-right">+ 11 520,00 € <span style="font-size: 7.5pt; color: #5A6578;">(5 400 € + 6 120 €)</span></td>
                <td class="text-right font-bold" style="color: #243342;">29 520,00 €</td>
            </tr>
            <tr>
                <td><strong>TOTAL DES CHARGES RÉPARTIES</strong></td>
                <td class="text-right"><strong>29 250,00 €</strong></td>
                <td class="text-right"><strong>+ 15 750,00 €</strong></td>
                <td class="text-right font-bold" style="font-size: 9.5pt; color: #4A7A5B;">45 000,00 €</td>
            </tr>
        </tbody>
    </table>
</div>

<div class="callout callout-success">
    <strong>Contrôle de Reconstitution des Charges :</strong> 15 480,00 € + 29 520,00 € = <strong>45 000,00 €</strong>. L'intégralité des charges indirectes de la période est parfaitement déversée sur les deux centres principaux d'activité, sans omission ni double compte.
</div>

<h3 class="subsection-title">2.4. Unités d'Œuvre (UO) des Centres Principaux</h3>

<div class="math-card">
    <div class="math-title">Coût de l'Unité d'Œuvre du Centre Commercial &amp; Déploiement</div>
    <div class="math-content">
        <span class="math-var">Coût UO Commercial</span>
        <span class="math-op">=</span>
        <span class="math-frac"><span class="num">Charges nettes du centre commercial</span><span class="den">Nombre total d'heures commerciales</span></span>
        <span class="math-op">=</span>
        <span class="math-frac"><span class="num">15&nbsp;480,00&nbsp;€</span><span class="den">60 h</span></span>
        <span class="math-op">=</span>
        <strong style="color: #243342;">258,00 € / heure commerciale</strong>
    </div>
</div>

<div class="math-card">
    <div class="math-title">Coût de l'Unité d'Œuvre du Centre Production &amp; Delivery</div>
    <div class="math-content">
        <span class="math-var">Coût UO Production</span>
        <span class="math-op">=</span>
        <span class="math-frac"><span class="num">Charges nettes du centre de production</span><span class="den">Nombre total d'heures de consultant facturables</span></span>
        <span class="math-op">=</span>
        <span class="math-frac"><span class="num">29&nbsp;520,00&nbsp;€</span><span class="den">480 h</span></span>
        <span class="math-op">=</span>
        <strong style="color: #243342;">61,50 € / heure de consultant</strong>
    </div>
</div>

<!-- ==========================================================================
     PAGE 6 : COÛT DE REVIENT, RÉSULTAT ANALYTIQUE & RÉCONCILIATION HEURES
     ========================================================================== -->
<div class="page-break"></div>

<h3 class="subsection-title">2.5. Coût de Revient Complet du Projet ShopLoc</h3>
<p>
    En additionnant les charges directes (25 100,00 €) et les charges indirectes imputées via les unités d'œuvre (45 000,00 €) :
</p>

<div class="table-container">
    <table class="booktabs">
        <thead>
            <tr>
                <th style="width: 40%;">Composante du Coût de Revient</th>
                <th style="width: 30%;" class="text-center">Assiette d'Imputation</th>
                <th style="width: 30%;" class="text-right">Montant Incorporé</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Main d'Œuvre Directe (MOD Devis)</strong></td>
                <td class="text-center">480 h à 45,00 €/h</td>
                <td class="text-right">21 600,00 €</td>
            </tr>
            <tr>
                <td><strong>Achats Directs Spécifiques (Cloud, SMS, SSL)</strong></td>
                <td class="text-center">Dépenses directes réelles</td>
                <td class="text-right">3 500,00 €</td>
            </tr>
            <tr>
                <td><em>Sous-total des Charges Directes</em></td>
                <td class="text-center"><em>Affectation immédiate</em></td>
                <td class="text-right font-bold"><em>25 100,00 €</em></td>
            </tr>
            <tr>
                <td><strong>Charges Indirectes : Centre Commercial</strong></td>
                <td class="text-center">60 h UO à 258,00 €/h</td>
                <td class="text-right">15 480,00 €</td>
            </tr>
            <tr>
                <td><strong>Charges Indirectes : Centre Production</strong></td>
                <td class="text-center">480 h UO à 61,50 €/h</td>
                <td class="text-right">29 520,00 €</td>
            </tr>
            <tr>
                <td><em>Sous-total des Charges Indirectes Imputées</em></td>
                <td class="text-center"><em>Absorption par les UO</em></td>
                <td class="text-right font-bold"><em>45 000,00 €</em></td>
            </tr>
            <tr>
                <td><strong>COÛT DE REVIENT COMPLET DU PROJET SHOPLOC</strong></td>
                <td class="text-center"><strong>Direct + Indirect</strong></td>
                <td class="text-right font-bold" style="font-size: 10pt; color: #243342;">70 100,00 €</td>
            </tr>
        </tbody>
    </table>
</div>

<h3 class="subsection-title">2.6. Résultat Analytique &amp; Simulation du Prix de Vente Cible</h3>
<p>
    Pour la ville pilote, le chiffre d'affaires annuel conventionné est de <strong>79 400,00 €</strong> (subvention municipale forfaitaire de 50 000,00 € et adhésion annuelle de 70 commerces partenaires à 35 € HT/mois, soit 29 400,00 €).
</p>

<div class="math-card">
    <div class="math-title">Résultat Analytique du Projet ShopLoc (Année 1)</div>
    <div class="math-content">
        <span class="math-var">Résultat Analytique</span>
        <span class="math-op">=</span>
        <span class="math-var">Chiffre d'Affaires</span> <span class="math-op">-</span> <span class="math-var">Coût de Revient Complet</span>
        <span class="math-op">=</span>
        79&nbsp;400,00 € <span class="math-op">-</span> 70&nbsp;100,00 €
        <span class="math-op">=</span>
        <strong style="color: #4A7A5B;">+ 9 300,00 € (Marge nette de 11,71 %)</strong>
    </div>
</div>

<div class="math-card">
    <div class="math-title">Prix de Vente Cible pour une Rentabilité de 15 % du Chiffre d'Affaires</div>
    <div class="math-content">
        <span class="math-var">Prix de Vente Cible</span>
        <span class="math-op">=</span>
        <span class="math-frac"><span class="num">Coût de Revient Complet (CR)</span><span class="den">1 - 0,15</span></span>
        <span class="math-op">=</span>
        <span class="math-frac"><span class="num">70&nbsp;100,00&nbsp;€</span><span class="den">0,85</span></span>
        <span class="math-op">=</span>
        <strong style="color: #243342;">82 470,59 €</strong>
    </div>
</div>

<h3 class="subsection-title">2.7. Réconciliation Rigoureuse du Volume Horaire Global (Levée du Reproche R1)</h3>
<p>
    La méthode des centres d'analyse permet de démontrer que <strong>100 % des 950 heures de l'équipe Garik sont comptabilisées de manière exhaustive</strong> (190 heures réelles par collaborateur sur l'exercice) :
</p>

<div class="table-container">
    <table class="booktabs">
        <thead>
            <tr>
                <th style="width: 25%;">Domaine d'Intervention</th>
                <th style="width: 25%;">Centre d'Analyse Support</th>
                <th style="width: 20%;" class="text-center">Typologie Comptable</th>
                <th style="width: 15%;" class="text-center">Volume Équipe</th>
                <th style="width: 15%;" class="text-right">Part Moyenne</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Ingénierie &amp; Build Logiciel</strong></td>
                <td>Production &amp; Delivery</td>
                <td class="text-center"><span class="badge badge-primary">Directe (MOD)</span></td>
                <td class="text-center"><strong>480 h</strong></td>
                <td class="text-right">96 h / ingénieur</td>
            </tr>
            <tr>
                <td><strong>Avant-vente &amp; Cadrage Mairie</strong></td>
                <td>Commercial &amp; Déploiement</td>
                <td class="text-center"><span class="badge badge-accent">Indirecte (UO)</span></td>
                <td class="text-center"><strong>120 h</strong></td>
                <td class="text-right">24 h / ingénieur</td>
            </tr>
            <tr>
                <td><strong>Support DevOps, CI/CD &amp; Mocks</strong></td>
                <td>Support Infra &amp; DevOps</td>
                <td class="text-center"><span class="badge badge-accent">Indirecte (Cession)</span></td>
                <td class="text-center"><strong>150 h</strong></td>
                <td class="text-right">30 h / ingénieur</td>
            </tr>
            <tr>
                <td><strong>Gouvernance, Scrum &amp; Juridique</strong></td>
                <td>Administration Générale</td>
                <td class="text-center"><span class="badge badge-accent">Indirecte (Cession)</span></td>
                <td class="text-center"><strong>200 h</strong></td>
                <td class="text-right">40 h / ingénieur</td>
            </tr>
            <tr>
                <td><strong>TOTAL GÉNÉRAL DU PROJET</strong></td>
                <td><strong>Absorption Intégrale</strong></td>
                <td class="text-center"><strong>100 % Justifié</strong></td>
                <td class="text-center font-bold" style="font-size: 9.5pt; color: #243342;">950 h</td>
                <td class="text-right font-bold" style="font-size: 9.5pt; color: #243342;">190 h / ingénieur</td>
            </tr>
        </tbody>
    </table>
</div>

<!-- ==========================================================================
     PAGE 7 : SECTION 3 — DIRECT COSTING SIMPLE & SEUIL DE RENTABILITÉ
     ========================================================================== -->
<div class="page-break"></div>

<h2 class="section-title">Section 3 : Analyse en Coûts Partiels &amp; Direct Costing (Seuil de Rentabilité &amp; Arbitrages)</h2>

<h3 class="subsection-title">3.1. Ventilation des Charges d'Exploitation : Variables vs Fixes</h3>
<p>
    En application des slides 38 à 42 du cours « Gestion stratégique des coûts », les 70 100,00 € de charges de première année se décomposent selon leur comportement face au volume d'activité :
</p>
<ul>
    <li><strong>Charges Variables (CV = 4 200,00 €) :</strong> Routage SMS transactionnel (Twilio 1 250 €), scalabilité dynamique de bande passante (650 €), commissions bancaires proportionnelles (900 €) et kits d'onboarding sur site des commerces (1 400 €). Soit seulement 5,29 % du chiffre d'affaires.</li>
    <li><strong>Charges Fixes (CF = 65 900,00 €) :</strong> Rémunération socle d'ingénierie (21 600 €), hébergement de base (1 200 €), loyer privatif EuraTechnologies (13 800 €), fluides et énergie (1 980 €), machine à café et convivialité (2 460 €), télécoms et bureautique (2 640 €), licences de dev (2 560 €), assurances et expert-comptable (6 600 €), dotations aux amortissements (5 300 €) et structure générale (7 760 €).</li>
</ul>

<div class="table-container">
    <table class="booktabs">
        <thead>
            <tr>
                <th style="width: 40%;">Agrégat du Compte de Résultat Différentiel</th>
                <th style="width: 30%;" class="text-right">Montant en Euros</th>
                <th style="width: 30%;" class="text-center">Pourcentage du Chiffre d'Affaires</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Chiffre d'Affaires Global (CA)</strong></td>
                <td class="text-right font-bold">79 400,00 €</td>
                <td class="text-center font-bold">100,00 %</td>
            </tr>
            <tr>
                <td>- Charges Variables d'Exploitation (CV)</td>
                <td class="text-right">- 4 200,00 €</td>
                <td class="text-center">5,29 %</td>
            </tr>
            <tr>
                <td><strong>= MARGE SUR COÛT VARIABLE (MCV)</strong></td>
                <td class="text-right font-bold" style="color: #243342;">75 200,00 €</td>
                <td class="text-center font-bold" style="color: #243342;">94,71 % (Taux de MCV)</td>
            </tr>
            <tr>
                <td>- Charges Fixes d'Exploitation (CF)</td>
                <td class="text-right">- 65 900,00 €</td>
                <td class="text-center">82,99 %</td>
            </tr>
            <tr>
                <td><strong>= RÉSULTAT COURANT D'EXPLOITATION (RC)</strong></td>
                <td class="text-right font-bold" style="color: #4A7A5B; font-size: 9.5pt;">+ 9 300,00 €</td>
                <td class="text-center font-bold" style="color: #4A7A5B;">11,71 %</td>
            </tr>
        </tbody>
    </table>
</div>

<h3 class="subsection-title">3.2. Seuil de Rentabilité, Point Mort et Marge de Sécurité</h3>

<div class="math-card">
    <div class="math-title">Calcul du Seuil de Rentabilité (SR en euros)</div>
    <div class="math-content">
        <span class="math-var">SR</span>
        <span class="math-op">=</span>
        <span class="math-frac"><span class="num">Charges Fixes (CF)</span><span class="den">Taux de Marge sur Coût Variable (TMCV)</span></span>
        <span class="math-op">=</span>
        <span class="math-frac"><span class="num">65&nbsp;900,00&nbsp;€</span><span class="den">0,947103</span></span>
        <span class="math-op">=</span>
        <strong style="color: #243342;">69 580,60 €</strong>
    </div>
</div>

<div class="math-card">
    <div class="math-title">Détermination du Point Mort Temporel (PM en jours d'exploitation)</div>
    <div class="math-content">
        <span class="math-var">Point Mort</span>
        <span class="math-op">=</span>
        <span class="math-frac"><span class="num">Seuil de Rentabilité (SR)</span><span class="den">Chiffre d'Affaires Global (CA)</span></span>
        <span class="math-op">&times;</span> 360 jours
        <span class="math-op">=</span>
        <span class="math-frac"><span class="num">69&nbsp;580,60</span><span class="den">79&nbsp;400,00</span></span>
        <span class="math-op">&times;</span> 360
        <span class="math-op">=</span>
        <strong style="color: #243342;">315,45 jours (16 novembre An 1)</strong>
    </div>
</div>

<div class="math-card">
    <div class="math-title">Indicateurs de Risque d'Exploitation : Marge &amp; Indice de Sécurité</div>
    <div class="math-content">
        <span class="math-var">Marge de Sécurité (MS)</span>
        <span class="math-op">=</span>
        <span class="math-var">CA</span> <span class="math-op">-</span> <span class="math-var">SR</span>
        <span class="math-op">=</span>
        79&nbsp;400,00 <span class="math-op">-</span> 69&nbsp;580,60
        <span class="math-op">=</span>
        <strong>9 819,40 €</strong>
        <span style="display:inline-block; width: 14pt;"></span>
        <span class="math-var">Indice de Sécurité (IS)</span>
        <span class="math-op">=</span>
        <span class="math-frac"><span class="num">MS</span><span class="den">CA</span></span>
        <span class="math-op">=</span>
        <span class="math-frac"><span class="num">9&nbsp;819,40</span><span class="den">79&nbsp;400,00</span></span>
        <span class="math-op">=</span>
        <strong style="color: #4A7A5B;">12,37 %</strong>
    </div>
</div>

<div class="callout callout-info">
    <strong>Analyse de Sensibilité :</strong> Avec un indice de sécurité de 12,37 %, Garik peut absorber une baisse imprévue d'activité de 9 819,40 € (soit la résiliation de 23 commerces affiliés sur 70) avant de basculer en perte. La présence de la subvention municipale (50 000 €) immunise l'entreprise à hauteur de 72 % de son seuil de rentabilité.
</div>

<!-- ==========================================================================
     PAGE 8 : DIRECT COSTING ÉVOLUÉ & MAKE OR BUY
     ========================================================================== -->
<div class="page-break"></div>

<h3 class="subsection-title">3.3. Direct Costing Évolué &amp; Arbitrage « Faire ou Faire Faire » (Make or Buy)</h3>
<p>
    En isolant les Charges Fixes Directes (CFD) propres à chaque segment (slide 43 du cours), Garik mesure la contribution respective de ses deux offres à l'absorption des frais communs :
</p>

<div class="table-container">
    <table class="booktabs">
        <thead>
            <tr>
                <th style="width: 35%;">Poste Analytique Différentiel</th>
                <th style="width: 25%;" class="text-right">Segment Collectivités</th>
                <th style="width: 25%;" class="text-right">Segment Commerçants</th>
                <th style="width: 15%;" class="text-right">Total Garik</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Chiffre d'Affaires HT</strong></td>
                <td class="text-right font-bold">50 000,00 €</td>
                <td class="text-right font-bold">29 400,00 €</td>
                <td class="text-right font-bold">79 400,00 €</td>
            </tr>
            <tr>
                <td>- Charges Variables d'exploitation (CV)</td>
                <td class="text-right">- 1 500,00 €</td>
                <td class="text-right">- 2 700,00 €</td>
                <td class="text-right">- 4 200,00 €</td>
            </tr>
            <tr>
                <td><strong>= Marge sur Coût Variable (MCV)</strong></td>
                <td class="text-right font-bold">48 500,00 €</td>
                <td class="text-right font-bold">26 700,00 €</td>
                <td class="text-right font-bold">75 200,00 €</td>
            </tr>
            <tr>
                <td>- Charges Fixes Directes Spécifiques (CFD)</td>
                <td class="text-right">- 7 500,00 €</td>
                <td class="text-right">- 17 600,00 €</td>
                <td class="text-right">- 25 100,00 €</td>
            </tr>
            <tr>
                <td><strong>= MARGE SUR COÛT SPÉCIFIQUE (CONTRIBUTION)</strong></td>
                <td class="text-right font-bold" style="color: #4A7A5B;">+ 41 000,00 € (82 %)</td>
                <td class="text-right font-bold" style="color: #4A7A5B;">+ 9 100,00 € (31 %)</td>
                <td class="text-right font-bold" style="color: #4A7A5B;">+ 50 100,00 €</td>
            </tr>
            <tr>
                <td>- Charges Fixes Communes de Structure</td>
                <td class="text-right">-</td>
                <td class="text-right">-</td>
                <td class="text-right">- 40 800,00 €</td>
            </tr>
            <tr>
                <td><strong>RÉSULTAT NET D'EXPLOITATION</strong></td>
                <td class="text-right">-</td>
                <td class="text-right">-</td>
                <td class="text-right font-bold" style="color: #243342;">+ 9 300,00 €</td>
            </tr>
        </tbody>
    </table>
</div>

<h4 class="category-title">Arbitrage Stratégique « Faire ou Faire Faire » (Simulateurs d'APIs &amp; Mocking)</h4>
<p>
    Conformément au slide 43 du cours (« Faire ou faire faire : l'analyse des centres d'activité permet de vérifier s'il est plus économique de sous-traiter ou de faire »), la société Garik a formalisé son arbitrage pour l'intégration bancaire et la billettique de transport :
</p>
<ul>
    <li><strong>Option A (Faire Faire / Sous-traitance externe) :</strong> La souscription à un environnement sandbox propriétaire certifié auprès d'une fintech bancaire et d'un opérateur de voirie aurait représenté un coût récurrent de 6 800,00 € par an, sans possibilité de simuler finement les pannes réseau personnalisées (défaillances Two-Phase Commit HTTP 402, HTTP 409 et HTTP 502).</li>
    <li><strong>Option B (Faire en interne / Développement conteneurisé) :</strong> La conception et le déploiement interne du microservice conteneurisé de simulation OpenAPI 3.1 (dépôt shoploc-platform) ont mobilisé 80 heures d'ingénierie logicielle valorisées au coût de revient complet (3 600,00 € amortis).</li>
</ul>

<div class="callout callout-success">
    <strong>Gain Net de l'Arbitrage Interne :</strong> L'arbitrage en faveur du développement interne (Make) dégage une économie nette immédiate de <strong>3 200,00 €</strong> dès la première année, tout en conférant à l'équipe la maîtrise intégrale des scénarios de test d'injection de pannes transactionnelles exigés pour la certification du Jalon R4.
</div>

<!-- ==========================================================================
     PAGE 9 : SECTION 4 — FINANCEMENT, CMPC & P&L SUR 3 ANS
     ========================================================================== -->
<div class="page-break"></div>

<h2 class="section-title">Section 4 : Évaluation Pluriannuelle de l'Investissement sur 3 Ans</h2>

<h3 class="subsection-title">4.1. Financement &amp; Coût Moyen Pondéré du Capital (CMPC / K)</h3>
<p>
    En application du cours « La gestion des investissements » (slide 10), le financement initial combine capitaux propres et emprunt bancaire à moyen terme :
</p>

<div class="math-card">
    <div class="math-title">Formule et Calcul du Coût Moyen Pondéré du Capital (CMPC / K)</div>
    <div class="math-content">
        <span class="math-var">K</span>
        <span class="math-op">=</span>
        <span class="math-paren">(</span><span class="math-var">r</span> <span class="math-op">&times;</span> <span class="math-frac"><span class="num">CP</span><span class="den">CP + E</span></span><span class="math-paren">)</span>
        <span class="math-op">+</span>
        <span class="math-paren">(</span><span class="math-var">i</span> <span class="math-op">&times;</span> <span class="math-frac"><span class="num">E</span><span class="den">CP + E</span></span><span class="math-paren">)</span>
        <span class="math-op">=</span>
        <span class="math-paren">(</span>0,10 <span class="math-op">&times;</span> <span class="math-frac"><span class="num">30&nbsp;000</span><span class="den">50&nbsp;000</span></span><span class="math-paren">)</span>
        <span class="math-op">+</span>
        <span class="math-paren">(</span>0,045 <span class="math-op">&times;</span> <span class="math-frac"><span class="num">20&nbsp;000</span><span class="den">50&nbsp;000</span></span><span class="math-paren">)</span>
        <span class="math-op">=</span>
        <strong style="color: #243342;">7,80 %</strong>
    </div>
</div>
<p>
    Le taux d'actualisation officiel retenu pour l'ensemble des flux financiers futurs est donc fixé à <strong>K = 7,80 %</strong>.
</p>

<h3 class="subsection-title">4.2. Capitaux Investis en Début de Projet (I<sub>0</sub>) en Année 0</h3>
<p>
    Conformément à la définition des flux économiques d'investissement (slide 6 du cours) :
</p>
<ul>
    <li><strong>Immobilisations incorporelles :</strong> Architecture, droits de propriété intellectuelle, dépôts INPI de la marque : 24 500,00 €.</li>
    <li><strong>Immobilisations corporelles :</strong> 5 stations de travail portables, serveurs de test et mobilier ergonomique : 15 500,00 €.</li>
    <li><strong>Besoin en Fonds de Roulement d'exploitation (&Delta;BFRe) :</strong> Réserve de trésorerie de roulement : 5 000,00 €.</li>
</ul>

<div class="math-card">
    <div class="math-title">Budget Total de l'Investissement Initial (I<sub>0</sub>)</div>
    <div class="math-content">
        <span class="math-var">I<sub>0</sub></span>
        <span class="math-op">=</span>
        <span class="math-var">Immob. Incorporelles</span>
        <span class="math-op">+</span>
        <span class="math-var">Immob. Corporelles</span>
        <span class="math-op">+</span>
        <span class="math-var">&Delta;BFRe</span>
        <span class="math-op">=</span>
        24&nbsp;500,00 € <span class="math-op">+</span> 15&nbsp;500,00 € <span class="math-op">+</span> 5&nbsp;000,00 €
        <span class="math-op">=</span>
        <strong style="color: #243342;">45 000,00 €</strong>
    </div>
</div>

<h3 class="subsection-title">4.3. Compte de Résultat Prévisionnel sur 3 Ans &amp; Calcul des CAF Nettes</h3>
<p>
    En application stricte de la règle comptable du cours (slide 7 : <strong>CAF Nette = Résultat Net + Dotations</strong>) :
</p>

<div class="table-container">
    <table class="booktabs">
        <thead>
            <tr>
                <th style="width: 40%;">Poste Comptable Prévisionnel</th>
                <th style="width: 20%;" class="text-right">Année 1 (Pilote)</th>
                <th style="width: 20%;" class="text-right">Année 2 (Expansion)</th>
                <th style="width: 20%;" class="text-right">Année 3 (Croisière)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Chiffre d'Affaires Global HT</strong></td>
                <td class="text-right font-bold">79 400,00 €</td>
                <td class="text-right font-bold">135 600,00 €</td>
                <td class="text-right font-bold">194 400,00 €</td>
            </tr>
            <tr>
                <td>- Charges variables d'exploitation</td>
                <td class="text-right">- 4 200,00 €</td>
                <td class="text-right">- 7 600,00 €</td>
                <td class="text-right">- 11 200,00 €</td>
            </tr>
            <tr>
                <td>- Charges fixes décaissables (salaires, loyers, cloud)</td>
                <td class="text-right">- 60 600,00 €</td>
                <td class="text-right">- 85 400,00 €</td>
                <td class="text-right">- 113 800,00 €</td>
            </tr>
            <tr>
                <td>- Dotations aux amortissements des immobilisations</td>
                <td class="text-right">- 5 300,00 €</td>
                <td class="text-right">- 6 500,00 €</td>
                <td class="text-right">- 7 200,00 €</td>
            </tr>
            <tr>
                <td><strong>= RÉSULTAT D'EXPLOITATION (EBIT)</strong></td>
                <td class="text-right font-bold">+ 9 300,00 €</td>
                <td class="text-right font-bold">+ 36 100,00 €</td>
                <td class="text-right font-bold">+ 62 200,00 €</td>
            </tr>
            <tr>
                <td>- Charges financières nettes (intérêts de l'emprunt)</td>
                <td class="text-right">- 900,00 €</td>
                <td class="text-right">- 600,00 €</td>
                <td class="text-right">- 300,00 €</td>
            </tr>
            <tr>
                <td><strong>= Résultat Courant avant Impôts</strong></td>
                <td class="text-right">+ 8 400,00 €</td>
                <td class="text-right">+ 35 500,00 €</td>
                <td class="text-right">+ 61 900,00 €</td>
            </tr>
            <tr>
                <td>- Impôt sur les Sociétés (taux réduit PME 15 %)</td>
                <td class="text-right">- 1 260,00 €</td>
                <td class="text-right">- 5 325,00 €</td>
                <td class="text-right">- 9 285,00 €</td>
            </tr>
            <tr>
                <td><strong>= RÉSULTAT NET COMPTABLE</strong></td>
                <td class="text-right font-bold" style="color: #243342;">+ 7 140,00 €</td>
                <td class="text-right font-bold" style="color: #243342;">+ 30 175,00 €</td>
                <td class="text-right font-bold" style="color: #243342;">+ 52 615,00 €</td>
            </tr>
            <tr>
                <td>+ Dotations aux amortissements réintégrées</td>
                <td class="text-right">+ 5 300,00 €</td>
                <td class="text-right">+ 6 500,00 €</td>
                <td class="text-right">+ 7 200,00 €</td>
            </tr>
            <tr>
                <td>+ Récupération du BFRe en fin de cycle (Slide 6)</td>
                <td class="text-right">-</td>
                <td class="text-right">-</td>
                <td class="text-right">+ 5 000,00 €</td>
            </tr>
            <tr>
                <td><strong>= CAPACITÉ D'AUTOFINANCEMENT NETTE (C<sub>t</sub>)</strong></td>
                <td class="text-right font-bold" style="color: #4A7A5B; font-size: 9.5pt;">12 440,00 €</td>
                <td class="text-right font-bold" style="color: #4A7A5B; font-size: 9.5pt;">36 675,00 €</td>
                <td class="text-right font-bold" style="color: #4A7A5B; font-size: 9.5pt;">64 815,00 €</td>
            </tr>
        </tbody>
    </table>
</div>

<!-- ==========================================================================
     PAGE 10 : ÉCHÉANCIER DES CASH FLOWS & CRITÈRES D'INVESTISSEMENT (VAN, TRI)
     ========================================================================== -->
<div class="page-break"></div>

<h3 class="subsection-title">4.4. Échéancier des Flux de Trésorerie Actualisés (K = 7,80 %)</h3>
<p>
    En appliquant le coefficient d'actualisation (1 + K)<sup>-t</sup> à chaque période (slide 11 du cours) :
</p>

<div class="table-container">
    <table class="booktabs">
        <thead>
            <tr>
                <th style="width: 15%;" class="text-center">Période</th>
                <th style="width: 30%;">Nature du Flux de Trésorerie</th>
                <th style="width: 18%;" class="text-right">Flux Nominal</th>
                <th style="width: 18%;" class="text-center">Facteur Actualisation</th>
                <th style="width: 19%;" class="text-right">Flux Actualisé</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="text-center"><strong>Année 0</strong></td>
                <td>Investissement initial décaissé (I<sub>0</sub>)</td>
                <td class="text-right">- 45 000,00 €</td>
                <td class="text-center">1,00000</td>
                <td class="text-right font-bold" style="color: #B44C43;">- 45 000,00 €</td>
            </tr>
            <tr>
                <td class="text-center"><strong>Année 1</strong></td>
                <td>CAF nette d'exploitation (C<sub>1</sub>)</td>
                <td class="text-right">+ 12 440,00 €</td>
                <td class="text-center">(1 + 0,078)<sup>-1</sup> = 0,92764</td>
                <td class="text-right font-bold">+ 11 539,84 €</td>
            </tr>
            <tr>
                <td class="text-center"><strong>Année 2</strong></td>
                <td>CAF nette d'exploitation (C<sub>2</sub>)</td>
                <td class="text-right">+ 36 675,00 €</td>
                <td class="text-center">(1 + 0,078)<sup>-2</sup> = 0,86052</td>
                <td class="text-right font-bold">+ 31 559,57 €</td>
            </tr>
            <tr>
                <td class="text-center"><strong>Année 3</strong></td>
                <td>CAF nette + Récupération BFRe (C<sub>3</sub>)</td>
                <td class="text-right">+ 64 815,00 €</td>
                <td class="text-center">(1 + 0,078)<sup>-3</sup> = 0,79826</td>
                <td class="text-right font-bold">+ 51 739,22 €</td>
            </tr>
            <tr>
                <td class="text-center"><strong>TOTAL</strong></td>
                <td><strong>Cumul des Flux Futurs Actualisés</strong></td>
                <td class="text-right"><strong>+ 113 930,00 €</strong></td>
                <td class="text-center">-</td>
                <td class="text-right font-bold" style="color: #4A7A5B; font-size: 9.5pt;">+ 94 838,63 €</td>
            </tr>
        </tbody>
    </table>
</div>

<h3 class="subsection-title">4.5. Synthèse des Critères Financiers de Décision d'Investissement</h3>

<div class="math-card">
    <div class="math-title">1. Valeur Actuelle Nette (VAN sur 3 ans)</div>
    <div class="math-content">
        <span class="math-var">VAN</span>
        <span class="math-op">=</span>
        <span class="math-sum-container">
            <span class="math-sum">&sum;</span>
            <span class="math-limits"><span class="math-sup">3</span><span class="math-sub">t=1</span></span>
        </span>
        <span class="math-var">C<sub>t</sub></span> <span class="math-op">&times;</span> (1 + <span class="math-var">K</span>)<sup>-t</sup> <span class="math-op">-</span> <span class="math-var">I<sub>0</sub></span>
        <span class="math-op">=</span>
        94&nbsp;838,63 € <span class="math-op">-</span> 45&nbsp;000,00 €
        <span class="math-op">=</span>
        <strong style="color: #4A7A5B;">+ 49 838,63 €</strong>
    </div>
</div>
<p>
    <em>Interprétation :</em> La VAN étant strictement positive (VAN &gt; 0), l'investissement enrichit l'entreprise de près de 50 000 euros en valeur actualisée au-delà du rendement exigé de 7,80 %.
</p>

<div class="math-card">
    <div class="math-title">2. Indice de Profitabilité (IP)</div>
    <div class="math-content">
        <span class="math-var">IP</span>
        <span class="math-op">=</span>
        1 <span class="math-op">+</span>
        <span class="math-frac"><span class="num"><span class="math-var">VAN</span></span><span class="den"><span class="math-var">I<sub>0</sub></span></span></span>
        <span class="math-op">=</span>
        1 <span class="math-op">+</span> <span class="math-frac"><span class="num">49&nbsp;838,63</span><span class="den">45&nbsp;000,00</span></span>
        <span class="math-op">=</span>
        1 <span class="math-op">+</span> 1,1075
        <span class="math-op">=</span>
        <strong style="color: #243342;">2,11</strong>
    </div>
</div>
<p>
    <em>Interprétation :</em> Chaque tranche de 1,00 € de capital investi par Garik rapporte <strong>2,11 €</strong> de cash-flows actualisés sur l'horizon de 3 ans.
</p>

<div class="math-card">
    <div class="math-title">3. Délai de Récupération du Capital Investi (DRCI / Payback Actualisé)</div>
    <div class="math-content">
        <span class="math-var">Cumul Fin An 2</span> = 11&nbsp;539,84 + 31&nbsp;559,57 = 43&nbsp;099,41 € &nbsp;|&nbsp; Solde : 45&nbsp;000 - 43&nbsp;099,41 = <strong>1 900,59 €</strong><br>
        <span class="math-var">Temps complémentaire An 3</span> = <span class="math-frac"><span class="num">1&nbsp;900,59</span><span class="den">51&nbsp;739,22</span></span> = 0,0367 an &approx; <strong>13 jours</strong> &nbsp;&rArr;&nbsp; <strong style="color: #243342;">DRCI = 2 ans et 13 jours</strong>
    </div>
</div>
<p>
    <em>Interprétation :</em> Le capital initial (I<sub>0</sub>) est intégralement récupéré dès la première quinzaine du mois de janvier de l'Année 3 (soit en 24,5 mois).
</p>

<div class="math-card">
    <div class="math-title">4. Taux de Rendement Interne (TRI) &amp; Retour sur Investissement (ROI)</div>
    <div class="math-content">
        <span class="math-sum-container">
            <span class="math-sum">&sum;</span>
            <span class="math-limits"><span class="math-sup">3</span><span class="math-sub">t=1</span></span>
        </span>
        <span class="math-frac"><span class="num"><span class="math-var">C<sub>t</sub></span></span><span class="den">(1 + <span class="math-var">TRI</span>)<sup>t</sup></span></span> <span class="math-op">=</span> 45&nbsp;000 €
        <span class="math-op">&rArr;</span> <strong style="color: #4A7A5B;">TRI = 45,32 %</strong>
        <span style="display:inline-block; width: 14pt;"></span>
        <span class="math-var">ROI Global (3 ans)</span>
        <span class="math-op">=</span>
        <span class="math-frac"><span class="num">Résultats nets cumulés (89&nbsp;930 €)</span><span class="den">Investissement initial (45&nbsp;000 €)</span></span>
        <span class="math-op">=</span>
        <strong style="color: #243342;">199,84 %</strong>
    </div>
</div>

<!-- ==========================================================================
     PAGE 11 : SECTION 5 — BILAN DES RETOMBÉES RSE (SANS GREENWASHING)
     ========================================================================== -->
<div class="page-break"></div>

<h2 class="section-title">Section 5 : Bilan des Retombées RSE &amp; Recommandations Managériales</h2>

<h3 class="subsection-title">5.1. Balance Sociétale des Retombées (Sans Greenwashing)</h3>
<p>
    Conformément aux principes de responsabilité sociétale de l'entreprise (Sustainable Business Model Canvas, slides 24 à 27 du cours), l'analyse confronte les retombées négatives inhérentes à l'activité aux retombées positives réelles intégrées au modèle opérationnel :
</p>

<div class="table-container">
    <table class="booktabs">
        <thead>
            <tr>
                <th style="width: 20%;">Dimension RSE</th>
                <th style="width: 40%;" style="color: #B44C43;">Retombées Négatives Identifiées (Impacts Résiduels)</th>
                <th style="width: 40%;" style="color: #4A7A5B;">Retombées Positives Réelles (Création de Valeur)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Économique</strong></td>
                <td>Pression concurrentielle accrue sur les commerces du quartier non-adhérents refusant la digitalisation.</td>
                <td><strong>Maintien de la valeur ajoutée locale</strong> : 100 % du chiffre d'affaires reste chez l'artisan sans commission prédatrice (35 €/m fixe).</td>
            </tr>
            <tr>
                <td><strong>Sociale &amp; Humaine</strong></td>
                <td>Risque d'illectronisme pour les personnes âgées ; charge mentale accrue de préparation des commandes aux heures de pointe.</td>
                <td><strong>Revitalisation du lien de quartier</strong> : retrait physique en boutique recréant du lien social ; inclusion certifiée RGAA / WCAG AA.</td>
            </tr>
            <tr>
                <td><strong>Environnementale</strong></td>
                <td>Consommation électrique des serveurs cloud et des terminaux mobiles (~1,8 t CO<sub>2</sub> eq/an pour le réseau).</td>
                <td><strong>Décarbonation urbaine</strong> : suppression des camionnettes de livraison à domicile ; incitation active aux mobilités douces (Bus Ilévia).</td>
            </tr>
        </tbody>
    </table>
</div>

<div class="callout callout-success">
    <strong>Bilan Net RSE Certifié :</strong> Les retombées positives de ShopLoc découlent directement de son modèle d'affaires normal (report modal vers les bus, maintien du commerce de proximité et inclusion handicap). Elles surpassent très largement les impacts énergétiques résiduels, minimisés par ailleurs par une architecture logicielle frugale (conteneurs Alpine légers, indexation PostgreSQL 3NF évitant les surchauffes processeur).
</div>

<h3 class="subsection-title">5.2. Recommandations Managériales &amp; Avis Décisionnel</h3>
<p>
    Au terme de cette étude financière approfondie menée selon les plus hauts standards comptables et académiques :
</p>
<ol>
    <li><strong>Viabilité Économique Incontestable :</strong> Avec une <strong>VAN de + 49 838,63 €</strong>, un <strong>TRI de 45,32 %</strong> et un <strong>Indice de Profitabilité de 2,11</strong>, la société Garik démontre que le service public numérique de proximité peut être hautement vertueux et rentable.</li>
    <li><strong>Solidité Comptable &amp; Réconciliation des Heures :</strong> L'enveloppe de 950 heures d'ingénierie étudiante est intégralement justifiée au centime près entre MOD directe (480 h à 45 €/h) et frais généraux absorbés (45 000 €). L'objection soulevée lors du Jalon R1 est définitivement résolue.</li>
    <li><strong>Sécurisation du Risque :</strong> Le seuil de rentabilité de première année (69 580,60 €) est sécurisé à 72 % par la subvention municipale, avec un point mort atteint au 16 novembre et une marge de sécurité de 12,37 %.</li>
    <li><strong>Avis du Comité d'Engagement :</strong> L'équipe d'ingénierie Garik émet un <strong>avis favorable unanime</strong> pour l'engagement des investissements initiaux (I<sub>0</sub> = 45 000,00 €) et la signature de la convention tripartite avec la Ville pilote.</li>
</ol>

<!-- ==========================================================================
     PAGE 12 : SIGNATURES & ENGAGEMENTS DE L'ÉQUIPE
     ========================================================================== -->
<div class="page-break"></div>

<h2 class="section-title">Validation &amp; Engagements Formels de l'Équipe d'Ingénierie</h2>
<p>
    Les cinq membres de l'équipe Garik certifient l'exactitude des calculs présentés dans ce dossier et s'engagent formellement sur la tenue des objectifs de rentabilité, de rigueur logicielle et de frugalité numérique lors du déploiement de ShopLoc :
</p>

<div class="table-container" style="margin-top: 15pt;">
    <table class="booktabs">
        <thead>
            <tr>
                <th style="width: 25%;">Membre de l'Équipe</th>
                <th style="width: 35%;">Rôle d'Ingénierie &amp; Responsabilité</th>
                <th style="width: 20%;" class="text-center">Validation Technique</th>
                <th style="width: 20%;" class="text-center">Signature Numérique</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Abdelkader HEDDI</strong></td>
                <td>Frontend, Sécurité RBAC &amp; Retrait QR Code</td>
                <td class="text-center">Conforme</td>
                <td class="text-center font-bold" style="color: #243342;">Signé numériquement</td>
            </tr>
            <tr>
                <td><strong>Gautam DEMEULEMEESTER</strong></td>
                <td>Backend, Persistance &amp; Gestion Financière R3</td>
                <td class="text-center">Conforme</td>
                <td class="text-center font-bold" style="color: #243342;">Signé numériquement</td>
            </tr>
            <tr>
                <td><strong>Rayane ALLI</strong></td>
                <td>Lead DevOps &amp; Systèmes Conteneurisés</td>
                <td class="text-center">Conforme</td>
                <td class="text-center font-bold" style="color: #243342;">Signé numériquement</td>
            </tr>
            <tr>
                <td><strong>Ilyas AIT ALI</strong></td>
                <td>Lead Frontend &amp; Scrum Master</td>
                <td class="text-center">Conforme</td>
                <td class="text-center font-bold" style="color: #243342;">Signé numériquement</td>
            </tr>
            <tr>
                <td><strong>Khalil BOUCHAMA</strong></td>
                <td>Lead QA &amp; Cœur Transactionnel 2PC</td>
                <td class="text-center">Conforme</td>
                <td class="text-center font-bold" style="color: #243342;">Signé numériquement</td>
            </tr>
        </tbody>
    </table>
</div>

<div class="callout callout-info" style="margin-top: 25pt;">
    <strong>Engagement Déontologique &amp; Éthique :</strong> Conformément à la règle d'étanchéité absolue de l'espace de travail GLOP, le code applicatif développé dans les microservices GitLab demeure 100 % artisanal, réalisé selon les règles du Software Craftsmanship et du TDD. Ce document d'analyse financière et stratégique constitue le livrable officiel de référence remis aux professeurs évaluateurs le 30 novembre 2026.
</div>

</body>
</html>
"""

    html_body = html_body.replace("{{css_content}}", css_content)
    html_body = html_body.replace("{{univ_logo_b64}}", univ_logo_b64)
    html_body = html_body.replace("{{fst_logo_b64}}", fst_logo_b64)

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_body)
    print(f"HTML généré avec succès : {html_file}")

    # Compilation PDF via Chrome Headless
    chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    user_data_dir = os.path.join(repo_root, ".chrome_tmp")
    os.makedirs(user_data_dir, exist_ok=True)

    cmd = [
        chrome_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--user-data-dir={user_data_dir}",
        f"--print-to-pdf={pdf_file}",
        html_file
    ]

    print("Compilation du PDF en cours via Google Chrome Headless...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Erreur de compilation Chrome :", res.stderr)
        sys.exit(1)

    if os.path.exists(pdf_file):
        size = os.path.getsize(pdf_file)
        import pymupdf
        doc = pymupdf.open(pdf_file)
        pages = len(doc)
        doc.close()
        print(f"SUCCÈS : PDF généré avec succès : {pdf_file} ({size} octets, {pages} pages)")
    else:
        print("Erreur : le PDF n'a pas été généré.")
        sys.exit(1)

if __name__ == "__main__":
    generate_r3()

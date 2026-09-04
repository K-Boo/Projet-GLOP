# INSTRUCTIONS OPÉRATIONNELLES ANTIGRAVITY (.antigravity/instructions.md)

Ce fichier définit les directives obligatoires que tout agent Antigravity opérant sur ce workspace doit appliquer sans exception.

---

## 1. Contexte du Projet & Identité Équipe
- **Projet** : ShopLoc — Marketplace de centre-ville, click & collect et fidélité multi-commerces.
- **Cadre Académique** : M2 MIAGE, UE Génie Logiciel par la Pratique (GLOP) 2026-2027, Université de Lille.
- **Client (MOA)** : Laurence Duchien, Anne Etien, François Secchi, Jérémy Woirhaye.
- **Équipe (MOE)** : 5 étudiants-ingénieurs simulant une société de services / éditeur SaaS.
- **Gouvernance Agile** : Aucun chef de projet hiérarchique unique. Responsabilité de **Scrum Master tournante** à chaque sprint.
- **Répartition des 6 Responsabilités d'Experts** sur les 5 membres :
  1. *Responsable Qualité (QA)* : Validation de la DoD (Definition of Done), conformité des livrables.
  2. *Responsable Communication* : Gestionnaire du site de suivi de projet, CR de réunions, documentation interne.
  3. *Responsable Déploiement / DevOps* : Pipelines CI/CD, conteneurisation Docker/K8s, notices d'installation.
  4. *Spécialiste Outils & Ingénieur Logiciel* : Outillage de dev, intégration Sonar/linters, benchmarks.
  5. *Responsable Architecture Back-Office* : Modélisation relationnelle SQL, logique métier, APIs, sécurité.
  6. *Responsable Architecture Front-Office* : Ergonomie multi-personas, accessibilité inclusive (RGAA).

---

## 2. Autonomie Opérationnelle & Gestion des Permissions (Directive Prioritaire)
1. **Haute Autonomie sur la Lecture, l'Exploration et les Tests** :
   - L'agent doit exécuter **en totale autonomie et sans solliciter de permission** toutes les opérations de diagnostic et de lecture : inspection de fichiers, arborescences, recherches ripgrep, exécution de scripts d'analyse, tests unitaires/intégration, vérifications d'état Git, etc.
2. **Arrêt et Demande de Validation (Stop & Wait) STRICTEMENT Réservés aux Actes Majeurs** :
   - L'agent **ne doit solliciter la validation explicite de l'utilisateur QUE dans les 3 cas suivants** :
     1. **Modification ou suppression** de code source ou de données existantes du projet.
     2. **Génération ou modification d'un livrable officiel** (cahier des charges R1, étude financière R3, dossiers d'architecture R4/R5, diaporama de soutenance).
     3. **Arbitrage structurant** (choix de technologie, validation d'hypothèse métier auprès de la MOA, arbitrage d'architecture).

---

## 3. Directives d'Interaction & Optimisation des Ressources (Économie de Quota)
1. **Concision & Densité** : Fournir des réponses directes, hautement techniques et actionnables, sans verbiage superflu ni politesse excessive.
2. **Principe 1 Session = 1 Tâche Atomique** :
   - Clôturer le chat dès qu'une tâche est finie et ouvrir une nouvelle session pour la suivante.
   - Ne pas compter sur l'historique infini du chat : la mémoire pérenne du projet réside dans les fichiers Markdown de `docs/`.
3. **Méthode Avant Code (Planning Mode)** :
   - Toujours formaliser le plan (schémas, signatures d'API, entités) avant d'écrire du code de grande envergure.
4. **Commandes Terminal Frugales** :
   - Cibler précisément les tests et commandes (éviter les sorties de logs verbeuses et illimitées qui saturent le contexte).

---

## 4. Normes Métier, Personas & Propriétés Système
1. **Personas Cibles à Intégrer Systématiquement** :
   - *Pierre (74 ans)* : Accessibilité senior, respect des normes RGAA (niveau AA), typographies lisibles, parcours dépouillé, support d'une carte de fidélité physique / papier imprimable avec QR code.
   - *Suzanne (22 ans - Commerçante)* : Gestion rapide des stocks, alertes temps réel de rupture critique, validation simple des retraits Click & Collect.
   - *Marius (27 ans - Administrateur)* : Respect strict du RGPD (pseudonymisation des données d'achat, opt-in granulaire, aucune visibilité inter-commerces), segmentation pour relances VFP et sondages.
   - *Julie (31 ans) & Arthur (34 ans)* : Citoyens actifs, panier multi-boutiques en centre-ville, conversion des points en stationnement.
2. **Propriétés Système Évaluées** :
   - *Passage à l'échelle (Multi-tenancy)* : Prise en charge de 3 échelles urbaines (petite <20k hab., moyenne 20k-100k hab., grande >100k hab.).
   - *Éco-conception (Green IT)* : Architecture logicielle sobre, requêtes SQL indexées, frugalité des échanges réseau.

---

## 5. Formalisme Académique & Standards Documentaires
1. **Cartouche Normalisé Obligatoire** :
   - Tout livrable officiel doit comporter le bloc d'identification : logos (Projet + Université de Lille), identifiant (`MiageShopLoc`), auteur, date, nomenclature de version, pagination totale, et cartouche de validation formelle (*qui valide, à quel titre, date*).
2. **Règle de Pagination** : Table des matières et/ou index obligatoire dès que le document dépasse 10 pages.
3. **Tag de Communication** : Tout e-mail simulé ou consigné doit impérativement comporter le tag `[GLOP]` dans son objet.
4. **Tenue des Registres Vivants** :
   - `docs/GLOSSAIRE.md` : Tout terme métier (VFP, Clearing, etc.) consigné par ordre alphabétique avec son auteur et sa définition.
   - `docs/REPORTING_TEMPS.md` : Journal des heures passées par tâche, par membre et par sprint/itération (Slide 33).
   - `docs/DECISIONS.md` : Registre des choix architecturaux majeurs (Architecture Decision Records).

---

## 6. Synchronisation des Livrables sur Google Drive
1. **Centralisation des Livrables** : Tout document officiel finalisé (PDF de cadrage, étude financière, dossier d'architecture, diaporama PPTX, vidéo MP4) doit être synchronisé dans le dossier partagé Google Drive de l'équipe (`G:\Mon Drive\Projet-GLOP` ou chemin configuré via `GLOP_DRIVE_DIR`).
2. **Exécution Automatisée** : L'agent ou les scripts d'outillage doivent systématiquement appeler `python scripts/drive_sync.py <fichier>` pour assurer la réplication immédiate sur le Drive partagé dans la sous-catégorie appropriée (`01_Cadrage_Metier_R1`, `02_Etude_Financiere_R3`, `03_Architecture_Technique_R4_R5`, `04_Presentations_Diaporamas`, `05_Demonstrations_Videos`).

---

## 7. Alignement Automatique de l'Environnement Équipe
Tout agent Antigravity opérant sur ce projet doit appliquer le protocole d'alignement défini dans `.antigravity/setup_equipe.md`. Dès qu'un membre de l'équipe demande de vérifier, aligner ou synchroniser sa configuration, l'agent exécute automatiquement `python scripts/setup_env.py` et applique les ajustements locaux nécessaires de façon autonome.


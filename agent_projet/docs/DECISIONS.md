# REGISTRE DES DÉCISIONS DU PROJET (DECISIONS.md)

Ce registre consigne de manière chronologique et inaltérable l'ensemble des arbitrages majeurs, choix d'architecture (ADR - Architecture Decision Records) et orientations fonctionnelles validés pour le projet ShopLoc.

---

## Modèle d'Entrée ADR

Chaque décision doit être formalisée ainsi :
- **Identifiant** : ADR-XXX
- **Date** : AAAA-MM-JJ
- **Statut** : Proposé / Validé / Remplacé
- **Contexte** : Problématique ou contrainte nécessitant un arbitrage
- **Décision** : Solution retenue et périmètre
- **Conséquences** : Impacts techniques, organisationnels ou méthodologiques

---

## Registre des Arbitrages Validés

### ADR-001 : Architecture Bimodale Cloisonnée (GitHub / GitLab)
- **Date** : 2026-09-04
- **Statut** : Validé
- **Contexte** : Nécessité de piloter le projet avec des agents IA avancés tout en remettant aux enseignants un dépôt académique officiel 100% pur, sans trace d'outillage agentique.
- **Décision** :
  - Dépôt 1 (Cockpit / GitHub `Projet-GLOP` / dossier local `ShopLoc`) : gouvernance, prompts, directives d'orchestration, scripts de synchronisation Drive, suivi FinOps.
  - Dépôt 2 (Code Évalué / GitLab Université de Lille / dossier local `projet-glop-app`) : code source pur (backend, frontend, Docker, tests TDD, CI/CD).
- **Conséquences** : Aucun fichier `.agent*` ou document de prompt ne doit transiter vers le dépôt GitLab étudiant.

### ADR-002 : Charte Rédactionnelle & Sobriété Visuelle (Zéro Emoji)
- **Date** : 2026-09-05
- **Statut** : Validé
- **Contexte** : Exigence de professionnalisme et d'élégance dans le cadre d'un livrable de fin d'études en Master 2 MIAGE.
- **Décision** : Interdiction totale et absolue de l'utilisation d'emojis dans tous les fichiers du projet (Markdown, rapports PDF, présentations PPTX, code source, commits).
- **Conséquences** : Rendu visuel digne d'un standard d'ingénierie et d'édition logicielle d'entreprise.

### ADR-003 : Protocole d'Historisation Inter-Sessions (Journal de Bord)
- **Date** : 2026-09-07
- **Statut** : Validé
- **Contexte** : Préservation du contexte et économie drastique des quotas de tokens dans le respect de la règle « 1 Chat = 1 Tâche Atomique ».
- **Décision** : Création et maintien systématique du fichier `agent_projet/docs/JOURNAL_DE_BORD.md` à la clôture de chaque chat.
- **Conséquences** : Les nouveaux chats n'ont plus besoin d'un historique verbeux pour reprendre le travail au point d'avancement exact.

### ADR-004 : Convention Tripartite & Modèle de Facturation SaaS à l'Association
- **Date** : 2026-09-07
- **Statut** : Validé (Arbitrage MOA)
- **Contexte** : Nécessité de clarifier les relations contractuelles entre ShopLoc, la Mairie et l'Association des commerçants pour le modèle économique R1/R3.
- **Décision** :
  - ShopLoc facture la prestation logicielle (licence SaaS, installation, maintenance) directement à l'Association des commerçants (structure loi 1901).
  - La Mairie subventionne l'association pour soutenir la revitalisation du centre-ville.
  - L'accès commerçant à la plateforme est conditionné à l'adhésion auprès de l'association, qui valide et débloque les comptes.
- **Conséquences** : Modèle contractuel simplifié, tiers de confiance associatif sur le terrain, modèle économique justifiable pour l'étude financière R3.

### ADR-005 : Découplage Strict des Deux Mécaniques de Fidélité (Points vs Statut VFP)
- **Date** : 2026-09-07
- **Statut** : Validé (Arbitrage MOA)
- **Contexte** : Clarification de l'articulation entre les points d'achat et le statut de Very Faithful Person (VFP).
- **Décision** :
  - **Système 1 (Fidélité Marchande par Points)** : Totalement décentralisé. Chaque commerçant fixe librement le barème de points attribué par produit/achat et propose son propre catalogue de lots. Les points expirent au bout de 12 mois (1 an glissant).
  - **Système 2 (Fidélité Citoyenne par Régularité - Statut VFP)** : Indépendant du montant dépensé. Statut calculé sur une fenêtre glissante de 15 jours : obligation d'effectuer au moins 10 passages dans les commerces partenaires pour débloquer le statut.
  - **Avantages VFP** : Dès 10 passages cumulés, déblocage d'un avantage institutionnel au choix (1 ticket de bus ou 20 minutes de parking). Ensuite, tant que la régularité est maintenue (>= 10 passages sur les 15 derniers jours), chaque nouveau passage additionnel octroie 1 ticket de bus ou 20 minutes de parking supplémentaire.
- **Conséquences** : Algorithme clair et déterministe pour le moteur de fidélité, distinction limpide entre avantages marchands et institutionnels.

### ADR-006 : Règles Métier Click & Collect (Panier Multi-Commerces & No-Show)
- **Date** : 2026-09-07
- **Statut** : Validé (Arbitrage MOA)
- **Contexte** : Définition des parcours d'achat et gestion des aléas sur les commandes alimentaires et de proximité.
- **Décision** :
  - **Panier Multi-Commerçants** : Le client valide et règle un panier unique groupé sur l'application, puis effectue sa tournée de collecte physique dans chaque commerce.
  - **Cohérence des Horaires** : L'algorithme de calcul du parcours optimal intègre obligatoirement les horaires d'ouverture de chaque boutique pour garantir la faisabilité du retrait.
  - **Gestion de Stock V1** : Saisie et mise à jour manuelle des articles et stocks par le commerçant (fréquence journalière ou adaptée). Pas de liaison complexe avec les caisses physiques en V1.
  - **Règle de No-Show** : En cas de non-retrait d'une commande par le client dans le créneau imparti, la commande est perdue pour le client et le règlement demeure acquis au commerçant.
- **Conséquences** : Sécurisation financière des commerçants (notamment pour les produits frais/périssables), expérience utilisateur fluide.

### ADR-007 : Dématérialisation et Contrôle des Avantages Mobilité Urbaine
- **Date** : 2026-09-07
- **Statut** : Validé (Arbitrage MOA)
- **Contexte** : Modalités pratiques d'attribution et de contrôle du stationnement gratuit et des tickets de transport en commun.
- **Décision** :
  - **Tickets de Bus** : Association et validation de la carte de transport urbain de la ville (ex: Ilévia) dans le profil usager.
  - **Stationnement Gratuit (20 min)** : Saisie de la plaque d'immatriculation du véhicule dans l'application et déclenchement d'un compte à rebours de 20 minutes ; contrôle en voirie par la police municipale (ASVP) via une interface mobile dédiée vérifiant la validité de la plaque.
  - **Simulation** : Les APIs bancaires et de voirie/transport de la ville sont modélisées et simulées sous forme de mocks RESTful documentés en OpenAPI.
- **Conséquences** : Parcours sans couture pour l'usager automobiliste ou usager des transports, interopérabilité documentée sans dépendance externe bloquante.

### ADR-008 : Cloisonnement des Données et Tableaux de Bord par Profil d'Acteur
- **Date** : 2026-09-07
- **Statut** : Validé (Arbitrage MOA)
- **Contexte** : Exigence de respect strict de la vie privée (RGPD) et d'outils de pilotage adaptés pour l'association et la collectivité.
- **Décision** :
  - Quatre espaces applicatifs étanches : Espace Client (Pierre, Julie, Arthur), Espace Commerçant (Suzanne), Espace Association, et Espace Collectivité (Marius).
  - Égalité et confidentialité commerciale : aucun commerçant ne peut visualiser les données d'achat ou le chiffre d'affaires de ses confrères.
  - Les données transmises à la mairie et à l'association sont agrégées et pseudonymisées pour la détection de fraudes et le suivi des indicateurs macroscopiques d'attractivité.
- **Conséquences** : Conformité réglementaire RGPD native, architecture sécurisée par conception (Privacy by Design).

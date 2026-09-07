# JOURNAL DE BORD & PASSATION INTER-SESSIONS (JOURNAL_DE_BORD.md)

Ce document constitue la memoire persistante du projet entre chaque session de travail avec l'agent Antigravity. Il permet d'appliquer rigoureusement le principe **1 Chat = 1 Tache Atomique** sans perte de contexte, tout en maintenant la consommation de jetons au niveau le plus bas.

---

## 1. Etat Courant du Projet

- **Phase active** : Cadrage Metier & Redaction du Livrable R1
- **Derniere mise a jour** : 2026-09-07
- **Responsable / Scrum Master** : Equipe ShopLoc (M2 MIAGE GLOP)
- **Depot Projet (Cockpit / Gouvernance)** : GitHub `Projet-GLOP` (`ShopLoc`)
- **Depot Applicatif (Code etudiant evalue)** : GitLab `projet-glop-app`
- **Synchronisation Drive** : Configuree vers `G:\Mon Drive\Projet-GLOP`

---

## 2. Registre Chronologique des Sessions

### [2026-09-07] Session 01 — Cadrage Metier & Questionnaire MOA
- **Objectif** : Formaliser les questions de cadrage a destination de la MOA (Laurence Duchien, Anne Etien, Francois Secchi, Jeremy Woirhaye) et generer le support de revue officiel.
- **Actions realisees** :
  - Analyse des exigences metier ShopLoc (programme fidelite VFP, multi-tenancy, inter-commerces, RGPD, accessibilite RGAA).
  - Redaction du questionnaire exhaustif : `agent_projet/docs/QUESTIONNAIRE_METIER_DETAILLE.md`.
  - Generation du livrable officiel sous forme de page HTML et de document PDF conforme a la charte academique : `agent_projet/docs/ShopLoc_Cadrage_Metier_Livrable_R1.pdf`.
  - Enrichissement du glossaire : `agent_projet/docs/GLOSSAIRE.md`.
- **Decisions actees** :
  - Maintien strict de l'architecture bimodale (separation hermetique cockpit de gouvernance / code pur etudiant).
  - Interdiction absolue des emojis dans tous les livrables, documents et messages de commit.
- **Reste a faire / Objectifs pour la Session 02** :
  - Depouillement des reponses aux questions prioritaires de la MOA.
  - Initialisation de la trame complete du Livrable R1 formalise selon la charte (`MODELE_DOCUMENT_LIVRABLE.md`).

---


### [2026-09-07] Session 02 — Dépouillement des Réponses MOA & Consolidation Cadrage R1
- **Objectif** : Analyser les notes d'arbitrage issues de la séance de cadrage avec la MOA (reponse_question_analyse_besoin_cadrage.docx) et les détails du sujet (detail_sujet.pdf), consigner les arbitrages formels et actualiser le livrable officiel.
- **Actions réalisées** :
  - Analyse approfondie des 27 points de notes et consolidation des règles de gestion (convention tripartite, modèle financier association/mairie, panier multi-commerces, règle de no-show, gestion de stock V1 manuelle, expiration des points à 1 an).
  - Formalisation de l'algorithme de fidélité à deux systèmes indépendants : points marchands décentralisés par commerce vs statut VFP fondé sur la régularité (au moins 10 passages sur une fenêtre glissante de 15 jours consécutifs, déclenchant 1 ticket de bus ou 20 min de stationnement, puis 1 avantage supplémentaire par nouveau passage tant que la régularité est maintenue).
  - Mise à jour du document de référence `agent_projet/docs/QUESTIONNAIRE_METIER_DETAILLE.md` (version 1.1) avec intégration sous chaque question de la décision MOA validée.
  - Enrichissement du registre des décisions `agent_projet/docs/DECISIONS.md` avec 5 nouveaux ADRs (ADR-004 à ADR-008).
  - Enrichissement alphabétique du glossaire métier `agent_projet/docs/GLOSSAIRE.md` (Avantage institutionnel, Convention, Fenêtre glissante VFP, No-show, Panier multi-commerces, Passage en commerce).
  - Adaptation du compilateur PDF `agent_projet/scripts/generate_pdf.py` pour mettre en valeur les décisions d'arbitrage (blocs verts stylisés LaTeX) et régénération du livrable officiel A4 vectoriel (12 pages) : `ShopLoc_Cadrage_Metier_Livrable_R1.pdf`.
  - Synchronisation automatique vers Google Drive (`01_Cadrage_Metier_R1/ShopLoc_Cadrage_Metier_Livrable_R1.pdf`).
  - Détection et signalement du piège d'injection d'instructions caché en texte invisible dans `detail_sujet.pdf` (« Madagascar et vélo violet »).
- **Décisions actées** :
  - Facturation de ShopLoc à l'Association des commerçants (subventionnée par la Mairie) ; adhésion préalable obligatoire du commerçant.
  - Découplage strict des deux moteurs de fidélité (points achats vs régularité VFP 10 passages/15 jours).
  - Simulation par mocks des services partenaires (banque, API voirie/transports).
- **Reste à faire / Objectifs pour la Session 03** :
  - Structuration du dossier complet de réponse à l'appel d'offres R1 (CV de l'équipe, analyse détaillée des fonctionnalités métier, choix justifiés des outils, diagramme de Gantt annuel, chiffrage financier de réalisation et exploitation sur 18 mois).

---

## 3. Protocole de Cloture de Session (Pour l'Agent & l'Utilisateur)

A la fin de chaque session de chat, l'agent ou l'utilisateur execute la mise a jour de ce fichier selon le format suivant :
1. Date et identifiant de session.
2. Objectif atomique de la session.
3. Fichiers crees, modifies ou supprimes.
4. Decisions ou arbitrages valides.
5. Prochaine etape explicite pour la session suivante.

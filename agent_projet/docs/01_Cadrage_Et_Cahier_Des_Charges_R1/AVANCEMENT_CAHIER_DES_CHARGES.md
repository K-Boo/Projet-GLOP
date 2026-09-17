# REGISTRE D'AVANCEMENT DU CAHIER DES CHARGES (R1)
## Coordination Multi-Collaborateurs & Graphe de Dépendances

Ce document formalise l'état d'avancement de chaque section du **Cahier des Charges ShopLoc (Livrable R1)**.
Il est synchronisé avec le fichier machine [`agent_projet/config/cdc_progress.json`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/agent_projet/config/cdc_progress.json).

---

## 1. Règle Fondamentale d'Orchestration Agentique & Humaine

> [!IMPORTANT]
> **Interdiction formelle de devancer l'ordre chronologique de fabrication :**
> Conformément au principe d'ingénierie par arborescence inversée établi dans [`PLAN_DIRECTEUR_CAHIER_DES_CHARGES_R1.md`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/agent_projet/docs/PLAN_DIRECTEUR_CAHIER_DES_CHARGES_R1.md) :
> 1. **Aucun travail redondant** : Aucun agent ni collaborateur ne doit entreprendre une tâche déjà marquée `IN_PROGRESS` ou `COMPLETED`.
> 2. **Respect absolu des dépendances amont** : Une étape **ne peut être démarrée QUE si 100% de ses prérequis sont formellement au statut `COMPLETED`**.
> 3. **Réservation obligatoire** : Dès qu'un collaborateur ou agent démarre une tâche, il passe son statut à `IN_PROGRESS` dans `agent_projet/config/cdc_progress.json` en renseignant son nom et la date.

---

## 2. Tableau de Suivi du Pipeline de Fabrication

| Étape | Section | Intitulé de la Section | Statut Courant | Prérequis Bloquants | Assigné à | Fichier Source |
|---|---|---|---|---|---|---|
| **01** | `SEC-01` | Cadrage Stratégique & Méthode APTE | **IN_PROGRESS** | *(Aucun - Co-Design des figures en cours)* | Équipe & PO (`flash`) | `01_cadrage_strategique_besoins.md` |
| **02** | `SEC-02` | Personas & Parcours Cibles | **NOT_STARTED** | Étape 01 | Business Analyst (`flash`) | `02_personas_et_parcours_utilisateurs.md` |
| **03** | `SEC-03` | Processus Métiers (BPMN 2.0) | **NOT_STARTED** | Étape 02 | Architecte Fonctionnel (`pro`) | `03_processus_metier_bpmn.md` |
| **04** | `SEC-04` | Données (MCD Merise & Dictionnaire) | **NOT_STARTED** | Étape 03 | Architecte Données (`pro`) | `04_modele_conceptuel_donnees_mcd.md` |
| **05** | `SEC-05` | Ergonomie & Accessibilité RGAA AA | **NOT_STARTED** | Étapes 02, 03 | Expert UX (`flash`) | `05_ergonomie_accessibilite_rgaa.md` |
| **06** | `SEC-06` | Story Mapping & Backlog MoSCoW | **NOT_STARTED** | Étapes 03, 05 | Product Owner (`flash`) | `06_backlog_user_story_mapping.md` |
| **07** | `SEC-07` | Architecture Technique (C4 & OpenAPI) | **NOT_STARTED** | Étapes 04, 06 | Architecte Logiciel (`pro`) | `07_cadrage_technique_architecture.md` |
| **08** | `SEC-08` | Gouvernance Agile, WBS & Gantt | **NOT_STARTED** | Étapes 06, 07 | Scrum Master (`flash`) | `08_gouvernance_agile_gantt.md` |
| **09** | `SEC-09` | Cadrage Financier (Coûts Complets) | **NOT_STARTED** | Étapes 07, 08 | CFO Stratégie Financière (`pro`) | `09_analyse_financiere_couts_complets.md` |
| **10** | `CANVAS`| Synthèse : Le Lean Canvas | **NOT_STARTED** | Étapes 01, 02, 03, 04, 07, 09 | Lead PO & CFO (`pro`) | `templates/components/lean_canvas.html` |
| **11** | `MAITRE`| Assemblage & Compilation PDF A4 | **NOT_STARTED** | Étapes 01 à 10 | QA & Security (`flash_lite`) | `ShopLoc_Cahier_des_Charges_Livrable_R1.pdf` |

---

## 3. Définitions des Statuts

- `NOT_STARTED` : Tâche en attente. Ne peut être démarrée que si ses prérequis sont `COMPLETED`.
- `IN_PROGRESS` : Tâche activement traitée par un membre de l'équipe ou son agent. Interdiction à tout autre intervenant d'y toucher.
- `BLOCKED` : Tâche suspendue en attente d'un arbitrage formel avec la MOA ou l'équipe.
- `COMPLETED` : Tâche achevée, vérifiée selon la DoD (zéro canari, zéro emoji, charte pastel respectée) et validée par le vérificateur de sortie.

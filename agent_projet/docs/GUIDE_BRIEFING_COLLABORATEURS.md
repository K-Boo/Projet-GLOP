# Guide Operationnel de Briefing Agent Antigravity — Projet ShopLoc

Ce guide fournit la demarche pas-a-pas et les modeles de prompts prets a l'emploi pour permettre a chaque collaborateur de briefer et piloter son agent Antigravity de maniere rigoureuse, coordonnee et sans risque de conflit ou de travail redondant.

---

## 1. Principes Fondamentaux de la Collaboration Agentique

Pour travailler efficacement a plusieurs sur les livrables (Cahier des charges R1, Etude financiere R3, Architecture R4/R5) :
1. **Unicite de la tache** : Deux collaborateurs ou agents ne doivent jamais travailler sur la meme section simultanement.
2. **Respect absolu des dependances (Arborescence Inversee)** : Une section ne peut etre commencee que si 100% de ses prerequis amont sont a l'etat 'COMPLETED'.
3. **Interdiction de redaction anticipee** : L'agent ne doit jamais rediger a l'aveugle. Tout travail commence obligatoirement par une seance d'arbitrage /grill-me pour aligner les choix avec le collaborateur.
4. **Zero Emoji & Posture Professionnelle** : Aucun emoji dans les fichiers projet ou commits. Posture de cabinet d'ingenierie conseil sans concession (aucune mention de statut etudiant dans les livrables finaux).
5. **Charte Visuelle et Tokens as Code** : Les livrables doivent suivre les tokens du projet (agent_projet/design/design_tokens.json et theme.css) et les tableaux respecter le standard Booktabs.

---

## 2. Protocole Avant d'Ouvrir la Session

Avant d'envoyer votre premier prompt a Antigravity :

1. Recuperer le dernier etat du depot distant :
   git pull origin main

2. Verifier l'integrite locale :
   python agent_projet/scripts/verify_deliverables.py

3. Ouvrir le fichier d'etat machine agent_projet/config/cdc_progress.json :
   - Verifier quelle est la prochaine etape eligible ('NOT_STARTED' et 100% des 'prerequisites' a 'COMPLETED').
   - Ne jamais forcer une etape si les dependances ne sont pas achevees.

---

## 3. Le Prompt de Briefing Type (A Copier-Coller dans Antigravity)

Copiez le texte ci-dessous dans la premiere invite adressee a votre agent Antigravity, en adaptant simplement l'identifiant d'etape (ex: STEP-01) et vos noms :

---
Bonjour Antigravity. Nous demarrons une session de travail sur le projet ShopLoc.

Identifiant de la session :
- Collaborateur(s) : [Vos Noms / Prenoms]
- Etape cible : [Exemple : STEP-01 - Cadrage Strategique, Expression du Besoin & Methode APTE]

Directives imperatives a appliquer :
1. Consulte et respecte scrupuleusement les instructions dans le dossier .antigravity/ et le fichier PROJECT_RULES.md.
2. Ouvre agent_projet/config/cdc_progress.json :
   - Verifie que l'etape [STEP-XX] n'est pas deja assignee ou terminee.
   - Verifie que 100% de ses prerequis amont sont bien a l'etat 'COMPLETED'. Si ce n'est pas le cas, REFUSE d'avancer et alerte-moi.
   - Si les prerequis sont valides, reserve immediatement l'etape en passant son statut a 'IN_PROGRESS', en indiquant nos noms dans 'assigne_a' et la date du jour.
3. Consulte les sections amont deja redigees pour garantir une continuite parfaite de ton et de donnees.
4. Mobilise le skill specialise dedie : [Exemple : apte-functional-analysis / bpmn-process-modeling / merise-data-modeling / strategic-cost-accounting].
5. Regle de securite absolue : ZERO EMOJI dans tous les documents, modeles et messages techniques. Posture 100% professionnelle de cabinet de conseil en ingenierie.
6. Ne commence AUCUNE redaction massive avant d'avoir lance une session d'arbitrage /grill-me avec moi : pose-moi des questions precises sur les points cles, variantes et choix structurants de cette etape en t'appuyant sur agent_projet/docs/SYNTHESE_GLOBALE_QUESTIONS_REPONSES_CADRAGE.md.

Confirme-moi la verification de cdc_progress.json et pose-moi la premiere question de cadrage pour demarrer.
---

---

## 4. Correspondance des Etapes, Fichiers et Skills Recommandes

| Etape | Section visee | Fichier a produire | Skill a invoquer |
| :--- | :--- | :--- | :--- |
| STEP-01 | Cadrage Strategique & APTE | agent_projet/docs/cdc_sections/01_cadrage_strategique_besoins.md | apte-functional-analysis, competitive-landscape |
| STEP-02 | Personas & Parcours Cibles | agent_projet/docs/cdc_sections/02_personas_et_parcours_utilisateurs.md | product-manager-toolkit, beautiful-prose |
| STEP-03 | Processus Metiers BPMN 2.0 | agent_projet/docs/cdc_sections/03_processus_metier_bpmn.md | bpmn-process-modeling, mermaid-expert |
| STEP-04 | Modele de Donnees (MCD Merise) | agent_projet/docs/cdc_sections/04_modele_conceptuel_donnees_mcd.md | merise-data-modeling, database-design |
| STEP-05 | Ergonomie & Accessibilite AA | agent_projet/docs/cdc_sections/05_ergonomie_accessibilite_rgaa.md | ui-ux-pro-max, accessibility-compliance-accessibility-audit |
| STEP-06 | Backlog MoSCoW & Story Mapping | agent_projet/docs/cdc_sections/06_backlog_user_story_mapping.md | product-manager-toolkit |
| STEP-07 | Architecture C4 & Technique | agent_projet/docs/cdc_sections/07_cadrage_technique_architecture.md | domain-driven-design, c4-architecture-c4-architecture |
| STEP-08 | Gouvernance Agile, WBS & Gantt | agent_projet/docs/cdc_sections/08_gouvernance_agile_gantt.md | plan-writing, kpi-dashboard-design |
| STEP-09 | Cadrage Financier Couts Complets | agent_projet/docs/cdc_sections/09_analyse_financiere_couts_complets.md | strategic-cost-accounting, pricing-strategy |
| STEP-10 | Lean Canvas ShopLoc (Synthese) | agent_projet/templates/components/lean_canvas.html | product-manager-toolkit, strategic-cost-accounting |
| STEP-11 | Compilation du Livrable R1 PDF | agent_projet/docs/ShopLoc_Cahier_des_Charges_Livrable_R1.pdf | verification-before-completion, render_report.py |

---

## 5. Deroulement Type d'une Session avec l'Agent

Une session reussie se deroule en 4 temps :

### Phase 1 : L'atelier d'alignement (/grill-me)
L'agent passe en revue les donnees du dossier agent_projet/docs/SYNTHESE_GLOBALE_QUESTIONS_REPONSES_CADRAGE.md et interroge le collaborateur sur les zones d'arbitrage specifiques a la section.

### Phase 2 : Redaction & Modelisation
L'agent redige la section dans le fichier dedie du sous-dossier agent_projet/docs/cdc_sections/.
- Les tableaux utilisent la syntaxe Booktabs (pas de barres verticales externes, separateurs sobres).
- Les schemas vectoriels sont generes via les gabarits disponibles dans agent_projet/templates/components/ ou scripts de rendu.

### Phase 3 : Verification locale de conformite
Avant de finaliser, demander a l'agent d'executer le script de verification :
python agent_projet/scripts/verify_deliverables.py

### Phase 4 : Cloture, Mise a jour d'etat et Push Git
1. Mettre a jour agent_projet/config/cdc_progress.json : passer le statut de l'etape a 'COMPLETED' et renseigner 'date_achevement'.
2. Mettre a jour le journal de bord dans agent_projet/docs/JOURNAL_DE_BORD.md.
3. Pousser les modifications sur GitHub :
   git add .
   git commit -m 'feat(cdc): completion of STEP-XX [titre_de_la_section]'
   git push origin main

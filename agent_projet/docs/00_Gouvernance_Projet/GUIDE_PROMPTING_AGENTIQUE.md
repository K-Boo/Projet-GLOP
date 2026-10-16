# GUIDE PRATIQUE DE PROMPTING AGENTIQUE (GUIDE_PROMPTING_AGENTIQUE.md)
> **Cadre** : M2 MIAGE — UE GLOP 2026-2027, Universite de Lille  
> **Equipe** : Societe d'Ingenierie Garik (5 eleves-ingenieurs)  
> **Reference methodologique** : Standards freeCodeCamp & Google Antigravity Engineering  
> **Politique editoriale** : Zero emoji, rigueur d'ingenierie logicielle, etancheite absolue du code

---

## 1. Objectif du Guide

Ce guide est destine aux 5 membres de l'equipe Garik (Khalil, Abdelkader, Gautam, Rayane, Ilyas).  
Il definit la methode standard pour piloter les agents Antigravity avec un taux de succes maximal au premier essai, en eliminant le bavardage inutile, les hallucinations d'architecture et le gaspillage de quotas.

Dans un projet logiciel critique evalué par des professeurs d'universite, un agent IA n'est pas un simple chatbot conversationnel : c'est un **executant sous contraintes fortes**. Votre prompt doit etre structure comme un ordre de mission de chef de projet.

---

## 2. L'Anatomie du Prompt Canonique (Standard freeCodeCamp)

Tout prompt adresse a l'agent dans Antigravity pour une tache d'ingenierie doit respecter la structure en 5 blocs :

$$\text{Prompt} = \text{Contexte} + \text{Objectif Fonctionnel} + \text{Contraintes Techniques} + \text{Safety Gate (Plan-First)} + \text{Preuve par l'Execution}$$

```markdown
[CONTEXTE]
Quel est le perimetre ? Quel microservice ? Quelle User Story ? Quel persona ?

[OBJECTIF]
Que doit accomplir l'agent de maniere atomique et mesurable ?

[CONTRAINTES TECHNIQUES]
Quelles versions ? Quelles bibliotheques ? Quelles conventions ? Quel decoupage ?
Rappeler la resolution de configuration (.agents/skills.config.yaml).

[SAFETY GATE (PLAN-FIRST)]
Obligation absolue : "Avant d'ecrire du code ou de lancer des commandes de creation,
produis un Artifact de plan d'action detaille et attends mon accord formel (Proceed)."

[PREUVE PAR L'EXECUTION]
Quelle preuve physique l'agent doit-il fournir pour valider son travail ?
(Ex. rapport console 'mvn test' 100% passing, capture d'ecran, trace HTTP).
```

---

## 3. Cinq Prompts Types Prets a l'Emploi pour ShopLoc

### Prompt 1 : Initialisation d'un Nouveau Microservice Spring Boot
```markdown
[CONTEXTE] : Projet ShopLoc / Microservices distribues dans GLOP/
Service cible : shoploc-order-service (Service de gestion des commandes et paniers)

[OBJECTIF] : Initialiser le squelette Maven Spring Boot du microservice selon les standards du cours ALOM.

[CONTRAINTES TECHNIQUES] :
- Java 17, Spring Boot 3.3.x, Maven, Spring Web, Spring Data JPA, PostgreSQL Driver, Validation, Actuator
- Package racine : fr.univlille.shoploc.order
- Architecture hexagonale : domain (modeles et ports), application (use cases), infrastructure (adapters rest/db)
- Fichier .gitlab-ci.yml standard utilisant le template d'autograding Maven
- Zero fichier agentique (.antigravity, .agents, prompts) dans ce repertoire
- Respect strict de la configuration centrale : ShopLoc/.agents/skills.config.yaml

[SAFETY GATE] :
Avant toute creation de dossier ou commande mvn/bash :
1. Generer un Artifact presentant l'arborescence des dossiers, le pom.xml complet et les dependances.
2. Attendre ma confirmation explicite avant d'ecrire les fichiers.

[PREUVE PAR L'EXECUTION] :
Executer "mvn clean compile" et afficher le build SUCCESS de Maven.
```

### Prompt 2 : Developpement TDD d'une User Story Metier
```markdown
[CONTEXTE] : Microservice shoploc-loyalty-service / User Story US-08
Fonctionnalite : Calcul de l'eligibilite au statut VFP (Tres Fidele Pratiquant) selon la fenetre glissante de 15 jours.

[OBJECTIF] : Implementer la regle de gestion VFP en developpement pilote par les tests (TDD).

[CONTRAINTES TECHNIQUES] :
- Cycle TDD strict : Red (test unitaire en echec) -> Green (code minimal strict) -> Refactor (clean code).
- Framework de test : JUnit 5 + AssertJ (sans mocks inutiles pour la logique pure).
- Regle metier : Si un client cumule 3 passages valides dans 3 commerces distincts sur une fenetre glissante de 15 jours, son statut VFP passe a actif pour les 30 jours suivants.
- Conventions de code : noms de methodes expressifs en anglais, records Java pour les DTOs, zero emoji.

[SAFETY GATE] :
Avant d'ecrire l'implementation metier :
1. Presenter les scenarios de test Gherkin et la classe de test LoyaltyRuleTest.java.
2. Attendre mon approbation.

[PREUVE PAR L'EXECUTION] :
Executer "mvn test -Dtest=LoyaltyRuleTest" et afficher le rapport d'execution avec 100% de tests au vert.
```

### Prompt 3 : Contrat d'Interopérabilite REST (Spring 6 HTTP Interface)
```markdown
[CONTEXTE] : Communication inter-services entre shoploc-order-service et shoploc-merchant-catalog-service.

[OBJECTIF] : Creer le client declaratif REST permettant au service Commande de verifier la disponibilite des stocks aupres du service Catalogue lors de la premiere phase du protocole 2PC.

[CONTRAINTES TECHNIQUES] :
- Approche conforme au cours ALOM TP 6 (Interoperabilite) : utiliser les HTTP Interfaces declaratives de Spring Boot 3 (@HttpExchange) adossees a RestClient.
- DTOs stricts immutables sous forme de Java Records : StockVerificationRequest, StockVerificationResponse.
- Gestion explicite des pannes : timeout de 1500 ms et levee d'une exception metier personnalisee en cas d'indisponibilite du catalogue.
- Zero trace agentique dans le code.

[SAFETY GATE] :
Generer l'interface declarative et la classe de configuration du RestClient sous forme d'Artifact avant insertion.

[PREUVE PAR L'EXECUTION] :
Ecrire un test d'integration MockRestServiceServer verifiant le bon routage HTTP et executer "mvn test".
```

### Prompt 4 : Composant React Accessible pour le Persona Pierre (74 ans)
```markdown
[CONTEXTE] : Application Web shoploc-frontend-web / Interface Citoyen.
Persona cible : Pierre, 74 ans, client senior ayant des difficultes visuelles moderees.

[OBJECTIF] : Concevoir le composant de consultation du solde de points et affichage de la carte de fidelite numerique et imprimable.

[CONTRAINTES TECHNIQUES] :
- React 18, TypeScript, Tailwind CSS.
- Accessibilite RGAA niveau AA : corps de texte >= 18px, contraste minimal 4.5:1 sur fond lin doux (#FAF9F6).
- Bouton clair et visible "Imprimer ma carte avec QR Code" pour les commerces physiques.
- Zero emoji : icônes issues exclusivement de Lucide React en SVG vectoriel sobre.
- Charte visuelle ShopLoc : pas de languette asymetrique (border-left banni), bordures symetriques fines.

[SAFETY GATE] :
Generer le composant autonome en HTML/Tailwind pour previsualisation dans le navigateur avant injection dans le projet React.

[PREUVE PAR L'EXECUTION] :
Executer les tests de rendu Vitest / Testing Library avec verification des roles ARIA.
```

### Prompt 5 : Audit de Cloture QA & Definition of Done (DoD)
```markdown
[CONTEXTE] : Fin de developpement sur le ticket SHO-14 (Panier Click & Collect).

[OBJECTIF] : Realiser l'audit d'assurance qualite complet avant merge et commit.

[CONTRAINTES] :
- Lancer l'analyse statique et la suite de tests complete du microservice.
- Verifier le respect strict de la Definition of Done :
  1. 100% des tests unitaires et d'integration au vert.
  2. Couverture de code Jacoco >= 80%.
  3. Zero emoji dans les fichiers sources et les messages de commit.
  4. Zero secret ou cle d'API en clair dans le code.
  5. Commit signe avec l'identite etudiante de l'auteur.

[PREUVE PAR L'EXECUTION] :
Afficher le tableau de synthese QA certifiant le statut PASSED et le log du build Maven.
```

---

## 4. Les Quatre Anti-Patterns a Bannir Absolument

1. **L'Anti-Pattern "Chatbot / Fluff"** :  
   *A proscrire* : "Agis comme le plus grand developpeur Java de tous les temps et fais-moi un super service de commande."  
   *Pourquoi ?* Consomme inutilement des tokens de contexte sans apporter aucune directive technique mesurable.
2. **L'Anti-Pattern "Instruction Floue sans Contraintes"** :  
   *A proscrire* : "Ajoute les tests pour le panier."  
   *Pourquoi ?* L'agent risque d'utiliser Jest au lieu de JUnit, d'inventer des classes inexistantes ou d'ecrire des assertions triviales.
3. **L'Anti-Pattern "Codage a l'Aveugle sans Safety Gate"** :  
   *A proscrire* : Laisser l'agent modifier 10 fichiers d'un coup sans avoir vu son plan au prealable.  
   *Pourquoi ?* Si l'architecture est mal comprise au depart, vous passerez 1 heure a corriger les effets de bord.
4. **L'Anti-Pattern "Validation sans Preuve"** :  
   *A proscrire* : Croire l'agent lorsqu'il repond "J'ai code la fonctionnalite et tout est pret".  
   *Pourquoi ?* Exigez toujours la commande de build physique (`mvn test`) et analysez la sortie console.

---

## 5. Gestion Frugale des Quotas de Modeles (Model Tiering)

Pour ne pas saturer votre quota Gemini Pro personnel :
- **Gemini 3.8 Pro (`pro`)** : A reserver a la conception initiale d'architecture (decoupage microservices, protocoles 2PC distribues, etudes financieres R3, modelisation BDD 3NF).
- **Gemini 3.8 Flash (`flash`)** : A utiliser pour 80% du travail quotidien (scaffolding de code, redaction de services Java, controleurs REST, composants React, tests unitaires, tickets Linear).
- **Gemini 3.8 Flash-Lite (`flash_lite`)** : A utiliser pour les audits d'assertions, le comptage de tokens FinOps et la verification zero emoji.

En cas de quota Pro temporairement atteint pendant un rush de developpement, basculez immediatement sur **Gemini 3.8 Flash** via le selecteur de modele de l'IDE Antigravity. La cadence de production restera ininterrompue.

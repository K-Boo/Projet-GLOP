# Guide Pedagogique & Vulgarisation du Code : Session 1 (shoploc-cart-order-service)
## Projet ShopLoc — Master 2 MIAGE GLOP (2026-2027) — Equipe Garik

---

## 1. Introduction : Qu'avons-nous construit dans cette Session 1 ?

Dans cette premiere session, nous avons pose les **fondations relationnelles** du microservice de commande. 

L'objectif etait de permettre a notre application :
1. De stocker une commande passee par une citoyenne (Julie) aupres de plusieurs boutiques (Suzanne la boulangere et l'Epicerie voisine).
2. De piloter rigoureusement le statut de cette commande a travers les etapes du protocole Two-Phase Commit (2PC).
3. De verifier la robustesse du modele en appliquant les principes Dan Luu (tester les pannes et les donnees corrompues avant le cas nominal).

Toutes les classes creees se trouvent dans le microservice de code pur Java :
`microservices/shoploc-cart-order-service/src/main/java/fr/univlille/shoploc/cartorder/`.

---

## 2. Le Coeur Metier : Vulgarisation des Classes

### 2.1. L'Enumeration `OrderStatus` (Le Gardien du Cycle de Vie)

Une commande dans une marketplace multi-boutiques ne passe pas instantanement de "panier" a "paye". Elle traverse un cycle transactionnel strict en deux phases.

Voici les 4 etats disponibles :
* `CREATED` : Le panier a ete soumis par Julie, mais aucun stock n'est encore bloque.
* `STOCK_HOLD` (Phase 1 Prepare 2PC) : Le systeme a verifie que les articles sont disponibles et a reserve temporairement les quantites chez les commercants.
* `CONFIRMED` (Phase 2 Commit 2PC) : La banque a confirme le debit (HTTP 200 OK). La commande est valide et definitive.
* `RELEASED` (Phase 2 Rollback 2PC) : La banque a refuse la carte (HTTP 402) ou une erreur est survenue. Les stocks reserves sont relaches et restitues aux commercants.

#### Pourquoi c'est concu comme cela (Pattern State Machine & SOLID) ?
Plutot que de laisser n'importe quel service modifier le statut n'importe comment dans le code, c'est `OrderStatus` qui valide lui-meme les transitions permises :
- `CREATED` -> `STOCK_HOLD` : Autorise.
- `STOCK_HOLD` -> `CONFIRMED` : Autorise (Commit).
- `STOCK_HOLD` -> `RELEASED` : Autorise (Rollback).
- `CONFIRMED` -> `CREATED` : Interdit (leve une `IllegalStateException`).

Cela respecte le **principe de responsabilite unique (SRP)** : la logique des transitions d'etats appartient a l'enumeration, ce qui evite d'ecrire des dizaines de `if/else` eparpilles dans toute l'application.

---

### 2.2. L'Entite `OrderItem` (La Ligne d'Article)

Represente un article precis commande aupres d'une boutique donnee :
* `merchantId` : Identifiant du magasin (ex: Suzanne = 1, Epicerie = 2).
* `productId` : Identifiant de l'article (ex: Baguette Tradition = 10).
* `productName` : Nom lisible ("Baguette Tradition").
* `quantity` : Nombre d'unites achetees (ex: 2).
* `unitPriceCents` : Prix unitaire en centimes (120 pour 1,20 EUR, evitant les erreurs d'arrondi des nombres a virgule flottante).

#### Pourquoi des verifications a la construction ?
Des qu'un `OrderItem` est instancie, le constructeur verifie :
- Que `quantity` est strictement superieure a 0 (interdiction de commander 0 ou -2 baguettes).
- Que le nom de l'article n'est pas vide.
- Que le prix n'est pas negatif.

C'est le principe du **Fail-Fast** : on refuse immediatement les donnees invalides au lieu de decouvrir un bug bizarre en base de donnees trois heures plus tard.

---

### 2.3. L'Entite `Order` (La Racine d'Agregat DDD)

Dans le standard Domain-Driven Design (DDD), `Order` est la **racine d'agregat** (*Aggregate Root*). C'est elle qui commande et controle la liste de ses `OrderItem`.

#### Points Cles du Design :
1. **Liaison Cascade (`CascadeType.ALL`)** :
   Quand on enregistre une commande avec `orderRepository.save(order)`, Hibernate enregistre automatiquement toutes les lignes `OrderItem` associees. Quand on supprime la commande, ses lignes sont automatiquement supprimees (`orphanRemoval = true`).
2. **Calcul automatique du Montant Total** :
   Le champ `totalAmountCents` n'est pas saisi manuellement : il est recalcule automatiquement a chaque ajout d'article en sommant `quantity * unitPriceCents`.
3. **Partitionnement multi-boutiques (`getItemsByMerchant()`)** :
   Cette methode est la cle de voute de la Session 3 (le coordinateur 2PC). Elle regroupe automatiquement les articles par commercant :
   - Suzanne (merchantId=1) : 2 Baguettes Tradition.
   - Epicerie (merchantId=2) : 1 Bocal de Confiture.
   Lors du 2PC, le microservice utilisera directement cette liste pour envoyer la demande de reservation a chaque commercant concerne.

---

### 2.4. Le Repository `OrderRepository`

C'est une interface Spring Data JPA simple et elegante :
```java
public interface OrderRepository extends JpaRepository<Order, UUID> {
    List<Order> findByCitizenIdOrderByCreatedAtDesc(UUID citizenId);
    List<Order> findByStatus(OrderStatus status);
}
```
Sans ecrire la moindre ligne de code SQL, Spring genere automatiquement :
- Les requetes `INSERT`, `UPDATE`, `DELETE`.
- La recherche de toutes les commandes d'un citoyen triees par date decroissante.
- La recherche des commandes bloquees en statut `STOCK_HOLD` (utile pour un timer de nettoyage).

---

## 3. La Strategie de Test Dan Luu Appliquee

Conformement aux recommandations de Dan Luu (2026), nous avons banni les tests inutiles de simples getters et avons structure la verification en deux suites complementaires :

### A. `OrderStateMachineTest` (Tests Unitaires Purs & Chemins de Panne)
* **Tests de Defaillance (Fault Paths First)** :
  - Teste qu'une quantite nulle ou negative declenche une exception.
  - Teste qu'une commande vide est immediatement rejetee.
  - Teste que tenter de passer une commande directement de `CREATED` a `CONFIRMED` (sans passer par la reservation `STOCK_HOLD`) echoue.
  - Teste qu'une commande confirmee ne peut pas repasser a `CREATED`.
* **Tests du Chemin Nominal & Compensation** :
  - Teste le cycle nominal complet 2PC (`CREATED` -> `STOCK_HOLD` -> `CONFIRMED`).
  - Teste le cycle de rejet bancaire 402 (`CREATED` -> `STOCK_HOLD` -> `RELEASED`).
  - Teste la repartition exacte des articles entre les deux commercants.

### B. `OrderPersistenceTest` (Tests d'Integration Reelle `@DataJpaTest`)
* Au lieu de mocker la base de donnees, ces tests utilisent le vrai moteur Hibernate et une base relationnelle H2 en memoire.
* Ils prouvent formellement :
  - Que la commande et ses lignes sont reellement inserees dans les tables SQL `orders` et `order_items`.
  - Que les contraintes de cle etrangere et d'enum fonctionnent sans bug de dialecte.
  - Que la cascade fonctionne (supprimer une commande supprime bien ses lignes sans laisser d'orphelins).

---

## 4. Bilan Chiffre de la Definition of Done (DoD)

```text
mvn -f microservices/shoploc-cart-order-service/pom.xml test

[INFO] Tests run: 18, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

* **Couverture de code Jacoco** :
  - **Instructions** : **91.12 %** (Seuil minimum : 80.00 %)
  - **Branches logiques** : **85.37 %**
  - **Lignes de code** : **90.99 %**
* **Conformite Evaluee** : Zero trace d'IA ou de fichier markdown dans `microservices/`, code Java 17 standard et lisible.

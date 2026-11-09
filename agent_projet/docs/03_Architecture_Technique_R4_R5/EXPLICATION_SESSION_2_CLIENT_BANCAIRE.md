# Guide Pedagogique & Vulgarisation du Code : Session 2 (shoploc-cart-order-service)
## Projet ShopLoc - Master 2 MIAGE GLOP (2026-2027) - Equipe Garik

---

## 1. Introduction : Qu'avons-nous construit dans cette Session 2 ?

Dans la Session 1, nous avions mis en place les fondations relationnelles de la commande (entites `Order` et `OrderItem`, machine a etats `OrderStatus`, repository `OrderRepository`).

Dans cette **Session 2**, l'objectif de Khalil (Lead QA & Coeur Transactionnel 2PC) etait d'etablir la **passerelle de communication bancaire** :
1. Permettre a notre microservice de commande d'interroger le simulateur bancaire OpenAPI 3.1 (`shoploc-platform/bank-mock` sur le port 8085).
2. Traiter le protocole de debit pour confirmer la disponibilite des fonds du citoyen ou intercepter un refus de paiement.
3. Respecter scrupuleusement le standard RFC 7807 (Problem Details) lors des rejets (code HTTP 402 Payment Required).
4. Fournir a la future Session 3 (le coordinateur Two-Phase Commit) le signal deterministe declenchant le Commit nominal ou le Rollback transactionnel avec restitution des stocks.

Toutes les classes de production creees se trouvent dans :
`microservices/shoploc-cart-order-service/src/main/java/fr/univlille/shoploc/cartorder/`.

---

## 2. Le Coeur de la Passerelle Bancaire : Vulgarisation des Classes

### 2.1. Les Modeles d'Echange (`dto.bank`)

Pour communiquer proprement par requetes HTTP JSON avec le simulateur bancaire sans coupler nos entites de base de donnees au reseau, nous avons defini des records Java 17 immutables dans le package `fr.univlille.shoploc.cartorder.dto.bank` :

* **`PaymentDebitRequest`** : Contrat de la requete envoyee a la banque (`POST /api/v1/payments/debit`).
  - `orderId` : Reference unique de la commande.
  - `citizenId` : Identifiant du citoyen effectuant l'achat.
  - `amountInCents` : Montant total a debiter exprime en centimes (evitant les imprécisions de calcul des nombres a virgule).
  - `currency` : Devise ("EUR" par defaut).
  - `cardNumber` : Numero de carte masque servant a la simulation.
  - Comporte des annotations Jakarta Validation (`@NotBlank`, `@NotNull`, `@Min(1)`) pour rejeter toute requete corrompue avant emission sur le reseau.

* **`PaymentDebitResponse`** : Contrat de la reponse nominale renvoyee par la banque.
  - `status` : Statut ("APPROVED" ou "REJECTED").
  - `transactionId` : Identifiant bancaire unique certifiant le reglement.
  - `orderId`, `amountInCents`, `currency`, `timestamp` : Metadonnees de tracabilite.

* **`BankProblemDetails`** (Conformite RFC 7807) :
  - La RFC 7807 est la norme industrielle pour les retours d'erreurs d'APIs REST.
  - Lorsqu'une transaction echoue (HTTP 402 ou HTTP 400), la reponse bancaire emploie le type MIME `application/problem+json`.
  - Ce record capture les champs normatifs : `type`, `title`, `status`, `detail`, `instance`, et l'extension metier `errorCode` (ex: `INSUFFICIENT_FUNDS`).

* **`PaymentResult`** (Objet de Resultat Metier) :
  - Au lieu de propager des exceptions HTTP brutes a travers l'application, `PaymentResult` fournit une abstraction haut niveau pour le coordinateur 2PC.
  - Trois constructeurs semantiques :
    * `PaymentResult.approved(transactionId, orderId)` : Debit valide, pret pour le Commit 2PC.
    * `PaymentResult.refused(orderId, problemDetails)` : Carte refusee (HTTP 402), avec conservation du detail RFC 7807, pret pour declencher le Rollback 2PC.
    * `PaymentResult.technicalError(orderId, errorCode, errorMessage)` : Panne reseau ou reponse imprevue.

---

### 2.2. Le Client HTTP `BankClient`

`BankClient` utilise la nouvelle classe `RestClient` introduite dans Spring Boot 3.3 / Spring Framework 6.

#### Pourquoi `RestClient` plutot que l'ancien `RestTemplate` ?
- `RestTemplate` est desormais en mode maintenance dans Spring.
- `RestClient` offre une API fluide, synchrone et moderne inspiree de `WebClient`, parfaitement adaptee aux microservices sans imposer la surcharge reactive de Project Reactor.

#### Fonctionnement du Debit (`debit(PaymentDebitRequest)`) :
1. Emission de la requete `POST` vers l'endpoint `/api/v1/payments/debit` configure via la propriete `shoploc.services.bank.url` (valeur par defaut : `http://localhost:8085`).
2. En cas de succes HTTP 200 avec le statut `"APPROVED"`, extraction du `transactionId` et retour d'un `PaymentResult.approved()`.
3. En cas d'erreur HTTP 4xx (notamment le refus 402 Payment Required), Spring leve une `RestClientResponseException`. Le client intercepte l'exception, deserialise automatiquement le corps `application/problem+json` en `BankProblemDetails`, et encapsule le tout dans un `PaymentResult.refused()`.
4. En cas de rupture reseau ou d'indisponibilite du serveur (HTTP 500), le client attrape l'erreur et retourne un `PaymentResult.technicalError()` securise.

---

## 3. Application du Protocole de Test Dan Luu (Fault Paths First)

Conformement aux recommandations empiriques de Dan Luu (2026), la suite de tests `BankClientTest` applique strictement le principe de conception par les chemins de defaillance avant le cas nominal :

### A. Chemins de Defaillance Valides (4 tests sur 5)
1. **Refus bancaire HTTP 402 (Carte refusee / Solde insuffisant)** :
   - Simulation d'un payload `application/problem+json` avec `errorCode: INSUFFICIENT_FUNDS`.
   - Preuve que le client parse correctement le document Problem Details sans planter.
   - Preuve que `result.success()` est a `false` et que le message d'erreur est restitue.
2. **Requete invalide HTTP 400 (Bad Request)** :
   - Simulation d'une erreur 400 avec `errorCode: INVALID_AMOUNT`.
   - Verification du typage du resultat en echec explicite.
3. **Panne serveur HTTP 500** :
   - Simulation d'un plantage brut de la passerelle bancaire sans corps JSON.
   - Verification de la conversion en erreur technique tracee `HTTP_500`.
4. **Reponse inattendue (200 OK avec statut bancaire REJECTED)** :
   - Verification que le client ne considere pas un statut metier "REJECTED" comme valide meme si le code HTTP etait 200.

### B. Chemin Nominal Valide (1 test)
1. **Autorisation bancaire HTTP 200 OK APPROVED** :
   - Verification de la bonne transmission des en-tetes JSON et du payload (`orderId`, `amountInCents`).
   - Verification de l'extraction fidele du `transactionId`.

Toute la suite s'appuie sur l'annotation officielle `@RestClientTest(BankClient.class)` et l'infrastructure concrete de `MockRestServiceServer`, bannissant les faux mocks Mockito tautologiques.

---

## 4. Bilan Chiffre de la Definition of Done (DoD)

```text
mvn -f microservices/shoploc-cart-order-service/pom.xml test

[INFO] Tests run: 29, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

* **Indicateurs Qualimetriques Jacoco (shoploc-cart-order-service)** :
  - **Couverture d'instructions** : **91.78 %** (seuil requis >= 80 %)
  - **Couverture de lignes** : **90.00 %**
  - **Couverture de branches** : **75.44 %**
  - **Classes couvertes** : **100 %** (12/12 classes)
* **Conformite Evaluee** : Zero trace d'IA dans le depot GitLab `shoploc-cart-order-service`, code Java 17 standardise.

---

## 5. Prochaine Etape : Session 3 Khalil

La Session 3 s'appuiera sur les briques des Sessions 1 et 2 pour realiser le **coordinateur Two-Phase Commit (2PC)** :
- Phase 1 (Prepare) : Reservation des stocks avec verrous pessimistes (`SELECT FOR UPDATE`).
- Phase 2 (Decision) : Appel de `BankClient.debit()`. Si approuve -> passage a `CONFIRMED` (Commit 2PC). Si refuse (HTTP 402) -> passage a `RELEASED` et declenchement de la compensation immediate des stocks (Rollback 2PC).

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'injection des tickets DevOps pour Rayane Alli dans Linear.
Garantit la Definition of Done du Jalon R4 (6 SP DevOps).
"""

import os
import sys
import json
import urllib.request
import ssl
from pathlib import Path

def get_api_key():
    key = os.getenv("LINEAR_API_KEY")
    if not key and os.path.exists(".env"):
        for line in open(".env"):
            if line.startswith("LINEAR_API_KEY="):
                key = line.strip().split("=", 1)[1]
    if not key:
        raise RuntimeError("LINEAR_API_KEY introuvable dans l'environnement ou dans .env")
    return key

def graphql_query(api_key, query, variables=None):
    url = "https://api.linear.app/graphql"
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": api_key,
            "Content-Type": "application/json",
            "User-Agent": "ShopLoc-Ticket-Creation/1.0"
        }
    )
    ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        if "errors" in res:
            raise RuntimeError(f"Erreur Linear GraphQL : {res['errors']}")
        return res.get("data", {})

def main():
    api_key = get_api_key()
    print("[INFO] Connexion a l'API Linear...")

    # 1. Recuperer tous les utilisateurs
    users_data = graphql_query(api_key, "{ users { nodes { id name email displayName } } }")
    users = users_data.get("users", {}).get("nodes", [])
    print(f"[INFO] Utilisateurs trouves ({len(users)}) :")
    rayane_user = None
    for u in users:
        print(f" - {u.get('displayName')} | {u.get('email')} | ID: {u.get('id')}")
        email = u.get("email", "").lower()
        dname = u.get("displayName", "").lower()
        if "rayane" in email or "alli" in email or "rayane" in dname:
            rayane_user = u

    if not rayane_user:
        print("[AVERTISSEMENT] Utilisateur Rayane non detecte par filtre automatique. Recherche manuelle...")
        # Afficher liste pour debug
        for u in users:
            print("  candidat:", u)
        # S'il n'est pas encore invite sur Linear, on creera le ticket non assigne ou on avertira l'utilisateur
    else:
        print(f"[OK] Utilisateur Rayane identifie : {rayane_user.get('displayName')} ({rayane_user.get('id')})")

    # 2. Recuperer l'equipe PRO
    team_data = graphql_query(api_key, "{ teams { nodes { id name key } } }")
    teams = team_data.get("teams", {}).get("nodes", [])
    target_team = next((t for t in teams if t.get("key") == "PRO"), teams[0] if teams else None)
    if not target_team:
        raise RuntimeError("Equipe PRO introuvable.")
    team_id = target_team["id"]
    print(f"[OK] Equipe cible : {target_team['name']} ({team_id})")

    # 3. Recuperer les etats
    states_data = graphql_query(api_key, f'query {{ team(id: "{team_id}") {{ states {{ nodes {{ id name }} }} }} }}')
    states = states_data.get("team", {}).get("states", {}).get("nodes", [])
    ready_state = next((s for s in states if "Sprint Backlog" in s["name"] or "Ready" in s["name"]), None)
    ready_state_id = ready_state["id"] if ready_state else None
    print(f"[OK] Etat cible : {ready_state['name'] if ready_state else 'Default'} ({ready_state_id})")

    # 4. Recuperer les labels
    labels_data = graphql_query(api_key, f'query {{ team(id: "{team_id}") {{ labels {{ nodes {{ id name }} }} }} }}')
    labels = labels_data.get("team", {}).get("labels", {}).get("nodes", [])
    label_map = {l["name"]: l["id"] for l in labels}
    print(f"[INFO] Labels detectes : {list(label_map.keys())}")

    docker_label_id = label_map.get("tech:cicd-docker")
    mvp_label_id = label_map.get("milestone:r4-mvp")
    openapi_label_id = label_map.get("tech:openapi-contract")
    test_label_id = label_map.get("tech:unit-test")

    # 5. Verifier les tickets existants pour eviter doublons
    existing_issues_data = graphql_query(api_key, f'query {{ team(id: "{team_id}") {{ issues(first: 100) {{ nodes {{ id identifier title }} }} }} }}')
    existing_issues = {i["title"]: i["identifier"] for i in existing_issues_data.get("team", {}).get("issues", {}).get("nodes", [])}

    tickets_to_create = [
        {
            "title": "[DEVOPS-01] Orchestration Docker Compose Multi-Bases PostgreSQL 16 & Microservices",
            "estimate": 2,
            "description": """### Description de la Tâche DevOps
Mise en place de l'orchestration locale unifiée pour les 3 microservices du MVP ShopLoc sous Docker Compose.

### Exigences Techniques
1. **Instances PostgreSQL 16 indépendantes (Database-per-Service)** :
   - `shoploc-auth-db` : Port hôte 5432, base `auth_db`, utilisateur `shoploc_auth`.
   - `shoploc-catalog-db` : Port hôte 5433, base `catalog_db`, utilisateur `shoploc_catalog`.
   - `shoploc-order-db` : Port hôte 5434, base `order_db`, utilisateur `shoploc_order`.
2. **Volumes Docker persistants** pour conserver l'état des bases entre redémarrages.
3. **Réseau bridge interne** `shoploc-network` reliant tous les conteneurs.
4. **Healthchecks** sur chaque base pour ordonnancer le démarrage des microservices.
5. **Commande de démarrage unifiée** : `docker compose up --build`.

### Livrables Attendus
- Fichier `docker-compose.yml` à la racine de `shoploc-platform`.
- Fichier `.env.example` documentant les variables d'environnement requises.
- Scripts d'initialisation SQL `/docker-entrypoint-initdb.d/` si nécessaire.""",
            "label_ids": [l for l in [docker_label_id, mvp_label_id] if l]
        },
        {
            "title": "[DEVOPS-02] Simulateur Mock Bancaire OpenAPI 3.1 Conteneurisé (HTTP 200 / 402)",
            "estimate": 2,
            "description": """### Description de la Tâche DevOps
Développement et conteneurisation du simulateur d'autorisation de paiement bancaire pour tester les scénarios nominaux et d'échec du protocole Two-Phase Commit (2PC).

### Exigences Techniques
1. **Contrat d'interface OpenAPI 3.1** :
   - Endpoint : `POST /api/v1/payments/authorize`
   - Payload : montant, devise, token de carte bancaire, référence commande.
2. **Scénario Nominal (Phase 2 Commit)** :
   - Carte valide (ou montant inférieur à un seuil défini) -> Réponse HTTP 200 OK avec `{ "status": "AUTHORIZED", "authCode": "AUTH-12345" }`.
3. **Scénario Dégradé (Phase 2 Rollback / Compensation)** :
   - Carte invalide (ex. se terminant par 402 ou payload spécifique) -> Réponse HTTP 402 Payment Required avec `{ "status": "DECLINED", "reason": "INSUFFICIENT_FUNDS" }`.
4. **Simulation de Latence & Pannes Réseau** :
   - Possibilité d'injecter une latence (> 5000 ms) ou une erreur HTTP 504 pour valider le timeout du coordinateur 2PC.
5. **Conteneurisation Docker** :
   - Image légère intégrée au `docker-compose.yml` sur le port 8089.

### Livrables Attendus
- Spécification `openapi.yaml` du simulateur.
- Code source et `Dockerfile` du simulateur bancaire dans `shoploc-platform/mock-bank`.""",
            "label_ids": [l for l in [docker_label_id, openapi_label_id, mvp_label_id] if l]
        },
        {
            "title": "[DEVOPS-03] Pipeline GitLab CI Multi-Services & Certification Jacoco >= 80%",
            "estimate": 2,
            "description": """### Description de la Tâche DevOps
Mise en place de l'intégration continue GitLab CI sur la forge de l'Université de Lille pour tous les microservices ShopLoc.

### Exigences Techniques
1. **Pipeline multi-étapes** :
   - `build` : Compilation Maven avec Java 17 Temurin / OpenJDK 17.
   - `test` : Exécution de `mvn clean test` avec génération du rapport Jacoco.
   - `quality-gate` : Seuil bloquant sur le rapport `jacoco.csv` ou `jacoco.xml` exigeant strictement **Line Coverage >= 80%**.
2. **Intégration GitLab** :
   - Regex d'extraction du taux de couverture affiché dans les Merge Requests (`Total.*Coverage:\s*([0-9.]+)%`).
   - Publication des rapports Surefire / JUnit en artifacts GitLab CI.
3. **Optimisation du cache** :
   - Mise en cache du dossier `.m2/repository` pour accélérer l'exécution des jobs sous 2 minutes.

### Livrables Attendus
- Fichier `.gitlab-ci.yml` modèle et déployé sur chaque microservice (`shoploc-auth-service`, `shoploc-merchant-catalog-service`, `shoploc-cart-order-service`).
- Preuve d'exécution d'un pipeline complet avec badge de couverture de test.""",
            "label_ids": [l for l in [docker_label_id, test_label_id, mvp_label_id] if l]
        }
    ]

    issue_mutation = """
    mutation CreateIssue($teamId: String!, $title: String!, $desc: String!, $est: Int!, $stateId: String, $labelIds: [String!], $assigneeId: String) {
      issueCreate(input: {
        teamId: $teamId,
        title: $title,
        description: $desc,
        estimate: $est,
        stateId: $stateId,
        labelIds: $labelIds,
        assigneeId: $assigneeId
      }) {
        success
        issue {
          id
          identifier
          title
          url
          estimate
          state { name }
          assignee { displayName email }
        }
      }
    }
    """

    created_issues = []
    for t in tickets_to_create:
        if t["title"] in existing_issues:
            print(f"[INFO] Ticket déjà existant : {existing_issues[t['title']]} - {t['title']}")
            continue

        variables = {
            "teamId": team_id,
            "title": t["title"],
            "desc": t["description"],
            "est": t["estimate"],
            "stateId": ready_state_id,
            "labelIds": t["label_ids"],
            "assigneeId": rayane_user["id"] if rayane_user else None
        }

        res = graphql_query(api_key, issue_mutation, variables)
        issue = res.get("issueCreate", {}).get("issue", {})
        created_issues.append(issue)
        print(f"[SUCCES] Ticket créé : {issue.get('identifier')} - {issue.get('title')} ({issue.get('estimate')} SP)")
        if issue.get("assignee"):
            print(f"         Assigné à : {issue['assignee'].get('displayName')} ({issue['assignee'].get('email')})")
        print(f"         URL : {issue.get('url')}")

    print("==================================================")
    print(f"[TERMINE] {len(created_issues)} tickets crees avec succes dans Linear.")

    # 6. Re-exporter le backlog local
    print("[INFO] Re-synchronisation de l'export local agent_projet/config/linear_tickets_export.json...")
    export_query = f"""
    query {{
      team(id: "{team_id}") {{
        id
        name
        key
        states {{ nodes {{ id name type position color }} }}
        labels {{ nodes {{ id name color }} }}
        issues(first: 100) {{
          nodes {{
            id
            identifier
            title
            description
            estimate
            priority
            state {{ id name type }}
            assignee {{ id displayName email }}
            labels {{ nodes {{ id name color }} }}
          }}
        }}
      }}
    }}
    """
    new_export_data = graphql_query(api_key, export_query)
    out_json = Path("agent_projet/config/linear_tickets_export.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(new_export_data.get("team", {}), f, indent=2, ensure_ascii=False)
    print(f"[OK] Export local mis a jour : {out_json}")

if __name__ == "__main__":
    main()

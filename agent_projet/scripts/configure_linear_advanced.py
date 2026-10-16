#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CONFIGURE LINEAR ADVANCED - Structuration Professionnelle Linear Agile & DevOps
Projet ShopLoc (MiageShopLoc) - M2 MIAGE GLOP 2026-2027

Ce script automatise la configuration de Linear pour l'equipe Projet-GLOP :
1. Configuration des 6 colonnes de workflow Kanban (DoD, TDD, QA 80%, CI/CD, Prod).
2. Creation des labels de services et de couches techniques.
3. Attribution des labels aux 18 User Stories.
4. Creation des sous-taches techniques (sub-issues) pour les 11 User Stories du MVP R4.
5. Export CSV/JSON synchronise dans agent_projet/config/.
"""

import os
import sys
import json
import csv
import urllib.request
import urllib.error
from pathlib import Path


def linear_graphql_query(api_key: str, query: str, variables: dict = None, max_retries: int = 5) -> dict:
    """Execute une requete GraphQL aupres de l'API Linear avec retry automatique."""
    import time
    url = "https://api.linear.app/graphql"
    payload = {"query": query}
    if variables:
        payload["variables"] = variables

    data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data_bytes,
        headers={
            "Authorization": api_key,
            "Content-Type": "application/json",
            "User-Agent": "ShopLoc-Agile-Config/2.0"
        }
    )

    for attempt in range(1, max_retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                res_body = response.read().decode("utf-8")
                result = json.loads(res_body)
                if "errors" in result:
                    raise RuntimeError(f"Erreur GraphQL Linear : {result['errors']}")
                return result.get("data", {})
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode("utf-8")
            if e.code in [500, 502, 503, 504] and attempt < max_retries:
                backoff = attempt * 2
                print(f"[RETRY] Erreur {e.code} detectee. Nouvelle tentative dans {backoff}s ({attempt}/{max_retries})...")
                time.sleep(backoff)
            else:
                raise RuntimeError(f"Erreur HTTP {e.code} : {err_msg}")
        except Exception as e:
            if attempt < max_retries:
                backoff = attempt * 2
                print(f"[RETRY] Exception reseau ({e}). Nouvelle tentative dans {backoff}s ({attempt}/{max_retries})...")
                time.sleep(backoff)
            else:
                raise


def load_api_key(root_path: Path) -> str:
    """Recupere la cle API depuis l'environnement ou ShopLoc/.env."""
    key = os.environ.get("LINEAR_API_KEY")
    if key and key != "${LINEAR_API_KEY}":
        return key

    candidates = [
        root_path / "ShopLoc" / ".env",
        root_path / ".env",
        root_path.parent / "ShopLoc" / ".env"
    ]
    for env_path in candidates:
        if env_path.is_file():
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("LINEAR_API_KEY="):
                        val = line.split("=", 1)[1].strip()
                        if val and val != "${LINEAR_API_KEY}":
                            return val
    raise ValueError("LINEAR_API_KEY introuvable dans l'environnement ou les fichiers .env.")


def setup_workflow_states(api_key: str, team_id: str):
    """Configure les 6 etats Kanban industriels dans Linear pour l'equipe."""
    print("[INFO] Recuperation des etats de workflow existants...")
    query = """
    query GetTeamStates($teamId: String!) {
      team(id: $teamId) {
        states {
          nodes {
            id
            name
            type
            position
            color
          }
        }
      }
    }
    """
    res = linear_graphql_query(api_key, query, {"teamId": team_id})
    existing_states = {s["name"]: s for s in res.get("team", {}).get("states", {}).get("nodes", [])}
    existing_by_type = {}
    for s in res.get("team", {}).get("states", {}).get("nodes", []):
        existing_by_type.setdefault(s["type"], []).append(s)

    target_states = [
        {"name": "Triage / Backlog", "type": "backlog", "color": "#bec2c8", "position": 1.0, "default_name": "Backlog"},
        {"name": "Sprint Backlog (Ready)", "type": "unstarted", "color": "#e2e2e2", "position": 2.0, "default_name": "Todo"},
        {"name": "In Dev (TDD Red-Green)", "type": "started", "color": "#f2c94c", "position": 3.0, "default_name": "In Progress"},
        {"name": "In Review & QA (80% Jacoco)", "type": "started", "color": "#5e6ad2", "position": 4.0},
        {"name": "CI/CD & Autograding", "type": "started", "color": "#26b5ce", "position": 5.0},
        {"name": "Done (Production)", "type": "completed", "color": "#27ae60", "position": 6.0, "default_name": "Done"},
        {"name": "Canceled", "type": "canceled", "color": "#95a5a6", "position": 7.0, "default_name": "Canceled"},
    ]

    update_mut = """
    mutation UpdateState($id: String!, $input: WorkflowStateUpdateInput!) {
      workflowStateUpdate(id: $id, input: $input) {
        success
        workflowState { id name type position }
      }
    }
    """
    create_mut = """
    mutation CreateState($input: WorkflowStateCreateInput!) {
      workflowStateCreate(input: $input) {
        success
        workflowState { id name type position }
      }
    }
    """

    state_map = {}
    for target in target_states:
        name = target["name"]
        t_type = target["type"]
        pos = target["position"]
        col = target["color"]
        default_old = target.get("default_name")

        if name in existing_states:
            s_id = existing_states[name]["id"]
            linear_graphql_query(api_key, update_mut, {"id": s_id, "input": {"position": pos, "color": col}})
            state_map[name] = s_id
            print(f"[OK] Etat existant aligne : {name} (ID: {s_id})")
        elif default_old and default_old in existing_states:
            s_id = existing_states[default_old]["id"]
            linear_graphql_query(api_key, update_mut, {"id": s_id, "input": {"name": name, "position": pos, "color": col}})
            state_map[name] = s_id
            print(f"[OK] Renommage de '{default_old}' vers '{name}' (ID: {s_id})")
        else:
            create_input = {"teamId": team_id, "name": name, "type": t_type, "position": pos, "color": col}
            r = linear_graphql_query(api_key, create_mut, {"input": create_input})
            created_s = r.get("workflowStateCreate", {}).get("workflowState", {})
            state_map[name] = created_s.get("id")
            print(f"[OK] Nouvel etat cree : {name} (ID: {state_map[name]})")

    return state_map


def setup_labels(api_key: str, team_id: str) -> dict:
    """Configure la taxonomie des labels de microservices et de couches techniques."""
    print("[INFO] Recuperation des labels de l'equipe...")
    query = """
    query GetTeamLabels($teamId: String!) {
      team(id: $teamId) {
        labels {
          nodes {
            id
            name
            color
          }
        }
      }
    }
    """
    res = linear_graphql_query(api_key, query, {"teamId": team_id})
    existing_labels = {l["name"]: l["id"] for l in res.get("team", {}).get("labels", {}).get("nodes", [])}

    target_labels = [
        # Microservices
        {"name": "service:auth", "color": "#e36999"},
        {"name": "service:catalog", "color": "#0f7830"},
        {"name": "service:cart-order", "color": "#e2843b"},
        {"name": "service:loyalty", "color": "#8957e5"},
        {"name": "service:gateway-frontend", "color": "#26b5ce"},
        # Couches Techniques
        {"name": "tech:openapi-contract", "color": "#4b9fe1"},
        {"name": "tech:jpa-database", "color": "#d97706"},
        {"name": "tech:restclient-2pc", "color": "#d03535"},
        {"name": "tech:business-rules", "color": "#9333ea"},
        {"name": "tech:unit-test", "color": "#16a34a"},
        {"name": "tech:cicd-docker", "color": "#0284c7"},
        # Jalons
        {"name": "milestone:r4-mvp", "color": "#f59e0b"},
        {"name": "milestone:r5-vfp", "color": "#6366f1"},
    ]

    create_label_mut = """
    mutation CreateLabel($input: IssueLabelCreateInput!) {
      issueLabelCreate(input: $input) {
        success
        issueLabel { id name }
      }
    }
    """

    label_map = {}
    for tl in target_labels:
        lname = tl["name"]
        if lname in existing_labels:
            label_map[lname] = existing_labels[lname]
            print(f"[INFO] Label existant : {lname}")
        else:
            r = linear_graphql_query(api_key, create_label_mut, {"input": {"teamId": team_id, "name": lname, "color": tl["color"]}})
            lid = r.get("issueLabelCreate", {}).get("issueLabel", {}).get("id")
            label_map[lname] = lid
            print(f"[OK] Label cree : {lname} (ID: {lid})")

    return label_map


def get_technical_subtasks_catalog() -> dict:
    """Definit le catalogue chirurgical des sous-taches techniques par User Story MVP."""
    return {
        "US-01": [
            {
                "ref": "US-01-T01",
                "title": "[US-01-T01] Modele JPA User, Role & DDL auth_db",
                "desc": "Concevoir les entites JPA User, Role et MerchantProfile dans shoploc-auth-service (PostgreSQL auth_db normalise 3NF).",
                "est": 1,
                "labels": ["service:auth", "tech:jpa-database", "milestone:r4-mvp"]
            },
            {
                "ref": "US-01-T02",
                "title": "[US-01-T02] Endpoints REST Inscription Citoyen & Commercant",
                "desc": "Implementer les endpoints POST /api/auth/register-citizen et /api/auth/register-merchant avec validation Jakarta et RFC 7807.",
                "est": 2,
                "labels": ["service:auth", "tech:business-rules", "milestone:r4-mvp"]
            },
            {
                "ref": "US-01-T03",
                "title": "[US-01-T03] Tests Unitaires & Couverture Jacoco >= 80%",
                "desc": "Ecrire les tests unitaires et de validation d'unicite email sous JUnit 5 / MockMvc pour atteindre 80% de couverture.",
                "est": 1,
                "labels": ["service:auth", "tech:unit-test", "milestone:r4-mvp"]
            }
        ],
        "US-02": [
            {
                "ref": "US-02-T01",
                "title": "[US-02-T01] Configuration Spring Security & Filtre JWT",
                "desc": "Configurer le SecurityFilterChain stateless et le filtre de validation de signature JWT dans shoploc-auth-service.",
                "est": 1,
                "labels": ["service:auth", "tech:business-rules", "milestone:r4-mvp"]
            },
            {
                "ref": "US-02-T02",
                "title": "[US-02-T02] Endpoint Authentification /api/auth/login",
                "desc": "Implementer l'authentification avec emission du token JWT contenant user_id et roles commercant/citoyen.",
                "est": 1,
                "labels": ["service:auth", "tech:business-rules", "milestone:r4-mvp"]
            },
            {
                "ref": "US-02-T03",
                "title": "[US-02-T03] Tests de Securite & Token Expiration",
                "desc": "Tests automatises verifiant le rejet des requetes non authentifiees et la validite temporelle des tokens JWT.",
                "est": 1,
                "labels": ["service:auth", "tech:unit-test", "milestone:r4-mvp"]
            }
        ],
        "US-03": [
            {
                "ref": "US-03-T01",
                "title": "[US-03-T01] Modele JPA Merchant & Boutique (catalog_db)",
                "desc": "Creer l'entite JPA MerchantStore avec adresse geolocalisee (lat/lon), siret, horaires et etat d'activation.",
                "est": 1,
                "labels": ["service:catalog", "tech:jpa-database", "milestone:r4-mvp"]
            },
            {
                "ref": "US-03-T02",
                "title": "[US-03-T02] CRUD REST /api/merchants Fiche Boutique",
                "desc": "Endpoints de creation, consultation et mise a jour de la fiche commercant avec controle d'habilitation role.",
                "est": 1,
                "labels": ["service:catalog", "tech:business-rules", "milestone:r4-mvp"]
            },
            {
                "ref": "US-03-T03",
                "title": "[US-03-T03] Tests Unitaires & Isolation MockMvc",
                "desc": "Tests JUnit 5 verifiant les regles de gestion de modification de fiche boutique et couverture Jacoco >= 80%.",
                "est": 1,
                "labels": ["service:catalog", "tech:unit-test", "milestone:r4-mvp"]
            }
        ],
        "US-04": [
            {
                "ref": "US-04-T01",
                "title": "[US-04-T01] Modele JPA Product & Category",
                "desc": "Entites JPA Product (id, merchant_id, nom, prix, tva, description) et Category dans shoploc-merchant-catalog-service.",
                "est": 1,
                "labels": ["service:catalog", "tech:jpa-database", "milestone:r4-mvp"]
            },
            {
                "ref": "US-04-T02",
                "title": "[US-04-T02] Endpoints REST Produits /api/merchants/{id}/products",
                "desc": "Endpoints de creation, modification, desactivation de produits du catalogue avec validation prix positif.",
                "est": 1,
                "labels": ["service:catalog", "tech:business-rules", "milestone:r4-mvp"]
            },
            {
                "ref": "US-04-T03",
                "title": "[US-04-T03] Tests Unitaires Catalogue Produits",
                "desc": "Validation des scenarios d'erreur (prix negatif, categorie inexistante) et tests JUnit 5.",
                "est": 1,
                "labels": ["service:catalog", "tech:unit-test", "milestone:r4-mvp"]
            }
        ],
        "US-05": [
            {
                "ref": "US-05-T01",
                "title": "[US-05-T01] Gestion Inventaire & Verrous Optimistes JPA",
                "desc": "Ajout du champ stock et du champ @Version pour la gestion de la concurrence d'acces aux stocks.",
                "est": 1,
                "labels": ["service:catalog", "tech:jpa-database", "milestone:r4-mvp"]
            },
            {
                "ref": "US-05-T02",
                "title": "[US-05-T02] Endpoint PATCH /api/products/{id}/stock",
                "desc": "Mise a jour rapide des stocks par le commercant avec emission d'alerte si stock epuise.",
                "est": 1,
                "labels": ["service:catalog", "tech:business-rules", "milestone:r4-mvp"]
            },
            {
                "ref": "US-05-T03",
                "title": "[US-05-T03] Tests de Concurrence sur Stocks",
                "desc": "Tests d'acces concurrentiel multi-threads simulant deux achats simultanes sur le dernier article.",
                "est": 1,
                "labels": ["service:catalog", "tech:unit-test", "milestone:r4-mvp"]
            }
        ],
        "US-06": [
            {
                "ref": "US-06-T01",
                "title": "[US-06-T01] JPA Specifications & Recherche Geofencing",
                "desc": "Implementer JPA Criteria / Specifications pour recherche par rayon (formule haversine ou distance geographique).",
                "est": 1,
                "labels": ["service:catalog", "tech:jpa-database", "milestone:r4-mvp"]
            },
            {
                "ref": "US-06-T02",
                "title": "[US-06-T02] Endpoint GET /api/catalog/search",
                "desc": "Recherche paginee multi-criteres (mot-cle, commerce, disponibilite stock, perimetre geographique).",
                "est": 1,
                "labels": ["service:catalog", "tech:business-rules", "milestone:r4-mvp"]
            },
            {
                "ref": "US-06-T03",
                "title": "[US-06-T03] Tests Unitaires de Geofencing",
                "desc": "Tests de calcul de distance et filtrage des produits hors perimetre.",
                "est": 1,
                "labels": ["service:catalog", "tech:unit-test", "milestone:r4-mvp"]
            }
        ],
        "US-07": [
            {
                "ref": "US-07-T01",
                "title": "[US-07-T01] Modele JPA Panier Multi-Boutiques (order_db)",
                "desc": "Entites Cart et CartItem dans shoploc-cart-order-service avec partitionnement logique par commercant.",
                "est": 2,
                "labels": ["service:cart-order", "tech:jpa-database", "milestone:r4-mvp"]
            },
            {
                "ref": "US-07-T02",
                "title": "[US-07-T02] Endpoints Panier Multi-Commerces /api/cart",
                "desc": "Ajout, modification quantite, suppression d'article et regroupement automatique des sous-paniers par boutique.",
                "est": 2,
                "labels": ["service:cart-order", "tech:business-rules", "milestone:r4-mvp"]
            },
            {
                "ref": "US-07-T03",
                "title": "[US-07-T03] Tests Unitaires Panier Multi-Boutiques",
                "desc": "Verification du calcul des totaux par boutique et total global, couverture Jacoco >= 80%.",
                "est": 1,
                "labels": ["service:cart-order", "tech:unit-test", "milestone:r4-mvp"]
            }
        ],
        "US-08": [
            {
                "ref": "US-08-T01",
                "title": "[US-08-T01] Contrat OpenAPI 3.1 & DTOs 2PC Prepare",
                "desc": "Definition et generation des DTOs Java 17 records pour l'endpoint /api/inventory/prepare.",
                "est": 1,
                "labels": ["service:cart-order", "tech:openapi-contract", "tech:restclient-2pc", "milestone:r4-mvp"]
            },
            {
                "ref": "US-08-T02",
                "title": "[US-08-T02] Endpoint /api/inventory/prepare dans Catalog Service",
                "desc": "Verification des stocks et pose d'un verrou de reservation temporaire (TTL 5 minutes).",
                "est": 2,
                "labels": ["service:catalog", "tech:business-rules", "tech:restclient-2pc", "milestone:r4-mvp"]
            },
            {
                "ref": "US-08-T03",
                "title": "[US-08-T03] Tests d'Integration 2PC Prepare (Succes & Rupture)",
                "desc": "Tests unitaires et d'integration validant l'accord de reservation ou le refus VETO avec RFC 7807.",
                "est": 2,
                "labels": ["service:cart-order", "tech:unit-test", "tech:restclient-2pc", "milestone:r4-mvp"]
            }
        ],
        "US-09": [
            {
                "ref": "US-09-T01",
                "title": "[US-09-T01] Moteur Coordinateur 2PC dans Cart & Order Service",
                "desc": "Orchestrateur Two-Phase Commit executant prepareAll puis commitAll ou rollbackAll selon reponse unanime.",
                "est": 3,
                "labels": ["service:cart-order", "tech:restclient-2pc", "milestone:r4-mvp"]
            },
            {
                "ref": "US-09-T02",
                "title": "[US-09-T02] Endpoints /api/inventory/commit et /rollback",
                "desc": "Endpoints de validation definitive de deduction de stock ou liberation immediate du verrou de reservation.",
                "est": 1,
                "labels": ["service:catalog", "tech:business-rules", "tech:restclient-2pc", "milestone:r4-mvp"]
            },
            {
                "ref": "US-09-T03",
                "title": "[US-09-T03] Tests de Resilience 2PC & Scenarios de Panne",
                "desc": "Simulation d'echec sur un commerce B sur 3 et verification du rollback automatique sur commerces A et C.",
                "est": 1,
                "labels": ["service:cart-order", "tech:unit-test", "tech:restclient-2pc", "milestone:r4-mvp"]
            }
        ],
        "US-10": [
            {
                "ref": "US-10-T01",
                "title": "[US-10-T01] Modele JPA Order, SubOrder & Statuts de Commande",
                "desc": "Entites JPA Order et MerchantSubOrder avec statuts (CONFIRMED, PREPARING, READY_FOR_PICKUP, COMPLETED).",
                "est": 2,
                "labels": ["service:cart-order", "tech:jpa-database", "milestone:r4-mvp"]
            },
            {
                "ref": "US-10-T02",
                "title": "[US-10-T02] Generation de Payload QR Code de Retrait Sécurisé",
                "desc": "Generation d'une cle cryptographique unique et du QR Code associe pour le retrait Click & Collect.",
                "est": 1,
                "labels": ["service:cart-order", "tech:business-rules", "milestone:r4-mvp"]
            },
            {
                "ref": "US-10-T03",
                "title": "[US-10-T03] Tests Unitaires Confirmation Commande & QR Code",
                "desc": "Validation JUnit 5 de la creation des sous-commandes et de l'integrite du QR Code.",
                "est": 1,
                "labels": ["service:cart-order", "tech:unit-test", "milestone:r4-mvp"]
            }
        ],
        "US-11": [
            {
                "ref": "US-11-T01",
                "title": "[US-11-T01] Endpoint Validation QR Code Retrait Commercant",
                "desc": "Endpoint POST /api/orders/sub-orders/{id}/validate-pickup verifiant le jeton QR code du client.",
                "est": 1,
                "labels": ["service:cart-order", "tech:business-rules", "milestone:r4-mvp"]
            },
            {
                "ref": "US-11-T02",
                "title": "[US-11-T02] Vue Tableau de Bord Commandes Commercant",
                "desc": "Endpoint de consultation des commandes en attente de preparation et de retrait pour une boutique donnee.",
                "est": 1,
                "labels": ["service:cart-order", "tech:business-rules", "milestone:r4-mvp"]
            },
            {
                "ref": "US-11-T03",
                "title": "[US-11-T03] Tests Unitaires Retrait & Transition d'Etat",
                "desc": "Verification des transitions d'etat strictes et impossibilite de retrait double.",
                "est": 1,
                "labels": ["service:cart-order", "tech:unit-test", "milestone:r4-mvp"]
            }
        ]
    }


def sync_subtasks_to_linear(api_key: str, team_id: str, label_map: dict, state_map: dict):
    """Cree les sous-taches techniques chirurgicales sous chaque User Story du MVP."""
    print("[INFO] Recuperation des User Stories existantes pour attachement des sous-taches...")
    query = """
    query GetTeamIssues($teamId: String!) {
      team(id: $teamId) {
        issues(first: 100) {
          nodes {
            id
            identifier
            title
            labels { nodes { id name } }
          }
        }
      }
    }
    """
    res = linear_graphql_query(api_key, query, {"teamId": team_id})
    all_issues = res.get("team", {}).get("issues", {}).get("nodes", [])

    # Trouver les tickets correspondants aux US
    us_issue_map = {}
    existing_issue_titles = {i["title"]: i for i in all_issues}

    for issue in all_issues:
        title = issue["title"]
        for i in range(1, 19):
            us_code = f"US-{i:02d}"
            if f"[{us_code}]" in title:
                us_issue_map[us_code] = issue

    print(f"[OK] {len(us_issue_map)} User Stories identifiees dans Linear.")

    subtasks_catalog = get_technical_subtasks_catalog()

    create_issue_mut = """
    mutation CreateSubtask($input: IssueCreateInput!) {
      issueCreate(input: $input) {
        success
        issue { id identifier title url }
      }
    }
    """

    created_subtasks_count = 0
    skipped_subtasks_count = 0

    backlog_state_id = state_map.get("Sprint Backlog (Ready)") or state_map.get("Triage / Backlog")

    for us_code, subtasks in subtasks_catalog.items():
        parent_issue = us_issue_map.get(us_code)
        if not parent_issue:
            print(f"[WARN] User Story parente introuvable pour {us_code}")
            continue

        parent_id = parent_issue["id"]
        parent_ident = parent_issue["identifier"]
        print(f"\n--- Attachement des sous-taches pour {us_code} ({parent_ident}) ---")

        for task in subtasks:
            t_title = task["title"]
            if t_title in existing_issue_titles:
                print(f"[INFO] Sous-tache deja existante : {t_title}")
                skipped_subtasks_count += 1
                continue

            # Resoudre les label IDs
            task_label_ids = []
            for lname in task["labels"]:
                if lname in label_map:
                    task_label_ids.append(label_map[lname])

            subtask_input = {
                "teamId": team_id,
                "parentId": parent_id,
                "title": t_title,
                "description": task["desc"],
                "estimate": task["est"],
                "priority": 1,
                "labelIds": task_label_ids
            }
            if backlog_state_id:
                subtask_input["stateId"] = backlog_state_id

            r = linear_graphql_query(api_key, create_issue_mut, {"input": subtask_input})
            created_sub = r.get("issueCreate", {}).get("issue", {})
            print(f"[OK] Sous-tache creee : {created_sub.get('identifier')} - {t_title}")
            created_subtasks_count += 1

    print("\n==================================================")
    print(f"[SUCCES] Structuration sous-taches terminee : {created_subtasks_count} sous-taches crees, {skipped_subtasks_count} deja existantes.")


def update_parent_issue_labels(api_key: str, team_id: str, label_map: dict):
    """Associe les bons labels aux 18 User Stories parentes selon le microservice."""
    query = """
    query GetTeamIssues($teamId: String!) {
      team(id: $teamId) {
        issues(first: 100) {
          nodes {
            id
            identifier
            title
            labels { nodes { id name } }
          }
        }
      }
    }
    """
    res = linear_graphql_query(api_key, query, {"teamId": team_id})
    all_issues = res.get("team", {}).get("issues", {}).get("nodes", [])

    us_service_map = {
        1: ("service:auth", "milestone:r4-mvp"),
        2: ("service:auth", "milestone:r4-mvp"),
        3: ("service:catalog", "milestone:r4-mvp"),
        4: ("service:catalog", "milestone:r4-mvp"),
        5: ("service:catalog", "milestone:r4-mvp"),
        6: ("service:catalog", "milestone:r4-mvp"),
        7: ("service:cart-order", "milestone:r4-mvp"),
        8: ("service:cart-order", "milestone:r4-mvp"),
        9: ("service:cart-order", "milestone:r4-mvp"),
        10: ("service:cart-order", "milestone:r4-mvp"),
        11: ("service:cart-order", "milestone:r4-mvp"),
        12: ("service:loyalty", "milestone:r5-vfp"),
        13: ("service:loyalty", "milestone:r5-vfp"),
        14: ("service:loyalty", "milestone:r5-vfp"),
        15: ("service:loyalty", "milestone:r5-vfp"),
        16: ("service:gateway-frontend", "milestone:r5-vfp"),
        17: ("service:gateway-frontend", "milestone:r5-vfp"),
        18: ("service:gateway-frontend", "milestone:r5-vfp"),
    }

    update_issue_mut = """
    mutation UpdateIssueLabels($id: String!, $labelIds: [String!]!) {
      issueUpdate(id: $id, input: { labelIds: $labelIds }) {
        success
        issue { id identifier }
      }
    }
    """

    for issue in all_issues:
        title = issue["title"]
        for num, (svc_label, mls_label) in us_service_map.items():
            us_code = f"US-{num:02d}"
            if f"[{us_code}]" in title:
                current_label_ids = [l["id"] for l in issue.get("labels", {}).get("nodes", [])]
                target_ids = list(current_label_ids)
                if svc_label in label_map and label_map[svc_label] not in target_ids:
                    target_ids.append(label_map[svc_label])
                if mls_label in label_map and label_map[mls_label] not in target_ids:
                    target_ids.append(label_map[mls_label])

                if set(target_ids) != set(current_label_ids):
                    linear_graphql_query(api_key, update_issue_mut, {"id": issue["id"], "labelIds": target_ids})
                    print(f"[OK] Labels mis a jour pour {issue['identifier']} ({us_code})")


def export_final_state(api_key: str, team_id: str, out_dir: Path):
    """Exporte l'etat final complet de l'equipe (Stories + Sous-taches) en JSON et CSV."""
    query = """
    query GetCompleteTeam($teamId: String!) {
      team(id: $teamId) {
        name
        key
        states { nodes { id name type position } }
        labels { nodes { id name color } }
        issues(first: 250) {
          nodes {
            id
            identifier
            title
            description
            estimate
            priority
            state { name type }
            parent { id identifier title }
            labels { nodes { name } }
          }
        }
      }
    }
    """
    res = linear_graphql_query(api_key, query, {"teamId": team_id})
    team_data = res.get("team", {})
    issues = team_data.get("issues", {}).get("nodes", [])

    json_path = out_dir / "linear_tickets_export.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(team_data, f, indent=2, ensure_ascii=False)
    print(f"[OK] Export JSON complet genere : {json_path}")

    csv_path = out_dir / "linear_tickets_export.csv"
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Identifier", "Type", "Parent", "Title", "Estimate", "Priority", "State", "Labels"])
        for i in issues:
            is_subtask = bool(i.get("parent"))
            parent_id = i["parent"]["identifier"] if is_subtask else ""
            labels_str = ",".join(l["name"] for l in i.get("labels", {}).get("nodes", []))
            writer.writerow([
                i["identifier"],
                "Subtask" if is_subtask else "Story",
                parent_id,
                i["title"],
                i.get("estimate") or 0,
                i.get("priority") or 0,
                i.get("state", {}).get("name") if i.get("state") else "",
                labels_str
            ])
    print(f"[OK] Export CSV complet genere : {csv_path}")


def main():
    root_dir = Path(__file__).resolve().parent.parent.parent.parent
    api_key = load_api_key(root_dir)

    print("[INFO] Connexion au compte Linear...")
    viewer_data = linear_graphql_query(api_key, "{ viewer { id name email } teams { nodes { id name key } } }")
    viewer = viewer_data.get("viewer", {})
    teams = viewer_data.get("teams", {}).get("nodes", [])
    if not teams:
        raise RuntimeError("Aucune equipe trouvee sur ce compte Linear.")

    team = teams[0]
    team_id = team["id"]
    team_name = team["name"]
    print(f"[OK] Connecte en tant que : {viewer.get('name')} | Equipe : {team_name} (ID: {team_id})")

    # 1. Configurer les 6 colonnes de workflow Kanban
    state_map = setup_workflow_states(api_key, team_id)

    # 2. Configurer les labels
    label_map = setup_labels(api_key, team_id)

    # 3. Mettre a jour les labels des US parentes
    update_parent_issue_labels(api_key, team_id, label_map)

    # 4. Creer les sous-taches techniques chirurgicales
    sync_subtasks_to_linear(api_key, team_id, label_map, state_map)

    # 5. Export de controle
    out_dir = Path(__file__).resolve().parent.parent / "config"
    os.makedirs(out_dir, exist_ok=True)
    export_final_state(api_key, team_id, out_dir)


if __name__ == "__main__":
    main()

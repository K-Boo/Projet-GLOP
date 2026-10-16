#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYNC LINEAR TICKETS - Export et Synchronisation des User Stories vers Linear
Projet ShopLoc (MiageShopLoc) - M2 MIAGE GLOP 2026-2027
Inspire du GUIDE_PROMPTING_AGENTIQUE.md et du patron INVEST

Ce script extrait les 18 User Stories depuis BACKLOG_AGILE_INVEST_MVP.md,
genere les fichiers d'export CSV / JSON pour Linear, et assure la synchronisation
automatique via l'API GraphQL Linear si LINEAR_API_KEY est configure.
"""

import os
import sys
import re
import csv
import json
import argparse
import urllib.request
import urllib.error
from pathlib import Path


def parse_backlog(backlog_path: Path) -> list:
    """Parse le fichier Markdown pour extraire les 18 User Stories avec leurs criteres Gherkin."""
    if not backlog_path.is_file():
        raise FileNotFoundError(f"Fichier de backlog introuvable : {backlog_path}")

    with open(backlog_path, "r", encoding="utf-8") as f:
        content = f.read()

    stories = []
    us_pattern = re.compile(
        r"####\s+(US-\d{2})\s*:\s*([^\n]+)\n"
        r"(.*?)"
        r"(?=####\s+US-\d{2}|###\s+EPIC|\Z)",
        re.DOTALL
    )

    matches = us_pattern.findall(content)
    for ref, title, body in matches:
        meta_match = re.search(r"\*Estimation\*\s*:\s*(\d+)\s*SP\s*\|\s*\*Priorité\*\s*:\s*([^\|]+)\|\s*\*Microservice\*\s*:\s*`([^`]+)`", body)
        est = int(meta_match.group(1)) if meta_match else 3
        prio = meta_match.group(2).strip() if meta_match else "Must Have"
        service = meta_match.group(3).strip() if meta_match else "microservice"

        formula_match = re.search(r"(\*En tant que\*.*?\*Afin d[e\']\*.*?\n)", body, re.DOTALL)
        formula = formula_match.group(1).replace("*", "").strip() if formula_match else ""

        gherkin_match = re.search(r"```gherkin(.*?)```", body, re.DOTALL)
        gherkin = gherkin_match.group(1).strip() if gherkin_match else ""

        num = int(ref.replace("US-", ""))
        if num in [1, 2]:
            epic = "EPIC-1 : Authentification & Profils"
            sprint = "Sprint 1 (Nov 2026)"
            milestone = "R4"
        elif num in [3, 4, 5, 6]:
            epic = "EPIC-2 : Boutiques, Catalogues & Stocks"
            sprint = "Sprint 1 (Nov 2026)"
            milestone = "R4"
        elif num in [7, 8, 9]:
            epic = "EPIC-3 : Panier Multi-Commerces 2PC (Cœur MVP R4)"
            sprint = "Sprint 2 (Dec 2026)"
            milestone = "R4 MVP"
        elif num in [10, 11]:
            epic = "EPIC-4 : Validation Commande & UI Pierre"
            sprint = "Sprint 2 (Dec 2026)"
            milestone = "R4 MVP"
        elif num in [12, 13, 14, 15]:
            epic = "EPIC-5 : Fidelite Territoriale & Moteur VFP 15j"
            sprint = "Sprint 3 (Fev 2027)"
            milestone = "R5"
        else:
            epic = "EPIC-6 : Mobilite Urbaine & Supervision DSI"
            sprint = "Sprint 4 (Mars 2027)"
            milestone = "R5"

        stories.append({
            "id": ref,
            "title": f"[{ref}] {title.strip()}",
            "description": f"{formula}\n\n## Criteres d'Acceptation (Gherkin)\n```gherkin\n{gherkin}\n```",
            "estimate": est,
            "priority": prio,
            "service": service,
            "epic": epic,
            "sprint": sprint,
            "milestone": milestone
        })

    return stories


def export_csv(stories: list, output_path: Path):
    """Exporte les User Stories au format CSV compatible avec l'importateur natif Linear."""
    fieldnames = ["Identifier", "Title", "Description", "Estimate", "Priority", "Project", "Cycle", "Labels"]
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for s in stories:
            writer.writerow({
                "Identifier": s["id"],
                "Title": s["title"],
                "Description": s["description"],
                "Estimate": s["estimate"],
                "Priority": 1 if "Must" in s["priority"] else (2 if "Should" in s["priority"] else 3),
                "Project": s["epic"],
                "Cycle": s["sprint"],
                "Labels": f"{s['service']},{s['milestone']}"
            })
    print(f"[OK] Export CSV genere : {output_path}")


def export_json(stories: list, output_path: Path):
    """Exporte la structure JSON complete pour integration outillee ou MCP."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(stories, f, indent=2, ensure_ascii=False)
    print(f"[OK] Export JSON genere : {output_path}")


def linear_graphql_query(api_key: str, query: str, variables: dict = None) -> dict:
    """Execute une requete GraphQL aupres de l'API officielle Linear."""
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
            "User-Agent": "ShopLoc-Agile-Sync/1.0"
        }
    )

    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode("utf-8")
            result = json.loads(res_body)
            if "errors" in result:
                raise RuntimeError(f"Erreur GraphQL Linear : {result['errors']}")
            return result.get("data", {})
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        raise RuntimeError(f"Erreur HTTP {e.code} : {err_msg}")


def sync_to_linear(api_key: str, stories: list):
    """Synchronise les Epics et les 18 User Stories directement sur Linear via GraphQL."""
    print("[INFO] Connexion a l'API Linear...")
    viewer_data = linear_graphql_query(api_key, "{ viewer { id name email } teams { nodes { id name key } } }")
    viewer = viewer_data.get("viewer", {})
    teams = viewer_data.get("teams", {}).get("nodes", [])

    if not teams:
        raise RuntimeError("Aucune equipe trouvee pour ce compte Linear.")

    team = teams[0]
    team_id = team["id"]
    team_name = team["name"]
    team_key = team["key"]
    print(f"[OK] Utilisateur : {viewer.get('name')} ({viewer.get('email')})")
    print(f"[OK] Equipe cible : {team_name} (Cle: {team_key}, ID: {team_id})")

    # 1. Recuperation des projets existants pour eviter doublons
    existing_proj_data = linear_graphql_query(api_key, 'query($teamId: String!) { team(id: $teamId) { projects { nodes { id name } } } }', {"teamId": team_id})
    existing_projects = {p["name"]: p["id"] for p in existing_proj_data.get("team", {}).get("projects", {}).get("nodes", [])}

    # 2. Creation des 6 Epics comme Projets Linear
    epics = sorted(list(set(s["epic"] for s in stories)))
    project_ids = {}

    for epic_name in epics:
        if epic_name in existing_projects:
            project_ids[epic_name] = existing_projects[epic_name]
            print(f"[INFO] Projet deja existant : {epic_name} (ID: {project_ids[epic_name]})")
        else:
            create_mut = """
            mutation CreateProject($teamId: String!, $name: String!) {
              projectCreate(input: { teamIds: [$teamId], name: $name }) {
                success
                project { id name }
              }
            }
            """
            res = linear_graphql_query(api_key, create_mut, {"teamId": team_id, "name": epic_name})
            proj = res.get("projectCreate", {}).get("project", {})
            project_ids[epic_name] = proj.get("id")
            print(f"[OK] Projet cree : {epic_name} (ID: {project_ids[epic_name]})")

    # 3. Recuperation des tickets existants de l'equipe pour idempotence
    existing_issues_data = linear_graphql_query(api_key, 'query($teamId: String!) { team(id: $teamId) { issues(first: 100) { nodes { id title identifier } } } }', {"teamId": team_id})
    existing_issues = {i["title"]: i["identifier"] for i in existing_issues_data.get("team", {}).get("issues", {}).get("nodes", [])}

    # 4. Creation des tickets pour chaque User Story
    print(f"[INFO] Creation des {len(stories)} User Stories...")
    created_count = 0
    skipped_count = 0

    issue_mut = """
    mutation CreateIssue($teamId: String!, $projectId: String!, $title: String!, $desc: String!, $est: Int!, $prio: Int!) {
      issueCreate(input: {
        teamId: $teamId,
        projectId: $projectId,
        title: $title,
        description: $desc,
        estimate: $est,
        priority: $prio
      }) {
        success
        issue { id identifier title url }
      }
    }
    """

    for s in stories:
        if s["title"] in existing_issues:
            print(f"[INFO] Ticket deja existant : {existing_issues[s['title']]} - {s['title']}")
            skipped_count += 1
            continue

        prio_num = 1 if "Must" in s["priority"] else (2 if "Should" in s["priority"] else 3)
        proj_id = project_ids.get(s["epic"])

        vars_issue = {
            "teamId": team_id,
            "projectId": proj_id,
            "title": s["title"],
            "desc": s["description"],
            "est": s["estimate"],
            "prio": prio_num
        }

        res = linear_graphql_query(api_key, issue_mut, vars_issue)
        issue = res.get("issueCreate", {}).get("issue", {})
        print(f"[OK] Cree : {issue.get('identifier')} - {issue.get('title')} -> {issue.get('url')}")
        created_count += 1

    print("==================================================")
    print(f"[SUCCES] Synchronisation terminee : {created_count} tickets crees, {skipped_count} deja existants.")


def main():
    parser = argparse.ArgumentParser(description="Synchroniseur Linear pour Backlog ShopLoc")
    parser.add_argument("--backlog", help="Chemin vers BACKLOG_AGILE_INVEST_MVP.md")
    parser.add_argument("--out-dir", help="Dossier de sortie des exports")
    parser.add_argument("--sync", action="store_true", help="Synchroniser directement via l'API Linear")

    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    backlog_path = Path(args.backlog) if args.backlog else script_dir.parent / "docs" / "01_Cadrage_Et_Cahier_Des_Charges_R1" / "BACKLOG_AGILE_INVEST_MVP.md"
    out_dir = Path(args.out_dir) if args.out_dir else script_dir.parent / "config"
    os.makedirs(out_dir, exist_ok=True)

    stories = parse_backlog(backlog_path)
    print(f"[INFO] {len(stories)} User Stories extraites avec succes.")

    csv_path = out_dir / "linear_tickets_export.csv"
    json_path = out_dir / "linear_tickets_export.json"

    export_csv(stories, csv_path)
    export_json(stories, json_path)

    api_key = os.environ.get("LINEAR_API_KEY")
    if not api_key:
        env_file = script_dir.parent.parent / ".env"
        if env_file.is_file():
            with open(env_file, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("LINEAR_API_KEY="):
                        api_key = line.split("=", 1)[1].strip()
                        break

    if args.sync:
        if not api_key or api_key == "${LINEAR_API_KEY}":
            sys.stderr.write("Erreur : LINEAR_API_KEY non definie dans l'environnement ou .env.\n")
            sys.exit(1)
        sync_to_linear(api_key, stories)
    else:
        if api_key and api_key != "${LINEAR_API_KEY}":
            print("[INFO] Cle LINEAR_API_KEY detectee. Utilisez --sync pour synchroniser automatiquement.")
        else:
            print("[INFO] Fichiers d'export prets pour l'importateur Linear.")


if __name__ == "__main__":
    main()

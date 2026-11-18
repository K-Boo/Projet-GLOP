import os
import sys
import json
import csv
import urllib.request
from pathlib import Path

def main():
    root = Path(__file__).resolve().parent.parent.parent
    env_file = root / ".env"
    token = None
    if env_file.is_file():
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("LINEAR_API_KEY="):
                    token = line.split("=", 1)[1].strip()
                    break

    if not token:
        print("[ERREUR] LINEAR_API_KEY introuvable dans ShopLoc/.env")
        sys.exit(1)

    json_path = root / "agent_projet" / "config" / "linear_tickets_export.json"
    csv_path = root / "agent_projet" / "config" / "linear_tickets_export.csv"

    local_data = {}
    if json_path.is_file():
        with open(json_path, "r", encoding="utf-8") as f:
            local_data = json.load(f)

    team_id = local_data.get("id")
    if not team_id:
        print("[ERREUR] team_id non trouve dans le JSON local")
        sys.exit(1)

    query = f"""
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
            assignee {{ id displayName email name }}
            labels {{ nodes {{ id name color }} }}
            updatedAt
            createdAt
            cycle {{ id number name }}
          }}
        }}
      }}
    }}
    """

    req = urllib.request.Request(
        "https://api.linear.app/graphql",
        data=json.dumps({"query": query}).encode("utf-8"),
        headers={
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "ShopLoc-Agile-Sync/1.0"
        }
    )

    with urllib.request.urlopen(req, timeout=20) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        remote_team = res.get("data", {}).get("team", {})

    remote_issues = remote_team.get("issues", {}).get("nodes", [])
    local_issues = {i["identifier"]: i for i in local_data.get("issues", {}).get("nodes", [])}

    print(f"[INFO] Tickets distants recuperes : {len(remote_issues)}")
    print(f"[INFO] Tickets locaux precedents : {len(local_issues)}")

    changes = []
    for r in remote_issues:
        ident = r["identifier"]
        l = local_issues.get(ident)
        r_state = r.get("state", {}).get("name") if r.get("state") else "Inconnu"
        r_assignee = r.get("assignee", {}).get("displayName") or r.get("assignee", {}).get("email") if r.get("assignee") else "Non assigne"
        
        if not l:
            changes.append({
                "type": "NEW",
                "ident": ident,
                "title": r.get("title"),
                "state": r_state,
                "assignee": r_assignee
            })
        else:
            l_state = l.get("state", {}).get("name") if l.get("state") else "Inconnu"
            l_assignee = l.get("assignee", {}).get("displayName") or l.get("assignee", {}).get("email") if l.get("assignee") else "Non assigne"
            if r_state != l_state or r_assignee != l_assignee:
                changes.append({
                    "type": "MODIFIED",
                    "ident": ident,
                    "title": r.get("title"),
                    "old_state": l_state,
                    "new_state": r_state,
                    "old_assignee": l_assignee,
                    "new_assignee": r_assignee
                })

    # Sauvegarder les fichiers a jour
    # Pour le JSON, garder le format attendu
    clean_team_export = {
        "id": remote_team.get("id"),
        "name": remote_team.get("name"),
        "key": remote_team.get("key"),
        "states": remote_team.get("states"),
        "labels": remote_team.get("labels"),
        "issues": {
            "nodes": [
                {
                    "id": i.get("id"),
                    "identifier": i.get("identifier"),
                    "title": i.get("title"),
                    "description": i.get("description"),
                    "estimate": i.get("estimate"),
                    "priority": i.get("priority"),
                    "state": i.get("state"),
                    "assignee": {
                        "id": i["assignee"]["id"],
                        "displayName": i["assignee"].get("displayName") or i["assignee"].get("name", ""),
                        "email": i["assignee"].get("email", "")
                    } if i.get("assignee") else None,
                    "labels": i.get("labels")
                }
                for i in remote_issues
            ]
        }
    }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(clean_team_export, f, indent=2, ensure_ascii=False)
    print(f"[OK] Fichier JSON actualise : {json_path}")

    # Sauvegarder le CSV a jour
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Identifier", "Title", "Estimate", "State", "Assignee", "Labels"])
        for i in remote_issues:
            ident = i.get("identifier")
            title = i.get("title")
            est = i.get("estimate") or ""
            st = i.get("state", {}).get("name") if i.get("state") else ""
            ass = i.get("assignee", {}).get("displayName") or i.get("assignee", {}).get("email") if i.get("assignee") else "Non assigne"
            lbls = ", ".join([l.get("name") for l in i.get("labels", {}).get("nodes", [])])
            writer.writerow([ident, title, est, st, ass, lbls])
    print(f"[OK] Fichier CSV actualise : {csv_path}")

    print("\n--- RESUME DES CHANGEMENTS DETECTES SUR LINEAR ---")
    if not changes:
        print("Aucun changement de statut ou d'assignation depuis le dernier export.")
    else:
        for c in changes:
            if c["type"] == "NEW":
                print(f"[NOUVEAU] {c['ident']} : {c['title']} | Etat: {c['state']} | Assignation: {c['assignee']}")
            else:
                print(f"[MODIFIE] {c['ident']} : {c['title']}")
                print(f"          Etat        : {c['old_state']} -> {c['new_state']}")
                print(f"          Assignation : {c['old_assignee']} -> {c['new_assignee']}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYNC GITLAB REPOS - Creation et Synchronisation des Depots GitLab Universite de Lille
Projet ShopLoc (MiageShopLoc) - M2 MIAGE GLOP 2026-2027

Ce script :
1. Verifie la connexion a l'instance GitLab Universite de Lille (gitlab.univ-lille.fr).
2. Verifie l'existence du groupe glop-garik et recupere son group_id.
3. Cree les 4 depots de microservices sous le groupe s'ils n'existent pas encore.
4. Retourne les URLs distantes pour configuration locale des remotes.
"""

import os
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path


def gitlab_api_request(url: str, token: str, method: str = "GET", data: dict = None) -> dict:
    """Execute une requete aupres de l'API REST v4 de GitLab."""
    headers = {
        "PRIVATE-TOKEN": token,
        "User-Agent": "ShopLoc-GitLab-Sync/1.0"
    }
    payload = None
    if data:
        payload = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=payload, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as res:
            res_body = res.read().decode("utf-8")
            return json.loads(res_body) if res_body else {}
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        raise RuntimeError(f"Erreur HTTP GitLab {e.code} ({e.reason}) : {err_msg}")


def load_gitlab_config(env_path: Path) -> tuple:
    """Charge le token et le groupe depuis ShopLoc/.env."""
    token = None
    group = "glop-garik"
    base_url = "https://gitlab.univ-lille.fr/api/v4"

    if env_path.is_file():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("GITLAB_PERSONAL_ACCESS_TOKEN="):
                    token = line.split("=", 1)[1].strip()
                elif line.startswith("GITLAB_API_URL="):
                    base_url = line.split("=", 1)[1].strip()
                elif line.startswith("GITLAB_GROUP="):
                    group = line.split("=", 1)[1].strip()

    if not token or token.startswith("${"):
        raise ValueError("GITLAB_PERSONAL_ACCESS_TOKEN introuvable dans .env")

    return token, base_url, group


def main():
    root_dir = Path(__file__).resolve().parent.parent.parent.parent
    env_path = root_dir / "ShopLoc" / ".env"
    token, base_url, group_name = load_gitlab_config(env_path)

    print(f"[INFO] Connexion a GitLab : {base_url}...")
    group_url = f"{base_url}/groups/{group_name}"
    group_data = gitlab_api_request(group_url, token)
    group_id = group_data.get("id")
    print(f"[OK] Groupe detecte : {group_data.get('name')} (ID: {group_id}, Web: {group_data.get('web_url')})")

    # Lister les projets existants dans le groupe
    projects_url = f"{base_url}/groups/{group_id}/projects?per_page=100"
    existing_projects = gitlab_api_request(projects_url, token)
    existing_by_path = {p["path"]: p for p in existing_projects}
    print(f"[INFO] {len(existing_projects)} projet(s) deja existant(s) dans le groupe.")

    services = [
        {
            "name": "shoploc-auth-service",
            "path": "shoploc-auth-service",
            "desc": "Microservice Authentification, SSO et Gestion des Roles pour ShopLoc (Spring Boot 3.3, Java 17)"
        },
        {
            "name": "shoploc-merchant-catalog-service",
            "path": "shoploc-merchant-catalog-service",
            "desc": "Microservice Boutiques, Catalogues et Stocks pour ShopLoc (Spring Boot 3.3, Java 17)"
        },
        {
            "name": "shoploc-cart-order-service",
            "path": "shoploc-cart-order-service",
            "desc": "Microservice Panier Multi-Boutiques et Coordinateur 2PC pour ShopLoc (Spring Boot 3.3, Java 17)"
        },
        {
            "name": "shoploc-loyalty-service",
            "path": "shoploc-loyalty-service",
            "desc": "Microservice Programme Fidelite et Cagnotte VFP pour ShopLoc (Spring Boot 3.3, Java 17)"
        }
    ]

    create_url = f"{base_url}/projects"
    results = {}

    for svc in services:
        spath = svc["path"]
        if spath in existing_by_path:
            proj = existing_by_path[spath]
            print(f"[INFO] Depot deja existant : {proj.get('web_url')}")
            results[spath] = proj
        else:
            payload = {
                "name": svc["name"],
                "path": spath,
                "namespace_id": group_id,
                "description": svc["desc"],
                "visibility": "private",
                "initialize_with_readme": False
            }
            new_proj = gitlab_api_request(create_url, token, method="POST", data=payload)
            print(f"[OK] Nouveau depot cree : {new_proj.get('web_url')}")
            results[spath] = new_proj

    # Sauvegarder les metadonnees
    out_file = root_dir / "ShopLoc" / "agent_projet" / "config" / "gitlab_repositories.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"[OK] Fichier de configuration genere : {out_file}")

    # Push initial securise vers chaque depot distant GitLab
    import subprocess
    print("\n--- Push initial des microservices vers GitLab Univ-Lille ---")
    microservices_dir = root_dir / "microservices"
    for svc in services:
        spath = svc["path"]
        svc_dir = microservices_dir / spath
        if not svc_dir.is_dir():
            print(f"[WARN] Repertoire local introuvable : {svc_dir}")
            continue

        remote_url_with_auth = f"https://oauth2:{token}@gitlab.univ-lille.fr/{group_name}/{spath}.git"
        clean_remote_url = f"https://gitlab.univ-lille.fr/{group_name}/{spath}.git"

        # Configurer l'URL distante propre
        subprocess.run(["git", "remote", "remove", "origin"], cwd=str(svc_dir), capture_output=True)
        subprocess.run(["git", "remote", "add", "origin", clean_remote_url], cwd=str(svc_dir), check=True)

        # Pousser sur main via l'URL avec token ephemere en argument CLI
        print(f"[INFO] Push de {spath} sur main...")
        cmd_push = ["git", "push", "-u", remote_url_with_auth, "main"]
        res_push = subprocess.run(cmd_push, cwd=str(svc_dir), capture_output=True, text=True)
        if res_push.returncode == 0:
            print(f"[SUCCES] {spath} synchronise sur GitLab : {clean_remote_url}")
        else:
            print(f"[WARN] Push de {spath} : {res_push.stderr.strip() or res_push.stdout.strip()}")


if __name__ == "__main__":
    main()

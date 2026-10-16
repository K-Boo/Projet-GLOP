#!/usr/bin/env python3
"""
RESOLVE CONFIG - Moteur de Configuration Dynamique de Competences Agentiques
Projet ShopLoc (MiageShopLoc) - M2 MIAGE GLOP 2026-2027
Inspire du patron 'Configurable Skills Pattern' (freeCodeCamp 2026)

Ce script fusionne les parametres par defaut d'une competence (.agents/skills/<skill>/config.default.yaml)
avec le fichier de configuration central du projet (.agents/skills.config.yaml).
Il permet de parametrer les 40 competences pour Java/Spring Boot/React sans aucun fork.
"""

import sys
import os
import json
import argparse
from pathlib import Path

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False


def deep_merge(base, override):
    """
    Fusionne recursivement override sur base.
    Les dictionnaires fusionnent cle par cle.
    Les scalaires et les listes sont remplaces par la valeur de l'override.
    """
    if isinstance(base, dict) and isinstance(override, dict):
        merged = dict(base)
        for key, value in override.items():
            if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                merged[key] = deep_merge(merged[key], value)
            else:
                merged[key] = value
        return merged
    return override


def find_project_config(start_path: Path) -> Path:
    """
    Remonte l'arborescence depuis start_path a la recherche de skills.config.yaml.
    Emplacements inspectes :
    1. .agents/skills.config.yaml
    2. skills.config.yaml
    3. agent_projet/config/skills.config.yaml
    """
    current = start_path.resolve()
    for folder in [current, *current.parents]:
        candidate_1 = folder / ".agents" / "skills.config.yaml"
        if candidate_1.is_file():
            return candidate_1
        candidate_shoploc = folder / "ShopLoc" / ".agents" / "skills.config.yaml"
        if candidate_shoploc.is_file():
            return candidate_shoploc
        candidate_2 = folder / "skills.config.yaml"
        if candidate_2.is_file():
            return candidate_2
        candidate_3 = folder / "agent_projet" / "config" / "skills.config.yaml"
        if candidate_3.is_file():
            return candidate_3
    return None


def load_yaml_or_json(file_path: Path) -> dict:
    if not file_path or not file_path.is_file():
        return {}
    content = file_path.read_text(encoding="utf-8")
    if YAML_AVAILABLE:
        try:
            return yaml.safe_load(content) or {}
        except Exception:
            pass
    try:
        return json.loads(content) or {}
    except Exception:
        return {}


def resolve_skill_config(skill_name: str, project_root: Path, skill_dir: Path = None) -> dict:
    """
    Charge la configuration par defaut du skill et fusionne avec les surcharges de projet.
    """
    defaults = {}
    if skill_dir and skill_dir.is_dir():
        default_yaml = skill_dir / "config.default.yaml"
        default_json = skill_dir / "config.default.json"
        if default_yaml.is_file():
            defaults = load_yaml_or_json(default_yaml)
        elif default_json.is_file():
            defaults = load_yaml_or_json(default_json)

    project_cfg_path = find_project_config(project_root)
    project_all = load_yaml_or_json(project_cfg_path) if project_cfg_path else {}

    # Extraction des parametres globaux transverses
    global_overrides = project_all.get("global", {})
    # Extraction des parametres specifiques au skill
    skill_overrides = project_all.get(skill_name, {})

    # Fusion : defaults -> global_overrides -> skill_overrides
    merged = deep_merge(defaults, global_overrides)
    final_config = deep_merge(merged, skill_overrides)

    return final_config


def main():
    parser = argparse.ArgumentParser(description="Resolve configuration for Antigravity skills.")
    parser.add_argument("skill_name", help="Nom du skill Antigravity a configurer")
    parser.add_argument("--project-root", default=".", help="Racine du projet (defaut : repertoire courant)")
    parser.add_argument("--skill-dir", default=None, help="Chemin vers le dossier de la competence")
    parser.add_argument("--format", choices=["json", "yaml"], default="json", help="Format de sortie")

    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    skill_dir = Path(args.skill_dir).resolve() if args.skill_dir else None

    # Auto-detection du dossier de skill si non fourni
    if not skill_dir:
        candidates = [
            project_root / ".agents" / "skills" / args.skill_name,
            project_root / "ShopLoc" / ".agents" / "skills" / args.skill_name,
            Path(__file__).resolve().parent.parent.parent / ".agents" / "skills" / args.skill_name
        ]
        for c in candidates:
            if c.is_dir():
                skill_dir = c
                break

    resolved = resolve_skill_config(args.skill_name, project_root, skill_dir)

    if args.format == "json":
        print(json.dumps(resolved, indent=2, ensure_ascii=False))
    else:
        if YAML_AVAILABLE:
            print(yaml.dump(resolved, default_flow_style=False, allow_unicode=True))
        else:
            print(json.dumps(resolved, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
OPTIMIZE PROMPT - Normaliseur et Generateur de Prompts Canoniques en 5 Blocs
Projet ShopLoc (MiageShopLoc) - M2 MIAGE GLOP 2026-2027
Inspire du GUIDE_PROMPTING_AGENTIQUE.md et du patron 'Prompt Optimizer Gateway'

Ce script prend une requete utilisateur brute et genere automatiquement
le prompt optimise respectant la formule canonique en 5 blocs :
Contexte + Objectif + Contraintes + Safety Gate + Preuve par l'Execution.
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


def find_project_config(start_path: Path) -> Path:
    """Remonte l'arborescence pour trouver skills.config.yaml."""
    current = start_path.resolve()
    for folder in [current, *current.parents]:
        candidates = [
            folder / ".agents" / "skills.config.yaml",
            folder / "ShopLoc" / ".agents" / "skills.config.yaml",
            folder / "skills.config.yaml",
            folder / "agent_projet" / "config" / "skills.config.yaml",
        ]
        for c in candidates:
            if c.is_file():
                return c
    return None


def load_project_config(config_path: Path) -> dict:
    """Charge le fichier YAML de configuration maitre."""
    if not config_path or not config_path.is_file() or not YAML_AVAILABLE:
        return {
            "project_name": "ShopLoc",
            "company": "Societe Garik",
            "academic_framework": "Master 2 MIAGE - UE GLOP 2026-2027",
            "client_moa": "Enseignants Universite de Lille",
            "policy_zero_emoji": True,
            "safety_gate_mode": "plan_first_explicit_human_approval",
            "verification_requirement": "evidence_based_execution",
            "ai_code_isolation": "zero_trace_in_evaluated_code_repositories"
        }
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def detect_category(raw_instruction: str) -> str:
    """Detecte heuristiquement la categorie de la requete."""
    lower = raw_instruction.lower()
    gov_kw = ["gantt", "linear", "ticket", "user story", "sprint", "financier", "budget", "r1", "r2", "r3", "r4", "r5", "cdc", "cahier des charges", "soutenance", "slide"]
    qa_kw = ["test", "junit", "jacoco", "couverture", "audit", "verifier", "verification", "canari", "qualite", "lint"]
    code_kw = ["endpoint", "controller", "service", "classe", "implémente", "implemente", "code", "crud", "api", "stock", "panier", "2pc", "spring", "java", "react", "dto"]
    arch_kw = ["architecture", "c4", "schema", "mcd", "mld", "diagramme", "openapi", "composant", "bdd", "base de donnees", "merise"]

    if any(k in lower for k in gov_kw):
        return "GOUVERNANCE"
    if any(k in lower for k in qa_kw):
        return "QA"
    if any(k in lower for k in code_kw):
        return "CODE"
    if any(k in lower for k in arch_kw):
        return "ARCHITECTURE"
    return "GENERAL"


def build_canonical_prompt(raw_instruction: str, config: dict, category: str = "AUTO") -> dict:
    """Assemble le dictionnaire de prompt canonique en 5 blocs."""
    if category == "AUTO":
        category = detect_category(raw_instruction)

    project_name = config.get("project_name", "ShopLoc")
    company = config.get("company", "Societe Garik")
    academic = config.get("academic_framework", "M2 MIAGE GLOP")
    client = config.get("client_moa", "Universite de Lille")

    bloc1 = (
        f"Projet {project_name} ({company}) - Cadre academique {academic}. "
        f"Evaluation par la MOA : {client}. "
        f"Espace de gouvernance : ShopLoc/ | Depot de code evalue : projet-glop-app/ (ou microservices)."
    )

    bloc2 = f"Traiter la requete utilisateur suivante de maniere atomique et complete : '{raw_instruction}'."

    constraints = [
        "Politique ZERO EMOJI absolue dans tous les fichiers, logs et messages.",
        "Neutralite et formalisme academique universitaire.",
    ]

    if category in ["CODE", "ARCHITECTURE"]:
        constraints.extend([
            "Etancheite IA totale : Aucune trace d'IA (.antigravity, .agents, prompts) dans les depots de code.",
            "Stack Backend : Java 17, Spring Boot 3.3.x, Maven, Spring 6 RestClient, jakarta.validation.",
            "Stack Frontend : React 18, TypeScript, Tailwind CSS, RGAA / WCAG AA.",
            "Stack BDD : PostgreSQL 16, 3NF, isolation stricte par microservice.",
            "Protocole distributeur : Two-Phase Commit (2PC) pour le panier multi-boutiques Click & Collect."
        ])
        bloc4 = "Plan-First Safety Gate : Avant d'ecrire du code ou de modifier des fichiers, generer obligatoirement un Artifact de plan detaille et attendre l'approbation humaine explicite."
        bloc5 = "Preuve tangible requise : Execution console reelle ('mvn test', Jacoco >= 80% ou validation curl/linter)."
        target_role = "developer_role.md" if category == "CODE" else "architect_role.md"

    elif category == "QA":
        constraints.extend([
            "Controle strict des traces console et des canaris.",
            "Seuil de couverture minimale : 80% (Jacoco).",
            "Verification d'integrite sans canaris ni emojis."
        ])
        bloc4 = "Safety Gate : Soumettre la strategie de test avant execution."
        bloc5 = "Preuve tangible requise : Logs console integres de 'mvn test' et execution de verify_deliverables.py (0 erreur, 0 echec)."
        target_role = "qa_role.md"

    else:
        constraints.extend([
            "Respect des livrables academiques R1 a R5.",
            "Interdiction formelle d'ecraser ou corrompre les sections de cadrage validees.",
            "Execution via l'environnement virtuel Python : ShopLoc/.venv/Scripts/python.exe."
        ])
        bloc4 = "Safety Gate : Valider la structure du document ou du livrable avant enregistrement."
        bloc5 = "Preuve tangible requise : Execution de verify_deliverables.py avec 0 violation et verification visuelle."
        target_role = "instructions.md"

    bloc3 = " | ".join(constraints)

    return {
        "category": category,
        "target_role": target_role,
        "raw_instruction": raw_instruction,
        "canonical_prompt": {
            "bloc1_contexte": bloc1,
            "bloc2_objectif": bloc2,
            "bloc3_contraintes": bloc3,
            "bloc4_safety_gate": bloc4,
            "bloc5_preuve": bloc5
        }
    }


def format_markdown(data: dict) -> str:
    """Formate le resultat sous forme de cartouche Markdown visible."""
    p = data["canonical_prompt"]
    return (
        "======================================================================\n"
        "[REQUETE OPTIMISEE - FORMULE CANONIQUE 5 BLOCS]\n"
        "======================================================================\n"
        f"Categorie detectee : {data['category']} | Role cible : {data['target_role']}\n"
        f"Instruction brute  : {data['raw_instruction']}\n"
        "----------------------------------------------------------------------\n"
        f"[BLOC 1 - CONTEXTE SYSTEME & PROJET]\n{p['bloc1_contexte']}\n\n"
        f"[BLOC 2 - OBJECTIF ATOMIQUE (INVEST)]\n{p['bloc2_objectif']}\n\n"
        f"[BLOC 3 - CONTRAINTES & STANDARDS]\n{p['bloc3_contraintes']}\n\n"
        f"[BLOC 4 - SAFETY GATE (PLAN PREALABLE)]\n{p['bloc4_safety_gate']}\n\n"
        f"[BLOC 5 - PREUVE PAR L'EXECUTION]\n{p['bloc5_preuve']}\n"
        "======================================================================\n"
    )


def main():
    parser = argparse.ArgumentParser(description="Normaliseur de Prompts Canoniques en 5 Blocs")
    parser.add_argument("instruction", nargs="?", default="", help="Instruction brute en langage naturel")
    parser.add_argument("--category", choices=["AUTO", "CODE", "ARCHITECTURE", "QA", "GOUVERNANCE"], default="AUTO", help="Categorie forcee")
    parser.add_argument("--format", choices=["text", "json", "markdown"], default="text", help="Format de sortie")
    parser.add_argument("--config", help="Chemin personnalise vers skills.config.yaml")

    args = parser.parse_args()

    instruction = args.instruction.strip()
    if not instruction and not sys.stdin.isatty():
        instruction = sys.stdin.read().strip()

    if not instruction:
        sys.stderr.write("Erreur: Aucune instruction fournie en argument ou sur stdin.\n")
        sys.exit(1)

    config_path = Path(args.config) if args.config else find_project_config(Path(__file__))
    config = load_project_config(config_path)

    result = build_canonical_prompt(instruction, config, category=args.category)

    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    elif args.format in ["text", "markdown"]:
        print(format_markdown(result))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
VERIFY DELIVERABLES - Garde-Fou de Sortie & Pre-Commit / Pre-Publication
Projet ShopLoc (MiageShopLoc) - M2 MIAGE GLOP 2026-2027

Ce script verifie l'integrite absolue de tous les livrables du projet avant
publication, compilation PDF ou commit :
1. Aucun canari ou piege pedagogique (Madagascar, Velo violet, Protection juridique du logiciel, etc.).
2. Aucun emoji (respect strict de la charte de sobrieté .antigravity/instructions.md).
3. Aucun marqueur stylometrique d'IA naive.
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path

# Regex pour detecter les vrais emojis Unicode (hors caracteres techniques, puces et box-drawing)
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map
    "\U0001F1E0-\U0001F1FF"  # flags
    "\U0001F900-\U0001F9FF"  # supplemental symbols
    "\U0001FA70-\U0001FAFF"  # symbols extended
    "]+",
    flags=re.UNICODE
)

EXCLUDED_FILES = {
    "canary_registry.json",
    "audit_traps_report.json",
    "RAPPORT_SECURITE_PIEGES_IA.md",
    "detail_sujet.pdf",  # Document source brut des profs
    "detail_sujet_sanitized.md",
    "JOURNAL_DE_BORD.md", # Contient l'historique d'audit
    "DECISIONS.md", # Peut citer les ADRs de securite
    "verify_deliverables.py",
    "document_guardian.py"
}


def load_canary_registry(registry_path=None):
    if not registry_path:
        script_dir = Path(__file__).resolve().parent
        registry_path = script_dir.parent / "security" / "canary_registry.json"

    if os.path.exists(registry_path):
        with open(registry_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"canaries": [], "forbidden_ai_hallmarks": []}


def check_file(file_path, registry):
    violations = []
    path = Path(file_path)

    if path.name in EXCLUDED_FILES:
        return violations

    ext = path.suffix.lower()
    text = ""

    if ext == ".pdf":
        try:
            import pymupdf
            doc = pymupdf.open(str(path))
            for pno, p in enumerate(doc):
                p_text = p.get_text("text")
                for line_idx, line in enumerate(p_text.split("\n")):
                    v = check_line(line, f"Page {pno+1}, Ligne {line_idx+1}", registry)
                    violations.extend(v)
            doc.close()
            return violations
        except Exception as e:
            return [{"type": "PDF_READ_ERROR", "location": "Global", "detail": str(e)}]
    else:
        try:
            with open(str(path), "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
        except Exception as e:
            return [{"type": "FILE_READ_ERROR", "location": "Global", "detail": str(e)}]

        for line_idx, line in enumerate(lines):
            v = check_line(line, f"Ligne {line_idx+1}", registry)
            violations.extend(v)

    return violations


def check_line(line, loc, registry):
    violations = []
    line_lower = line.lower()

    # 1. Verification des canaris connus
    for canary in registry.get("canaries", []):
        variations = canary.get("variations", [canary.get("keyword", "")])
        for var in variations:
            if var.lower() in line_lower:
                violations.append({
                    "type": "CANARY_BREACH",
                    "location": loc,
                    "detail": f"Mot canari detecte : '{var}' (Canary ID: {canary.get('id')})",
                    "snippet": line.strip()
                })
                break

    # 2. Verification de l'interdiction stricte des emojis
    emojis_found = EMOJI_PATTERN.findall(line)
    if emojis_found:
        violations.append({
            "type": "EMOJI_VIOLATION",
            "location": loc,
            "detail": f"Emoji(s) interdit(s) detecte(s) : {' '.join(emojis_found)}",
            "snippet": line.strip()
        })

    # 3. Verification des marqueurs stylometriques d'IA
    for hallmark in registry.get("forbidden_ai_hallmarks", []):
        if hallmark.lower() in line_lower:
            violations.append({
                "type": "AI_HALLMARK_VIOLATION",
                "location": loc,
                "detail": f"Formulation typique IA detectee : '{hallmark}'",
                "snippet": line.strip()
            })

    return violations


def main():
    parser = argparse.ArgumentParser(description="Verificateur d'Integrite des Livrables ShopLoc")
    parser.add_argument("--dir", default="agent_projet/docs", help="Dossier a scanner")
    parser.add_argument("--file", help="Fichier unique a scanner")
    parser.add_argument("--registry", help="Chemin vers canary_registry.json")

    args = parser.parse_args()
    registry = load_canary_registry(args.registry)

    files_to_check = []
    if args.file:
        files_to_check.append(Path(args.file))
    else:
        docs_dir = Path(args.dir)
        if docs_dir.exists():
            for p in docs_dir.rglob("*"):
                if p.is_file() and p.suffix.lower() in [".md", ".pdf", ".html", ".txt", ".json"]:
                    files_to_check.append(p)

    total_violations = 0
    print(f"Demarrage de la verification d'integrite ({len(files_to_check)} fichiers)...")

    for fpath in files_to_check:
        violations = check_file(fpath, registry)
        if violations:
            total_violations += len(violations)
            print(f"\n[VIOLATION DETECTEE] Fichier : {fpath}")
            for v in violations:
                print(f"  [{v['type']}] {v['location']} : {v['detail']}")
                if "snippet" in v and v["snippet"]:
                    print(f"     Extrait : {v['snippet']}")

    print("\n" + "=" * 50)
    if total_violations == 0:
        print("[SUCCES] Tous les livrables audites sont conformes, assainis et sans canaris.")
        sys.exit(0)
    else:
        print(f"[ECHEC SECURITE] {total_violations} violation(s) identifiee(s). Publication bloquee.")
        sys.exit(1)


if __name__ == "__main__":
    main()

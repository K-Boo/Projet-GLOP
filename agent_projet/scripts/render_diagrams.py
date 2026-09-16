#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MOTEUR DE GENERATION DE DIAGRAMMES & SCHEMAS VISUELS (render_diagrams.py)
Master 2 MIAGE — Universite de Lille — UE GLOP (2026-2027)

Compile, assemble et valide les diagrammes vectoriels (BPMN, MCD, C4, Gantt, APTE, Lean Canvas).
Supporte le rendu des composants modulaires HTML/SVG et l'export d'aperçus vectoriels.

Usage:
    python agent_projet/scripts/render_diagrams.py --export-all
    python agent_projet/scripts/render_diagrams.py --component <nom_composant>
"""

import argparse
import os
import subprocess
import sys

def get_paths():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    agent_projet_dir = os.path.join(project_root, "agent_projet")
    templates_dir = os.path.join(agent_projet_dir, "templates", "components")
    design_dir = os.path.join(agent_projet_dir, "design")
    docs_dir = os.path.join(agent_projet_dir, "docs")
    return {
        "script": script_dir,
        "templates": templates_dir,
        "design": design_dir,
        "docs": docs_dir,
        "theme_css": os.path.join(design_dir, "theme.css")
    }

def render_standalone_component(component_name, output_html_path):
    paths = get_paths()
    comp_file = os.path.join(paths["templates"], f"{component_name}.html")
    if not os.path.exists(comp_file):
        print(f"[ERREUR] Composant introuvable : {comp_file}")
        return False

    with open(paths["theme_css"], "r", encoding="utf-8") as f:
        theme_css = f.read()

    with open(comp_file, "r", encoding="utf-8") as f:
        comp_content = f.read()

    html_wrapper = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Apercu Composant — {component_name}</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/latin-modern-web@1.0.0/style.css">
  <style>
    {theme_css}
    body {{
      max-width: 960px;
      margin: 30px auto;
      padding: 20px;
      background: #F8FAFC;
    }}
  </style>
</head>
<body>
  {comp_content}
</body>
</html>
"""
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_wrapper)
    print(f"[SUCCES] Composant autonome genere : {output_html_path}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Moteur de generation des diagrammes et composants ShopLoc")
    parser.add_argument("--component", "-c", help="Nom du composant a generer (lean_canvas, apte_pieuvre, matrice_positionnement, ui_wireframe_card)")
    parser.add_argument("--export-all", action="store_true", help="Generer tous les composants autonomes dans agent_projet/docs/")

    args = parser.parse_args()
    paths = get_paths()

    components = [
        "lean_canvas",
        "apte_pieuvre",
        "matrice_positionnement",
        "ui_wireframe_card",
        "bpmn_swimlane_template",
        "merise_mcd_template"
    ]

    if args.component:
        out_file = os.path.join(paths["docs"], f"preview_{args.component}.html")
        render_standalone_component(args.component, out_file)
    elif args.export_all:
        for c in components:
            out_file = os.path.join(paths["docs"], f"preview_{c}.html")
            render_standalone_component(c, out_file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

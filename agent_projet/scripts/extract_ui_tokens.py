#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MOTEUR D EXTRACTION ET RETRO-INGENIERIE DE DESIGN TOKENS (extract_ui_tokens.py)
Master 2 MIAGE — Universite de Lille — UE GLOP (2026-2027)

Ce script permet a l agent UI d extraire et d harmoniser l identite visuelle
a partir d un site web, d un fichier CSS ou d une capture d ecran.
Il verifie simplement la bonne lisibilite des contrastes et produit des
Design Tokens normalises utilisables dans l application et les livrables.

Usage:
    python agent_projet/scripts/extract_ui_tokens.py --css path/to/styles.css
    python agent_projet/scripts/extract_ui_tokens.py --image path/to/screenshot.png
    python agent_projet/scripts/extract_ui_tokens.py --url https://example.com
    python agent_projet/scripts/extract_ui_tokens.py --css styles.css --update-tokens
"""

import argparse
import json
import os
import re
import sys
import urllib.request
from collections import Counter

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

try:
    from rich.console import Console
    from rich.table import Table
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


def srgb_to_luminance(r: int, g: int, b: int) -> float:
    """Calcule la luminance relative standard d une couleur."""
    def channel_linear(c_byte: int) -> float:
        c = c_byte / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r_lin = channel_linear(r)
    g_lin = channel_linear(g)
    b_lin = channel_linear(b)
    return 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin


def hex_to_rgb(hex_str: str) -> tuple:
    """Convertit un code hexadecimal (#RGB ou #RRGGBB) en tuple (R, G, B)."""
    hex_str = hex_str.lstrip("#")
    if len(hex_str) == 3:
        hex_str = "".join([c * 2 for c in hex_str])
    elif len(hex_str) == 8:
        hex_str = hex_str[:6]
    return tuple(int(hex_str[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Convertit un triplet RGB en code hexadecimal majuscule."""
    return f"#{r:02X}{g:02X}{b:02X}"


def calculate_contrast_ratio(hex1: str, hex2: str) -> float:
    """Calcule le ratio de contraste entre deux couleurs."""
    r1, g1, b1 = hex_to_rgb(hex1)
    r2, g2, b2 = hex_to_rgb(hex2)
    l1 = srgb_to_luminance(r1, g1, b1)
    l2 = srgb_to_luminance(r2, g2, b2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return round((lighter + 0.05) / (darker + 0.05), 2)


def extract_colors_from_image(image_path: str, max_colors: int = 8) -> list:
    """Extrait la palette dominante d une image via quantification Pillow."""
    if not PIL_AVAILABLE:
        print("[ERREUR] Pillow (PIL) n est pas installe. Impossible d analyser l image.")
        return []
    if not os.path.exists(image_path):
        print(f"[ERREUR] Image introuvable : {image_path}")
        return []

    img = Image.open(image_path).convert("RGB")
    img.thumbnail((300, 300))
    quantized = img.quantize(colors=max_colors, method=Image.Quantize.MEDIANCUT)
    palette = quantized.getpalette()[:max_colors * 3]

    color_counts = Counter(quantized.getdata())
    sorted_palette_indices = [idx for idx, _ in color_counts.most_common(max_colors)]

    colors = []
    for idx in sorted_palette_indices:
        r = palette[idx * 3]
        g = palette[idx * 3 + 1]
        b = palette[idx * 3 + 2]
        colors.append(rgb_to_hex(r, g, b))
    return colors


def extract_from_css_text(css_text: str) -> dict:
    """Extrait les couleurs, typographies et echelles d espacement d un texte CSS."""
    results = {
        "colors": [],
        "fonts": [],
        "radii": [],
        "shadows": []
    }

    # Extraction des couleurs hexadécimales
    hex_pattern = re.compile(r"#(?:[0-9a-fA-F]{3,4}){1,2}\b")
    raw_hexes = hex_pattern.findall(css_text)
    normalized_hexes = []
    for h in raw_hexes:
        clean = h.upper()
        if len(clean) == 4:
            clean = "#" + "".join([c * 2 for c in clean[1:]])
        elif len(clean) == 9:
            clean = clean[:7]
        normalized_hexes.append(clean)
    results["colors"] = [col for col, _ in Counter(normalized_hexes).most_common(20)]

    # Extraction des polices (font-family)
    font_pattern = re.compile(r"font-family\s*:\s*([^;]+);", re.IGNORECASE)
    raw_fonts = font_pattern.findall(css_text)
    fonts_list = []
    for f in raw_fonts:
        cleaned_font = f.strip().strip("'\"").split(",")[0].strip().strip("'\"")
        if cleaned_font and cleaned_font.lower() not in ["inherit", "initial", "unset"]:
            fonts_list.append(cleaned_font)
    results["fonts"] = [fnt for fnt, _ in Counter(fonts_list).most_common(5)]

    # Extraction des border-radius
    radius_pattern = re.compile(r"border-radius\s*:\s*([^;]+);", re.IGNORECASE)
    raw_radii = radius_pattern.findall(css_text)
    cleaned_radii = [r.strip() for r in raw_radii if r.strip()]
    results["radii"] = [rad for rad, _ in Counter(cleaned_radii).most_common(5)]

    # Extraction des box-shadow
    shadow_pattern = re.compile(r"box-shadow\s*:\s*([^;]+);", re.IGNORECASE)
    raw_shadows = shadow_pattern.findall(css_text)
    cleaned_shadows = [s.strip() for s in raw_shadows if s.strip() and s.strip() != "none"]
    results["shadows"] = [sh for sh, _ in Counter(cleaned_shadows).most_common(5)]

    return results


def check_contrast_readability(color_hex: str) -> dict:
    """Evalue le confort visuel et la lisibilite d une couleur."""
    contrast_on_white = calculate_contrast_ratio(color_hex, "#FFFFFF")
    contrast_on_dark = calculate_contrast_ratio(color_hex, "#0F2A4A")

    is_good = contrast_on_white >= 4.5 or contrast_on_dark >= 4.5
    is_medium = contrast_on_white >= 3.0 or contrast_on_dark >= 3.0

    best_bg = "#FFFFFF" if contrast_on_white >= contrast_on_dark else "#0F2A4A"
    best_contrast = max(contrast_on_white, contrast_on_dark)

    readability = "TRES LISIBLE" if is_good else ("CORRECT (TITRES)" if is_medium else "PEU LISIBLE")

    return {
        "color": color_hex,
        "contrast_white": contrast_on_white,
        "contrast_dark": contrast_on_dark,
        "best_bg": best_bg,
        "best_contrast": best_contrast,
        "readability": readability,
        "pierre_friendly": best_contrast >= 4.5
    }


def build_tokens_payload(extracted: dict, source_label: str) -> dict:
    """Construit un objet Design Tokens simple au format W3C Community Group."""
    colors = extracted.get("colors", [])
    fonts = extracted.get("fonts", [])
    radii = extracted.get("radii", [])

    primary_color = colors[0] if len(colors) > 0 else "#0F2A4A"
    secondary_color = colors[1] if len(colors) > 1 else "#6A1B29"
    accent_color = colors[2] if len(colors) > 2 else "#1E3A8A"

    font_heading = fonts[0] if len(fonts) > 0 else "Liberation Sans"
    font_body = fonts[1] if len(fonts) > 1 else "Liberation Sans"

    tokens = {
        "$schema": "https://design-tokens.github.io/community-group/format/",
        "name": f"ShopLoc Tokens - {source_label}",
        "version": "1.1.0",
        "description": f"Tokens adaptes pour ShopLoc M2 MIAGE GLOP depuis {source_label}",
        "color": {
            "brand": {
                "primary": {
                    "value": primary_color,
                    "type": "color",
                    "description": "Couleur maitresse pour en-tetes et elements structurants"
                },
                "secondary": {
                    "value": secondary_color,
                    "type": "color",
                    "description": "Couleur secondaire et accents"
                },
                "accent": {
                    "value": accent_color,
                    "type": "color",
                    "description": "Couleur d action pour boutons et liens"
                }
            }
        },
        "typography": {
            "fontFamily": {
                "heading": {
                    "value": font_heading,
                    "type": "fontFamily",
                    "description": "Typographie pour les titres"
                },
                "body": {
                    "value": font_body,
                    "type": "fontFamily",
                    "description": "Typographie de lecture agreable et lisible"
                }
            }
        },
        "border": {
            "radius": {
                "sm": {"value": radii[0] if len(radii) > 0 else "4px", "type": "dimension"},
                "md": {"value": radii[1] if len(radii) > 1 else "8px", "type": "dimension"}
            }
        }
    }
    return tokens


def display_audit_report(extracted: dict, source_label: str):
    """Affiche le rapport d extraction et de lisibilite dans le terminal."""
    if RICH_AVAILABLE:
        console = Console()
        console.print(f"\n[bold blue]=== ANALYSE DE L IDENTITE VISUELLE : {source_label} ===[/bold blue]\n")

        # Table Couleurs & Lisibilité
        table = Table(title="Palette Extraite & Confort de Lecture")
        table.add_column("Couleur", justify="center")
        table.add_column("Apercu", justify="center")
        table.add_column("Sur Blanc", justify="right")
        table.add_column("Sur Fond Sombre", justify="right")
        table.add_column("Lisibilite", justify="center")
        table.add_column("Senior Pierre (Lisible)", justify="center")

        for col in extracted.get("colors", [])[:10]:
            audit = check_contrast_readability(col)
            statut_style = "green" if "TRES LISIBLE" in audit["readability"] else ("yellow" if "CORRECT" in audit["readability"] else "red")
            pierre_style = "green" if audit["pierre_friendly"] else "red"
            pierre_label = "OUI" if audit["pierre_friendly"] else "A AMELIORER"
            table.add_row(
                col,
                f"[{col}][=====][/{col}]",
                f"{audit['contrast_white']}:1",
                f"{audit['contrast_dark']}:1",
                f"[{statut_style}]{audit['readability']}[/{statut_style}]",
                f"[{pierre_style}]{pierre_label}[/{pierre_style}]"
            )
        console.print(table)

        if extracted.get("fonts"):
            console.print(f"\n[bold]Typographies detectees :[/bold] {', '.join(extracted['fonts'])}")
        if extracted.get("radii"):
            console.print(f"[bold]Arrondis de boutons detectes :[/bold] {', '.join(extracted['radii'])}")
        console.print("\n[bold green][SUCCES] Analyse terminee avec zero emoji conforme aux regles GLOP.[/bold green]\n")
    else:
        print(f"\n=== ANALYSE DE L IDENTITE VISUELLE : {source_label} ===")
        print("Couleurs extraites et lisibilite :")
        for col in extracted.get("colors", [])[:10]:
            audit = check_contrast_readability(col)
            print(f"  - {col} | Blanc: {audit['contrast_white']}:1 | Sombre: {audit['contrast_dark']}:1 | Lisibilite: {audit['readability']}")
        if extracted.get("fonts"):
            print(f"Typographies : {', '.join(extracted['fonts'])}")
        print("[SUCCES] Analyse terminee sans emoji.\n")


def main():
    parser = argparse.ArgumentParser(description="Extraction et harmonisation des Design Tokens ShopLoc")
    parser.add_argument("--url", type=str, help="URL cible a analyser pour extraire l identite visuelle")
    parser.add_argument("--css", type=str, help="Chemin vers un fichier CSS local")
    parser.add_argument("--image", type=str, help="Chemin vers une capture d ecran ou maquette PNG/JPG")
    parser.add_argument("--export-json", type=str, help="Chemin d export pour les tokens au format W3C JSON")
    parser.add_argument("--update-tokens", action="store_true", help="Proposer ou sauvegarder les tokens pour ShopLoc")
    parser.add_argument("--export-css", type=str, help="Chemin d export pour les variables CSS correspondantes")
    args = parser.parse_args()

    if not args.url and not args.css and not args.image:
        parser.print_help()
        sys.exit(1)

    extracted = {"colors": [], "fonts": [], "radii": [], "shadows": []}
    source_label = "Inconnu"

    if args.image:
        source_label = os.path.basename(args.image)
        colors = extract_colors_from_image(args.image)
        extracted["colors"] = colors

    elif args.css:
        source_label = os.path.basename(args.css)
        if not os.path.exists(args.css):
            print(f"[ERREUR] Fichier CSS introuvable : {args.css}")
            sys.exit(1)
        with open(args.css, "r", encoding="utf-8", errors="ignore") as f:
            css_content = f.read()
        extracted = extract_from_css_text(css_content)

    elif args.url:
        source_label = args.url
        try:
            req = urllib.request.Request(args.url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
            with urllib.request.urlopen(req, timeout=10) as response:
                html_text = response.read().decode("utf-8", errors="ignore")
                extracted = extract_from_css_text(html_text)
        except Exception as e:
            print(f"[ERREUR] Echec du telechargement de l URL {args.url} : {e}")
            sys.exit(1)

    display_audit_report(extracted, source_label)

    tokens_data = build_tokens_payload(extracted, source_label)

    if args.export_json:
        with open(args.export_json, "w", encoding="utf-8") as f:
            json.dump(tokens_data, f, indent=2)
        print(f"[SUCCES] Tokens exportes dans : {args.export_json}")

    if args.export_css:
        css_vars = [":root {"]
        colors = extracted.get("colors", [])
        if len(colors) > 0:
            css_vars.append(f"  --sl-color-brand-primary: {colors[0]};")
        if len(colors) > 1:
            css_vars.append(f"  --sl-color-brand-secondary: {colors[1]};")
        if len(colors) > 2:
            css_vars.append(f"  --sl-color-brand-accent: {colors[2]};")
        for i, rad in enumerate(extracted.get("radii", [])[:3]):
            css_vars.append(f"  --sl-radius-{i+1}: {rad};")
        css_vars.append("}")
        with open(args.export_css, "w", encoding="utf-8") as f:
            f.write("\n".join(css_vars) + "\n")
        print(f"[SUCCES] Variables CSS exportees dans : {args.export_css}")

    if args.update_tokens:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(script_dir))
        proposal_file = os.path.join(project_root, "agent_projet", "design", "design_tokens_proposal.json")
        with open(proposal_file, "w", encoding="utf-8") as f:
            json.dump(tokens_data, f, indent=2)
        print(f"[SUCCES] Proposition de tokens sauvegardee dans : {proposal_file}")


if __name__ == "__main__":
    main()

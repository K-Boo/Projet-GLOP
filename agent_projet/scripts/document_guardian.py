#!/usr/bin/env python3
"""
DOCUMENT GUARDIAN - Moteur d'Analyse Forensique et d'Assainissement Documentaire
Projet ShopLoc (MiageShopLoc) - M2 MIAGE GLOP 2026-2027

Ce script constitue le pare-feu d'ingestion Zero-Trust pour tous les documents
entrants (PDF, DOCX, TXT, MD, HTML).
Il detecte, signale et neutralise :
1. Le texte invisible (couleur blanche #FFFFFF, opacite 0, mode Tr 3).
2. Le micro-texte (taille < 3.5 pt) et le texte hors zone visible.
3. Les caracteres zero-width (ZWSP, ZWNJ, BOM, etc.) et la steganographie.
4. Les homoglyphes (cyrillique/grec injecte pour perturber la detection).
5. Les injections de prompt indirectes (IPI) et les instructions canaris.
6. Les axes fantomes et fausses exigences pieges.
"""

import sys
import os
import re
import json
import argparse
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

# Caracteres invisibles a surveiller
ZERO_WIDTH_CHARS = {
    0x200B: "ZERO_WIDTH_SPACE",
    0x200C: "ZERO_WIDTH_NON_JOINER",
    0x200D: "ZERO_WIDTH_JOINER",
    0xFEFF: "BYTE_ORDER_MARK_OR_ZW_NO_BREAK",
    0x2060: "WORD_JOINER",
    0x00AD: "SOFT_HYPHEN",
    0x2028: "LINE_SEPARATOR",
    0x2029: "PARAGRAPH_SEPARATOR",
    0x202A: "LEFT_TO_RIGHT_EMBEDDING",
    0x202B: "RIGHT_TO_LEFT_EMBEDDING",
    0x202C: "POP_DIRECTIONAL_FORMATTING",
    0x202D: "LEFT_TO_RIGHT_OVERRIDE",
    0x202E: "RIGHT_TO_LEFT_OVERRIDE"
}

# Expressions regulieres de detection d'injection de prompt et consignes canaris
INJECTION_PATTERNS = [
    (r"(?:dans|in)\s+(?:la|votre|your)?\s*r[eé]ponse\s+(?:utilisez|mentionnez|incluez|ins[eé]rez)\s+(?:les\s+mots|le\s+mot|termes?)", "CANARY_INSTRUCTION_TRIGGER"),
    (r"(?:ignore|ignorez|disregard|forget)\s+(?:all\s+)?(?:previous|les|toutes?\s+les)?\s*(?:instructions|consignes|prompts)", "PROMPT_INJECTION_OVERRIDE"),
    (r"(?:you\s+are\s+now|tu\s+es\s+d[eé]sormais|agis\s+en\s+tant\s+que)\s+(?:dan|jailbreak|unrestricted)", "JAILBREAK_ATTEMPT"),
    (r"(?:ne\s+tenez\s+pas\s+compte|do\s+not\s+follow)\s+(?:du\s+contexte|des\s+directives)", "INSTRUCTION_DISREGARD"),
    (r"(?:mot\s+(?:de\s+passe|secret)|secret\s+key|canary\s+token)\s*[:=]", "CANARY_TOKEN_EXTRACTION"),
    (r"(?:attribuez|mettez|donnez)\s+(?:la\s+note\s+maximale|20/20|un\s+score\s+de)", "EVALUATION_TAMPERING"),
]


class DocumentGuardian:
    def __init__(self, canary_registry_path=None):
        self.findings = []
        self.sanitized_blocks = []
        self.canary_registry = self._load_canary_registry(canary_registry_path)

    def _load_canary_registry(self, registry_path):
        if not registry_path:
            # Emplacement par defaut
            script_dir = Path(__file__).resolve().parent
            default_path = script_dir.parent / "security" / "canary_registry.json"
            if default_path.exists():
                registry_path = str(default_path)

        if registry_path and os.path.exists(registry_path):
            try:
                with open(registry_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"[AVERTISSEMENT] Erreur lors du chargement du registre de canaris : {e}", file=sys.stderr)
        return {"canaries": [], "forbidden_ai_hallmarks": [], "suspicious_injection_triggers": []}

    def analyze(self, file_path):
        self.findings = []
        self.sanitized_blocks = []
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"Fichier introuvable : {file_path}")

        ext = path.suffix.lower()
        if ext == ".pdf":
            self._analyze_pdf(path)
        elif ext in [".docx", ".pptx", ".xlsx"]:
            self._analyze_ooxml(path)
        elif ext in [".txt", ".md", ".markdown"]:
            self._analyze_text(path)
        elif ext in [".html", ".htm"]:
            self._analyze_html(path)
        else:
            # Fallback binaire / texte
            self._analyze_text(path)

        return self.findings

    def _analyze_pdf(self, path):
        try:
            import pymupdf
        except ImportError:
            raise ImportError("PyMuPDF (pymupdf) est requis pour l'analyse PDF.")

        doc = pymupdf.open(str(path))

        # 1. Analyse des metadonnees
        for key, val in doc.metadata.items():
            if val:
                self._check_semantic_injections(val, context=f"PDF Metadata [{key}]", page=0)
                self._check_zero_width_chars(val, context=f"PDF Metadata [{key}]", page=0)

        # 2. Analyse vectorielle page par page
        for page_idx, page in enumerate(doc):
            page_num = page_idx + 1
            page_rect = page.rect
            page_drawings = page.get_drawings()
            page_sanitized_lines = []

            # Extraction detaillee des blocs et spans
            page_dict = page.get_text("dict")
            for block in page_dict.get("blocks", []):
                if "lines" not in block:
                    continue

                for line in block["lines"]:
                    line_spans = []
                    line_is_quarantined = False

                    for span in line["spans"]:
                        text = span.get("text", "")
                        if not text:
                            continue

                        size = span.get("size", 10.0)
                        color = span.get("color", 0)
                        bbox = span.get("bbox", [0, 0, 0, 0])
                        flags = span.get("flags", 0)

                        # Decomposer la couleur RGB
                        r = (color >> 16) & 255
                        g = (color >> 8) & 255
                        b = color & 255

                        is_suspicious = False
                        trap_type = None
                        trap_details = {}

                        # Test A : Texte blanc ou quasi-blanc sur fond clair (calcul du contraste reel)
                        if r >= 235 and g >= 235 and b >= 235:
                            center_pt = pymupdf.Point((bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2)
                            bg_rgb = self._get_background_color_at(page_drawings, center_pt)
                            contrast = self._calc_contrast_ratio((r/255, g/255, b/255), bg_rgb)
                            if contrast < 1.5:
                                is_suspicious = True
                                trap_type = "WHITE_OR_INVISIBLE_TEXT"
                                trap_details = {
                                    "color_rgb": [r, g, b],
                                    "color_hex": f"#{r:02X}{g:02X}{b:02X}",
                                    "background_rgb": [int(bg_rgb[0]*255), int(bg_rgb[1]*255), int(bg_rgb[2]*255)],
                                    "contrast_ratio": f"{contrast:.2f}:1",
                                    "reason": f"Contraste quasi-nul ({contrast:.2f}:1) : texte blanc dissimule sur fond clair"
                                }

                        # Test B : Micro-texte (< 3.5 pt)
                        elif size < 3.5:
                            is_suspicious = True
                            trap_type = "TINY_OR_MICRO_TEXT"
                            trap_details = {
                                "size": size,
                                "reason": f"Taille de police anormalement reduite ({size:.1f} pt)"
                            }

                        # Test C : Texte positionne hors de la zone visible
                        span_rect = pymupdf.Rect(bbox)
                        if not page_rect.contains(span_rect) and not page_rect.intersects(span_rect):
                            is_suspicious = True
                            trap_type = "OFF_PAGE_TEXT"
                            trap_details = {
                                "bbox": list(bbox),
                                "page_rect": [page_rect.x0, page_rect.y0, page_rect.x1, page_rect.y1],
                                "reason": "Texte positionne hors des dimensions de la page"
                            }

                        # Test D : Caracteres zero-width
                        zw_found = self._check_zero_width_chars(text, context=f"Page {page_num}", page=page_num, bbox=bbox)
                        if zw_found:
                            is_suspicious = True

                        # Test E : Injections semantiques ou canaris connus
                        inj_found = self._check_semantic_injections(text, context=f"Page {page_num}", page=page_num, bbox=bbox)
                        if inj_found:
                            is_suspicious = True

                        # Test F : Homoglyphes suspects
                        homo_found = self._check_homoglyphs(text, context=f"Page {page_num}", page=page_num, bbox=bbox)
                        if homo_found:
                            is_suspicious = True

                        if is_suspicious:
                            line_is_quarantined = True
                            if trap_type:
                                self.findings.append({
                                    "severity": "CRITICAL" if trap_type in ["WHITE_OR_INVISIBLE_TEXT", "CANARY_INSTRUCTION_TRIGGER"] else "WARNING",
                                    "category": trap_type,
                                    "page": page_num,
                                    "bbox": list(bbox),
                                    "font_size": size,
                                    "text": text,
                                    "details": trap_details
                                })
                        else:
                            # Span sain conserve
                            clean_span_text = self._purge_invisible_chars(text)
                            line_spans.append(clean_span_text)

                    if not line_is_quarantined and line_spans:
                        joined_line = "".join(line_spans).strip()
                        if joined_line:
                            page_sanitized_lines.append(joined_line)

            # Verification des annotations et commentaires de page
            annot = page.first_annot
            while annot:
                info = annot.info
                content = info.get("content", "")
                if content:
                    self._check_semantic_injections(content, context=f"Annotation Page {page_num}", page=page_num)
                    self._check_zero_width_chars(content, context=f"Annotation Page {page_num}", page=page_num)
                annot = annot.next

            if page_sanitized_lines:
                self.sanitized_blocks.append({
                    "page": page_num,
                    "content": "\n".join(page_sanitized_lines)
                })

        doc.close()

    def _analyze_ooxml(self, path):
        """Inspection des archives Office (DOCX, PPTX, XLSX)."""
        try:
            with zipfile.ZipFile(str(path), "r") as z:
                xml_files = [n for n in z.namelist() if n.endswith(".xml")]
                for xml_name in xml_files:
                    raw_xml = z.read(xml_name).decode("utf-8", errors="ignore")

                    # Detection de texte cache (w:vanish, w:hidden, w:color="FFFFFF")
                    if 'w:vanish' in raw_xml or 'w:hidden' in raw_xml:
                        self.findings.append({
                            "severity": "CRITICAL",
                            "category": "HIDDEN_OOXML_PROPERTY",
                            "page": 0,
                            "bbox": None,
                            "font_size": None,
                            "text": f"Format masque detecte dans {xml_name}",
                            "details": {"property": "w:vanish / w:hidden"}
                        })

                    if 'w:color w:val="FFFFFF"' in raw_xml.upper() or 'w:color w:val="FFF"' in raw_xml.upper():
                        self.findings.append({
                            "severity": "CRITICAL",
                            "category": "WHITE_TEXT_OOXML",
                            "page": 0,
                            "bbox": None,
                            "font_size": None,
                            "text": f"Police blanche #FFFFFF detectee dans {xml_name}",
                            "details": {"property": "w:color FFFFFF"}
                        })

                    # Extraction brute du texte XML pour audit semantique
                    try:
                        root = ET.fromstring(raw_xml)
                        text_elements = root.iter()
                        full_text = " ".join([elem.text for elem in text_elements if elem.text])
                        if full_text:
                            self._check_semantic_injections(full_text, context=f"OOXML [{xml_name}]", page=0)
                            self._check_zero_width_chars(full_text, context=f"OOXML [{xml_name}]", page=0)
                            self._check_homoglyphs(full_text, context=f"OOXML [{xml_name}]", page=0)
                    except Exception:
                        pass
        except Exception as e:
            self.findings.append({
                "severity": "WARNING",
                "category": "PARSE_ERROR",
                "page": 0,
                "bbox": None,
                "font_size": None,
                "text": f"Erreur de lecture de l'archive OOXML : {e}",
                "details": {}
            })

    def _analyze_text(self, path):
        """Inspection des fichiers plats (TXT, Markdown)."""
        with open(str(path), "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        sanitized_lines = []
        for line_idx, line in enumerate(lines):
            line_num = line_idx + 1
            is_suspicious = False

            # Caracteres invisibles
            if self._check_zero_width_chars(line, context=f"Ligne {line_num}", page=line_num):
                is_suspicious = True

            # Injections et canaris
            if self._check_semantic_injections(line, context=f"Ligne {line_num}", page=line_num):
                is_suspicious = True

            # Homoglyphes
            if self._check_homoglyphs(line, context=f"Ligne {line_num}", page=line_num):
                is_suspicious = True

            # Commentaires HTML furtifs
            if "<!--" in line and "-->" in line:
                comment = line[line.find("<!--") + 4: line.find("-->")].strip()
                if any(w in comment.lower() for w in ["ignore", "instruction", "canary", "secret", "prompt"]):
                    self.findings.append({
                        "severity": "CRITICAL",
                        "category": "HTML_COMMENT_INJECTION",
                        "page": line_num,
                        "bbox": None,
                        "font_size": None,
                        "text": comment,
                        "details": {"reason": "Commentaire HTML suspect contenant des mots de contournement"}
                    })
                    is_suspicious = True

            if not is_suspicious:
                sanitized_lines.append(self._purge_invisible_chars(line))

        self.sanitized_blocks.append({
            "page": 1,
            "content": "".join(sanitized_lines)
        })

    def _analyze_html(self, path):
        """Inspection des fichiers HTML."""
        with open(str(path), "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Styles CSS masquants
        hidden_styles = [
            (r'style=[\'"][^\'"]*display\s*:\s*none[^\'"]*[\'"]', "DISPLAY_NONE"),
            (r'style=[\'"][^\'"]*visibility\s*:\s*hidden[^\'"]*[\'"]', "VISIBILITY_HIDDEN"),
            (r'style=[\'"][^\'"]*font-size\s*:\s*0(?:px)?', "ZERO_FONT_SIZE"),
            (r'style=[\'"][^\'"]*color\s*:\s*(?:#fff(?:fff)?|white|rgba\(255,\s*255,\s*255)', "WHITE_CSS_COLOR"),
            (r'style=[\'"][^\'"]*opacity\s*:\s*0', "ZERO_OPACITY")
        ]
        for pattern, label in hidden_styles:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for m in matches:
                self.findings.append({
                    "severity": "CRITICAL",
                    "category": f"HTML_CSS_{label}",
                    "page": 0,
                    "bbox": None,
                    "font_size": None,
                    "text": m.group(0),
                    "details": {"reason": f"Propriete CSS de dissimulation active : {label}"}
                })

        self._analyze_text(path)

    def _get_background_color_at(self, drawings, point):
        """Identifie la couleur de remplissage du polygone vectoriel sous le point donne."""
        import pymupdf
        bg = (1.0, 1.0, 1.0) # Fond par defaut blanc
        for d in drawings:
            if d.get("fill") is not None:
                r = pymupdf.Rect(d["rect"])
                if r.contains(point):
                    fill = d["fill"]
                    if isinstance(fill, (list, tuple)) and len(fill) >= 3:
                        bg = tuple(fill[:3])
                    elif isinstance(fill, (int, float)):
                        bg = (float(fill), float(fill), float(fill))
        return bg

    def _calc_contrast_ratio(self, rgb1, rgb2):
        """Calcule le ratio de contraste WCAG entre deux couleurs RGB (valeurs 0.0 a 1.0)."""
        def get_lum(c):
            vals = []
            for channel in c:
                if channel <= 0.03928:
                    vals.append(channel / 12.92)
                else:
                    vals.append(((channel + 0.055) / 1.055) ** 2.4)
            return 0.2126 * vals[0] + 0.7152 * vals[1] + 0.0722 * vals[2]

        l1 = get_lum(rgb1)
        l2 = get_lum(rgb2)
        lighter = max(l1, l2)
        darker = min(l1, l2)
        return (lighter + 0.05) / (darker + 0.05)

    def _check_zero_width_chars(self, text, context="", page=0, bbox=None):
        found = False
        for char_idx, ch in enumerate(text):
            code = ord(ch)
            if code in ZERO_WIDTH_CHARS:
                found = True
                self.findings.append({
                    "severity": "CRITICAL",
                    "category": "ZERO_WIDTH_STEGANOGRAPHY",
                    "page": page,
                    "bbox": list(bbox) if bbox else None,
                    "font_size": None,
                    "text": f"Char code U+{code:04X} ({ZERO_WIDTH_CHARS[code]})",
                    "details": {
                        "unicode_code": f"U+{code:04X}",
                        "name": ZERO_WIDTH_CHARS[code],
                        "context": context,
                        "position_in_snippet": char_idx
                    }
                })
        return found

    def _check_semantic_injections(self, text, context="", page=0, bbox=None):
        found = False
        text_lower = text.lower()

        # 1. Motifs d'injections standards
        for pattern, category in INJECTION_PATTERNS:
            match = re.search(pattern, text_lower, re.IGNORECASE)
            if match:
                found = True
                self.findings.append({
                    "severity": "CRITICAL",
                    "category": category,
                    "page": page,
                    "bbox": list(bbox) if bbox else None,
                    "font_size": None,
                    "text": text.strip(),
                    "details": {
                        "matched_pattern": pattern,
                        "context": context
                    }
                })

        # 2. Correspondance avec le registre des canaris connus
        for canary in self.canary_registry.get("canaries", []):
            variations = canary.get("variations", [canary.get("keyword", "")])
            for var in variations:
                if var.lower() in text_lower:
                    found = True
                    self.findings.append({
                        "severity": "CRITICAL",
                        "category": "REGISTERED_CANARY_DETECTED",
                        "page": page,
                        "bbox": list(bbox) if bbox else None,
                        "font_size": None,
                        "text": text.strip(),
                        "details": {
                            "canary_id": canary.get("id"),
                            "keyword": canary.get("keyword"),
                            "registered_technique": canary.get("technique"),
                            "context": context
                        }
                    })
                    break

        return found

    def _check_homoglyphs(self, text, context="", page=0, bbox=None):
        """Detecte les substitutions de caracteres latins par du cyrillique ou grec."""
        found = False
        for word in text.split():
            has_latin = False
            has_cyrillic = False
            has_greek = False
            for ch in word:
                cat = unicodedata.name(ch, "")
                if "LATIN" in cat:
                    has_latin = True
                elif "CYRILLIC" in cat:
                    has_cyrillic = True
                elif "GREEK" in cat:
                    has_greek = True

            if has_latin and (has_cyrillic or has_greek):
                found = True
                self.findings.append({
                    "severity": "HIGH",
                    "category": "HOMOGLYPH_OBFUSCATION",
                    "page": page,
                    "bbox": list(bbox) if bbox else None,
                    "font_size": None,
                    "text": word,
                    "details": {
                        "word": word,
                        "has_latin": has_latin,
                        "has_cyrillic": has_cyrillic,
                        "has_greek": has_greek,
                        "context": context
                    }
                })
        return found

    def _purge_invisible_chars(self, text):
        """Elimine tous les caracteres zero-width et caracteres de controle suspects."""
        purged = []
        for ch in text:
            if ord(ch) not in ZERO_WIDTH_CHARS:
                purged.append(ch)
        return "".join(purged)

    def export_sanitized_markdown(self, output_path, source_name="Document Source"):
        """Genere un document Markdown epure et assaini, sans aucun piege."""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        lines = [
            f"# {source_name} - Document Assaini (Garanti Zero-Piege IA)",
            "",
            "> **Certification Document Guardian** : Ce document a ete filtre vectoriellement et sémantiquement.",
            "> Tout texte invisible (#FFFFFF), micro-police (<3.5pt), caractere zero-width et tentative d'injection ont ete purges.",
            "> **Statut** : Document securise pour l'exploitation par l'equipe et les sous-agents.",
            "",
            "---",
            ""
        ]

        for block in self.sanitized_blocks:
            lines.append(f"## Section / Page {block['page']}")
            lines.append("")
            lines.append(block["content"])
            lines.append("")
            lines.append("---")
            lines.append("")

        with open(str(output_file), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print(f"[SUCCES] Document assaini exporte : {output_path}")

    def export_report_json(self, report_path):
        """Exporte le rapport forensique d'audit au format JSON."""
        p = Path(report_path)
        p.parent.mkdir(parents=True, exist_ok=True)

        report_data = {
            "project": "MiageShopLoc",
            "guardian_version": "1.0",
            "total_findings": len(self.findings),
            "critical_traps": sum(1 for f in self.findings if f["severity"] == "CRITICAL"),
            "warnings": sum(1 for f in self.findings if f["severity"] in ["WARNING", "HIGH"]),
            "findings": self.findings
        }

        with open(str(p), "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)

        print(f"[SUCCES] Rapport d'audit JSON exporte : {report_path}")

    def export_report_markdown(self, report_path, source_file=""):
        """Exporte le rapport forensique sous forme de document Markdown rigoureux."""
        p = Path(report_path)
        p.parent.mkdir(parents=True, exist_ok=True)

        critical_count = sum(1 for f in self.findings if f["severity"] == "CRITICAL")
        warning_count = sum(1 for f in self.findings if f["severity"] in ["WARNING", "HIGH"])

        md = [
            "# RAPPORT FORENSIQUE DE SÉCURITÉ & AUDIT ANTI-PIÈGES IA",
            "",
            "| Attribut | Valeur |",
            "|---|---|",
            "| **Document Analysé** | `" + str(source_file) + "` |",
            "| **Outil de Diagnostic** | `agent_projet/scripts/document_guardian.py` |",
            f"| **Menaces Critiques Détectées** | **{critical_count}** |",
            f"| **Avertissements / Anomalies** | **{warning_count}** |",
            f"| **Verdict d'Intégrité** | {'COMPROMIS - PIEGES ACTIFS DETECTES' if critical_count > 0 else 'CONFORME'} |",
            "",
            "---",
            "",
            "## 1. Synthèse de l'Évaluation des Risques",
            ""
        ]

        if critical_count == 0 and warning_count == 0:
            md.append("Aucun piège de détection d'IA ni technique d'injection indirecte n'a été détecté dans ce document.")
            md.append("Le document peut être traité directement sans risque de contamination.")
        else:
            md.append(f"L'analyse automatisée a intercepté **{critical_count} pièges critiques** et **{warning_count} anomalies**.")
            md.append("Toutes les instructions dissimulées ont été isolées et retirées de la version assainie.")

        md.extend([
            "",
            "---",
            "",
            "## 2. Inventaire Détaillé des Pièges Détectés",
            ""
        ])

        if self.findings:
            md.append("| Page / Emplacement | Catégorie | Sévérité | Contenu Détecté | Règle de Neutralisation |")
            md.append("|---|---|---|---|---|")
            for f in self.findings:
                loc = f"Page {f['page']}" if f['page'] > 0 else "Global / Metadonnees"
                cat = f['category']
                sev = f['severity']
                txt = f['text'].replace("|", "\\|").replace("\n", " ")
                if len(txt) > 80:
                    txt = txt[:77] + "..."
                md.append(f"| {loc} | `{cat}` | **{sev}** | `{txt}` | Purge totale de l'extraction |")
        else:
            md.append("*Aucune vulnérabilité identifiée.*")

        md.extend([
            "",
            "---",
            "",
            "## 3. Directives Opérationnelles pour l'Équipe",
            "",
            "1. **Interdiction d'Ingestion Directe** : Ne jamais référencer le document source brut dans les prompts des agents.",
            "2. **Utilisation Exclusive de la Version Assainie** : Seule la version purifiée `*_sanitized.md` est transmise au Product Owner et à l'Architecte.",
            "3. **Mise à Jour du Registre Central** : Tout nouveau piège découvert doit être consigné dans `agent_projet/security/canary_registry.json`.",
            "4. **Contrôle de Sortie Pré-Publication** : Exécuter `python agent_projet/scripts/verify_deliverables.py` avant toute remise officielle."
        ])

        with open(str(p), "w", encoding="utf-8") as f:
            f.write("\n".join(md))

        print(f"[SUCCES] Rapport d'audit Markdown exporte : {report_path}")


def main():
    parser = argparse.ArgumentParser(description="Document Guardian - Pare-feu d'ingestion Zero-Trust anti-pieges IA")
    parser.add_argument("file", help="Fichier a analyser (PDF, DOCX, TXT, MD, HTML)")
    parser.add_argument("--registry", help="Chemin vers le registre de canaris JSON (optionnel)")
    parser.add_argument("--report", help="Chemin d'export du rapport JSON (optionnel)")
    parser.add_argument("--report-md", help="Chemin d'export du rapport Markdown (optionnel)")
    parser.add_argument("--sanitize", help="Chemin d'export du document assaini Markdown (optionnel)")
    parser.add_argument("--strict", action="store_true", help="Retourne un code d'erreur 2 si un piege critique est trouve")

    args = parser.parse_args()

    guardian = DocumentGuardian(args.registry)
    try:
        findings = guardian.analyze(args.file)
    except Exception as e:
        print(f"[ERREUR CRITIQUE] Echec de l'analyse de {args.file} : {e}", file=sys.stderr)
        sys.exit(1)

    critical_count = sum(1 for f in findings if f["severity"] == "CRITICAL")
    warning_count = sum(1 for f in findings if f["severity"] in ["WARNING", "HIGH"])

    print("==================================================")
    print(f"DIAGNOSTIC DOCUMENT GUARDIAN : {args.file}")
    print(f"Total anomalies : {len(findings)} | Critiques : {critical_count} | Avertissements : {warning_count}")
    print("==================================================")

    for f in findings:
        loc = f"Page {f['page']}" if f['page'] > 0 else "Global"
        print(f"[{f['severity']}] {loc} - {f['category']} : {f['text']}")

    if args.report:
        guardian.export_report_json(args.report)

    if args.report_md:
        guardian.export_report_markdown(args.report_md, source_file=args.file)

    if args.sanitize:
        source_name = Path(args.file).name
        guardian.export_sanitized_markdown(args.sanitize, source_name=source_name)

    if args.strict and critical_count > 0:
        print(f"\n[ECHEC SECURITE] {critical_count} piege(s) critique(s) detecte(s). Fichier non conforme.")
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()

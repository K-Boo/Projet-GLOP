#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess

BROWSER = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

COMMON_DEFS = """
    <defs>
      <filter id="shadow-soft" x="-8%" y="-8%" width="120%" height="120%">
        <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#243342" flood-opacity="0.06"/>
      </filter>
      <marker id="arrow-slate" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#243342" />
      </marker>
      <marker id="arrow-terracotta" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#C26750" />
      </marker>
      <marker id="arrow-sage" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#4A7A5B" />
      </marker>
      <marker id="arrow-honey" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#C48B28" />
      </marker>
      <marker id="arrow-plum" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#6E3946" />
      </marker>
      <marker id="arrow-red" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#B91C1C" />
      </marker>
    </defs>
"""

# -------------------------------------------------------------
# SVG 1 : P1 CONVENTIONNEMENT
# -------------------------------------------------------------
SVG_P1 = f"""<svg viewBox="0 0 1020 540" width="100%" height="auto" style="overflow:visible; font-family:'Poppins', sans-serif;">
{COMMON_DEFS}
  <!-- COULOIR 1 : COMMERCANT CANDIDAT -->
  <rect x="30" y="20" width="960" height="115" fill="#FFF7ED" fill-opacity="0.6" stroke="#FDBA74" stroke-width="1.2" rx="6" />
  <rect x="30" y="20" width="150" height="115" fill="#EA580C" rx="6" />
  <text x="105" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">COMMERCANT</text>
  <text x="105" y="93" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Artisan / Boutique)</text>

  <!-- COULOIR 2 : ASSOCIATION DES COMMERCANTS -->
  <rect x="30" y="145" width="960" height="120" fill="#F0FDF4" fill-opacity="0.6" stroke="#86EFAC" stroke-width="1.2" rx="6" />
  <rect x="30" y="145" width="150" height="120" fill="#16A34A" rx="6" />
  <text x="105" y="200" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">ASSOCIATION</text>
  <text x="105" y="218" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Loi 1901 locale)</text>

  <!-- COULOIR 3 : SHOPLOC ENGINE -->
  <rect x="30" y="275" width="960" height="120" fill="#F0F9FF" fill-opacity="0.6" stroke="#BAE6FD" stroke-width="1.2" rx="6" />
  <rect x="30" y="275" width="150" height="120" fill="#0284C7" rx="6" />
  <text x="105" y="330" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">SHOPLOC CORE</text>
  <text x="105" y="348" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(SaaS Multi-tenant)</text>

  <!-- COULOIR 4 : MAIRIE DE LILLE -->
  <rect x="30" y="405" width="960" height="115" fill="#FEFCE8" fill-opacity="0.6" stroke="#FDE047" stroke-width="1.2" rx="6" />
  <rect x="30" y="405" width="150" height="115" fill="#CA8A04" rx="6" />
  <text x="105" y="460" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">VILLE DE LILLE</text>
  <text x="105" y="478" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(DSI &amp; Commerce)</text>

  <!-- DEBUT -->
  <circle cx="210" cy="77" r="14" fill="#FFFFFF" stroke="#16A34A" stroke-width="2.5" filter="url(#shadow-soft)" />
  <polygon points="207,71 217,77 207,83" fill="#16A34A" />

  <!-- T1 : Commercant depose dossier -->
  <g filter="url(#shadow-soft)">
    <rect x="245" y="48" width="125" height="58" rx="7" fill="#FFFFFF" stroke="#EA580C" stroke-width="1.4" />
    <text x="307" y="66" text-anchor="middle" font-size="8" font-weight="700" fill="#EA580C" text-transform="uppercase">FORMULAIRE</text>
    <text x="307" y="82" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Deposer dossier</text>
    <text x="307" y="96" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Kbis, RIB &amp; catalogue</text>
  </g>
  <line x1="224" y1="77" x2="245" y2="77" stroke="#243342" stroke-width="1.8" marker-end="url(#arrow-slate)" />

  <!-- Message T1 -> Association T2 -->
  <path d="M 307 106 L 307 175" fill="none" stroke="#243342" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-slate)" />

  <!-- T2 : Association instruit -->
  <g filter="url(#shadow-soft)">
    <rect x="245" y="175" width="125" height="58" rx="7" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.4" />
    <text x="307" y="193" text-anchor="middle" font-size="8" font-weight="700" fill="#16A34A" text-transform="uppercase">INSTRUCTION</text>
    <text x="307" y="209" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Verifier eligibilite</text>
    <text x="307" y="223" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Commerce local</text>
  </g>

  <!-- Passerelle XOR Association -->
  <polygon points="415,204 430,189 445,204 430,219" fill="#FFFFFF" stroke="#243342" stroke-width="1.8" filter="url(#shadow-soft)" />
  <text x="430" y="208" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">x</text>
  <line x1="370" y1="204" x2="415" y2="204" stroke="#243342" stroke-width="1.8" marker-end="url(#arrow-slate)" />

  <!-- Branche Refus (vers le haut) -->
  <path d="M 430 189 L 430 77 L 465 77" fill="none" stroke="#B91C1C" stroke-width="1.6" marker-end="url(#arrow-red)" />
  <text x="440" y="145" font-size="8.5" font-weight="700" fill="#B91C1C">[Rejete]</text>

  <!-- T3 : Notification Refus -->
  <g filter="url(#shadow-soft)">
    <rect x="465" y="48" width="120" height="58" rx="7" fill="#FFFFFF" stroke="#B91C1C" stroke-width="1.4" />
    <text x="525" y="66" text-anchor="middle" font-size="8" font-weight="700" fill="#B91C1C" text-transform="uppercase">ANOMALIE</text>
    <text x="525" y="82" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Notifier refus</text>
    <text x="525" y="96" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Motif ineligibilite</text>
  </g>
  <!-- Fin anomalie -->
  <circle cx="615" cy="77" r="12" fill="#FFFFFF" stroke="#B91C1C" stroke-width="2.5" />
  <circle cx="615" cy="77" r="7" fill="#B91C1C" />
  <line x1="585" y1="77" x2="603" y2="77" stroke="#B91C1C" stroke-width="1.6" marker-end="url(#arrow-red)" />

  <!-- Branche Accord (vers la droite) -->
  <line x1="445" y1="204" x2="480" y2="204" stroke="#16A34A" stroke-width="1.8" marker-end="url(#arrow-sage)" />
  <text x="447" y="198" font-size="8.5" font-weight="700" fill="#16A34A">[Valide]</text>

  <!-- T4 : Signature Convention Tripartite -->
  <g filter="url(#shadow-soft)">
    <rect x="480" y="175" width="130" height="58" rx="7" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.4" />
    <text x="545" y="193" text-anchor="middle" font-size="8" font-weight="700" fill="#16A34A" text-transform="uppercase">CONVENTION</text>
    <text x="545" y="209" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Signer convention</text>
    <text x="545" y="223" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Adhesion tripartite</text>
  </g>

  <!-- Message vers Mairie T5 -->
  <path d="M 545 233 L 545 435" fill="none" stroke="#243342" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-slate)" />

  <!-- T5 : Mairie valide subvention -->
  <g filter="url(#shadow-soft)">
    <rect x="480" y="435" width="130" height="58" rx="7" fill="#FFFFFF" stroke="#CA8A04" stroke-width="1.4" />
    <text x="545" y="453" text-anchor="middle" font-size="8" font-weight="700" fill="#CA8A04" text-transform="uppercase">COLLECTIVITE</text>
    <text x="545" y="469" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Valider perimetre</text>
    <text x="545" y="483" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Subvention R3</text>
  </g>

  <!-- Message Mairie -> ShopLoc T6 -->
  <path d="M 610 464 L 665 464 L 665 334 L 685 334" fill="none" stroke="#0284C7" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-slate)" />

  <!-- T6 : ShopLoc provisionne tenant -->
  <g filter="url(#shadow-soft)">
    <rect x="685" y="305" width="135" height="58" rx="7" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.4" />
    <text x="752" y="323" text-anchor="middle" font-size="8" font-weight="700" fill="#0284C7" text-transform="uppercase">PROVISIONING</text>
    <text x="752" y="339" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Creer tenant &amp; POS</text>
    <text x="752" y="353" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Cles API &amp; catalogue</text>
  </g>

  <!-- Message ShopLoc -> Commercant T7 -->
  <path d="M 752 305 L 752 106" fill="none" stroke="#EA580C" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-terracotta)" />

  <!-- T7 : Commercant active caisse -->
  <g filter="url(#shadow-soft)">
    <rect x="690" y="48" width="130" height="58" rx="7" fill="#FFFFFF" stroke="#EA580C" stroke-width="1.4" />
    <text x="755" y="66" text-anchor="middle" font-size="8" font-weight="700" fill="#EA580C" text-transform="uppercase">ACTIVATION</text>
    <text x="755" y="82" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Activer caisse tactile</text>
    <text x="755" y="96" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Boutique live (0%)</text>
  </g>

  <!-- Fin nominale -->
  <circle cx="875" cy="77" r="14" fill="#FFFFFF" stroke="#16A34A" stroke-width="2.5" filter="url(#shadow-soft)" />
  <circle cx="875" cy="77" r="9" fill="#16A34A" />
  <line x1="820" y1="77" x2="861" y2="77" stroke="#16A34A" stroke-width="1.8" marker-end="url(#arrow-sage)" />
  <text x="875" y="105" text-anchor="middle" font-size="9" font-weight="600" fill="#16A34A">Adherent actif</text>
</svg>"""

# -------------------------------------------------------------
# SVG 2 : P2 COMMANDE C&C & RETRAIT 2PC
# -------------------------------------------------------------
SVG_P2 = f"""<svg viewBox="0 0 1020 540" width="100%" height="auto" style="overflow:visible; font-family:'Poppins', sans-serif;">
{COMMON_DEFS}
  <!-- COULOIR 1 : CITOYEN USAGER -->
  <rect x="30" y="20" width="960" height="115" fill="#FFF1F2" fill-opacity="0.6" stroke="#FECDD3" stroke-width="1.2" rx="6" />
  <rect x="30" y="20" width="150" height="115" fill="#E11D48" rx="6" />
  <text x="105" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">CITOYEN</text>
  <text x="105" y="93" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Julie &amp; Arthur / Pierre)</text>

  <!-- COULOIR 2 : SHOPLOC TRANSACTION MANAGER -->
  <rect x="30" y="145" width="960" height="125" fill="#F0F9FF" fill-opacity="0.6" stroke="#BAE6FD" stroke-width="1.2" rx="6" />
  <rect x="30" y="145" width="150" height="125" fill="#0284C7" rx="6" />
  <text x="105" y="200" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">SHOPLOC 2PC</text>
  <text x="105" y="218" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Orchestrateur Panier)</text>

  <!-- COULOIR 3 : COMMERCANTS PARTENAIRES -->
  <rect x="30" y="280" width="960" height="120" fill="#F0FDF4" fill-opacity="0.6" stroke="#86EFAC" stroke-width="1.2" rx="6" />
  <rect x="30" y="280" width="150" height="120" fill="#16A34A" rx="6" />
  <text x="105" y="335" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">COMMERCANTS</text>
  <text x="105" y="353" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Suzanne, Boulangerie...)</text>

  <!-- COULOIR 4 : SYSTEME BANCAIRE & CLEARING -->
  <rect x="30" y="410" width="960" height="110" fill="#FAF5FF" fill-opacity="0.6" stroke="#E9D5FF" stroke-width="1.2" rx="6" />
  <rect x="30" y="410" width="150" height="110" fill="#9333EA" rx="6" />
  <text x="105" y="460" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">BANQUE SEPA</text>
  <text x="105" y="478" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Clearing 0% Stripe Mock)</text>

  <!-- DEBUT -->
  <circle cx="205" cy="77" r="14" fill="#FFFFFF" stroke="#16A34A" stroke-width="2.5" filter="url(#shadow-soft)" />
  <polygon points="202,71 212,77 202,83" fill="#16A34A" />

  <!-- T1 : Citoyen valide panier mutualise -->
  <g filter="url(#shadow-soft)">
    <rect x="235" y="48" width="125" height="58" rx="7" fill="#FFFFFF" stroke="#E11D48" stroke-width="1.4" />
    <text x="297" y="66" text-anchor="middle" font-size="8" font-weight="700" fill="#E11D48" text-transform="uppercase">CLICK &amp; COLLECT</text>
    <text x="297" y="82" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Valider panier</text>
    <text x="297" y="96" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Multi-boutiques</text>
  </g>
  <line x1="219" y1="77" x2="235" y2="77" stroke="#243342" stroke-width="1.8" marker-end="url(#arrow-slate)" />

  <!-- Message T1 -> ShopLoc Phase 1 -->
  <path d="M 297 106 L 297 175" fill="none" stroke="#243342" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-slate)" />

  <!-- T2 : 2PC Phase 1 Prepare -->
  <g filter="url(#shadow-soft)">
    <rect x="235" y="175" width="130" height="60" rx="7" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.4" />
    <text x="300" y="193" text-anchor="middle" font-size="8" font-weight="700" fill="#0284C7" text-transform="uppercase">PHASE 1 : PREPARE</text>
    <text x="300" y="209" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Verrouiller stocks</text>
    <text x="300" y="223" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Appels concurrents</text>
  </g>

  <!-- Message vers Commercants -->
  <path d="M 300 235 L 300 310 L 390 310" fill="none" stroke="#0284C7" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-slate)" />

  <!-- T3 : Commercant confirme dispo -->
  <g filter="url(#shadow-soft)">
    <rect x="390" y="310" width="125" height="58" rx="7" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.4" />
    <text x="452" y="328" text-anchor="middle" font-size="8" font-weight="700" fill="#16A34A" text-transform="uppercase">INVENTAIRE</text>
    <text x="452" y="344" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Confirmer stock</text>
    <text x="452" y="358" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Reservation active</text>
  </g>

  <!-- Message retour vers ShopLoc XOR -->
  <path d="M 452 310 L 452 235 L 485 205" fill="none" stroke="#243342" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-slate)" />

  <!-- Passerelle XOR Consensus 2PC -->
  <polygon points="505,205 520,190 535,205 520,220" fill="#FFFFFF" stroke="#243342" stroke-width="1.8" filter="url(#shadow-soft)" />
  <text x="520" y="209" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">x</text>

  <!-- Branche Rupture -->
  <path d="M 520 190 L 520 106" fill="none" stroke="#B91C1C" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-red)" />
  <text x="525" y="150" font-size="8.5" font-weight="700" fill="#B91C1C">[Rupture]</text>

  <!-- Branche 2PC Phase 2 Commit -->
  <line x1="535" y1="205" x2="560" y2="205" stroke="#16A34A" stroke-width="1.8" marker-end="url(#arrow-sage)" />
  <text x="536" y="198" font-size="8.5" font-weight="700" fill="#16A34A">[100% OK]</text>

  <!-- T4 : 2PC Phase 2 Commit -->
  <g filter="url(#shadow-soft)">
    <rect x="560" y="175" width="130" height="60" rx="7" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.4" />
    <text x="625" y="193" text-anchor="middle" font-size="8" font-weight="700" fill="#0284C7" text-transform="uppercase">PHASE 2 : COMMIT</text>
    <text x="625" y="209" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Valider commande</text>
    <text x="625" y="223" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Ordre de prelevement</text>
  </g>

  <!-- Message vers Banque T5 -->
  <path d="M 625 235 L 625 435" fill="none" stroke="#9333EA" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-slate)" />

  <!-- T5 : Banque capture debit unique -->
  <g filter="url(#shadow-soft)">
    <rect x="560" y="435" width="130" height="58" rx="7" fill="#FFFFFF" stroke="#9333EA" stroke-width="1.4" />
    <text x="625" y="453" text-anchor="middle" font-size="8" font-weight="700" fill="#9333EA" text-transform="uppercase">PAIEMENT UNIQUE</text>
    <text x="625" y="469" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Debiter citoyen</text>
    <text x="625" y="483" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Preuve SEPA</text>
  </g>

  <!-- Message Banque -> Commercant T6 -->
  <path d="M 690 464 L 720 464 L 720 340 L 735 340" fill="none" stroke="#16A34A" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-slate)" />

  <!-- T6 : Commercant prepare sachet -->
  <g filter="url(#shadow-soft)">
    <rect x="735" y="310" width="125" height="58" rx="7" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.4" />
    <text x="797" y="328" text-anchor="middle" font-size="8" font-weight="700" fill="#16A34A" text-transform="uppercase">PREPARATION</text>
    <text x="797" y="344" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Preparer sachet</text>
    <text x="797" y="358" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">En attente retrait</text>
  </g>

  <!-- Message notification vers Citoyen T7 -->
  <path d="M 797 310 L 797 106" fill="none" stroke="#E11D48" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-terracotta)" />

  <!-- T7 : Citoyen recupere en boutique -->
  <g filter="url(#shadow-soft)">
    <rect x="735" y="48" width="125" height="58" rx="7" fill="#FFFFFF" stroke="#E11D48" stroke-width="1.4" />
    <text x="797" y="66" text-anchor="middle" font-size="8" font-weight="700" fill="#E11D48" text-transform="uppercase">RETRAIT PEDESTRE</text>
    <text x="797" y="82" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Presenter pass QR</text>
    <text x="797" y="96" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Scan caisse &lt; 3s</text>
  </g>

  <!-- Message final de cloture vers ShopLoc -->
  <path d="M 860 77 L 885 77 L 885 185" fill="none" stroke="#243342" stroke-width="1.6" marker-end="url(#arrow-slate)" />

  <!-- T8 : ShopLoc solde & libere fonds -->
  <g filter="url(#shadow-soft)">
    <rect x="830" y="185" width="115" height="58" rx="7" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.4" />
    <text x="887" y="203" text-anchor="middle" font-size="8" font-weight="700" fill="#0284C7" text-transform="uppercase">CLEARING</text>
    <text x="887" y="219" text-anchor="middle" font-size="9.5" font-weight="600" fill="#243342">Virer fonds 0%</text>
    <text x="887" y="233" text-anchor="middle" font-size="8" font-weight="400" fill="#5A6578">Sans commission</text>
  </g>

  <!-- Fin nominale -->
  <circle cx="975" cy="214" r="14" fill="#FFFFFF" stroke="#16A34A" stroke-width="2.5" filter="url(#shadow-soft)" />
  <circle cx="975" cy="214" r="9" fill="#16A34A" />
  <line x1="945" y1="214" x2="961" y2="214" stroke="#16A34A" stroke-width="1.8" marker-end="url(#arrow-sage)" />
  <text x="975" y="242" text-anchor="middle" font-size="8.5" font-weight="600" fill="#16A34A">Solde</text>
</svg>"""

# -------------------------------------------------------------
# SVG 3 : P3 PASSAGE EN CAISSE & MOTEUR FIDELITE
# -------------------------------------------------------------
SVG_P3 = f"""<svg viewBox="0 0 1020 530" width="100%" height="auto" style="overflow:visible; font-family:'Poppins', sans-serif;">
{COMMON_DEFS}
  <!-- COULOIR 1 : CITOYEN PRESENTIEL -->
  <rect x="30" y="20" width="960" height="125" fill="#FFF1F2" fill-opacity="0.6" stroke="#FECDD3" stroke-width="1.2" rx="6" />
  <rect x="30" y="20" width="150" height="125" fill="#E11D48" rx="6" />
  <text x="105" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">CITOYEN</text>
  <text x="105" y="93" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Pierre Dupont, 74 ans)</text>

  <!-- COULOIR 2 : COMMERCANTE EN CAISSE -->
  <rect x="30" y="155" width="960" height="135" fill="#F0FDF4" fill-opacity="0.6" stroke="#86EFAC" stroke-width="1.2" rx="6" />
  <rect x="30" y="155" width="150" height="135" fill="#16A34A" rx="6" />
  <text x="105" y="215" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">COMMERCANTE</text>
  <text x="105" y="233" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Suzanne, POS tactile)</text>

  <!-- COULOIR 3 : SHOPLOC ENGINE DOUBLE MOTEUR -->
  <rect x="30" y="300" width="960" height="205" fill="#F0F9FF" fill-opacity="0.6" stroke="#BAE6FD" stroke-width="1.2" rx="6" />
  <rect x="30" y="300" width="150" height="205" fill="#0284C7" rx="6" />
  <text x="105" y="390" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">SHOPLOC ENGINE</text>
  <text x="105" y="408" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Moteur Decouple ADR-005)</text>

  <!-- DEBUT -->
  <circle cx="205" cy="82" r="14" fill="#FFFFFF" stroke="#16A34A" stroke-width="2.5" filter="url(#shadow-soft)" />
  <polygon points="202,76 212,82 202,88" fill="#16A34A" />

  <!-- T1 : Citoyen presente pass papier / NFC -->
  <g filter="url(#shadow-soft)">
    <rect x="235" y="53" width="130" height="58" rx="7" fill="#FFFFFF" stroke="#E11D48" stroke-width="1.4" />
    <text x="300" y="71" text-anchor="middle" font-size="8" font-weight="700" fill="#E11D48" text-transform="uppercase">ACHAT EN BOUTIQUE</text>
    <text x="300" y="87" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Presenter pass</text>
    <text x="300" y="101" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Carte papier QR ou NFC</text>
  </g>
  <line x1="219" y1="82" x2="235" y2="82" stroke="#243342" stroke-width="1.8" marker-end="url(#arrow-slate)" />

  <!-- Interaction physique vers Suzanne en caisse -->
  <path d="M 300 111 L 300 190" fill="none" stroke="#243342" stroke-width="1.8" marker-end="url(#arrow-slate)" />

  <!-- T2 : Suzanne scanne POS express -->
  <g filter="url(#shadow-soft)">
    <rect x="235" y="190" width="130" height="62" rx="7" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.4" />
    <text x="300" y="208" text-anchor="middle" font-size="8" font-weight="700" fill="#16A34A" text-transform="uppercase">SCAN RAPIDE &lt; 3S</text>
    <text x="300" y="225" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Scanner le pass</text>
    <text x="300" y="239" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Validation sans blocage</text>
  </g>

  <!-- Message vers ShopLoc Engine -->
  <path d="M 300 252 L 300 335" fill="none" stroke="#0284C7" stroke-width="1.8" stroke-dasharray="4,3" marker-end="url(#arrow-slate)" />

  <!-- T3 : ShopLoc dispatch split -->
  <g filter="url(#shadow-soft)">
    <rect x="235" y="335" width="135" height="60" rx="7" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.4" />
    <text x="302" y="353" text-anchor="middle" font-size="8" font-weight="700" fill="#0284C7" text-transform="uppercase">DISPATCH ASYNCHRONE</text>
    <text x="302" y="369" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Enregistrer passage</text>
    <text x="302" y="383" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Horodatage &amp; montant</text>
  </g>

  <!-- FORK PARALLELE (2 SYSTEMES DECOUPLES ADR-005) -->
  <path d="M 370 365 L 415 340" fill="none" stroke="#243342" stroke-width="1.6" marker-end="url(#arrow-slate)" />
  <path d="M 370 365 L 415 440" fill="none" stroke="#243342" stroke-width="1.6" marker-end="url(#arrow-slate)" />

  <!-- BRANCHE HAUTE : FIDELITE MARCHANDE -->
  <g filter="url(#shadow-soft)">
    <rect x="415" y="315" width="160" height="56" rx="7" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.4" />
    <text x="495" y="333" text-anchor="middle" font-size="8" font-weight="700" fill="#16A34A" text-transform="uppercase">SYSTEME 1 : MARCHAND</text>
    <text x="495" y="348" text-anchor="middle" font-size="9.5" font-weight="600" fill="#243342">Crediter points boutique</text>
    <text x="495" y="361" text-anchor="middle" font-size="8" font-weight="400" fill="#5A6578">Bareme autonome (exp. 1 an)</text>
  </g>

  <!-- BRANCHE BASSE : FIDELITE CITOYENNE VFP -->
  <g filter="url(#shadow-soft)">
    <rect x="415" y="415" width="160" height="56" rx="7" fill="#FFFFFF" stroke="#CA8A04" stroke-width="1.4" />
    <text x="495" y="433" text-anchor="middle" font-size="8" font-weight="700" fill="#CA8A04" text-transform="uppercase">SYSTEME 2 : CITOYEN VFP</text>
    <text x="495" y="448" text-anchor="middle" font-size="9.5" font-weight="600" fill="#243342">Calculer fenetre 15j</text>
    <text x="495" y="461" text-anchor="middle" font-size="8" font-weight="400" fill="#5A6578">Requete glissante SQL</text>
  </g>

  <!-- Passerelle XOR VFP -->
  <polygon points="615,443 630,428 645,443 630,458" fill="#FFFFFF" stroke="#243342" stroke-width="1.8" filter="url(#shadow-soft)" />
  <text x="630" y="447" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">x</text>
  <line x1="575" y1="443" x2="615" y2="443" stroke="#243342" stroke-width="1.8" marker-end="url(#arrow-slate)" />

  <!-- Branche >= 10 passages -->
  <line x1="645" y1="443" x2="680" y2="443" stroke="#16A34A" stroke-width="1.8" marker-end="url(#arrow-sage)" />
  <text x="646" y="437" font-size="8" font-weight="700" fill="#16A34A">[&gt;= 10 passages]</text>

  <!-- T4a : Activation VFP & Voucher -->
  <g filter="url(#shadow-soft)">
    <rect x="680" y="415" width="150" height="56" rx="7" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.4" />
    <text x="755" y="433" text-anchor="middle" font-size="8" font-weight="700" fill="#16A34A" text-transform="uppercase">STATUT DEBLOQUE</text>
    <text x="755" y="448" text-anchor="middle" font-size="9.5" font-weight="600" fill="#243342">Activer statut VFP</text>
    <text x="755" y="461" text-anchor="middle" font-size="8" font-weight="400" fill="#5A6578">Droit mobilite J+1 emis</text>
  </g>

  <!-- Branche < 10 passages -->
  <path d="M 630 428 L 630 380 L 680 380" fill="none" stroke="#5A6578" stroke-width="1.6" marker-end="url(#arrow-slate)" />
  <text x="635" y="395" font-size="8" font-weight="700" fill="#5A6578">[&lt; 10 passages]</text>

  <!-- T4b : MAJ jauge restante -->
  <g filter="url(#shadow-soft)">
    <rect x="680" y="355" width="150" height="50" rx="7" fill="#FFFFFF" stroke="#5A6578" stroke-width="1.2" />
    <text x="755" y="375" text-anchor="middle" font-size="9" font-weight="600" fill="#243342">Mettre a jour jauge</text>
    <text x="755" y="390" text-anchor="middle" font-size="8" font-weight="400" fill="#5A6578">Notifier passages restants</text>
  </g>

  <!-- Message vers ecran de caisse Suzanne -->
  <path d="M 830 443 L 860 443 L 860 252" fill="none" stroke="#16A34A" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-sage)" />

  <!-- T5 : Suzanne confirme et felicite -->
  <g filter="url(#shadow-soft)">
    <rect x="800" y="190" width="125" height="62" rx="7" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.4" />
    <text x="862" y="208" text-anchor="middle" font-size="8" font-weight="700" fill="#16A34A" text-transform="uppercase">ECRAN CAISSE</text>
    <text x="862" y="225" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Badge VFP vert</text>
    <text x="862" y="239" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Feliciter le client</text>
  </g>

  <!-- Interaction vers Pierre -->
  <path d="M 862 190 L 862 111" fill="none" stroke="#E11D48" stroke-width="1.8" marker-end="url(#arrow-terracotta)" />

  <!-- T6 : Pierre prend ticket et beneficie -->
  <g filter="url(#shadow-soft)">
    <rect x="800" y="53" width="125" height="58" rx="7" fill="#FFFFFF" stroke="#E11D48" stroke-width="1.4" />
    <text x="862" y="71" text-anchor="middle" font-size="8" font-weight="700" fill="#E11D48" text-transform="uppercase">RECONNAISSANCE</text>
    <text x="862" y="87" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Ticket remis</text>
    <text x="862" y="101" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Droit bus debloque</text>
  </g>

  <!-- Fin nominale -->
  <circle cx="965" cy="82" r="14" fill="#FFFFFF" stroke="#16A34A" stroke-width="2.5" filter="url(#shadow-soft)" />
  <circle cx="965" cy="82" r="9" fill="#16A34A" />
  <line x1="925" y1="82" x2="951" y2="82" stroke="#16A34A" stroke-width="1.8" marker-end="url(#arrow-sage)" />
  <text x="965" y="108" text-anchor="middle" font-size="8.5" font-weight="600" fill="#16A34A">Fidelite MAJ</text>
</svg>"""

# -------------------------------------------------------------
# SVG 4 : P4 CONVERSION MOBILITE URBAINE
# -------------------------------------------------------------
SVG_P4 = f"""<svg viewBox="0 0 1020 540" width="100%" height="auto" style="overflow:visible; font-family:'Poppins', sans-serif;">
{COMMON_DEFS}
  <!-- COULOIR 1 : CITOYEN BENEFICIAIRE -->
  <rect x="30" y="20" width="960" height="115" fill="#FFF1F2" fill-opacity="0.6" stroke="#FECDD3" stroke-width="1.2" rx="6" />
  <rect x="30" y="20" width="150" height="115" fill="#E11D48" rx="6" />
  <text x="105" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">CITOYEN VFP</text>
  <text x="105" y="93" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Arthur / Pierre)</text>

  <!-- COULOIR 2 : SHOPLOC MODULE MOBILITE -->
  <rect x="30" y="145" width="960" height="120" fill="#F0F9FF" fill-opacity="0.6" stroke="#BAE6FD" stroke-width="1.2" rx="6" />
  <rect x="30" y="145" width="150" height="120" fill="#0284C7" rx="6" />
  <text x="105" y="200" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">SHOPLOC CORE</text>
  <text x="105" y="218" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Controle des Quotas)</text>

  <!-- COULOIR 3 : APIS EXTERNES MOBILITE (MOCKS) -->
  <rect x="30" y="275" width="960" height="125" fill="#FAF5FF" fill-opacity="0.6" stroke="#E9D5FF" stroke-width="1.2" rx="6" />
  <rect x="30" y="275" width="150" height="125" fill="#9333EA" rx="6" />
  <text x="105" y="330" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">SERVICES MOBILITE</text>
  <text x="105" y="348" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Ilevia Bus &amp; Voirie Mock)</text>

  <!-- COULOIR 4 : MAIRIE DE LILLE -->
  <rect x="30" y="410" width="960" height="110" fill="#FEFCE8" fill-opacity="0.6" stroke="#FDE047" stroke-width="1.2" rx="6" />
  <rect x="30" y="410" width="150" height="110" fill="#CA8A04" rx="6" />
  <text x="105" y="460" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">VILLE DE LILLE</text>
  <text x="105" y="478" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Clearing Subvention)</text>

  <!-- DEBUT -->
  <circle cx="205" cy="77" r="14" fill="#FFFFFF" stroke="#16A34A" stroke-width="2.5" filter="url(#shadow-soft)" />
  <polygon points="202,71 212,77 202,83" fill="#16A34A" />

  <!-- T1 : Citoyen choisit avantage -->
  <g filter="url(#shadow-soft)">
    <rect x="235" y="48" width="125" height="58" rx="7" fill="#FFFFFF" stroke="#E11D48" stroke-width="1.4" />
    <text x="297" y="66" text-anchor="middle" font-size="8" font-weight="700" fill="#E11D48" text-transform="uppercase">CHOIX DU JOUR</text>
    <text x="297" y="82" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Choisir avantage</text>
    <text x="297" y="96" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Parking ou Bus</text>
  </g>
  <line x1="219" y1="77" x2="235" y2="77" stroke="#243342" stroke-width="1.8" marker-end="url(#arrow-slate)" />

  <!-- Passerelle XOR de selection -->
  <polygon points="385,77 400,62 415,77 400,92" fill="#FFFFFF" stroke="#243342" stroke-width="1.8" filter="url(#shadow-soft)" />
  <text x="400" y="81" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">x</text>
  <line x1="360" y1="77" x2="385" y2="77" stroke="#243342" stroke-width="1.8" marker-end="url(#arrow-slate)" />

  <!-- Branche Parking (Haut) -->
  <path d="M 400 62 L 400 45 L 435 45" fill="none" stroke="#243342" stroke-width="1.6" marker-end="url(#arrow-slate)" />
  <text x="405" y="38" font-size="8" font-weight="700" fill="#243342">[Parking]</text>

  <!-- T2a : Saisir plaque (Arthur) -->
  <g filter="url(#shadow-soft)">
    <rect x="435" y="27" width="135" height="42" rx="6" fill="#FFFFFF" stroke="#E11D48" stroke-width="1.2" />
    <text x="502" y="44" text-anchor="middle" font-size="9.5" font-weight="600" fill="#243342">Plaque auto (Arthur)</text>
    <text x="502" y="58" text-anchor="middle" font-size="8" font-weight="400" fill="#5A6578">20 min de voirie</text>
  </g>

  <!-- Branche Bus (Bas) -->
  <path d="M 400 92 L 400 108 L 435 108" fill="none" stroke="#243342" stroke-width="1.6" marker-end="url(#arrow-slate)" />
  <text x="405" y="104" font-size="8" font-weight="700" fill="#243342">[Bus]</text>

  <!-- T2b : Selection ticket bus (Pierre) -->
  <g filter="url(#shadow-soft)">
    <rect x="435" y="85" width="135" height="42" rx="6" fill="#FFFFFF" stroke="#E11D48" stroke-width="1.2" />
    <text x="502" y="102" text-anchor="middle" font-size="9.5" font-weight="600" fill="#243342">Ticket bus (Pierre)</text>
    <text x="502" y="116" text-anchor="middle" font-size="8" font-weight="400" fill="#5A6578">1 trajet unitaire</text>
  </g>

  <!-- Convergence vers ShopLoc -->
  <path d="M 570 48 L 600 48 L 600 175 L 625 175" fill="none" stroke="#0284C7" stroke-width="1.6" marker-end="url(#arrow-slate)" />
  <path d="M 570 106 L 600 106 L 600 175" fill="none" stroke="#0284C7" stroke-width="1.6" />

  <!-- T3 : ShopLoc verifie quota 1/jour -->
  <g filter="url(#shadow-soft)">
    <rect x="625" y="175" width="135" height="60" rx="7" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.4" />
    <text x="692" y="193" text-anchor="middle" font-size="8" font-weight="700" fill="#0284C7" text-transform="uppercase">REGLE METIER</text>
    <text x="692" y="209" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Valider quota 1/jour</text>
    <text x="692" y="223" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Consommer droit VFP</text>
  </g>

  <!-- Message vers APIs Mobilites T4 -->
  <path d="M 692 235 L 692 305" fill="none" stroke="#9333EA" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-slate)" />

  <!-- T4 : API Mock Voirie ou Ilevia -->
  <g filter="url(#shadow-soft)">
    <rect x="625" y="305" width="135" height="60" rx="7" fill="#FFFFFF" stroke="#9333EA" stroke-width="1.4" />
    <text x="692" y="323" text-anchor="middle" font-size="8" font-weight="700" fill="#9333EA" text-transform="uppercase">APPEL REST MOCK</text>
    <text x="692" y="339" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Crediter le droit</text>
    <text x="692" y="353" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Horodateur / QR Ilevia</text>
  </g>

  <!-- Message vers Mairie T5 -->
  <path d="M 692 365 L 692 435 L 750 435" fill="none" stroke="#CA8A04" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-slate)" />

  <!-- T5 : Mairie impute subvention R3 -->
  <g filter="url(#shadow-soft)">
    <rect x="750" y="435" width="130" height="58" rx="7" fill="#FFFFFF" stroke="#CA8A04" stroke-width="1.4" />
    <text x="815" y="453" text-anchor="middle" font-size="8" font-weight="700" fill="#CA8A04" text-transform="uppercase">COMPENSATION</text>
    <text x="815" y="469" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Imputer subvention</text>
    <text x="815" y="483" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Bordereau mensuel</text>
  </g>

  <!-- Message vers Citoyen confirmation T6 -->
  <path d="M 760 335 L 815 335 L 815 106" fill="none" stroke="#E11D48" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-terracotta)" />

  <!-- T6 : Citoyen utilise avantage -->
  <g filter="url(#shadow-soft)">
    <rect x="750" y="48" width="130" height="58" rx="7" fill="#FFFFFF" stroke="#E11D48" stroke-width="1.4" />
    <text x="815" y="66" text-anchor="middle" font-size="8" font-weight="700" fill="#E11D48" text-transform="uppercase">USAGE GRATUIT</text>
    <text x="815" y="82" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Profiter mobilite</text>
    <text x="815" y="96" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">20 min parking ou bus</text>
  </g>

  <!-- Fin nominale -->
  <circle cx="945" cy="77" r="14" fill="#FFFFFF" stroke="#16A34A" stroke-width="2.5" filter="url(#shadow-soft)" />
  <circle cx="945" cy="77" r="9" fill="#16A34A" />
  <line x1="880" y1="77" x2="931" y2="77" stroke="#16A34A" stroke-width="1.8" marker-end="url(#arrow-sage)" />
  <text x="945" y="105" text-anchor="middle" font-size="8.5" font-weight="600" fill="#16A34A">Avantage honore</text>
</svg>"""

# -------------------------------------------------------------
# SVG 5 : P5 ANOMALIES, RUPTURES & NO-SHOW
# -------------------------------------------------------------
SVG_P5 = f"""<svg viewBox="0 0 1020 540" width="100%" height="auto" style="overflow:visible; font-family:'Poppins', sans-serif;">
{COMMON_DEFS}
  <!-- COULOIR 1 : CITOYEN DEMANDEUR -->
  <rect x="30" y="20" width="960" height="115" fill="#FFF1F2" fill-opacity="0.6" stroke="#FECDD3" stroke-width="1.2" rx="6" />
  <rect x="30" y="20" width="150" height="115" fill="#E11D48" rx="6" />
  <text x="105" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">CITOYEN</text>
  <text x="105" y="93" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Acheteur / Usager)</text>

  <!-- COULOIR 2 : COMMERCANT PARTENAIRE -->
  <rect x="30" y="145" width="960" height="120" fill="#F0FDF4" fill-opacity="0.6" stroke="#86EFAC" stroke-width="1.2" rx="6" />
  <rect x="30" y="145" width="150" height="120" fill="#16A34A" rx="6" />
  <text x="105" y="200" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">COMMERCANT</text>
  <text x="105" y="218" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Boutique / Artisan)</text>

  <!-- COULOIR 3 : SHOPLOC GESTIONNAIRE D'INCIDENTS -->
  <rect x="30" y="275" width="960" height="125" fill="#F0F9FF" fill-opacity="0.6" stroke="#BAE6FD" stroke-width="1.2" rx="6" />
  <rect x="30" y="275" width="150" height="125" fill="#0284C7" rx="6" />
  <text x="105" y="330" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">SHOPLOC ENGINE</text>
  <text x="105" y="348" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Gestion des Alertes)</text>

  <!-- COULOIR 4 : ASSOCIATION & SUPPORT -->
  <rect x="30" y="410" width="960" height="110" fill="#FEFCE8" fill-opacity="0.6" stroke="#FDE047" stroke-width="1.2" rx="6" />
  <rect x="30" y="410" width="150" height="110" fill="#CA8A04" rx="6" />
  <text x="105" y="460" text-anchor="middle" font-size="11.5" font-weight="700" fill="#FFFFFF" letter-spacing="0.04em">ASSOCIATION</text>
  <text x="105" y="478" text-anchor="middle" font-size="9.5" font-weight="400" fill="#FFFFFF" opacity="0.95">(Mediation Amiable)</text>

  <!-- DEBUT D'INCIDENT DANS SHOPLOC -->
  <circle cx="205" cy="337" r="14" fill="#FFFFFF" stroke="#B91C1C" stroke-width="2.5" filter="url(#shadow-soft)" />
  <polygon points="202,331 212,337 202,343" fill="#B91C1C" />

  <!-- Passerelle XOR de Typologie d'Anomalie -->
  <polygon points="250,337 265,322 280,337 265,352" fill="#FFFFFF" stroke="#243342" stroke-width="1.8" filter="url(#shadow-soft)" />
  <text x="265" y="341" text-anchor="middle" font-size="12" font-weight="700" fill="#243342">x</text>
  <line x1="219" y1="337" x2="250" y2="337" stroke="#243342" stroke-width="1.8" marker-end="url(#arrow-slate)" />

  <!-- CAS A : RUPTURE STOCK EN BOUTIQUE -->
  <path d="M 265 322 L 265 204 L 305 204" fill="none" stroke="#243342" stroke-width="1.6" marker-end="url(#arrow-slate)" />
  <text x="270" y="250" font-size="8" font-weight="700" fill="#243342">[Rupture boutique]</text>

  <g filter="url(#shadow-soft)">
    <rect x="305" y="175" width="135" height="58" rx="7" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.4" />
    <text x="372" y="193" text-anchor="middle" font-size="8" font-weight="700" fill="#16A34A" text-transform="uppercase">DECLARATION</text>
    <text x="372" y="209" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Signaler rupture</text>
    <text x="372" y="223" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Article manquant</text>
  </g>
  <!-- Message vers ShopLoc Remboursement partiel -->
  <path d="M 440 204 L 475 204 L 475 305" fill="none" stroke="#0284C7" stroke-width="1.6" marker-end="url(#arrow-slate)" />
  <g filter="url(#shadow-soft)">
    <rect x="440" y="305" width="145" height="58" rx="7" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.4" />
    <text x="512" y="323" text-anchor="middle" font-size="8" font-weight="700" fill="#0284C7" text-transform="uppercase">COMPENSATION SEPA</text>
    <text x="512" y="339" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Rembourser partiel</text>
    <text x="512" y="353" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Reste du panier actif</text>
  </g>
  <!-- Message vers Citoyen notification -->
  <path d="M 512 305 L 512 106" fill="none" stroke="#E11D48" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-terracotta)" />
  <g filter="url(#shadow-soft)">
    <rect x="440" y="48" width="145" height="58" rx="7" fill="#FFFFFF" stroke="#E11D48" stroke-width="1.4" />
    <text x="512" y="66" text-anchor="middle" font-size="8" font-weight="700" fill="#E11D48" text-transform="uppercase">AVOIR INSTANTANE</text>
    <text x="512" y="82" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Avoir credite</text>
    <text x="512" y="96" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Articles restants prets</text>
  </g>

  <!-- CAS B : DEFAUT DE RETRAIT (NO-SHOW 24H) -->
  <path d="M 280 337 L 310 337" fill="none" stroke="#243342" stroke-width="1.6" marker-end="url(#arrow-slate)" />
  <text x="282" y="330" font-size="8" font-weight="700" fill="#243342">[No-show]</text>

  <g filter="url(#shadow-soft)">
    <rect x="310" y="305" width="115" height="58" rx="7" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.4" />
    <text x="367" y="323" text-anchor="middle" font-size="8" font-weight="700" fill="#0284C7" text-transform="uppercase">TIMER 24H</text>
    <text x="367" y="339" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Delai expire</text>
    <text x="367" y="353" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Relance SMS/Mail</text>
  </g>

  <!-- Passerelle No-Show confirme -->
  <path d="M 425 334 L 435 334 L 435 385 L 615 385" fill="none" stroke="#243342" stroke-width="1.6" marker-end="url(#arrow-slate)" />

  <g filter="url(#shadow-soft)">
    <rect x="615" y="355" width="155" height="60" rx="7" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.4" />
    <text x="692" y="373" text-anchor="middle" font-size="8" font-weight="700" fill="#0284C7" text-transform="uppercase">PROTECTION MARCHAND</text>
    <text x="692" y="389" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Cloturer la commande</text>
    <text x="692" y="403" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Paiement commercant du</text>
  </g>

  <!-- Message vers Commercant gestion stock -->
  <path d="M 692 355 L 692 233" fill="none" stroke="#16A34A" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-sage)" />
  <g filter="url(#shadow-soft)">
    <rect x="615" y="175" width="155" height="58" rx="7" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.4" />
    <text x="692" y="193" text-anchor="middle" font-size="8" font-weight="700" fill="#16A34A" text-transform="uppercase">RETOUR STOCK</text>
    <text x="692" y="209" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Reintegrer les secs</text>
    <text x="692" y="223" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Perissables factures</text>
  </g>

  <!-- Escalade Association en cas de litige -->
  <path d="M 770 385 L 810 385 L 810 435" fill="none" stroke="#CA8A04" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arrow-slate)" />
  <g filter="url(#shadow-soft)">
    <rect x="745" y="435" width="135" height="58" rx="7" fill="#FFFFFF" stroke="#CA8A04" stroke-width="1.4" />
    <text x="812" y="453" text-anchor="middle" font-size="8" font-weight="700" fill="#CA8A04" text-transform="uppercase">TIERS DE CONFIANCE</text>
    <text x="812" y="469" text-anchor="middle" font-size="10" font-weight="600" fill="#243342">Mediation humaine</text>
    <text x="812" y="483" text-anchor="middle" font-size="8.5" font-weight="400" fill="#5A6578">Reglement amiable</text>
  </g>

  <!-- Fin nominale -->
  <circle cx="945" cy="385" r="14" fill="#FFFFFF" stroke="#16A34A" stroke-width="2.5" filter="url(#shadow-soft)" />
  <circle cx="945" cy="385" r="9" fill="#16A34A" />
  <line x1="880" y1="464" x2="945" y2="464 L 945 403" stroke="#16A34A" stroke-width="1.8" marker-end="url(#arrow-sage)" />
  <line x1="770" y1="385" x2="931" y2="385" stroke="#16A34A" stroke-width="1.8" marker-end="url(#arrow-sage)" />
  <text x="945" y="415" text-anchor="middle" font-size="8.5" font-weight="600" fill="#16A34A">Incident clos</text>
</svg>"""

DIAGRAMS = [
    {
        "title": "Processus P1 : Conventionnement Municipal, Adhésion Commerçante et Déblocage SaaS",
        "subtitle": "Processus Administratif Tripartite",
        "fig_num": "3.1",
        "svg": SVG_P1,
        "width": 1020,
        "height": 540,
        "html_file": "agent_projet/templates/components/bpmn_p1_conventionnement.html",
        "png_file": "agent_projet/docs/01_Cadrage_Et_Cahier_Des_Charges_R1/figures/fig_3_1_bpmn_conventionnement.png"
    },
    {
        "title": "Processus P2 : Commande Click &amp; Collect Multi-Boutiques et Retrait (Two-Phase Commit)",
        "subtitle": "Orchestration Transactionnelle",
        "fig_num": "3.2",
        "svg": SVG_P2,
        "width": 1020,
        "height": 540,
        "html_file": "agent_projet/templates/components/bpmn_p2_click_and_collect.html",
        "png_file": "agent_projet/docs/01_Cadrage_Et_Cahier_Des_Charges_R1/figures/fig_3_2_bpmn_commande_cc.png"
    },
    {
        "title": "Processus P3 : Passage en Caisse Physique et Double Moteur de Fidélité Découplé",
        "subtitle": "Algorithme Glissant 15 Jours (ADR-005)",
        "fig_num": "3.3",
        "svg": SVG_P3,
        "width": 1020,
        "height": 530,
        "html_file": "agent_projet/templates/components/bpmn_p3_caisse_vfp.html",
        "png_file": "agent_projet/docs/01_Cadrage_Et_Cahier_Des_Charges_R1/figures/fig_3_3_bpmn_caisse_vfp.png"
    },
    {
        "title": "Processus P4 : Conversion des Droits de Fidélité VFP en Mobilité Urbaine Subventionnée",
        "subtitle": "Interconnexion APIs Mocks Voirie &amp; Bus",
        "fig_num": "3.4",
        "svg": SVG_P4,
        "width": 1020,
        "height": 540,
        "html_file": "agent_projet/templates/components/bpmn_p4_conversion_mobilite.html",
        "png_file": "agent_projet/docs/01_Cadrage_Et_Cahier_Des_Charges_R1/figures/fig_3_4_bpmn_mobilite.png"
    },
    {
        "title": "Processus P5 : Traitement des Anomalies, Ruptures de Stock, Annulations et No-Show",
        "subtitle": "Résilience Opérationnelle &amp; Médiation",
        "fig_num": "3.5",
        "svg": SVG_P5,
        "width": 1020,
        "height": 540,
        "html_file": "agent_projet/templates/components/bpmn_p5_anomalies_noshow.html",
        "png_file": "agent_projet/docs/01_Cadrage_Et_Cahier_Des_Charges_R1/figures/fig_3_5_bpmn_anomalies_noshow.png"
    }
]

def export_png(svg_content, width, height, output_png):
    os.makedirs(os.path.dirname(output_png), exist_ok=True)
    temp_html = output_png.replace(".png", "_render_tmp.html")
    html_page = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html, body {{ width: {width}px; height: {height}px; background: #FFFFFF; overflow: hidden; }}
    svg {{ display: block; width: {width}px; height: {height}px; }}
  </style>
</head>
<body>
{svg_content}
</body>
</html>"""
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_page)

    cmd = [
        BROWSER,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=2",
        f"--window-size={width},{height}",
        f"--screenshot={output_png}",
        f"file://{os.path.abspath(temp_html)}"
    ]
    subprocess.run(cmd, check=True, stderr=subprocess.DEVNULL)
    if os.path.exists(temp_html):
        os.remove(temp_html)
    print(f"Exported: {output_png} ({width}x{height})")

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    for d in DIAGRAMS:
        # 1. Sauvegarde du composant HTML
        html_path = os.path.join(repo_root, d["html_file"])
        os.makedirs(os.path.dirname(html_path), exist_ok=True)
        component_content = f"""<!-- FIGURE {d['fig_num']} : {d['title'].upper()} -->
<div class="figure-card" style="background:#FFFFFF; border:1px solid #E8E6DF; border-radius:16px; padding:24px; margin-bottom:28px; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px; border-bottom:1px solid #E8E6DF; padding-bottom:12px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#243342;"></span>
        <span style="font-size:11px; font-weight:700; color:#243342; text-transform:uppercase; letter-spacing:0.08em;">Norme BPMN 2.0 (ISO/IEC 19510)</span>
      </div>
      <h3 style="font-size:17px; font-weight:700; color:#243342; margin:0;">Figure {d['fig_num']} — {d['title']}</h3>
    </div>
    <span style="font-size:11px; background:#FAF9F6; border:1px solid #E8E6DF; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600;">{d['subtitle']}</span>
  </div>
{d['svg']}
</div>
"""
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(component_content)
        print(f"HTML écrit : {html_path}")

        # 2. Export PNG haute résolution
        png_path = os.path.join(repo_root, d["png_file"])
        export_png(d["svg"], d["width"], d["height"], png_path)

    print("Tous les 5 diagrammes BPMN 2.0 ont été générés avec succès !")

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import os

# Create assets directory if it doesn't exist
os.makedirs('assets', exist_ok=True)

def create_formula_image(tex, filename):
    fig = plt.figure(figsize=(6, 1))
    fig.text(0.5, 0.5, tex, fontsize=16, ha='center', va='center', usetex=False, math_fontfamily='cm')
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight', dpi=300, transparent=True)
    plt.close(fig)

formulas = {
    'formule_1.png': r"$\text{Coût de l'Unité d'Œuvre (UO)} = \frac{\text{Total des charges du centre}}{\text{Nombre total d'UO}}$",
    'formule_2.png': r"$\text{Coût de l'Unité d'Œuvre (Vente)} = \frac{11\,040\, \text{€}}{60\, \text{h}} = 184\, \text{€/h}$",
    'formule_3.png': r"$\text{Coût de l'Unité d'Œuvre (Production)} = \frac{24\,960\, \text{€}}{480\, \text{h}} = 52\, \text{€/h}$",
    'formule_4.png': r"$\text{Résultat Analytique} = \text{Prix de Vente (CA)} - \text{Coût de Revient Complet}$",
    'formule_5.png': r"$\text{Résultat Analytique} = 88\,000\, \text{€} - 50\,400\, \text{€} = +37\,600\, \text{€}$",
    'formule_6.png': r"$\text{Prix de Vente Cible} = \frac{\text{Coût de Revient Complet}}{1 - 0{,}15} = \frac{50\,400}{0{,}85} = 59\,294{,}12\, \text{€}$"
}

for filename, tex in formulas.items():
    try:
        create_formula_image(tex, os.path.join('assets', filename))
    except Exception as e:
        print(f"Error creating {filename}: {e}")

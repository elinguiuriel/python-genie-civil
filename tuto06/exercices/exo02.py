# Exercice 2: Recherche de la Valeur Maximale
# d'une Fonction avec SciPy
from scipy.optimize import minimize_scalar

# Fonction représentant la charge sur une structure


def fonction_charge(x):
    return -(x**2) + 10*x - 20


# Utilisation de SciPy pour trouver la valeur maximale
resultat_optimisation = minimize_scalar(
    fonction_charge, bounds=(0, 10), method='bounded')

charge_maximale = -resultat_optimisation.fun
position_maximale = resultat_optimisation.x

print("La charge maximale sur la structure est",
      f"{charge_maximale} kN à la position",
      f"{position_maximale} mètres.")

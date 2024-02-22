# Importation de SciPy
from scipy import constants, optimize

# Utilisation de constantes de SciPy
gravité_terrestre = constants.g

# Utilisation de SciPy pour trouver la racine d'une fonction


def equation_racine(x):
    return x**2 - 4


racine = optimize.root(equation_racine, [0, 5])
print(f"Racine de l'équation : {racine.x}")

# Importer les bibliothèques nécessaires :
import numpy as np
from scipy.linalg import solve

# Définir les paramètres :
# Longueur de la poutre (en mètres)
longueur_poutre = 5

# Moment d'inertie de la section transversale (en m^4)
moment_inertie = 500

# Charge appliquée à l'extrémité de la poutre (en Newtons)
charge = 1000

# Définir la matrice du système d'équations :
A = np.array([[longueur_poutre**3 / 3, longueur_poutre**2 / 2],
              [longueur_poutre**2 / 2, longueur_poutre]])

# Définir le vecteur des constantes :
b = np.array([charge, 0])

# Résoudre le système d'équations :
solution = solve(A, b)

# Extraire la déformation maximale :
deformation_maximale = solution[0]

# Afficher les résultats :
print(f"Déformation maximale dans la poutre : {deformation_maximale} mètres.")

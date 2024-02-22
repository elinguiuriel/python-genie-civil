# ===============================================================
# Objectif :
# Modéliser et analyser une poutre en treillis soumise à des charges.
# ===============================================================

# Étapes :
# Importer les bibliothèques nécessaires :
import numpy as np
from scipy.linalg import solve

# Définir les paramètres :

# Matrice de rigidité de la poutre en treillis
K = np.array([[2, -1, 0, 0],
              [-1, 2, -1, 0],
              [0, -1, 2, -1],
              [0, 0, -1, 1]])

# Forces appliquées aux nœuds (en Newtons)
forces = np.array([10, 0, 5, 0])

# Résoudre le système d'équations pour les déformations :
# Résolution du système d'équations
deformations = solve(K, forces)

# Afficher les résultats :
print(f"Déformations dans la poutre en treillis : {deformations} mètres.")

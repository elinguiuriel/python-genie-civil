# Exemple: Analyse de structures - Détermination des déformations
import numpy as np
from scipy.linalg import solve

# Matrice de rigidité de la poutre
K = np.array([[2, -1], [-1, 1]])

# Forces appliquées
F = np.array([10, 0])

# Résolution du système d'équations pour les déformations
déformations = solve(K, F)

print(f"Déformations de la poutre : {déformations}")

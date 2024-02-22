# Exercice 1: Résolution d'un Système d'Équations Linéaires avec NumPy
import numpy as np

# Matrice de rigidité de la poutre
K = np.array([[2, -1], [-1, 1]])

# Forces appliquées
F = np.array([10, 0])

# Résolution du système d'équations pour les déformations
déformations = np.linalg.solve(K, F)

print(f"Déformations de la poutre : {déformations}")

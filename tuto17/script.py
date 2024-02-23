import matplotlib.pyplot as plt
import numpy as np


# Définition du problème
L = 10.0  # Longueur de la poutre
E = 2.1e11  # Module d'élasticité
I = 4.5e-6  # Moment d'inertie
q = 1000.0  # Charge répartie


# Discrétisation de la poutre
N = 10  # Nombre d'éléments
x = np.linspace(0, L, N+1)  # Positions des nœuds


# Formation de la matrice de raideur
K = np.zeros((N+1, N+1))
for i in range(N):
    L_element = x[i+1] - x[i]
    ke = E * I / L_element * np.array([[12, 6*L_element],
                                       [6*L_element, 4*L_element**2]])
    K[i:i+2, i:i+2] += ke


# Application des conditions aux limites (encastrée à une extrémité)
K[0, :] = 0
K[:, 0] = 0
K[0, 0] = 1


# Application de la charge répartie
F = np.zeros(N+1)
for i in range(N):
    L_element = x[i+1] - x[i]
    F[i:i+2] += q * L_element / 2

# Résolution du système d'équations
u = np.linalg.solve(K, F)


# Visualisation des déformations

plt.plot(x, u, marker='o')
plt.xlabel('Position (m)')
plt.ylabel('Déformation (m)')
plt.title('Déformation de la Poutre')
plt.grid(True)
plt.show()



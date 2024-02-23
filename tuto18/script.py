import numpy as np
import matplotlib.pyplot as plt

# Paramètres du problème
L = 1.0  # Longueur du domaine
T = 0.5  # Temps total de simulation
alpha = 0.01  # Diffusivité thermique

# Discrétisation spatiale
Nx = 100  # Nombre de points de grille
dx = L / (Nx - 1)  # Espacement spatial
x = np.linspace(0, L, Nx)  # Grille spatiale

# Discrétisation temporelle
Nt = 500  # Nombre de pas de temps
dt = T / Nt  # Pas de temps
t = np.linspace(0, T, Nt)  # Grille temporelle

# Conditions initiales
u0 = np.sin(np.pi * x)  # Profil initial de la température

# Solution par différences finies
u = np.zeros((Nx, Nt))

# Conditions initiales
u[:, 0] = u0

# Application des différences finies explicites
for n in range(0, Nt - 1):
    for i in range(1, Nx - 1):
        u[i, n + 1] = u[i, n] + alpha * dt / dx**2 * \
            (u[i + 1, n] - 2 * u[i, n] + u[i - 1, n])

# Visualisation de la solution
plt.figure(figsize=(10, 6))
plt.imshow(u, aspect='auto', extent=[0, T, 0, L],
           cmap='hot', origin='lower')
plt.colorbar(label='Température')
plt.title('Évolution de la Température dans le Domaine')
plt.xlabel('Temps')
plt.ylabel('Position')
plt.show()


# Paramètres supplémentaires
Ne = Nx - 1  # Nombre d'éléments
nodes_per_element = 2  # Nombre de nœuds par élément

# Connectivité des nœuds par élément
elements = np.array([np.arange(i, i + nodes_per_element) for i in range(Ne)])

# Matrice de masse élémentaire
Me = (dx / 6) * np.array([[2, 1], [1, 2]])

# Matrice de rigidité élémentaire
Ke = (alpha / dx) * np.array([[1, -1], [-1, 1]])

# Assemblage des matrices globales
M = np.zeros((Nx, Nx))
K = np.zeros((Nx, Nx))

for i in range(Ne):
    indices = elements[i]
    M[np.ix_(indices, indices)] += Me
    K[np.ix_(indices, indices)] += Ke

# Conditions aux limites
M[0, 0] = 1
M[-1, -1] = 1
K[0, :] = 0
K[-1, :] = 0
K[0, 0] = 1
K[-1, -1] = 1

# Solution par éléments finis
u_fe = np.linalg.solve(M + dt * K, u0)

# Visualisation de la solution
plt.figure(figsize=(10, 6))
plt.plot(x, u_fe, label='Éléments Finis')
plt.title('Évolution de la Température avec les Éléments Finis')
plt.xlabel('Position')
plt.ylabel('Température')
plt.legend()
plt.show()

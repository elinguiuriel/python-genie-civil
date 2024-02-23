import numpy as np
import matplotlib.pyplot as plt

# Paramètres du problème
L = 1.0 # Longueur de la barre (m)
T0 = 100.0 # Température à l'extrémité gauche (°C)
alpha = 1e-4 # Diffusivité thermique (m²/s)

# Discrétisation spatiale
Nx = 100 # Nombre de points de grille
dx = L / (Nx - 1) # Espacement spatial
x = np.linspace(0, L, Nx) # Grille spatiale

# Discrétisation temporelle
Nt = 500 # Nombre de pas de temps
dt = 0.1 # Pas de temps (s)
t = np.linspace(0, Nt * dt, Nt) # Grille temporelle

# Conditions initiales
u0 = np.zeros(Nx)
u0[0] = T0 # Température initiale à l'extrémité gauche

# Solution par différences finies
u = np.zeros((Nx, Nt))
u[:, 0] = u0

# Application des différences finies explicites
for n in range(0, Nt - 1):
    for i in range(1, Nx - 1):
        u[i, n + 1] = u[i, n] + alpha * dt / dx**2 * (u[i + 1, n] - 2 * u[i, n] + u[i - 1, n])

# Visualisation de la solution
plt.figure(figsize=(10, 6))
plt.imshow(u, aspect='auto', extent=[0, Nt * dt, 0, L], cmap='hot', origin='lower')
plt.colorbar(label='Température (°C)')
plt.title('Modélisation du Flux de Chaleur dans une Barre en Acier')
plt.xlabel('Temps (s)')
plt.ylabel('Position')
plt.show()

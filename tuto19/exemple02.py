import numpy as np
import matplotlib.pyplot as plt

# Paramètres du problème
L = 5.0  # Longueur de la poutre (m)
E = 2.1e11  # Module d'élasticité (Pa)
I = 4.5e-6  # Moment d'inertie (m^4)
q = 1000.0  # Charge uniformément répartie (N/m)

# Discrétisation spatiale
Nx = 100  # Nombre de points de grille
dx = L / (Nx - 1)  # Espacement spatial
x = np.linspace(0, L, Nx)  # Grille spatiale

# Conditions aux limites
w0 = 0.0  # Déplacement initial
theta0 = 0.0  # Inclinaison initiale
dw0 = 0.0  # Dérivée première initiale
dtheta0 = 0.0  # Dérivée seconde initiale

# Solution par éléments finis
w = np.zeros(Nx)
w[0] = w0

# Application des éléments finis
for i in range(1, Nx):
    dx_local = x[i] - x[i - 1]
    w[i] = w[i - 1] + (dw0 * dx_local)
    dw0 = dw0 - (q * dx_local**3) / (6 * E * I) + (dtheta0 * dx_local)
    dtheta0 = dtheta0 - (q * dx_local**2) / (2 * E * I)

# Visualisation de la déformation
plt.figure(figsize=(10, 6))
plt.plot(x, w, label='Déformation de la Poutre')
plt.title('Simulation de la Déformation d\'une Poutre sous Charge')
plt.xlabel('Position sur la Poutre (m)')
plt.ylabel('Déplacement Vertical (m)')
plt.legend()
plt.show()

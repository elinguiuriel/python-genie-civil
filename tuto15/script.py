def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    """
    Applique la méthode de Newton-Raphson pour 
    résoudre l'équation f(x) = 0.

    Parameters:
    - f: Fonction à résoudre.
    - f_prime: Dérivée de la fonction f.
    - x0: Estimation initiale de la racine.
    - tol: Tolérance pour la convergence.
    - max_iter: Nombre maximal d'itérations.

    Returns:
    - La valeur estimée de la racine.
    """
    x = x0
    for _ in range(max_iter):
        f_value = f(x)
        if abs(f_value) < tol:
            return x
        f_prime_value = f_prime(x)
        if f_prime_value == 0:
            raise ValueError(
                "La dérivée est nulle. La méthode de",
                "Newton-Raphson ne peut pas converger.")
        x = x - f_value / f_prime_value
    raise ValueError(
        "La méthode de Newton-Raphson n'a pas convergé",
        "après le nombre maximal d'itérations.")


def deformation_equation(x, P, E, I, delta):
    return (P * x**3) / (3 * E * I) - delta


def deformation_equation_prime(x, P, E, I, delta):
    return (P * x**2) / (E * I)


# Paramètres du problème
charge_appliquee = 1000  # en Newtons
module_elasticite = 2.1e11  # en Pascal
moment_inertie = 5e-6  # en m^4
deformation_maximale = 0.01  # en mètres

# Estimation initiale de la déformation
estimation_initiale = 0.005

# Application de la méthode de Newton-Raphson
resultat = newton_raphson(
    lambda x: deformation_equation(
        x, charge_appliquee, module_elasticite,
        moment_inertie, deformation_maximale),
    lambda x: deformation_equation_prime(
        x, charge_appliquee, module_elasticite,
        moment_inertie, deformation_maximale),
    estimation_initiale
)

print(f"La déformation maximale est estimée à {resultat:.4f} mètres.")

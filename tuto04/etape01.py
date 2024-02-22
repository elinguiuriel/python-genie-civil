# ===============================================================
# Déclaration de Fonctions :
# Les fonctions en Python sont définies avec le mot-clé def.
# ===============================================================

# Exemple : Fonction pour calculer la charge sur une poutre
def calcul_charge_poutre(longueur, largeur, densité, gravité):
    volume = longueur * largeur * 1  # Assumption: hauteur de 1 mètre
    charge = volume * densité * gravité
    return charge

# ===============================================================
# Appel de Fonctions :
# Les fonctions sont appelées en utilisant leur nom suivi
# des arguments.
# ===============================================================


# Utilisation de la fonction pour calculer la charge sur une poutre
charge_poutre = calcul_charge_poutre(10, 0.3, 2500, 9.81)
print(f"La charge sur la poutre est de {charge_poutre} Newtons.")

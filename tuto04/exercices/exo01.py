# Exercice 1: Calcul de la surface d'un mur
def calcul_surface_mur(longueur, hauteur):
    surface = longueur * hauteur
    return surface


# Utilisation de la fonction pour calculer la surface d'un mur
longueur_mur = 8  # en mètres
hauteur_mur = 3  # en mètres

surface_mur = calcul_surface_mur(longueur_mur, hauteur_mur)
print(f"La surface du mur est de {surface_mur} mètres carrés.")
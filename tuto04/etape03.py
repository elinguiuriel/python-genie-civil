# ===============================================================
# Paramètres par Défaut :
# Les fonctions peuvent avoir des paramètres par défaut
# pour une plus grande flexibilité.
# ===============================================================

# Exemple : Fonction pour calculer le volume d'une colonne
def calcul_volume_colonne(hauteur, rayon_base=1):
    volume = 3.14 * rayon_base**2 * hauteur
    return volume


# Utilisation de la fonction avec paramètre par défaut
# Utilise le rayon_base par défaut
volume_colonne = calcul_volume_colonne(5)
print(f"Le volume de la colonne est de {volume_colonne} mètres cubes.")

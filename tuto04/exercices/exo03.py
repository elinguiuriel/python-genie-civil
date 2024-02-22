# Exercice 3: Calcul de la charge sur une colonne
# avec paramètre par défaut
def calcul_charge_colonne(hauteur, rayon_base=1,
                          densité=2500, gravité=9.81):
    volume = 3.14 * rayon_base**2 * hauteur
    charge = volume * densité * gravité
    return charge


# Utilisation de la fonction pour calculer la charge sur une colonne
hauteur_colonne = 10  # en mètres
charge_colonne = calcul_charge_colonne(hauteur_colonne)
print(f"La charge sur la colonne est de {charge_colonne} Newtons.")

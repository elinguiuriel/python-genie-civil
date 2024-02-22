import pandas as pd

# Importation de données depuis un fichier texte
chemin_fichier_texte = 'data/terrain_elevation.txt'

donnees_texte = pd.read_table(
    chemin_fichier_texte,
    header=None,
    delim_whitespace=True)

# Affichage des données
print(donnees_texte)

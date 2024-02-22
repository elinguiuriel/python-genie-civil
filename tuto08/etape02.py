import pandas as pd

# Importation du fichier CSV
chemin_fichier_csv = 'data/charges_structure.csv'
donnees_csv = pd.read_csv(chemin_fichier_csv)

# Affichage des données
print(donnees_csv)

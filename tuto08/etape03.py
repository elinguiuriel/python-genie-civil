# Importation du fichier Excel
import pandas as pd

chemin_fichier_excel = 'data/dimensions_poutres.xlsx'
donnees_excel = pd.read_excel(chemin_fichier_excel)

# Affichage des données
print(donnees_excel)

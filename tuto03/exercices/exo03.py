# Exercice 3: Simulation de l'élévation de la charge sur une colonne

charge_maximale_colonne = 10000  # en Newtons
resistance_colonne = 0
coeff_securite = 1.5

while resistance_colonne < charge_maximale_colonne / coeff_securite:
    resistance_colonne += 500
    print("Test de résistance: Résistance actuelle",
          f" de la colonne - {resistance_colonne} Newtons")

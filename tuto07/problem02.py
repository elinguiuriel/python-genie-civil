# ===============================================================
# Objectif :
# Déterminer les dimensions d'une poutre en flexion 
# pour supporter une charge donnée.
# ===============================================================

# Importer les bibliothèques nécessaires :
import numpy as np

# Définir les paramètres :
# Charge appliquée à la poutre (en Newtons)
charge = 5000

# Contrainte maximale admissible (en Pascal)
contrainte_maximale = 20e6

# Propriétés du matériau :
# Module de Young (en Pascal)
module_young = 200e9

# Calculer les dimensions requises :
# Calcul de la section transversale nécessaire en 
# fonction de la contrainte maximale
section_transversale = charge / contrainte_maximale

# Calcul de la distance maximale de flexion pour 
# une contrainte maximale donnée
distance_flexion_maximale = (
    charge * (3 / 2) * (1 / module_young) * 
    (section_transversale / 2)) ** (1 / 3)

# Afficher les résultats :
print("Section transversale nécessaire : ",
      f"{section_transversale:.10f} mètres carrés.")
print("Distance maximale de flexion pour une contrainte"
      "maximale donnée : ",
      f"{distance_flexion_maximale:.10f} mètres.")

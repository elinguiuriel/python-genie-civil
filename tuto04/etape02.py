# ===============================================================
# Utilisation de Fonctions pour la Modularité :
# Les fonctions permettent de diviser le code en parties
# réutilisables, améliorant ainsi la modularité.
# ===============================================================

# Exemple : Fonction pour analyser la résistance d'un matériau
def analyse_resistance_materiau(resistance_materiau, resistance_limite):
    if resistance_materiau >= resistance_limite:
        print("Le matériau satisfait les spécifications",
              "de résistance.")
    else:
        print("Le matériau ne satisfait pas les spécifications",
              "de résistance.")


# Utilisation de la fonction d'analyse de résistance
resistance_limite = 30  # en MPa
resistance_materiau = 25

analyse_resistance_materiau(resistance_materiau, resistance_limite)

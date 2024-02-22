# ===============================================================
# Déclaration "if" :
# La déclaration "if" est utilisée pour exécuter un bloc
# de code si une condition est vraie.
# ===============================================================

# Exemple : Vérification de la résistance d'un matériau
resistance_limite = 30  # en MPa
resistance_materiau = 25

if resistance_materiau >= resistance_limite:
    print("Le matériau satisfait les spécifications de résistance.")
else:
    print("Le matériau ne satisfait pas les spécifications de résistance.")


# ===============================================================
# Déclaration "else" et "elif" :
# La déclaration "else" est utilisée pour exécuter un bloc
# de code lorsque la condition "if" est fausse.
# La déclaration "elif" permet de vérifier plusieurs conditions
# de manière séquentielle.
# ===============================================================

# Exemple : Classement des matériaux en fonction de la résistance
if resistance_materiau >= 40:
    print("Matériau de haute résistance.")
elif resistance_materiau >= 30:
    print("Matériau de résistance moyenne.")
else:
    print("Matériau de faible résistance.")

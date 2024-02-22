# ===============================================================
# Création de Listes :
# Les listes sont des séquences mutables d'éléments.
# ===============================================================

# Exemple : Liste de matériaux de construction
materiaux_construction = ['béton', 'acier', 'bois', 'verre']


# ===============================================================
# Accès aux Éléments de la Liste :
# Les éléments d'une liste sont accessibles par leur indice.
# ===============================================================

# Exemple : Accès au premier élément de la liste
premier_matériau = materiaux_construction[0]
print(f"Le premier matériau de construction est {premier_matériau}.")

# ===============================================================
# Modification de Listes :
# Les listes peuvent être modifiées en ajoutant ou supprimant des éléments.
# ===============================================================

# Exemple : Ajout d'un nouveau matériau
materiaux_construction.append('aluminium')

# Exemple : Suppression d'un matériau existant
materiaux_construction.remove('bois')

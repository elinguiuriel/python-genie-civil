# ===============================================================
# Création de Tuples :
# Les tuples sont des séquences immuables d'éléments.
# ===============================================================

# Exemple : Tuple de dimensions d'une poutre
dimensions_poutre = (10, 0.3, 0.5)


# ===============================================================
# Accès aux Éléments du Tuple :
# Les éléments d'un tuple sont également accessibles par leur indice.
# ===============================================================

# Exemple : Accès à la deuxième dimension de la poutre
deuxième_dimension = dimensions_poutre[1]
print("La deuxième dimension de la poutre est",
      f"{deuxième_dimension} mètres.")

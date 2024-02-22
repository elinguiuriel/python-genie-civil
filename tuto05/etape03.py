# ===============================================================
# Création de Dictionnaires :
# Les dictionnaires stockent des paires clé-valeur.
# ===============================================================

# Exemple : Dictionnaire de propriétés d'un matériau
proprietes_beton = {
    'résistance': 30,
    'densité': 2400,
    'module_élasticité': 25e9
}

# ===============================================================
# Accès aux Valeurs par Clé :
# Les valeurs d'un dictionnaire sont accessibles par leur clé.
# ===============================================================

# Exemple : Accès à la résistance du béton
résistance_béton = proprietes_beton['résistance']
print(f"La résistance du béton est {résistance_béton} MPa.")

# ===============================================================
# Modification de Dictionnaires :
# Les dictionnaires peuvent être mis à jour avec de nouvelles clés ou valeurs.
# ===============================================================

# Exemple : Ajout d'une nouvelle propriété au dictionnaire
proprietes_beton['conductivité_thermique'] = 1.7

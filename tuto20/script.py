# Paramètres de la poutre
longueur_poutre = 6.0  # Longueur de la poutre (m)
charge_permanente = 20.0  # Charge permanente sur la poutre (kN/m)
charge_temporaire = 15.0  # Charge temporaire sur la poutre (kN/m)

# Propriétés du matériau
resistance_beton = 25.0  # Résistance du béton (MPa)
resistance_acier = 400.0  # Résistance de l'acier (MPa)

# Autres paramètres
facteur_sécurité = 1.5  # Facteur de sécurité


# Calcul des charges totales
charge_totale = charge_permanente + charge_temporaire


# Vérification des charges
if charge_totale > resistance_beton:
    print("La charge totale dépasse la résistance du béton. Révision nécessaire.")
else:
    print("Les charges sont dans les limites admissibles. Continuer la conception.")


# Calcul des contraintes dans la poutre
contrainte_beton = charge_totale / (longueur_poutre * facteur_sécurité)

# Vérification des contraintes
if contrainte_beton > resistance_beton:
    print("La contrainte dans le béton dépasse la résistance. Révision nécessaire.")
else:
    print("La contrainte dans le béton est acceptable. Continuer la conception.")


# Vérification des armatures
section_poutre = longueur_poutre ** 2 / 6  # Section transversale de la poutre
armature_minimale = resistance_acier * section_poutre / \
    (facteur_sécurité * contrainte_beton)

# Vérification des armatures minimales
if armature_minimale > 0.0:
    print(f"Armature minimale requise : {armature_minimale} mm²")
else:
    print("Pas d'armature minimale requise.")

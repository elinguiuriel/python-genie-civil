# Exercice 3: Dictionnaire des Propriétés d'un Sol et Mise à Jour
propriétés_sol = {
    'type': 'argile',
    'densité': 1800,
    'perméabilité': 'faible'
}

# Mise à jour de la densité du sol
propriétés_sol['densité'] = 2000

print("Propriétés mises à jour du sol:")
for clé, valeur in propriétés_sol.items():
    print(f"{clé}: {valeur}")

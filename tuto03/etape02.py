# ===============================================================
# Boucle "for" :
# La boucle "for" est utilisée pour itérer sur une séquence
# (liste, tuple, etc.).
# ===============================================================

# Exemple : Itération sur une liste de matériaux
matériaux = ['béton', 'acier', 'bois']

for matériau in matériaux:
    print(f"Analyse du matériau: {matériau}")

# ===============================================================
# Boucle "while" :
# La boucle "while" est utilisée pour exécuter un bloc de code
# tant que la condition spécifiée est vraie.
# ===============================================================

# Exemple : Calcul de la charge maximale supportée par un pilier
charge_maximale = 5000  # en Newtons
resistance_pilier = 0
coeff_securite = 1.5

while resistance_pilier < charge_maximale / coeff_securite:
    resistance_pilier += 100
    print(f"Test de résistance: {resistance_pilier} Newtons")

# Exercice 1: Vérification de la charge supportée
# par une poutre en acier

charge_maximale = 8000  # en Newtons
charge_actuelle = 7500

if charge_actuelle <= charge_maximale:
    print("La poutre en acier peut supporter la charge.")
else:
    print("La poutre en acier ne peut pas supporter la charge.",
          "Des renforcements sont nécessaires.")

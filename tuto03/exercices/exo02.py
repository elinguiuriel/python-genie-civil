types_sols = ['argile', 'sable', 'roche']

for sol in types_sols:
    if sol == 'argile':
        print(f"Le sol de type {sol} peut nécessiter",
              "des fondations spéciales.")
    elif sol == 'sable':
        print(
            f"Le sol de type {sol} offre une bonne stabilité",
            " pour les fondations.")
    elif sol == 'roche':
        print(f"Le sol de type {sol} est idéal pour",
              " des structures robustes.")
    else:
        print(f"Type de sol non reconnu.")

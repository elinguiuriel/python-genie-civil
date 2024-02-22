# Exercice 2: Détermination du type de fondation recommandé
def type_fondation_recommande(type_sol):
    if type_sol == 'argile':
        return "Fondation profonde recommandée."
    elif type_sol == 'sable':
        return "Fondation superficielle suffisante."
    elif type_sol == 'roche':
        return "Fondation superficielle recommandée."
    else:
        return "Type de sol non reconnu. Consultez un ingénieur géotechnique."


# Utilisation de la fonction pour déterminer le type de fondation
type_sol_projet = 'argile'

recommandation_fondation = type_fondation_recommande(type_sol_projet)
print(f"Recommandation pour le type de fondation: {recommandation_fondation}")

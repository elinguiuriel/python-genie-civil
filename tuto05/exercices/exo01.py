# Exercice 1: Liste de Projets de Construction
projets_construction = ['Pont de la Réconciliation',
                        'Centre Commercial Ville-Mall',
                        'Hôtel Horizon']

# Ajout d'un nouveau projet
projets_construction.append('Stade MégaSport')

# Suppression d'un projet existant
projets_construction.remove('Centre Commercial Ville-Mall')

print("Liste des projets de construction mis à jour:")
for projet in projets_construction:
    print(f"- {projet}")

# Importation des Bibliothèques Tkinter
import tkinter as tk
from tkinter import ttk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calcul de Section Transversale")

# Ajout d'un libellé
libelle = ttk.Label(
    fenetre, 
    text="Calcul de Section Transversale d'une Poutre", 
    font=("Arial", 14))
libelle.grid(row=0, column=0, columnspan=2, pady=10)

# Création des Widgets
# Entrée pour la charge appliquée à la poutre
libelle_charge = ttk.Label(fenetre, text="Charge Appliquée (kN) :")
libelle_charge.grid(row=1, column=0, padx=10, pady=5, sticky="E")

entree_charge = ttk.Entry(fenetre)
entree_charge.grid(row=1, column=1, padx=10, pady=5)

# Entrée pour la contrainte maximale admissible (en Pascal)
libelle_contrainte = ttk.Label(
    fenetre, text="Contrainte Maximale Admissible (Pa) :")
libelle_contrainte.grid(row=2, column=0, padx=10, pady=5, sticky="E")

entree_contrainte = ttk.Entry(fenetre)
entree_contrainte.grid(row=2, column=1, padx=10, pady=5)

# Bouton pour calculer la section transversale nécessaire


def calculer_section_transversale():
    try:
        charge = float(entree_charge.get())
        contrainte = float(entree_contrainte.get())

        # Calcul de la section transversale nécessaire
        section_transversale = charge / contrainte

        # Affichage du résultat
        resultat.config(
            text=f"Section Transversale Nécessaire : {section_transversale:.4f} m²")

    except ValueError:
        resultat.config(text="Veuillez entrer des valeurs numériques valides.")


bouton_calculer = ttk.Button(
    fenetre, text="Calculer", command=calculer_section_transversale)
bouton_calculer.grid(row=3, column=0, columnspan=2, pady=10)

# Libellé pour afficher les résultats
resultat = ttk.Label(fenetre, text="")
resultat.grid(row=4, column=0, columnspan=2, pady=10)

# Lancement de la boucle principale
fenetre.mainloop()

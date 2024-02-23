import tkinter as tk
from tkinter import ttk


def calculer_moments_flechissants():
    try:
        # Récupération des données depuis les champs d'entrée
        longueur = float(entree_longueur.get())
        charge = float(entree_charge.get())

        # Calcul des moments fléchissants (formule simplifiée)
        moment_maximal = (charge * longueur**2) / 8

        # Affichage du résultat
        resultat.config(
            text=f"Le moment fléchissant maximal est de {moment_maximal:.2f} kNm")

    except ValueError:
        resultat.config(text="Veuillez entrer des valeurs numériques valides.")


# Création de la fenêtre principale
fenetre1 = tk.Tk()
fenetre1.title("Calcul de Moments Fléchissants")

# Widgets pour l'interface
libelle_longueur = ttk.Label(fenetre1, text="Longueur de la Poutre (m) :")
libelle_longueur.grid(row=1, column=0, padx=10, pady=5, sticky="E")

entree_longueur = ttk.Entry(fenetre1)
entree_longueur.grid(row=1, column=1, padx=10, pady=5)

libelle_charge = ttk.Label(
    fenetre1, text="Charge Uniformément Répartie (kN/m) :")
libelle_charge.grid(row=2, column=0, padx=10, pady=5, sticky="E")

entree_charge = ttk.Entry(fenetre1)
entree_charge.grid(row=2, column=1, padx=10, pady=5)

bouton_calculer = ttk.Button(
    fenetre1, text="Calculer", command=calculer_moments_flechissants)
bouton_calculer.grid(row=3, column=0, columnspan=2, pady=10)

resultat = ttk.Label(fenetre1, text="")
resultat.grid(row=4, column=0, columnspan=2, pady=10)

# Lancement de la boucle principale
fenetre1.mainloop()

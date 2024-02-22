# Importation des Bibliothèques Tkinter
import tkinter as tk
from tkinter import ttk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calcul de Déformations")

# Ajout d'un libellé
libelle = ttk.Label(
    fenetre,
    text="Calcul de Déformations d'une Poutre",
    font=("Arial", 14))
libelle.grid(row=0, column=0, columnspan=2, pady=10)

# Entrée pour la longueur de la poutre
libelle_longueur = ttk.Label(
    fenetre,
    text="Longueur de la Poutre (m) :")
libelle_longueur.grid(
    row=1, column=0, padx=10,
    pady=5, sticky="E")

entree_longueur = ttk.Entry(fenetre)
entree_longueur.grid(row=1, column=1, padx=10, pady=5)

# Entrée pour la charge appliquée
libelle_charge = ttk.Label(fenetre, text="Charge Appliquée (kN) :")
libelle_charge.grid(row=2, column=0, padx=10, pady=5, sticky="E")

entree_charge = ttk.Entry(fenetre)
entree_charge.grid(row=2, column=1, padx=10, pady=5)

# Bouton pour calculer les déformations


def calculer_deformations():
    # Code pour le calcul des déformations
    longueur = float(entree_longueur.get())
    charge = float(entree_charge.get())
    # Exemple de formule simplifiée
    deformations = (charge * longueur**3) / (48 * 500)

    # Affichage des déformations
    resultat.config(text=f"Déformations : {deformations:.2f} mètres")


bouton_calculer = ttk.Button(
    fenetre, text="Calculer", command=calculer_deformations)
bouton_calculer.grid(row=3, column=0, columnspan=2, pady=10)

# Libellé pour afficher les résultats
resultat = ttk.Label(fenetre, text="")
resultat.grid(row=4, column=0, columnspan=2, pady=10)

# Lancement de la boucle principale
fenetre.mainloop()

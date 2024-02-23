import tkinter as tk
from tkinter import ttk

# Définition de la fonction pour calculer la conception de la poutre
def calculer_conception():
    # Récupération des valeurs depuis les champs d'entrée
    longueur_poutre = float(entry_longueur.get())
    charge_permanente = float(entry_charge_permanente.get())
    charge_temporaire = float(entry_charge_temporaire.get())
    resistance_beton = float(entry_resistance_beton.get())
    resistance_acier = float(entry_resistance_acier.get())
    facteur_securite = float(entry_facteur_securite.get())

    # Calcul des charges totales
    charge_totale = charge_permanente + charge_temporaire

    # Vérification des charges
    if charge_totale > resistance_beton:
        resultat.configure(
            text="La charge totale dépasse la résistance du béton. Révision nécessaire.")
        return

    # Calcul des contraintes dans la poutre
    contrainte_beton = charge_totale / (longueur_poutre * facteur_securite)

    # Vérification des contraintes
    if contrainte_beton > resistance_beton:
        resultat.configure(
            text="La contrainte dans le béton dépasse la résistance. Révision nécessaire.")
        return

    # Calcul des armatures minimales
    section_poutre = longueur_poutre ** 2 / 6
    armature_minimale = resistance_acier * section_poutre / \
        (facteur_securite * contrainte_beton)

    # Affichage des résultats
    resultat.configure(
        text=f"Armature minimale requise : {armature_minimale:.2f} mm²")


# Création de l'interface graphique
app = tk.Tk()
app.title("Conception de Poutre en Béton Armé")

# Création des widgets
frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Longueur de la Poutre (m):").grid(
    row=0, column=0, sticky=tk.W)
entry_longueur = ttk.Entry(frame)
entry_longueur.grid(row=0, column=1)

ttk.Label(frame, text="Charge Permanente (kN/m):").grid(row=1,
                                                        column=0, sticky=tk.W)
entry_charge_permanente = ttk.Entry(frame)
entry_charge_permanente.grid(row=1, column=1)

ttk.Label(frame, text="Charge Temporaire (kN/m):").grid(row=2,
                                                        column=0, sticky=tk.W)
entry_charge_temporaire = ttk.Entry(frame)
entry_charge_temporaire.grid(row=2, column=1)

ttk.Label(frame, text="Résistance du Béton (MPa):").grid(
    row=3, column=0, sticky=tk.W)
entry_resistance_beton = ttk.Entry(frame)
entry_resistance_beton.grid(row=3, column=1)

ttk.Label(frame, text="Résistance de l'Acier (MPa):").grid(
    row=4, column=0, sticky=tk.W)
entry_resistance_acier = ttk.Entry(frame)
entry_resistance_acier.grid(row=4, column=1)

ttk.Label(frame, text="Facteur de Sécurité:").grid(
    row=5, column=0, sticky=tk.W)
entry_facteur_securite = ttk.Entry(frame)
entry_facteur_securite.grid(row=5, column=1)

btn_calculer = ttk.Button(frame, text="Calculer", command=calculer_conception)
btn_calculer.grid(row=6, column=0, columnspan=2, pady=10)

resultat = ttk.Label(frame, text="")
resultat.grid(row=7, column=0, columnspan=2)

# Lancement de l'application
app.mainloop()

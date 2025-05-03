import tkinter as tk
import random
from Code_final import renouveler

#aléatoire
def remp_alea():
    empty = [(i, j) for i in range(TAILLE) for j in range(TAILLE) if grid_values[i][j] == 0]
    if empty:
        i, j = random.choice(empty)
        grid_values[i][j] = random.choice([2, 4])

# Initialize game
for _ in range(2):
    remp_alea()
renouveler()

#fin de la partie
def game_over(root):
    root.unbind("<Left>")   # On désactive les touches
    root.unbind("<Right>")
    root.unbind("<Up>")
    root.unbind("<Down>")
    
    game_over_label = tk.Label(
        root,
        text="Game Over",
        font=("Helvetica", 24, "bold"),
        background="#BBADA0",
        foreground="red"
    )
    game_over_label.grid(row=2, column=0, columnspan=4, sticky="nsew")
    #tk.Label ➔ crée une étiquette (un petit cadre avec du texte dedans).
    #root ➔ c'est la fenêtre principale où tu places ce label.
    #text="Game Over" ➔ le texte affiché.
    #font=("Helvetica", 24, "bold") ➔ police d'écriture : Helvetica, taille 24, en gras.
    #background="#BBADA0" ➔ couleur de fond du label (un peu marron clair, comme dans 2048).
    #foreground="red" ➔ couleur du texte (rouge pour attirer l'attention).
    #grid(row=2, column=0, columnspan=4, sticky="nsew") ➔ place le label au centre de la fenêtre, il prend 4 colonnes.
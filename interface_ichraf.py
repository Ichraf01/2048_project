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


def game_over():
    # Désactive les touches fléchées pour empêcher tout autre mouvement
    root.unbind("<Left>")
    root.unbind("<Right>")
    root.unbind("<Up>")
    root.unbind("<Down>")
    # Affiche un message "GAME OVER" au centre de la fenêtre
    game_over_label = tk.Label(root, text="GAME OVER", font=("Helvetica", 24, "bold"), bg="#BBADA0", fg="red")
    game_over_label.place(relx=0.5, rely=0.5, anchor="center")  # Centre le label dans la fenêtre

def you_win():
    # Désactive les touches fléchées lorsque le joueur gagne
    root.unbind("<Left>")
    root.unbind("<Right>")
    root.unbind("<Up>")
    root.unbind("<Down>")
    # Affiche un message "YOU WIN" au centre de la fenêtre
    win_label = tk.Label(root, text="YOU WIN", font=("Helvetica", 24, "bold"), bg="#BBADA0", fg="green")
    win_label.place(relx=0.5, rely=0.5, anchor="center")  # Centre le label dans la fenêtre
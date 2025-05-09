import tkinter as tk
import random

# Color configuration
taille_grille = 4
couleurs = {
    0: "#CDC1B4", 2: "#EEE4DA", 4: "#EDE0C8", 8: "#F2B179",
    16: "#F59563", 32: "#F67C5F", 64: "#F65E3B", 128: "#EDCF72",
    256: "#EDCC61", 512: "#EDC850", 1024: "#EDC53F", 2048: "#EDC22E"
}  # bibliothèque de couleurs

# nada


def merge(ligne, taille_grille):
    nv_ligne = [value for value in ligne if value != 0]  # liste  nt le val de chq cell sauf les 0
    i = 0  # compteur
    while i < len(nv_ligne) - 1:  # condition d'arret: arreter quand i +contena grand que la taille de la list nv_ligne
        if nv_ligne[i] == nv_ligne[i + 1]:  # comparer si les elements de la liste 2 par 2 sont égaux
            nv_ligne[i] *= 2  # si oui on multiplie l'element i par 2
            nv_ligne[i + 1] = 0  # et l'element i+1 devient =0
            i += 1  # finalement on avance le compteur par 1
        i += 1  # si ils sont pas égaux on avance le compteur par 1
    nv_ligne = [value for value in nv_ligne if value != 0]  # actualiser la liste(annuler les 0)
    # completer avec des 0 àn droite jusqu'à ce que taille liste=tailles de la grilles
    return nv_ligne + [0] * (taille_grille - len(nv_ligne))


# creation de notre fenetre tkinter
root = tk.Tk()
root.attributes('-fullscreen',True)
# lier la touche Escape à la fermeture de la fenêtre
root.bind("<Escape>", lambda e: root.destroy())
frame = tk.Frame(root, bg="#BBADA0")
frame.pack(expand=True)
# creation de la grille
TAILLE = taille_grille  # variable contenant la taille de notre grille
cells = []  # une listes qui va stocker la couleur et le texte (donnée graphigues)
# une liste de liste de val numerique qui contient des 0 partout
grid_values = [[0 for _ in range(TAILLE)] for _ in range(TAILLE)]

# nada


def renouveler():
    for i in range(TAILLE):  # parcour de ligne
        for j in range(TAILLE):  # parcour de colonne
            val = grid_values[i][j]  # variable qui stock les valeurs de chaque cases
            cell = cells[i][j]  # variable qui stock les données graphique de chaque cases
            cell.config(
                text=str(val) if val != 0 else "",  # affiche la valeurs si elle est diff de 0 snn elle affiche vide
                # change la couleur de fond selon la valeur de la case, en utilisant le dictionnaire couleurs. Si la valeur n'est pas dans le dictionnaire, utilise la couleur par défaut #CDC1B4
                bg=couleurs.get(val, "#CDC1B4"),
                fg="#776E65" if val < 8 else "#F9F6F2"  # si val<8 change la couleur de text en couleur foncé sinon en couleur claire
            )


# nada
for i in range(TAILLE):  # parcours des lignes
    row = []  # liste qui contient les cells de la linge
    for j in range(TAILLE):  # parcours des colonnes
        cell = tk.Label(
            frame,
            borderwidth=2,
            relief="solid",
            width=10,
            height=5,
            font=("Arial", 16, "bold"),
            justify="center"
        )  # On crée un widget Label Tkinter pour représenter une case de la grille, avec des options de style (bordure, police, etc.).
        # plaçage de chq cell chq cell  le paddig c'est la distance de chaque cell de la grille
        cell.grid(row=i, column=j, padx=5, pady=5)
        row.append(cell)  # ajouter  a la liste de la ligne
    cells.append(row)  # on ajoute la liste obtenue à la liste princpale cells pour avoir une sorte de matrice

# ichraf


def remp_alea():
    # Crée une liste de toutes les positions vides (valeurs égales à 0) dans la grille
    empty = [(i, j) for i in range(TAILLE) for j in range(TAILLE) if grid_values[i][j] == 0]
    # Vérifie s'il existe au moins une case vide
    if empty:
        # Choisit aléatoirement une des positions vides
        i, j = random.choice(empty)
        # Remplit cette case avec un 2 ou un 4, choisis aléatoirement
        grid_values[i][j] = random.choice([2, 4])


# touria
def move(direction):
    global grid_values
    original_grid = [row[:] for row in grid_values]  # Copy original grid

    if direction == "left":
        grid_values = [merge(row, TAILLE) for row in grid_values]
    elif direction == "right":
        grid_values = [merge(row[::-1], TAILLE)[::-1] for row in grid_values]
    elif direction == "up":
        grid_values = list(map(list, zip(*[merge(col, TAILLE) for col in zip(*grid_values)])))
    elif direction == "down":
        grid_values = list(map(list, zip(*[merge(col[::-1], TAILLE)[::-1] for col in zip(*grid_values)])))

    if grid_values != original_grid:
        remp_alea()
        renouveler()
    #Ichraf
    # Vérifie si la valeur 2048 est présente dans une des lignes de la grille.
    # Si c’est le cas, cela signifie que le joueur a gagné,
    # donc on appelle la fonction you_win() et on arrête la suite du code avec return.
    if any(2048 in row for row in grid_values):
        you_win()
        return

    if not can_move():
        game_over()


# touria


def can_move():

    if any(0 in row for row in grid_values):
        return True

    for row in grid_values:
        for i in range(TAILLE - 1):
            if row[i] == row[i + 1]:
                return True

    for col in zip(*grid_values):
        for i in range(TAILLE - 1):
            if col[i] == col[i + 1]:
                return True

    return False

# ichraf


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



# initialization du jeu
# ichraf

# Place deux tuiles aléatoires au début du jeu
for _ in range(2):
    remp_alea()
# Met à jour l'affichage de la grille (fonction définit par Nada)
renouveler()

# touria
root.bind("<Left>", lambda e: move("left"))
root.bind("<Right>", lambda e: move("right"))
root.bind("<Up>", lambda e: move("up"))
root.bind("<Down>", lambda e: move("down"))


def rejouer():
    global grid_values
    # Supprime les messages "GAME OVER" ou "YOU WIN" s'ils existent
    for widget in root.winfo_children():
        #voir si c une instance d'une classe ou une sous classe
        # et si le texte est "GAME OVER" ou "YOU WIN"
        if isinstance(widget, tk.Label) and widget.cget("text") in ["GAME OVER", "YOU WIN"]:
            widget.destroy()

    # Réinitialise la grille avec des zéros
    grid_values = [[0 for _ in range(TAILLE)] for _ in range(TAILLE)]
    # Place deux tuiles aléatoires au début
    for _ in range(2):
        remp_alea()
    # Met à jour l'affichage de la grille
    renouveler()

    # Réactive les touches fléchées
    root.bind("<Left>", lambda e: move("left"))
    root.bind("<Right>", lambda e: move("right"))
    root.bind("<Up>", lambda e: move("up"))
    root.bind("<Down>", lambda e: move("down"))


rejouer_button = tk.Button(root, text="Rejouer", font=("Helvetica", 16, "bold"), bg="#8F7A66", fg="white", command=rejouer)
rejouer_button.pack(pady=10)  # Place le bouton en bas avec un espacement vertical

root.mainloop()

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
    nv_ligne = [value for value in ligne if value != 0]  # liste contenant le val de chq cell sauf les 0
    i = 0  # compteur
    while i < len(nv_ligne) - 1:  # condition d'arret: arreter quand i + grand que la taille de la list nv_ligne
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
root.geometry("400x400")
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
    empty = [(i, j) for i in range(TAILLE) for j in range(TAILLE) if grid_values[i][j] == 0]
    if empty:
        i, j = random.choice(empty)
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
    root.unbind("<Left>")
    root.unbind("<Right>")
    root.unbind("<Up>")
    root.unbind("<Down>")
    game_over_label = tk.Label(root, text="GAME OVER", font=("Helvetica", 24, "bold"), bg="#BBADA0", fg="red")
    game_over_label.place(relx=0.5, rely=0.5, anchor="center")  # Center the label

def you_win():
    root.unbind("<Left>")
    root.unbind("<Right>")
    root.unbind("<Up>")
    root.unbind("<Down>")
    win_label = tk.Label(root, text="YOU WIN", font=("Helvetica", 24, "bold"), bg="#BBADA0", fg="green")
    win_label.place(relx=0.5, rely=0.5, anchor="center")  # Center the label    



# initialization du jeu
# ichraf
for _ in range(2):
    remp_alea()
renouveler()

# touria
root.bind("<Left>", lambda e: move("left"))
root.bind("<Right>", lambda e: move("right"))
root.bind("<Up>", lambda e: move("up"))
root.bind("<Down>", lambda e: move("down"))

root.mainloop()

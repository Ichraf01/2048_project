import tkinter as Tk

#Déplacement d'une cellule NSEW
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


def can_move(grid):
    for row in grid:
        for i in range(len(row) - 1):
            if row[i] == row[i + 1] or row[i] == 0 or row[i + 1] == 0:
                return True
    for col in zip(*grid):   #zip(*grid) transforme les lignes en colonnes pour pouvoir les parcourir de la même façon.
        for i in range(len(col) - 1):
            if col[i] == col[i + 1] or col[i] == 0 or col[i + 1] == 0:
                return True
    return False

#Bouton de controle 
def move(direction, grid):

    if direction == "left":
        grid[:] = [merge(row) for row in grid]
    elif direction == "right":
        grid[:] = [merge(row[::-1])[::-1] for row in grid]
    elif direction == "up":
        grid[:] = list(map(list, zip(*grid)))  # Transpose la grille
        grid[:] = [merge(row) for row in grid]
        grid[:] = list(map(list, zip(*grid)))  # Re-transpose
    elif direction == "down":
        grid[:] = list(map(list, zip(*grid)))  # Transpose la grille
        grid[:] = [merge(row[::-1])[::-1] for row in grid]
        grid[:] = list(map(list, zip(*grid)))  # Re-transpose
    
    
    if not move(grid):
        game_over()



        
#map => executer une fonction sur l'ensemble 
# self => grille qui ca contenir une information
#zip => transposer des cellules !!!!!

#Bouton de controle


def bouton_controle(root):
    button_play = Tk.Button(root, text="Play")
    button_play.grid(row=1, column=0, columnspan=4, sticky="nsew")  #Nord/Sud/Est/West
    root.bind("<Left>", lambda event: move("left"))
    root.bind("<Right>", lambda event: move("right"))  #bind => associer mvt avec clavier
    root.bind("<Up>", lambda event: move("up")) #lambda => une méthode pour ecrire mes fonctions sous formes linéaire
    root.bind("<Down>", lambda event: move("down"))
    

bouton_controle()





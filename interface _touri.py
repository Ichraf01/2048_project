import tkinter as Tk

#Déplacement d'une cellule NSEW
def game_over(root):
    
    root.unbind("<Left>")  #unbind => plus possible de bouger dans les sens L.R.U.D  => Game Over
    root.unbind("<Right>")  # Désactive les événements de touche (flèches directionnelles)
    root.unbind("<Up>")
    root.unbind("<Down>")
    
    
    game_over_label = Tk.Label(root,text="Game Over") # Crée un label "Game Over" et l'affiche
    game_over_label.pack()


def deplacer(direction, grid):

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
    
    
    if not deplacer(grid):
        game_over()


#fusionner des cellules

def merge(ligne, taille_grille):

    nv_ligne= [value for value in ligne if value != 0]   # Supprime les zéros de la ligne
    
    
    for i in range(len(nv_ligne) - 1):  #dernière case
        if nv_ligne[i] == nv_ligne[i + 1]: #fusionner les valeurs pareil pourqu'il y est multiplication 
            nv_ligne[i] *= 2  #multiplier le nombre par 2
            nv_ligne[i + 1] = 0  #chager de cellule
    
    
    nv_ligne = [value for value in nv_ligne if value != 0] # Supp encore les zéros après la fusion
    
    
    return nv_ligne + [0] * (taille_grille - len(nv_ligne)) # Complète la ligne avec des zéros pour atteindre la taille de la grille


        
#map => executer une fonction sur l'ensemble 
# self => grille qui ca contenir une information mais que pour class 
#zip => transposer des cellules !!!!!

#Bouton de controle
def move():
    #...

def bouton_controle(root):
    button_play = Tk.Button(root, text="Play")
    button_play.grid(row=1, column=0, columnspan=4, sticky="nsew")  #Nord/Sud/Est/West
    root.bind("<Left>", lambda event: move("left"))
    root.bind("<Right>", lambda event: move("right"))  #bind => associer mvt avec clavier
    root.bind("<Up>", lambda event: move("up")) #lambda => une méthode pour ecrire mes fonctions sous formes linéaire
    root.bind("<Down>", lambda event: move("down"))
    

bouton_controle()







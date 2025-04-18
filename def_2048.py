# touria 
def new_game(taille_grille):
    grid = [[0] * taille_grille for _ in range(taille_grille)]
    add_tile(grid)
    add_tile(grid)
    update_ui(grid)

import random

def initialize_game():
    # Crée une grille 4x4 initialisée avec des zéros
    grid = [[0] * 4 for _ in range(4)]
    
    # Ajoute deux nombres initiaux (2 ou 4) à la grille
    add_new_number(grid)
    add_new_number(grid)
    
    return grid

def add_new_number(grid):
    # Trouve toutes les cellules vides
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    
    if not empty_cells:
        return
    
    # Choisit une cellule vide au hasard
    i, j = random.choice(empty_cells)
    
    # Place un 2 ou un 4 dans la cellule choisie (90% de chance pour un 2, 10% pour un 4)
    grid[i][j] = 2 if random.random() < 0.9 else 4

def print_grid(grid):
    for row in grid:
        print("\t".join(str(num) if num != 0 else "." for num in row))
    print()

# Initialise le jeu
grid = initialize_game()

# Affiche la grille initiale
print_grid(grid)

def game_over(root):
    
    root.unbind("<Left>")  #unbind => plus possible de bouger dans les sens L.R.U.D  => Game Over
    root.unbind("<Right>")  # Désactive les événements de touche (flèches directionnelles)
    root.unbind("<Up>")
    root.unbind("<Down>")
    
    
    game_over_label = Tk.Label(root,text="Game Over") # Crée un label "Game Over" et l'affiche
    game_over_label.pack()
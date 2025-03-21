from tkinter import *

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

if __name__ == '_main_':
    
    root = Tk()

    canvas = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    
    x0 = 100
    x1 = CANVAS_WIDTH - 100
    y1 = CANVAS_HEIGHT / 2
    y2 = CANVAS_HEIGHT / 2
    y3= CANVAS_HEIGHT / 2
    y4 = CANVAS_HEIGHT / 2
    y5 = CANVAS_HEIGHT / 2
    

    canvas.create_line(x0, y1, x1, y1)
    canvas.create_line(x0, y2, x1, y2)
    canvas.create_line(x0, y3, x1, y3)
    canvas.create_line(x0, y4, x1, y4)
    canvas.create_line(x0, y5, x1, y5)

    if __name__ == "__main__":
        root = tk.Tk()
    root.mainloop()






global sens

def deplacer_cell (cell, sens):
    if sens == "left":
        #cell.grid... for ligne in grille
    elif sens == "right":
        #cell.grid...
    elif sens == "up":
        #cell.grid...
    elif sens == "down":
        #cell.grid
        

# self => grille qui ca contenir une information mais que pour class 
#zip => transposer des cellules !!!!!






# Pour afficher les tuiles dans la matrice 4x4 
taille_grille = 4 # 4x4

for i in range(taille_grille):
    ligne = []
    for j in range(taille_grille):
        cell = tk.Label(self.frame, text="", width=5, height=2)
        cell.grid(row=i, column=j, padx=5, pady=5)
        ligne.append(cell)


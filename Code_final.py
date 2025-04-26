<<<<<<< HEAD
import tkinter as tk
import random


class Game2048:
    def __init__(self, root):
        # Configuration
        self.taille_grille = 4
        self.couleurs = {
            0: "#CDC1B4", 2: "#EEE4DA", 4: "#EDE0C8", 8: "#F2B179",
            16: "#F59563", 32: "#F67C5F", 64: "#F65E3B", 128: "#EDCF72",
            256: "#EDCC61", 512: "#EDC850", 1024: "#EDC53F", 2048: "#EDC22E"
        }

        # GUI Setup
        self.root = root
        self.root.geometry("400x400")
        self.frame = tk.Frame(root, bg="#BBADA0")
        self.frame.pack(expand=True)

        self.cells = []
        self.grid_values = [[0 for _ in range(self.taille_grille)] for _ in range(self.taille_grille)]

        self.create_grid()
        self.add_random_tile()
        self.add_random_tile()
        self.update_display()

        # Key bindings
        self.root.bind("<Left>", self.on_left)
        self.root.bind("<Right>", self.on_right)
        self.root.bind("<Up>", self.on_up)
        self.root.bind("<Down>", self.on_down)

    # Your modified merge function
    def merge(self, row):
        new_row = [value for value in row if value != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [value for value in new_row if value != 0]
        return new_row + [0] * (self.taille_grille - len(new_row))

    def create_grid(self):
        for i in range(self.taille_grille):
            row = []
            for j in range(self.taille_grille):
                cell = tk.Label(
                    self.frame,
                    borderwidth=2,
                    relief="solid",
                    width=10,
                    height=5,
                    font=("Arial", 16, "bold"),
                    justify="center"
                )
                cell.grid(row=i, column=j, padx=5, pady=5)
                row.append(cell)
            self.cells.append(row)

    def update_display(self):
        for i in range(self.taille_grille):
            for j in range(self.taille_grille):
                val = self.grid_values[i][j]
                cell = self.cells[i][j]
                cell.config(
                    text=str(val) if val != 0 else "",
                    bg=self.couleurs.get(val, "#CDC1B4"),
                    fg="#776E65" if val < 8 else "#F9F6F2"
                )

    def add_random_tile(self):
        empty = [(i, j) for i in range(self.taille_grille)
                 for j in range(self.taille_grille) if self.grid_values[i][j] == 0]
        if empty:
            i, j = random.choice(empty)
            self.grid_values[i][j] = random.choice([2, 4])


# Start the game
root = tk.Tk()
game = Game2048(root)
root.mainloop()
=======
>>>>>>> 0fdd39711d2432d600395849feea07298d3ea39b

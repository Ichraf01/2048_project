<<<<<<< HEAD
import tkinter as tk
import random

# Color configuration
taille_grille = 4
couleurs = {
    0: "#CDC1B4", 2: "#EEE4DA", 4: "#EDE0C8", 8: "#F2B179",
    16: "#F59563", 32: "#F67C5F", 64: "#F65E3B", 128: "#EDCF72",
    256: "#EDCC61", 512: "#EDC850", 1024: "#EDC53F", 2048: "#EDC22E"
}


def merge(ligne, taille_grille):
    nv_ligne = [value for value in ligne if value != 0]
    i = 0
    while i < len(nv_ligne) - 1:
        if nv_ligne[i] == nv_ligne[i + 1]:
            nv_ligne[i] *= 2
            nv_ligne[i + 1] = 0
            i += 1
        i += 1
    nv_ligne = [value for value in nv_ligne if value != 0]
    return nv_ligne + [0] * (taille_grille - len(nv_ligne))


# --- GUI SETUP ---
root = tk.Tk()
root.geometry("400x400")
frame = tk.Frame(root, bg="#BBADA0")
frame.pack(expand=True)

TAILLE = taille_grille
cells = []
grid_values = [[0 for _ in range(TAILLE)] for _ in range(TAILLE)]


def update_display():
    for i in range(TAILLE):
        for j in range(TAILLE):
            val = grid_values[i][j]
            cell = cells[i][j]
            cell.config(
                text=str(val) if val != 0 else "",
                bg=couleurs.get(val, "#CDC1B4"),
                fg="#776E65" if val < 8 else "#F9F6F2"
            )


for i in range(TAILLE):
    row = []
    for j in range(TAILLE):
        cell = tk.Label(
            frame,
            borderwidth=2,
            relief="solid",
            width=10,
            height=5,
            font=("Arial", 16, "bold"),
            justify="center"
        )
        cell.grid(row=i, column=j, padx=5, pady=5)
        row.append(cell)
    cells.append(row)


def add_random_tile():
    empty = [(i, j) for i in range(TAILLE) for j in range(TAILLE) if grid_values[i][j] == 0]
    if empty:
        i, j = random.choice(empty)
        grid_values[i][j] = random.choice([2, 4])

# --- CRITICAL FIXES START HERE ---


def move(direction):
    global grid_values
    original_grid = [row[:] for row in grid_values]  # Copy original grid

    # Apply move
    if direction == "left":
        grid_values = [merge(row, TAILLE) for row in grid_values]
    elif direction == "right":
        grid_values = [merge(row[::-1], TAILLE)[::-1] for row in grid_values]
    elif direction == "up":
        grid_values = list(map(list, zip(*[merge(col, TAILLE) for col in zip(*grid_values)])))
    elif direction == "down":
        grid_values = list(map(list, zip(*[merge(col[::-1], TAILLE)[::-1] for col in zip(*grid_values)])))

    # Only continue if grid changed
    if grid_values != original_grid:
        add_random_tile()
        update_display()

    # Always check game over after move
    if not can_move():
        game_over()


def can_move():
    # Check for zeros first (fast check)
    if any(0 in row for row in grid_values):
        return True

    # Check horizontal merges
    for row in grid_values:
        for i in range(TAILLE - 1):
            if row[i] == row[i + 1]:
                return True

    # Check vertical merges
    for col in zip(*grid_values):
        for i in range(TAILLE - 1):
            if col[i] == col[i + 1]:
                return True

    return False


def game_over():
    root.unbind("<Left>")
    root.unbind("<Right>")
    root.unbind("<Up>")
    root.unbind("<Down>")
    game_over_label = tk.Label(
        root,
        text="GAME OVER",
        font=("Helvetica", 24, "bold"),
        bg="#BBADA0",
        fg="red"
    )
    game_over_label.place(relx=0.5, rely=0.5, anchor="center")  # Center the label


# Initialize game
for _ in range(2):
    add_random_tile()
update_display()

root.bind("<Left>", lambda e: move("left"))
root.bind("<Right>", lambda e: move("right"))
root.bind("<Up>", lambda e: move("up"))
root.bind("<Down>", lambda e: move("down"))

root.mainloop()
=======


>>>>>>> 6b365e0772bb0ae77dba3a2162aefd077efbcf1e

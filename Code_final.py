import tkinter as tk
import random


def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


def update_cell(cell):
    new_value = random.randint(-100, 100)
    cell.config(text=str(new_value), bg=random_color())


root = tk.Tk()
root.geometry("400x400")  # Set a fixed window size

# Configure rows and columns of the root window to center the grid
root.rowconfigure(0, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=1)

# Create a frame to hold the grid
frame = tk.Frame(root)
frame.grid(row=1, column=1)  # Place the frame in the center cell of the root grid
frame.configure(bg='skyblue')

# Add cells (widgets) to the frame
cells = []
for i in range(4):  # 4 rows
    for j in range(4):  # 4 columns
        cell = tk.Label(frame, borderwidth=2, relief="solid", width=10, height=5)
        cell.grid(row=i, column=j, padx=5, pady=5)
        cell.bind('<Button-1>', lambda e, c=cell: update_cell(c))
        cells.append(cell)

# Initial update of all cells
for cell in cells:
    update_cell(cell)

root.mainloop()

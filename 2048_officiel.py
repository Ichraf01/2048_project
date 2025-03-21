import tkinter as tk
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

def create_2048_canvas():
    root = tk.Tk()
    root.title("2048 Canvas")
    
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    x0 = 100
    x1 = CANVAS_WIDTH - 100
    y = CANVAS_HEIGHT / 2
    
    # Ici c'est la ligne centrale
    canvas.create_line(x0, y, x1, y, width=2, fill="black")
    
    # Les filles la j'ai fait les rectangles j'ai pas aime les cercles
    canvas.create_rectangle(x0 - 50, y + 50, x0 + 50, y - 50, outline="black", width=2)
    canvas.create_rectangle(x1 - 50, y + 50, x1 + 50, y - 50, outline="black", width=2)
    canvas.create_rectangle((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50, outline="black", width=2)

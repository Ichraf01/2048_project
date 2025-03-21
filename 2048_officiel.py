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

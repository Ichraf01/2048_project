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
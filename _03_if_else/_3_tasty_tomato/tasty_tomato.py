from tkinter import messagebox, simpledialog, Tk
import tkinter as tk

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
color = simpledialog.askstring(title= "Color", prompt= "Type a color red, blue or green")

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if color == 'red' or color == 'Red' or color == 'RED':
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="black")
if color == 'green' or color == 'Green' or color == 'GREEN':
    canvas.create_oval(75, 200, 400, 450, fill="green", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="green", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="black")

if color == 'blue' or color == 'Blue' or color == 'BLUE':
    canvas.create_oval(75, 200, 400, 450, fill="blue", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="blue", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="black")

root.mainloop()

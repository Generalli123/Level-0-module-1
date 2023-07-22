import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    t = turtle.Turtle()
    t.pencolor('blue')
    t.speed(2)
    t.hideturtle()
    # Ask the user what shape they want to draw and store it in a variable
    ans = simpledialog.askstring(title= "Shape", prompt= "Do you want a triangle, square, or circle to be drawn?")
    # Draw the shape requested by the user using if-elif-else statements
    if ans == "triangle" or "Triangle" or "TRIANGLE":
        t.penup()
        t.goto(0, 105)
        t.pendown()
        t.goto(150, -105)
        t.goto(-150, -105)
        t.goto(0, 105)
    if ans == "square":
        t.penup()
        t.goto()

    # Call the turtle .done() method
    turtle.done()

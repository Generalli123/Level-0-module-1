from tkinter import messagebox, simpledialog, Tk
import tkinter as tk
# Write a Python program that asks the user for the radius of a circle.
radius = simpledialog.askstring(title= "Radius", prompt= "Type the radius of a circle")
# Next, ask the user if they would like to calculate the area or circumference of a circle.
answer = simpledialog.askstring(title= "area or circumference", prompt= "Do you want to calculate the area or circumference")
# If they choose area, display the area of the circle using the radius.
if answer == "area":

# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr

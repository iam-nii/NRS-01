import turtle
from customtkinter import *

app = CTk()

canvas = CTkCanvas(app)
canvas.config(width=800, height=500)
canvas.grid(column=0, row=0, padx=70, pady=80, columnspan=4)

screen = turtle.TurtleScreen(canvas)
screen.bgcolor('#E0E0E0')

pen = turtle.RawTurtle(screen)
pen.pensize(8)
pen.forward(25)

app.mainloop()

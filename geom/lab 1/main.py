from tkinter import *
from tkinter.ttk import *
from customtkinter import *
import math

FONT = ('san-serif',20,'normal')
# button = customtkinter.CTkButton(app, font=("<family name>", <size in px>, "<optional keywords>"))

choice = 'menu'


def optionmenu_callback(choice_):
    global choice
    choice = choice_

    # Moving the figure
    if choice_.lower() == 'move':

        # Removing other elements if they exist
        try:
            for element in entries:
                if element.winfo_exists():
                    element.grid_forget()
                else:
                    continue

        except UnboundLocalError:
            # Adding the new elements

            # Position the x label in the first column in the second row
            x_label.grid(column=0, row=1)
            # Position the x_textbox from the second column to the third column in the second row
            xo.grid(column=1, row=1,columnspan=2)
            # Position the y label in the 4th colum
            y_label.grid(column=3, row=1)
            # Position the y_textbox from the 5th column to the 6th column in the second row
            yo.grid(column=4, row=1, columnspan=2)
        else:
            # Adding the new elements
            # Position the x label in the first column in the second row
            x_label.grid(column=0, row=1, padx=0)
            # Position the x_textbox from the second column to the third column in the second row
            xo.grid(column=1, row=1, columnspan=2, padx=0)
            # Position the y label in the 4th colum
            y_label.grid(column=3, row=1, padx=0)
            # Position the y_textbox from the 5th column to the 6th column in the second row
            yo.grid(column=4, row=1, columnspan=2,padx=0)

    # Rotating the figure

    elif choice_.lower() == 'rotate':
        try:
            for element in entries:
                if element.winfo_exists():
                    element.grid_forget()
                else:
                    continue
        except UnboundLocalError:
            angle.grid(row=1, pady=5)
        else:
            angle.grid(row=1, pady=5)

    # Scaling the element
    elif choice_.lower() == 'scale':
        try:
            for element in entries:
                if element.winfo_exists():
                    element.grid_forget()
        except:

            scale.grid(row=1, pady=5)
        else:
            scale.grid(row=1, pady=5)


def draw_rhombus(x ,y , scale = 1,angle = 0):
    # Clear previous drawing
    canvas.delete("all")

    # Length of the diagonals
    D1 = 100 # First diagonal
    D2 = 200 # Second diagonal

    d1 = D1 * scale
    d2 = D2 * scale

    # Calculate the coordinates of the rhombus based on the new center
    points = [
        x + d2 / 2 * math.cos(math.radians(angle)), y - d1 / 2 * math.sin(math.radians(angle)),  # Top
        x + d2 / 2 * math.cos(math.radians(angle + 90)), y - d1 / 2 * math.sin(math.radians(angle + 90)),  # Right
        x + d2 / 2 * math.cos(math.radians(angle + 180)), y - d1 / 2 * math.sin(math.radians(angle + 180)),  # Bottom
        x + d2 / 2 * math.cos(math.radians(angle + 270)), y - d1 / 2 * math.sin(math.radians(angle + 270))  # Left
    ]

    # Draw the rhombus
    canvas.create_polygon(points, outline='black', fill='lightblue')

def go_callback(choice):
    global x0, y0
    if choice == 'menu':
        warning.grid(column=0, row=1, pady=5)
    else:
        if choice == 'move':
            canvas.delete('all')

            new_x = float(options['move']['xo'].get())
            new_y = float(options['move']['yo'].get())
            draw_rhombus(x=x0+new_x,y=y0-new_y)

        else:
            option_value = float(options[choice].get())
            if choice == 'rotate':
                draw_rhombus(x = x0,y = y0, angle=option_value)
            if choice == 'scale':
                if option_value < 0:
                    value = 1/option_value
                    draw_rhombus(x = x0,y = y0, scale=value)
                else:
                    draw_rhombus(x=x0, y=y0, scale=option_value)


# Window settings
# app = TK()
app = CTk()
app.title('Создание изображений  плоских геометрических объектов')
app.geometry("900x600")


# Variable elements
x_label = CTkLabel(app,text="X: ")
y_label = CTkLabel(app,text="Y: ")
xo = CTkEntry(app, placeholder_text='New Center (x)')
yo = CTkEntry(app, placeholder_text='New Center (y)')
angle = CTkEntry(app, placeholder_text='Угол поворота')
scale = CTkEntry(app, placeholder_text='Маштаб')
warning = CTkLabel(app, text='Select an operation',text_color='red',font=('Arial',22,'italic'))

entries = [xo, yo,x_label,y_label, angle, scale, warning]
options = {
    'move': {
        'xo':entries[0],
        'yo':entries[1]
    },
    'rotate': entries[4],
    'scale': entries[5],
}

# Menu
title = StringVar(value="Menu")

optionmenu = CTkOptionMenu(app, values=["Rotate", "Move", "Scale"],
                                font=FONT, variable=title, dropdown_font=FONT,
                                command=optionmenu_callback,width=300)


# Position the menu from the first column to the third in the first row
optionmenu.grid(row=0, pady=3,column=0, columnspan=3)
# Canvas
canvas = CTkCanvas(app)
canvas.config(width=1800,height=900)

# Size of the canvas
canvas_width = canvas.winfo_reqwidth()
canvas_height = canvas.winfo_reqheight()

# Calculate the center of the canvas
x0 = canvas_width / 2
y0 = canvas_height / 2


# Calculate the corner points of the rhombus
# points = [
#     x0, y0 - d1/2,  # Top
#     x0 + d2/2, y0,  # Right
#     x0, y0 + d1/2,  # Bottom
#     x0 - d2/2, y0    # Left
# ]
canvas.grid(column=0,row=2, padx=70,pady=80, columnspan=8)

# Drawing the rhombus
draw_rhombus(x0,y0)

# rhombus = canvas.create_polygon(points,outline="black", fill="lightblue")


# Go button
button = CTkButton(app, text="Go", command=lambda :go_callback(choice.lower()))
button.grid(padx=5, pady=2,column=3)

app.mainloop()

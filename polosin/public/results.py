import customtkinter as c
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class Results:
    def __init__(self,root):
        self.root = root
        self.table = c.CTkScrollableFrame(master=self.root,width=700,height=500)


    def create_result_table(self,temperatures:list,viscosities:list,coordinates:list,prod_temp_visc):
        # code for creating table
        n = c.CTkLabel(master=self.table, text='Координаты по длине канала, м', fg_color='black',width=250)
        temp_title = c.CTkLabel(master=self.table, text='Температура, °C', fg_color='black',width=250)
        viscosity_title = c.CTkLabel(master=self.table, text='Вязкость, Па*с', fg_color='black',width=250)
        n.grid(row=0, column=0)
        temp_title.grid(row=0, column=1)
        viscosity_title.grid(row=0, column=2)
        self.table.pack()

        for i in range(len(temperatures)):
            for j in range(4):
                if j == 1:
                    self.temp = c.CTkLabel(self.table, width=250, height=30, text=f'{temperatures[i]}', fg_color='grey',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.temp.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                elif j == 2:
                    self.viscocity = c.CTkLabel(self.table, width=250, height=30, text=f'{viscosities[i]}', fg_color='grey',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.viscocity.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                else:
                    self.col = c.CTkLabel(self.table, width=250, height=30, text=f'{coordinates[i]}', fg_color='black',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.col.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame

        self.results = c.CTkTextbox(self.root,width=200,height=90)
        self.results.insert(c.END,f'{prod_temp_visc[0]}')
        self.results.insert(c.END,prod_temp_visc[1])
        self.results.insert(c.END,prod_temp_visc[2])
        self.results.pack(pady=10)

    def create_result_graph(self,frame,prop:list,coordinates:list,title:str):
        # Convert lists to numpy arrays
        x = np.array(coordinates)
        y = np.array(prop)

        # # Create a new figure
        # fig, ax = plt.subplots()

        # Create a new figure with a specific size (width, height)
        fig = plt.figure(figsize=(20, 15))

        # Plot the data
        # Plot the data
        ax = fig.add_subplot(111)
        ax.plot(x, y)

        # Set labels and title
        ax.set_xlabel("Координаты по длине канала",fontsize=20)
        ax.set_ylabel(title,fontsize=20)
        ax.set_title(f'График изменения {title} по длине канала',fontsize=25)

        # Create a Tkinter canvas and draw the figure on it
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)
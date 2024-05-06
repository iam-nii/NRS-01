import customtkinter as c
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class Results:
    def __init__(self,root):
        self.root = root

        self.table = c.CTkScrollableFrame(master=self.root,width=700,height=500)
        self.results = c.CTkTextbox(self.root,width=250,height=90,fg_color='white',text_color='black')
        self.canvas = None
        self.ax = None
        self.fig = None

    def update_results(self):
        try:
            self.table.grid_forget()
            self.results.grid_forget()
        except Exception as e:
            print(e)
        else:
            self.table = c.CTkScrollableFrame(master=self.root, width=700, height=500)
            self.results = c.CTkTextbox(self.root, width=250, height=90, fg_color='white', text_color='black')
            print("New table")

    def create_result_table(self,temperatures:list,viscosities:list,coordinates:list,prod_temp_visc):
        self.update_results()
        # code for creating table
        n = c.CTkLabel(master=self.table, text='Координаты по длине канала, м',text_color='black', fg_color='#E9E5E5',width=250)
        temp_title = c.CTkLabel(master=self.table, text='Температура, °C', text_color='black',fg_color='#E9E5E5',width=250)
        viscosity_title = c.CTkLabel(master=self.table, text='Вязкость, Па*с', text_color='black',fg_color='#E9E5E5',width=250)
        n.grid(row=0, column=0)
        temp_title.grid(row=0, column=1)
        viscosity_title.grid(row=0, column=2)
        self.table.grid(column=1,row=1)

        for i in range(len(temperatures)):
            for j in range(4):
                if j == 1:
                    self.temp = c.CTkLabel(self.table, width=250, height=30, text=f'{temperatures[i]}', fg_color='white',
                                             text_color='black', font=('Arial', 16, 'bold'))
                    self.temp.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                elif j == 2:
                    self.viscocity = c.CTkLabel(self.table, width=250, height=30, text=f'{viscosities[i]}', fg_color='white',
                                             text_color='black', font=('Arial', 16, 'bold'))
                    self.viscocity.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                else:
                    self.col = c.CTkLabel(self.table, width=250, height=30, text=f'{coordinates[i]}', fg_color='#E9E5E5',
                                             text_color='black', font=('Arial', 16, 'bold'))
                    self.col.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame

        # self.results = c.CTkTextbox(self.root,width=250,height=90,fg_color='white',text_color='black')
        self.results.insert(c.END,f'{prod_temp_visc[0]}')
        self.results.insert(c.END,prod_temp_visc[1])
        self.results.insert(c.END,prod_temp_visc[2])
        self.results.grid(column=1,row=2)

    # def create_result_graph(self,frame,prop:list,coordinates:list,title_main:str,title_y:str):
    #     # Convert lists to numpy arrays
    #     x = np.array(coordinates)
    #     y = np.array(prop)
    #
    #     # # Create a new figure
    #     # fig, ax = plt.subplots()
    #
    #     # Create a new figure with a specific size (width, height)
    #     fig = plt.figure(figsize=(20, 15))
    #
    #     # Increase the font size of the x and y axis values
    #     plt.xticks(fontsize=14)
    #     plt.yticks(fontsize=14)
    #
    #     # Plot the data
    #     # Plot the data
    #     ax = fig.add_subplot(111)
    #     ax.plot(x, y)
    #
    #     # Set labels and title
    #     ax.set_xlabel("Координата по длине канала, м",fontsize=20)
    #     ax.set_ylabel(title_y.title(),fontsize=20)
    #     ax.set_title(f'График изменения {title_main} по длине канала',fontsize=25)
    #
    #     # Create a Tkinter canvas and draw the figure on it
    #     canvas = FigureCanvasTkAgg(fig, master=frame)
    #     canvas.draw()
    #     canvas.get_tk_widget().pack(pady=10)

    def create_result_graph(self, frame, prop: list, coordinates: list, title_main: str, title_y: str):

        # try:
        #     # Later, when you want to replot the graph with new data
        #     # Clear the current axes
        #     self.ax.cla()
        #
        #     # Clear the current figure
        #     self.fig.clf()
        #
        # except Exception as e:
        #     print(e)
        # else:
        #     print("New graph")

        # Convert lists to numpy arrays
        x = np.array(coordinates)
        y = np.array(prop)

        # Create a new figure with a specific size (width, height)
        self.fig = plt.figure(figsize=(20, 15))

        # # Increase the font size of the x and y axis values
        # plt.xticks(fontsize=18)
        # plt.yticks(fontsize=18)

        # Plot the data
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(x, y)

        # Set labels and title with font size 18
        self.ax.set_xlabel("Координата по длине канала, м", fontsize=22)
        self.ax.set_ylabel(title_y.title(), fontsize=22)
        self.ax.set_title(f'График изменения {title_main} по длине канала', fontsize=22)

        # # Destroy the old canvas if it exists
        # try:
        #     if self.canvas is not None:
        #        self.canvas.get_tk_widget().destroy()
        # except Exception as e:
        #     print(e)

        # Create a Tkinter canvas and draw the figure on it
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.get_tk_widget().grid(column=1,row=1)
        self.canvas.draw()


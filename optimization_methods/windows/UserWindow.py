import customtkinter as c
import json

try:
    file = open("../data/data.json",encoding='utf-8', mode="r")
    new_data = json.load(file)
    file.close()
except FileNotFoundError:
    print(FileNotFoundError)

print(new_data)
FONT = ('Times New Roman', 17)

class UserWindow(c.CTk):
    def __init__(self):
        super().__init__()
        # Geometry and window config
        self.main_width = 1055
        self.main_height = 700
        self.geometry(f"{self.main_width}x{self.main_height}")
        self.configure(title='User Window', fg_color='#FFFFFF', padx=0)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(2, weight=1)

        # Task frame
        self.task_frame = c.CTkFrame(self,width=500,height=700,fg_color='#FFFFFF')
        self.task_frame.grid(column=0,row=0)
        self.list_of_taks = [key for (key,value) in new_data.items()]

        self.task_label = c.CTkLabel(self.task_frame,text="Задание : ",text_color="#000000",font=('Arial', 18),anchor='e')
        self.task_label.grid(column=0,row=0,pady=10,sticky=c.E)

        self.menu_variable = c.StringVar(value="Варианты")
        self.tasks = c.CTkOptionMenu(self.task_frame,values=self.list_of_taks, corner_radius=10,anchor='w',
                                         command=self.select_task, variable=self.menu_variable)
        self.tasks.grid(column=1,row=0,pady=10,sticky=c.W)


        # Text field to print the Задание
        self.task_text = c.CTkTextbox(self.task_frame,width=500,height=500,border_width=1,fg_color="#EBEBEB")

        self.task_text.grid(column=0,row=1,pady=10,padx=20, columnspan=2)

        # Input fields frame
        self.input_frame = c.CTkFrame(self,width=500,height=700,fg_color="#FFFFFF")
        self.input_frame.grid(column=1,row=0)

        self.params_label = c.CTkLabel(self.input_frame,text="Параметры задачи",text_color="#000000",
                                       font=("Arial",25))
        self.params_label.pack(pady=10)

        # Fields
        self.params_fields_frame = c.CTkFrame(self.input_frame,width=500,height=500,border_width=1,fg_color="#FFFFFF",
                                              border_color="#000000")
        self.params_fields_frame.pack()

        #---------------------------Function frame-------------------------#
        self.function_frame = c.CTkFrame(self.params_fields_frame)
        self.function_frame.pack()

        # Function label
        self.function_label = c.CTkLabel(self.function_frame,text="Целевая функция: ",text_color="#000000")
        self.function_label.grid(column=0,row=0)

        # Function entry
        self.function_entry = c.CTkEntry(self.function_frame,width=50,height=40)
        self.function_entry.grid(column=1,row=0)

        #--------------------------Coefficient frame------------------------#
        self.coeff_frame = c.CTkFrame(self.params_fields_frame,fg_color="#FFFFFF")
        self.coeff_frame.pack()

        # Label
        self.coeff_frame_label = c.CTkLabel(self.coeff_frame,text="Нормирующие коэффициенты ")
        self.coeff_frame_label.pack()

        # Coefficient values frame
        self.values_frame = c.CTkFrame(self.coeff_frame,fg_color="#FFFFFF")
        self.values_frame.pack()

        # a frame
        self.a_frame = c.CTkFrame(self.values_frame,fg_color="#FFFFFF")
        self.a_frame.grid(column=0)

        # a
        self.a_label = c.CTkLabel(self.a_frame, text="α : ", text_color="#000000")
        self.a_entry = c.CTkEntry(self.a_frame,width=30,height=30)
        self.a_label.grid(column=0,row=0)
        self.a_entry.grid(column=1,row=0)

        # a1
        self.a1_label = c.CTkLabel(self.a_frame, text="α1 : ", text_color="#000000")
        self.a1_entry = c.CTkEntry(self.a_frame, width=30, height=30)
        self.a1_label.grid(column=0, row=1)
        self.a1_entry.grid(column=1, row=1)
        # b frame
        self.b_frame = c.CTkFrame(self.values_frame,fg_color="#FFFFFF")
        self.b_frame.grid(column=1)

        # b
        self.b_label = c.CTkLabel(self.b_frame, text="β: ", text_color="#000000")
        self.b_entry = c.CTkEntry(self.a_frame, width=30, height=30)
        self.b_label.grid(column=0,row=0)
        self.b_entry.grid(column=1, row=0)

        # b1
        self.b1_label = c.CTkLabel(self.b_frame, text="β1 : ", text_color="#000000")
        self.b1_entry = c.CTkEntry(self.a_frame, width=30, height=30)
        self.b1_label.grid(column=0, row=1)
        self.b1_entry.grid(column=1, row=1)

        # mu frame
        self.mu_frame = c.CTkFrame(self.values_frame,fg_color="#FFFFFF")
        self.mu_frame.grid(column=2)

        # mu
        self.mu_label = c.CTkLabel(self.mu_frame,text="μ : ",text_color="#000000")
        self.mu_entry = c.CTkEntry(self.a_frame, width=30, height=30)
        self.mu_label.grid(column=0, row=0)
        self.mu_entry.grid(column=1, row=0)

        # mu1
        self.mu1_label = c.CTkLabel(self.mu_frame,text="μ1 : ",text_color="#000000")
        self.mu1_entry = c.CTkEntry(self.a_frame, width=30, height=30)
        self.mu1_label.grid(column=0, row=1)
        self.mu1_entry.grid(column=1, row=1)

    def select_task(self, choice):
        print(choice)
        try:
            self.task_text.delete("0.0", "end")  # delete all text
            print("delete success")
        except Exception as e:
            print(f"Error: {e}")

        print(new_data[choice])

        self.task_text.insert("0.0", new_data[choice])
        self.task_text.configure(text_color="#000000", font=FONT)

app = UserWindow()
app.mainloop()
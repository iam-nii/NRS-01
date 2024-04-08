import customtkinter as c

# Create a font object
FONT = ("MS Serif",20)
ENTRY_FONT = ("Arial",16)
class Geometric:
    def __init__(self,params):
        # Geometric values
        geometric_tab = c.CTkTabview(master=params,fg_color='#1F2022',width=430,height=250,state='disabled',text_color='white',
                                     segmented_button_selected_color='#4A4A4A')
        geometric_tab.__setattr__('-alpha',0.5)
        geometric_tab.grid(column=0,row=0,padx=5,pady=10)

        # Main Label
        geometric_frame = geometric_tab.add('Геометрические параметры')
        # geometric_frame.pack(pady=10)

        # Width
        width_frame = c.CTkFrame(master=geometric_frame, fg_color='#1F2022')
        width_frame.pack(pady=10)
        # Label
        width_label = c.CTkLabel(master=width_frame, text='Ширина : ', text_color='#D6D7D8',
                                   font=FONT, justify='right', width=100, anchor='e')
        width_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        width_entry = c.CTkEntry(master=width_frame, fg_color='#1F2022', font=ENTRY_FONT, text_color='#D6D7D8', width=60)
        width_entry.grid(row=0, column=1, padx=5)
        # unit
        width_unit_label = c.CTkLabel(master=width_frame, font=FONT, text='м', text_color='#D6D7D8')
        width_unit_label.grid(row=0, column=2, padx=5)

        # Depth
        depth_frame = c.CTkFrame(master=geometric_frame, fg_color='#1F2022')
        depth_frame.pack(pady=10)
        # Label
        depth_label = c.CTkLabel(master=depth_frame, text='Глубина : ', text_color='#D6D7D8',
                                 font=FONT, justify='right', width=100, anchor='e')
        depth_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        depth_entry = c.CTkEntry(master=depth_frame, fg_color='#1F2022', font=ENTRY_FONT, text_color='#D6D7D8', width=60)
        depth_entry.grid(row=0, column=1, padx=5)
        # unit
        depth_unit_label = c.CTkLabel(master=depth_frame, font=FONT, text='м', text_color='#D6D7D8')
        depth_unit_label.grid(row=0, column=2, padx=5)


        # Length
        length_frame = c.CTkFrame(master=geometric_frame, fg_color='#1F2022')
        length_frame.pack(pady=10)
        # Label
        length_label = c.CTkLabel(master=length_frame, text='Длина : ', text_color='#D6D7D8',
                                 font=FONT, justify='right', width=100, anchor='e')
        length_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        length_entry = c.CTkEntry(master=length_frame, fg_color='#1F2022', font=ENTRY_FONT, text_color='#D6D7D8', width=60)
        length_entry.grid(row=0, column=1, padx=5)
        # unit
        length_unit_label = c.CTkLabel(master=length_frame, font=FONT, text='м', text_color='#D6D7D8')
        length_unit_label.grid(row=0, column=2, padx=5)
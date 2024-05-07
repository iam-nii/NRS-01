import customtkinter as c
from polosin.public.Input_validation import validate_float

# Create a font object
FONT = ("MS Serif", 20)
ENTRY_FONT = ("Arial", 16)


class Geometric:
    def __init__(self, params,DATA):
        # Geometric values
        self.geometric_tab = c.CTkTabview(master=params, fg_color='#CECECE', width=430, height=250, state='disabled',
                                      text_color='black',segmented_button_selected_color='white',
                                                       segmented_button_unselected_color='white',)
        self.geometric_tab.__setattr__('-alpha', 0.5)
        self.geometric_tab.grid(column=0, row=1, padx=5, pady=10)

        # Main Label
        self.geometric_frame = self.geometric_tab.add('Геометрические параметры канала')
        # geometric_frame.pack(pady=10)

        # Width
        self.width_frame = c.CTkFrame(master=self.geometric_frame, fg_color='#CECECE')
        self.width_frame.pack(pady=10)
        # Label
        self.width_label = c.CTkLabel(master=self.width_frame, text='Ширина : ', text_color='#000000',
                                 font=FONT, justify='right', width=100, anchor='e')
        self.width_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.width_entry = c.CTkEntry(master=self.width_frame, fg_color='#CECECE', font=ENTRY_FONT, validate="key",
                                 validatecommand=(params.register(validate_float), "%S"), text_color='#000000',
                                      width=60)
        self.width_entry.grid(row=0, column=1, padx=5)
        # unit
        self.width_unit_label = c.CTkLabel(master=self.width_frame, font=FONT, text='м', text_color='#000000')
        self.width_unit_label.grid(row=0, column=2, padx=5)

        # Depth
        self.depth_frame = c.CTkFrame(master=self.geometric_frame, fg_color='#CECECE')
        self.depth_frame.pack(pady=10)
        # Label
        self.depth_label = c.CTkLabel(master=self.depth_frame, text='Глубина : ', text_color='#000000',
                                 font=FONT, justify='right', width=100, anchor='e')
        self.depth_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.depth_entry = c.CTkEntry(master=self.depth_frame, fg_color='#CECECE', font=ENTRY_FONT, validate="key",
                                 validatecommand=(params.register(validate_float), "%S"), text_color='#000000', width=60)
        self.depth_entry.grid(row=0, column=1, padx=5)
        # unit
        self.depth_unit_label = c.CTkLabel(master=self.depth_frame, font=FONT, text='м', text_color='#000000')
        self.depth_unit_label.grid(row=0, column=2, padx=5)

        # Length
        self.length_frame = c.CTkFrame(master=self.geometric_frame, fg_color='#CECECE')
        self.length_frame.pack(pady=10)
        # Label
        self.length_label = c.CTkLabel(master=self.length_frame, text='Длина : ', text_color='#000000',
                                  font=FONT, justify='right', width=100, anchor='e')
        self.length_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.length_entry = c.CTkEntry(master=self.length_frame, fg_color='#CECECE', font=ENTRY_FONT, validate="key",
                                  validatecommand=(params.register(validate_float), "%S"), text_color='#000000', width=60)
        self.length_entry.grid(row=0, column=1, padx=5)
        # unit
        self.length_unit_label = c.CTkLabel(master=self.length_frame, font=FONT, text='м', text_color='#000000')
        self.length_unit_label.grid(row=0, column=2, padx=5)


        self.width_entry.insert(0,DATA['width'])
        self.depth_entry.insert(0,DATA['depth'])
        self.length_entry.insert(0,DATA['length'])

    def get_values(self):
        return {
            'width': self.width_entry.get(),
            'depth': self.depth_entry.get(),
            'length':self.length_entry.get(),
        }

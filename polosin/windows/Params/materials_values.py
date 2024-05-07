import customtkinter as c
from polosin.public.Input_validation import validate_float

# Create a font object
FONT = ("MS Serif", 20)
ENTRY_FONT = ("Arial", 16)


class Material_values:
    def __init__(self, params,DATA):
        # Material properties
        self.material_props_tab = c.CTkTabview(master=params, fg_color='#CECECE', width=430, height=250, state='disabled',
                                          text_color='black',segmented_button_selected_color='white',
                                                       segmented_button_unselected_color='white')
        self.material_props_tab.grid(row=1, column=1, padx=5, pady=10)

        # Main Label
        self.material_props_frame = self.material_props_tab.add('Параметры свойств материала:')
        # material_frame.pack(pady=10)

        # Density
        self.density_frame = c.CTkFrame(master=self.material_props_frame, fg_color='#CECECE')
        self.density_frame.pack(pady=10)
        # Label
        self.density_label = c.CTkLabel(master=self.density_frame, text='Плотность : ', text_color='#000000',
                                   font=FONT, justify='right', width=250, anchor='e')
        self.density_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.density_entry = c.CTkEntry(master=self.density_frame, fg_color='#CECECE', font=ENTRY_FONT, validate="key",
                                   validatecommand=(params.register(validate_float), "%S"), text_color='#000000',
                                   width=60)
        self.density_entry.grid(row=0, column=1, padx=5)
        # unit
        self.density_unit_label = c.CTkLabel(master=self.density_frame, font=FONT, text='кг/м^3', text_color='#000000')
        self.density_unit_label.grid(row=0, column=2, padx=5)

        # Heat Capacity
        self.heat_capacity_frame = c.CTkFrame(master=self.material_props_frame, fg_color='#CECECE')
        self.heat_capacity_frame.pack(pady=10)
        # Label
        self.heat_capacity_label = c.CTkLabel(master=self.heat_capacity_frame, text='Удельная теплоемкость : ',
                                         text_color='#000000',
                                         font=FONT, justify='right', width=250, anchor='e')
        self.heat_capacity_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.heat_capacity_entry = c.CTkEntry(master=self.heat_capacity_frame, fg_color='#CECECE', font=ENTRY_FONT,
                                         validate="key", validatecommand=(params.register(validate_float), "%S"),
                                         text_color='#000000', width=60)
        self.heat_capacity_entry.grid(row=0, column=1, padx=5)
        # unit
        self.heat_capacity_unit_label = c.CTkLabel(master=self.heat_capacity_frame, font=FONT, text='Дж/(кг*°C)',
                                              text_color='#000000')
        self.heat_capacity_unit_label.grid(row=0, column=2, padx=5)

        # Melting temperature
        self.melting_temp_frame = c.CTkFrame(master=self.material_props_frame, fg_color='#CECECE')
        self.melting_temp_frame.pack(pady=10)
        # Label
        self.melting_temp_label = c.CTkLabel(master=self.melting_temp_frame, text='Температура плавления  : ',
                                        text_color='#000000',
                                        font=FONT, justify='right', width=250, anchor='e')
        self.melting_temp_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.melting_temp_entry = c.CTkEntry(master=self.melting_temp_frame, fg_color='#CECECE', font=ENTRY_FONT, validate="key",
                                        validatecommand=(params.register(validate_float), "%S"),
                                        text_color='#000000', width=60)
        self.melting_temp_entry.grid(row=0, column=1, padx=5)
        # unit
        self.melting_temp_unit_label = c.CTkLabel(master=self.melting_temp_frame, font=FONT, text='°C', text_color='#000000')
        self.melting_temp_unit_label.grid(row=0, column=2, padx=5)

        self.density_entry.insert(0,DATA['density'])
        self.melting_temp_entry.insert(0,DATA['melting_temperature'])
        self.heat_capacity_entry.insert(0,DATA['heat_capacity'])

    def get_values(self):
        return {
            'density':self.density_entry.get(),
            'heat_capacity':self.heat_capacity_entry.get(),
            'melting_temperature':self.melting_temp_entry.get(),
        }
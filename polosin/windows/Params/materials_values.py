import customtkinter as c
# Create a font object
FONT = ("MS Serif",20)
ENTRY_FONT = ("Arial",16)

class Material_values:
    def __init__(self,params):
        # Material properties
        material_props_tab = c.CTkTabview(master=params, fg_color='#1F2022', width=430, height=250, state='disabled',
                                          segmented_button_selected_color='#4A4A4A')
        material_props_tab.grid(row=0, column=1, padx=5, pady=10)

        # Main Label
        material_props_frame = material_props_tab.add('Параметры свойств материала:')
        # material_frame.pack(pady=10)

        # Density
        density_frame = c.CTkFrame(master=material_props_frame, fg_color='#1F2022')
        density_frame.pack(pady=10)
        # Label
        density_label = c.CTkLabel(master=density_frame, text='Плотность : ', text_color='#D6D7D8',
                                   font=FONT, justify='right', width=250, anchor='e')
        density_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        density_entry = c.CTkEntry(master=density_frame, fg_color='#1F2022', font=ENTRY_FONT, text_color='#D6D7D8',
                                   width=60)
        density_entry.grid(row=0, column=1, padx=5)
        # unit
        density_unit_label = c.CTkLabel(master=density_frame, font=FONT, text='кг/м^3', text_color='#D6D7D8')
        density_unit_label.grid(row=0, column=2, padx=5)

        # Heat Capacity
        heat_capacity_frame = c.CTkFrame(master=material_props_frame, fg_color='#1F2022')
        heat_capacity_frame.pack(pady=10)
        # Label
        heat_capacity_label = c.CTkLabel(master=heat_capacity_frame, text='Удельная температура : ',
                                         text_color='#D6D7D8',
                                         font=FONT, justify='right', width=250, anchor='e')
        heat_capacity_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        heat_capacity_entry = c.CTkEntry(master=heat_capacity_frame, fg_color='#1F2022', font=ENTRY_FONT,
                                         text_color='#D6D7D8', width=60)
        heat_capacity_entry.grid(row=0, column=1, padx=5)
        # unit
        heat_capacity_unit_label = c.CTkLabel(master=heat_capacity_frame, font=FONT, text='Дж/кг/°C',
                                              text_color='#D6D7D8')
        heat_capacity_unit_label.grid(row=0, column=2, padx=5)

        # Melting temperature
        melting_temp_frame = c.CTkFrame(master=material_props_frame, fg_color='#1F2022')
        melting_temp_frame.pack(pady=10)
        # Label
        melting_temp_label = c.CTkLabel(master=melting_temp_frame, text='Температура плавления  : ',
                                        text_color='#D6D7D8',
                                        font=FONT, justify='right', width=250, anchor='e')
        melting_temp_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        melting_temp_entry = c.CTkEntry(master=melting_temp_frame, fg_color='#1F2022', font=ENTRY_FONT,
                                        text_color='#D6D7D8', width=60)
        melting_temp_entry.grid(row=0, column=1, padx=5)
        # unit
        melting_temp_unit_label = c.CTkLabel(master=melting_temp_frame, font=FONT, text='°C', text_color='#D6D7D8')
        melting_temp_unit_label.grid(row=0, column=2, padx=5)
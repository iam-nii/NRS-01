import customtkinter as c
from polosin.public.Input_validation import validate_float
# Create a font object
FONT = ("MS Serif",20)
ENTRY_FONT = ("Arial",16)

class Math_model_values:
    def __init__(self,params,DATA):
        # Math model
        self.math_model_tab = c.CTkTabview(master=params, fg_color='#1F2022', width=430, height=250, state='disabled',
                                      segmented_button_selected_color='#4A4A4A')
        self.math_model_tab.grid(row=1, column=1, pady=5)
        self.math_model_frame = self.math_model_tab.add('Эмперические коеффициенты модели')

        # Consistence coefficient
        self.const_coeff_frame = c.CTkFrame(master=self.math_model_frame, fg_color='#1F2022')
        self.const_coeff_frame.pack(pady=10)
        # Label
        self.const_coeff_label = c.CTkLabel(master=self.const_coeff_frame,
                                       text='Коеффициент консистенции при температуре приведения : ',wraplength=300,
                                       text_color='#D6D7D8',font=FONT, justify='right', width=300, anchor='e')
        self.const_coeff_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.const_coeff_entry = c.CTkEntry(master=self.const_coeff_frame, fg_color='#1F2022', font=ENTRY_FONT,validate="key",
                                       validatecommand=(params.register(validate_float), "%S"), text_color='#D6D7D8',
                                   width=60)
        self.const_coeff_entry.grid(row=0, column=1, padx=5)
        # unit
        self.const_coeff_unit_label = c.CTkLabel(master=self.const_coeff_frame, font=FONT, text='Па*с^n', text_color='#D6D7D8')
        self.const_coeff_unit_label.grid(row=0, column=2, padx=5)

        # Temperature viscocity coefficient
        self.temp_viscosity_coeff_frame = c.CTkFrame(master=self.math_model_frame, fg_color='#1F2022')
        self.temp_viscosity_coeff_frame.pack(pady=10)
        # Label
        self.temp_viscosity_coeff_label = c.CTkLabel(master=self.temp_viscosity_coeff_frame, text='Температурный коеффициент вязкости : ',
                                         text_color='#D6D7D8',wraplength=300,font=FONT, justify='right', width=250, anchor='e')
        self.temp_viscosity_coeff_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.temp_viscosity_coeff_entry = c.CTkEntry(master=self.temp_viscosity_coeff_frame, fg_color='#1F2022', font=ENTRY_FONT,
                                                validate="key",validatecommand=(params.register(validate_float), "%S"),
                                         text_color='#D6D7D8', width=60)
        self.temp_viscosity_coeff_entry.grid(row=0, column=1, padx=5)
        # unit
        self.temp_viscosity_coeff_unit_label = c.CTkLabel(master=self.temp_viscosity_coeff_frame, font=FONT, text='1/°C',
                                              text_color='#D6D7D8')
        self.temp_viscosity_coeff_unit_label.grid(row=0, column=2, padx=5)

        # Casting temperature
        self.casting_temp_frame = c.CTkFrame(master=self.math_model_frame, fg_color='#1F2022')
        self.casting_temp_frame.pack(pady=10)
        # Label
        self.casting_temp_label = c.CTkLabel(master=self.casting_temp_frame, text='Температура приведения  : ',
                                        text_color='#D6D7D8',
                                        font=FONT, justify='right', width=250, anchor='e')
        self.casting_temp_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.casting_temp_entry = c.CTkEntry(master=self.casting_temp_frame, fg_color='#1F2022', font=ENTRY_FONT,validate="key",
                                        validatecommand=(params.register(validate_float), "%S"),
                                        text_color='#D6D7D8', width=60)
        self.casting_temp_entry.grid(row=0, column=1, padx=5)
        # unit
        self.casting_temp_unit_label = c.CTkLabel(master=self.casting_temp_frame, font=FONT, text='°C', text_color='#D6D7D8')
        self.casting_temp_unit_label.grid(row=0, column=2, padx=5)

        # Flow Index
        self.flow_index_frame = c.CTkFrame(master=self.math_model_frame, fg_color='#1F2022')
        self.flow_index_frame.pack(pady=10)
        # Label
        self.flow_index_label = c.CTkLabel(master=self.flow_index_frame, text='Индекс течения  : ',wraplength=300,
                                        text_color='#D6D7D8',font=FONT, justify='right', width=250, anchor='e')
        self.flow_index_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.flow_index_entry = c.CTkEntry(master=self.flow_index_frame, fg_color='#1F2022', font=ENTRY_FONT,validate="key",
                                      validatecommand=(params.register(validate_float), "%S"),
                                        text_color='#D6D7D8', width=60)
        self.flow_index_entry.grid(row=0, column=1, padx=5)

        # Heat transfer coefficient
        self.heat_transfer_coeff_frame = c.CTkFrame(master=self.math_model_frame, fg_color='#1F2022')
        self.heat_transfer_coeff_frame.pack(pady=10)
        # Label
        self.heat_transfer_label = c.CTkLabel(master=self.heat_transfer_coeff_frame,
                                         text='Коэффициент теплоотдачи от крышки канала к материалу  : ', wraplength=300,
                                      text_color='#D6D7D8', font=FONT, justify='right', width=250, anchor='e')
        self.heat_transfer_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.heat_transfer_entry = c.CTkEntry(master=self.heat_transfer_coeff_frame, fg_color='#1F2022', font=ENTRY_FONT,
                                         validate="key",validatecommand=(params.register(validate_float), "%S"),
                                      text_color='#D6D7D8', width=60)
        self.heat_transfer_entry.grid(row=0, column=1, padx=5)
        # unit
        self.heat_transfer_unit_label = c.CTkLabel(master=self.heat_transfer_coeff_frame, font=FONT, text='Вт/м^2*С', text_color='#D6D7D8')
        self.heat_transfer_unit_label.grid(row=0, column=2, padx=5)


        self.flow_index_entry.insert(0,DATA['flow_index'])
        self.casting_temp_entry.insert(0,DATA['casting_temperature'])
        self.const_coeff_entry.insert(0,DATA['consistency_coefficient'])
        self.temp_viscosity_coeff_entry.insert(0,DATA['temp_viscosity_coefficient'])
        self.heat_transfer_entry.insert(0,DATA['cover_heat_transfer_coefficient'])


    def get_values(self):
        return {
            'consistency_coefficient': self.const_coeff_entry.get(),
            'temp_viscosity_coeff':self.temp_viscosity_coeff_entry.get(),
            'casting_temp': self.casting_temp_entry.get(),
            'flow_index': self.flow_index_entry.get(),
            'heat_transfer':self.heat_transfer_entry.get(),
        }

import customtkinter as c
from polosin.public.Input_validation import validate_float
# Create a font object
FONT = ("MS Serif",20)
ENTRY_FONT = ("Arial",16)

class Process_values:
    def __init__(self,params):
        self.process_params_tab = c.CTkTabview(master=params, fg_color='#1F2022', width=430, height=350, state='disabled',
                                          segmented_button_selected_color='#4A4A4A')
        self.process_params_tab.grid(row=1, column=0, pady=5)

        # Main Label
        self.process_params_frame = self.process_params_tab.add('Режимные параметры процесса:')
        # self.process_params_frame.pack(pady=10)

        # Cover speed
        self.cover_speed_frame = c.CTkFrame(master=self.process_params_frame, fg_color='#1F2022')
        self.cover_speed_frame.pack(pady=10)
        # Label
        self.cover_speed_label = c.CTkLabel(master=self.cover_speed_frame, text='Скорость крышки : ', text_color='#D6D7D8',
                                   font=FONT, justify='right', width=250, anchor='e')
        self.cover_speed_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.cover_speed_entry = c.CTkEntry(master=self.cover_speed_frame, fg_color='#1F2022', font=ENTRY_FONT,validate="key",
                                       validatecommand=(params.register(validate_float), "%S"), text_color='#D6D7D8',
                                   width=60)
        self.cover_speed_entry.grid(row=0, column=1, padx=5)
        # unit
        self.cover_speed_unit_label = c.CTkLabel(master=self.cover_speed_frame, font=FONT, text='м/с', text_color='#D6D7D8')
        self.cover_speed_unit_label.grid(row=0, column=2, padx=5)

        # Cover temperature
        self.cover_temperature_frame = c.CTkFrame(master=self.process_params_frame, fg_color='#1F2022')
        self.cover_temperature_frame.pack(pady=10)
        # Label
        self.cover_temperature_label = c.CTkLabel(master=self.cover_temperature_frame, text='Температура крышки : ',
                                         text_color='#D6D7D8',
                                         font=FONT, justify='right', width=250, anchor='e')
        self.cover_temperature_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.cover_temperature_entry = c.CTkEntry(master=self.cover_temperature_frame, fg_color='#1F2022', font=ENTRY_FONT,
                                             validate="key",validatecommand=(params.register(validate_float), "%S"),
                                         text_color='#D6D7D8', width=60)
        self.cover_temperature_entry.grid(row=0, column=1, padx=5)
        # unit
        self.cover_temperature_unit_label = c.CTkLabel(master=self.cover_temperature_frame, font=FONT, text='°C',
                                              text_color='#D6D7D8')
        self.cover_temperature_unit_label.grid(row=0, column=2, padx=5)

        # Calculation step
        self.calculation_step_frame = c.CTkFrame(master=self.process_params_frame, fg_color='#1F2022')
        self.calculation_step_frame.pack(pady=10)
        # Label
        self.calculation_step_label = c.CTkLabel(master=self.calculation_step_frame, text='Шаг расчёта по длине канала  : ',
                                        text_color='#D6D7D8',
                                        font=FONT, justify='right', width=250, anchor='e')
        self.calculation_step_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.calculation_step_entry = c.CTkEntry(master=self.calculation_step_frame, fg_color='#1F2022', font=ENTRY_FONT,
                                            validate="key",validatecommand=(params.register(validate_float), "%S"),
                                        text_color='#D6D7D8', width=60)
        self.calculation_step_entry.grid(row=0, column=1, padx=5)
        # unit
        self.calculation_step_unit_label = c.CTkLabel(master=self.calculation_step_frame, font=FONT, text='м', text_color='#D6D7D8')
        self.calculation_step_unit_label.grid(row=0, column=2, padx=5)

    def get_values(self):
        return {
            'cover_speed':self.cover_speed_entry.get(),
            'cover_temperature':self.cover_temperature_entry.get(),
            'step':self.calculation_step_entry.get()
        }
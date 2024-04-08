import customtkinter as c
# Create a font object
FONT = ("MS Serif",20)
ENTRY_FONT = ("Arial",16)

class Process_values:
    def __init__(self,params):
        process_params_tab = c.CTkTabview(master=params, fg_color='#1F2022', width=430, height=350, state='disabled',
                                          segmented_button_selected_color='#4A4A4A')
        process_params_tab.grid(row=1, column=0, pady=5)

        # Main Label
        process_params_frame = process_params_tab.add('Режимные параметры процесса:')
        # process_params_frame.pack(pady=10)

        # Cover speed
        cover_speed_frame = c.CTkFrame(master=process_params_frame, fg_color='#1F2022')
        cover_speed_frame.pack(pady=10)
        # Label
        cover_speed_label = c.CTkLabel(master=cover_speed_frame, text='Скорость крышки : ', text_color='#D6D7D8',
                                   font=FONT, justify='right', width=250, anchor='e')
        cover_speed_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        cover_speed_entry = c.CTkEntry(master=cover_speed_frame, fg_color='#1F2022', font=ENTRY_FONT, text_color='#D6D7D8',
                                   width=60)
        cover_speed_entry.grid(row=0, column=1, padx=5)
        # unit
        cover_speed_unit_label = c.CTkLabel(master=cover_speed_frame, font=FONT, text='м/с', text_color='#D6D7D8')
        cover_speed_unit_label.grid(row=0, column=2, padx=5)

        # Cover temperature
        cover_temperature_frame = c.CTkFrame(master=process_params_frame, fg_color='#1F2022')
        cover_temperature_frame.pack(pady=10)
        # Label
        cover_temperature_label = c.CTkLabel(master=cover_temperature_frame, text='Температура крышки : ',
                                         text_color='#D6D7D8',
                                         font=FONT, justify='right', width=250, anchor='e')
        cover_temperature_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        cover_temperature_entry = c.CTkEntry(master=cover_temperature_frame, fg_color='#1F2022', font=ENTRY_FONT,
                                         text_color='#D6D7D8', width=60)
        cover_temperature_entry.grid(row=0, column=1, padx=5)
        # unit
        cover_temperature_unit_label = c.CTkLabel(master=cover_temperature_frame, font=FONT, text='°C',
                                              text_color='#D6D7D8')
        cover_temperature_unit_label.grid(row=0, column=2, padx=5)

        # Calculation step
        calculation_step_frame = c.CTkFrame(master=process_params_frame, fg_color='#1F2022')
        calculation_step_frame.pack(pady=10)
        # Label
        calculation_step_label = c.CTkLabel(master=calculation_step_frame, text='Шаг расчёта по длине канала  : ',
                                        text_color='#D6D7D8',
                                        font=FONT, justify='right', width=250, anchor='e')
        calculation_step_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        calculation_step_entry = c.CTkEntry(master=calculation_step_frame, fg_color='#1F2022', font=ENTRY_FONT,
                                        text_color='#D6D7D8', width=60)
        calculation_step_entry.grid(row=0, column=1, padx=5)
        # unit
        calculation_step_unit_label = c.CTkLabel(master=calculation_step_frame, font=FONT, text='м', text_color='#D6D7D8')
        calculation_step_unit_label.grid(row=0, column=2, padx=5)
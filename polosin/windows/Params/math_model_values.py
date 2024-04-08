import customtkinter as c
# Create a font object
FONT = ("MS Serif",20)
ENTRY_FONT = ("Arial",16)

class Math_model_values:
    def __init__(self,params):
        # Math model
        math_model_tab = c.CTkTabview(master=params, fg_color='#1F2022', width=430, height=250, state='disabled',
                                      segmented_button_selected_color='#4A4A4A')
        math_model_tab.grid(row=1, column=1, pady=5)
        math_model_frame = math_model_tab.add('Эмперические коеффициенты мат. модели')

        # Consistence coefficient
        const_coeff_frame = c.CTkFrame(master=math_model_frame, fg_color='#1F2022')
        const_coeff_frame.pack(pady=10)
        # Label
        const_coeff_label = c.CTkLabel(master=const_coeff_frame,
                                       text='Коеффициент консистенции при температуре плавления : ',wraplength=300,
                                       text_color='#D6D7D8',font=FONT, justify='right', width=300, anchor='e')
        const_coeff_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        const_coeff_entry = c.CTkEntry(master=const_coeff_frame, fg_color='#1F2022', font=ENTRY_FONT, text_color='#D6D7D8',
                                   width=60)
        const_coeff_entry.grid(row=0, column=1, padx=5)
        # unit
        const_coeff_unit_label = c.CTkLabel(master=const_coeff_frame, font=FONT, text='Па*с^n', text_color='#D6D7D8')
        const_coeff_unit_label.grid(row=0, column=2, padx=5)

        # Temperature viscocity coefficient
        temp_viscosity_coeff_frame = c.CTkFrame(master=math_model_frame, fg_color='#1F2022')
        temp_viscosity_coeff_frame.pack(pady=10)
        # Label
        temp_viscosity_coeff_label = c.CTkLabel(master=temp_viscosity_coeff_frame, text='Температурны коеффициент вязкости : ',
                                         text_color='#D6D7D8',wraplength=300,font=FONT, justify='right', width=250, anchor='e')
        temp_viscosity_coeff_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        temp_viscosity_coeff_entry = c.CTkEntry(master=temp_viscosity_coeff_frame, fg_color='#1F2022', font=ENTRY_FONT,
                                         text_color='#D6D7D8', width=60)
        temp_viscosity_coeff_entry.grid(row=0, column=1, padx=5)
        # unit
        temp_viscosity_coeff_unit_label = c.CTkLabel(master=temp_viscosity_coeff_frame, font=FONT, text='1/°C',
                                              text_color='#D6D7D8')
        temp_viscosity_coeff_unit_label.grid(row=0, column=2, padx=5)

        # Casting temperature
        casting_temp_frame = c.CTkFrame(master=math_model_frame, fg_color='#1F2022')
        casting_temp_frame.pack(pady=10)
        # Label
        casting_temp_label = c.CTkLabel(master=casting_temp_frame, text='Температура приведения  : ',
                                        text_color='#D6D7D8',
                                        font=FONT, justify='right', width=250, anchor='e')
        casting_temp_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        casting_temp_entry = c.CTkEntry(master=casting_temp_frame, fg_color='#1F2022', font=ENTRY_FONT,
                                        text_color='#D6D7D8', width=60)
        casting_temp_entry.grid(row=0, column=1, padx=5)
        # unit
        casting_temp_unit_label = c.CTkLabel(master=casting_temp_frame, font=FONT, text='°C', text_color='#D6D7D8')
        casting_temp_unit_label.grid(row=0, column=2, padx=5)

        # Flow Index
        flow_index_frame = c.CTkFrame(master=math_model_frame, fg_color='#1F2022')
        flow_index_frame.pack(pady=10)
        # Label
        flow_index_label = c.CTkLabel(master=flow_index_frame, text='Шаг расчёта по длине канала  : ',wraplength=300,
                                        text_color='#D6D7D8',font=FONT, justify='right', width=250, anchor='e')
        flow_index_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        flow_index_entry = c.CTkEntry(master=flow_index_frame, fg_color='#1F2022', font=ENTRY_FONT,
                                        text_color='#D6D7D8', width=60)
        flow_index_entry.grid(row=0, column=1, padx=5)

        # Heat transfer coefficient
        heat_transfer_coeff_frame = c.CTkFrame(master=math_model_frame, fg_color='#1F2022')
        heat_transfer_coeff_frame.pack(pady=10)
        # Label
        heat_transfer_label = c.CTkLabel(master=heat_transfer_coeff_frame,
                                         text='Коэффициент теплоотдачи от крышки канала к материалу  : ', wraplength=300,
                                      text_color='#D6D7D8', font=FONT, justify='right', width=250, anchor='e')
        heat_transfer_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        heat_transfer_entry = c.CTkEntry(master=heat_transfer_coeff_frame, fg_color='#1F2022', font=ENTRY_FONT,
                                      text_color='#D6D7D8', width=60)
        heat_transfer_entry.grid(row=0, column=1, padx=5)
        # unit
        heat_transfer_unit_label = c.CTkLabel(master=heat_transfer_coeff_frame, font=FONT, text='Вт/м^2*С', text_color='#D6D7D8')
        heat_transfer_unit_label.grid(row=0, column=2, padx=5)
import customtkinter as c
import tkinter as tk
from polosin.public.Input_validation import validate_float

# Create a font object
FONT = ("MS Serif", 20)
ENTRY_FONT = ("Arial", 16)


class Solution_method_values:
    def __init__(self, params,DATA):
        # Material properties
        self.solution_method_params_tab = c.CTkTabview(master=params,
                                                       width=430,
                                                       height=100,
                                                       state='disabled',
                                                       segmented_button_selected_color='#E3E3E3',
                                                       segmented_button_unselected_color='#E3E3E3',
                                                       segmented_button_fg_color="black",
                                                       fg_color='#CECECE',
                                                       text_color="#000870",
                                                       border_width=1
                                                       )
        # self.solution_method_params_tab.grid(row=0, column=1, padx=5, pady=10)
        self.solution_method_params_tab.pack(pady=10)

        # Main Label
        self.solution_method_params_frame = self.solution_method_params_tab.add('Параметры метода решения:')
        # self.solution_method_params_frame.pack()
        # material_frame.pack(pady=10)

        # Calculation step
        self.calculation_step_frame = c.CTkFrame(master=self.solution_method_params_frame, fg_color='#CECECE')
        self.calculation_step_frame.grid(row=1, column=0, sticky=tk.W, pady=10, padx=5)
        # Label
        self.calculation_step_label = c.CTkLabel(master=self.calculation_step_frame,
                                                 text='Шаг расчета по длине канала  : ',
                                                 text_color='#000000',
                                                 font=FONT, justify='right', width=250, anchor='e')
        self.calculation_step_label.grid(row=0, column=0, padx=5, sticky='e')
        # Entry
        self.calculation_step_entry = c.CTkEntry(master=self.calculation_step_frame, fg_color='#CECECE',
                                                  font=ENTRY_FONT,border_width=2,
                                                  validate="key",
                                                  validatecommand=(params.register(validate_float), "%S"),
                                                  text_color='#000000', width=60)
        # unit
        self.calculation_step_unit_label = c.CTkLabel(master=self.calculation_step_frame, font=FONT, text='м',
                                                   text_color='#000000')
        self.calculation_step_unit_label.grid(row=0, column=2, padx=5)

        # self.calculation_step_entry = c.CTkEntry(master=self.calculation_step_frame, fg_color='#CECECE',
        #                                          font=ENTRY_FONT,
        #                                          # validate="key",
        #                                          # validatecommand=(params.register(validate_float), "%S"),
        #                                          text_color='#000000', width=60)
        self.calculation_step_entry.insert(0,'0.1')
        self.calculation_step_entry.grid(row=0, column=1, padx=5)

    def get_values(self):
        return {
            'step':self.calculation_step_entry.get(),
        }
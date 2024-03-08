import customtkinter

class Admin_login(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")

        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
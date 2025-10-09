import customtkinter as ctk

class TaxCalculator:
    def __init__(self):
        # Initialize our window
        self.window = ctk.CTk()
        self.window.title('Tax Calculator')
        self.window.geometry('280x200')
        self.window.resizable(False, False)


         # Initialize our window
        self.padding: dict = {'padx': 20, 'pady': 10}
        
        # Income label and entry
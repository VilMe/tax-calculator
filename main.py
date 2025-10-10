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
        
        # Income label and entr
        self.income_label = ctk.CTkLabel(self.window, text='Income: ')
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        # Income label and entry
        self.tax_label = ctk.CTkLabel(self.window, text='Percent: ')
        self.tax_label.grid(row=1, column=0, **self.padding)
        self.tax_entry = ctk.CTkEntry(self.window)
        self.tax_entry.grid(row=1, column=1, **self.padding)

        # Result label annd entry
        self.result_label = ctk.CTkLabel(self.window, text='Result: ')
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.grid(row=2, column=1, **self.padding)


    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()
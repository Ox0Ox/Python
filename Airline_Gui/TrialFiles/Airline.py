import customtkinter as ct

ct.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

from customtkinter import *

class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.compText = StringVar()

        # configure window
        self.title("BravoAirlines")
        self.geometry(f"{1100}x{580}")


        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = ct.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = ct.CTkLabel(self.sidebar_frame, text="BravoAirlines", font=ct.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = ct.CTkButton(self.sidebar_frame, command = self.printer)
        self.logo_label.grid(row=0, column=0, padx=20)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.printtest = ct.CTkLabel(self.sidebar_frame, textvariable= self.compText, font=ct.CTkFont(size=20, weight="bold"))
        self.printtest.grid(row=2, column=0, padx=20, pady=(20, 10))


    
    def printer(self):
        self.compText.set('Hello Yall')

if __name__ == "__main__":
    app = App()
    app.mainloop()
import tkinter as tk
from tkinter import ttk

from MenuBar import MenuBar
from StartPage import StartPage
from SecondPage import SecondPage


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {
            "script_name": tk.StringVar(),
        }

        # MenuBar
        menubar = MenuBar(self)
        self.config(menu=menubar)

        # Grid config
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.geometry("500x200")

        # Estilo general de las ventanas.
        # Paleta de colores (de más oscuro a más claro): #343d46 #4f5b66 #65737e #a7adba #c0c5ce
        s = ttk.Style()
        s.configure('.', background='#c0c5ce')
        s.configure('TButton', background='#343d46')

        # Carga todas las ventanas.
        self.frames = {}
        for F in (StartPage, SecondPage): 
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew") 
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

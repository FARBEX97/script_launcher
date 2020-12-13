import tkinter as tk
from tkinter import ttk
import json

from MenuBar import MenuBar
from MainFrame import MainFrame
from StartPage import StartPage
from RunScriptPage import RunScriptPage


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("ScriptLauncher by FARBEX97")

        self.shared_data = {
            "script_name": tk.StringVar(),
            "src_dir": json.load(open("config.json"))["src_dir"]
        }

        # MenuBar
        menubar = MenuBar(self)
        self.config(menu=menubar)

        # MainFrame config
        container = MainFrame(self)
        self.geometry("500x200")

        # Window style config
        s = ttk.Style()
        s.configure(".", background="#c0c5ce")
        s.configure("TButton", background="#343d46")

        # Load all frames
        self.frames = {}
        for F in (StartPage, RunScriptPage): 
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

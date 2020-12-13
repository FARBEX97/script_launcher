import tkinter as ttk


class MainFrame(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # Frame config
        self.pack(side="top", fill="both", expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
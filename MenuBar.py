import sys
import tkinter as tk
from popup.Popup import Popup

class MenuBar(tk.Menu):

    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        self.add_command(label="Hello!")
        self.add_command(label="Exit", underline=1, command=self.quit)

    def quit(self):
        answer = Popup.ask_yes_no("Exit", "Are you sure you want to quit?")
        
        if answer:
            sys.exit(0)
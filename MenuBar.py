import sys
import tkinter as tk


class MenuBar(tk.Menu):

    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        self.add_command(label="Hello!")
        self.add_command(label="Exit", underline=1, command=self.quit)

    def quit(self):
        sys.exit(0)
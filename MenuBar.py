import sys
import json
import webbrowser  
import tkinter as tk
from pycofeece.Popup import Popup

class MenuBar(tk.Menu):

    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        self.parent = parent

        self.settings_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Settings", menu=self.settings_menu, command=self.configure)
        self.settings_menu.add_command(label="Source Directory", command=self.select_source_directory)
        self.add_command(label="About", command=self.about)
        self.add_command(label="Exit", underline=1, command=self.quit)


    def select_source_directory(self):
        """Changes source directory and restart app"""
        # Change source direrctory
        new_src_dir = Popup.ask_directory()
        config = json.load(open("config.json"))
        config["src_dir"] = new_src_dir
        json.dump(config, open("config.json", "w"))

        # Restart App
        self.parent.destroy()
        self.parent.__init__()


    def about(self):
        webbrowser.open(r"https://github.com/FARBEX97/script_launcher", new=0, autoraise=True)


    def quit(self):
        answer = Popup.ask_yes_no("Exit", "Are you sure you want to quit?")
        
        if answer:
            sys.exit(0)
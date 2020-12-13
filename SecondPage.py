import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Oswald", 12)

class SecondPage(ttk.Frame):

    def __init__(self, parent, controller):


        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Script Name", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        def exec_script(script_name):
            print(script_name)
            exec(open(f".\\scripts\\{script_name}.py").read())
            
        btn = ttk.Button(self, text="Run script",command= lambda: exec_script(controller.shared_data["script_name"]))
        btn.pack(pady=10,padx=10)
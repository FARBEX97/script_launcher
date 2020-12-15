import tkinter as tk
from tkinter import ttk
import os
from RunScriptPage import RunScriptPage

import coffeece
from coffeece.SysWalker import SysWalker
from coffeece.Popup import Popup

LARGE_FONT= ("Oswald", 12)

class StartPage(ttk.Frame):

    def __init__(self, parent, controller):


        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Choose script.", font=LARGE_FONT)
        label.grid(row=0, column= 0, pady=10,padx=20)


        combo = ttk.Combobox(self, state="readonly")
        def make_py_list():
            """Generate .py files list"""
            try:
                src_dir = controller.shared_data["src_dir"]
                return SysWalker.list_files_by_type(src_dir,".py")
            except FileNotFoundError:
                return list()

        combovalues = make_py_list()
        combo["values"] = combovalues
        combo.grid(row=0, column= 1)

        def choose_script():
            controller.shared_data["script_name"] = combo.get()
            controller.show_frame(RunScriptPage)

        btn = ttk.Button(self, text="Run", command=choose_script)
        btn.grid(row=0, column=2, pady=10,padx=20)

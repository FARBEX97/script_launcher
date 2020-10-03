import tkinter as tk
from tkinter import ttk
import os
import glob
from SecondPage import SecondPage

LARGE_FONT= ("Verdana", 12)

class StartPage(ttk.Frame):

    def __init__(self, parent, controller):


        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Elige un script.", font=LARGE_FONT)
        label.grid(row=0, column= 0, pady=10,padx=20)


        combo = ttk.Combobox(self, state="readonly")
        def generar_lista_py():
            """Generar lista con los archivos .xlsx de la carpeta."""
            cwd = os.getcwd()
            os.chdir(cwd+'\\scripts\\')
            py_files = []
            for file in glob.glob("*.py"):
                file = file.replace('.py','')
                py_files.append(file)
            os.chdir(cwd)
            return py_files
        combovalues = generar_lista_py()
        combo["values"] = combovalues
        combo.grid(row=0, column= 1)

        def elegir_script():
            controller.shared_data["script_name"] = combo.get()
            # Transformar valor en página
            controller.show_frame(SecondPage)

        btn = ttk.Button(self, text='Aceptar', command=elegir_script)
        btn.grid(row=0, column=2, pady=10,padx=20)

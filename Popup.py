import os
from tkinter import Frame
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showinfo
import pandas as pd



class Popup():

    def show_info(message):
        showinfo("Información",message)


    def ask_file():
        """Ask user for a file. Returns path as string"""
        Tk().withdraw()
        path = askopenfilename()
        filename = os.path.relpath(path, '.') 
        return filename


    def ask_directory():
        """Pide un directorio a traves de una ventana emergente, devuelve string con el path"""
        Tk().withdraw()
        path = askdirectory()
        folder_selected = os.path.abspath(path) 
        return folder_selected
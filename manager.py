from tkinter import *  
from tkinter import ttk
from container import Container
from login import Login
from login import Registro
import sys 
import os

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Manager")
        self.geometry("1100x650+120+20")
        self.resizable(False, False)
        
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.configure(bg="#f0f0f0")
        
        # Configuración de la grilla para que los frames se ajusten
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (Login, Registro, Container):
            frame = F(container, self)  # instanciamos la clase
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # apilamos los frames
        
        self.show_frame(Container)
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

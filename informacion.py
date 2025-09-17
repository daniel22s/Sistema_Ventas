from tkinter import *
import tkinter as tk

class Informacion(tk.Frame):
    
    def __init__(self, padre,**kwargs):
        super().__init__(padre,**kwargs)
        self.widgets()
        
    def widgets(self):
        Label(self, text="Información", font=("Helvetica", 20), bg="#232327", fg="white").pack(pady=20)
        
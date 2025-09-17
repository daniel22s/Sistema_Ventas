from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk

class Inventario(tk.Frame):
    
    def __init__(self, padre, **kwargs):
        super().__init__(padre, **kwargs)
        self.widgets()
        
    def widgets(self):
        self.configure(bg="#232327")
        Label(self, text="Inventario", font=("Helvetica", 20), bg="#232327", fg="white").pack(pady=20)
        
        # LabelFrame para artículos
        canvas_articulos = tk.LabelFrame(self, text="Artículos", bg="#232327", fg="white", font=("Helvetica", 12, "bold"))
        canvas_articulos.place(x=300, y=10, width=780, height=500)
        
        # Canvas dentro del LabelFrame
        self.canvas = tk.Canvas(canvas_articulos, bg="#1E1E2E", highlightthickness=1, highlightbackground="#3E3EB8")
        self.scrollbar = tk.Scrollbar(canvas_articulos, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#1E1E2E")
        
        # Vincular scrollbar
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Empaquetar canvas y scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    #------------------------------------------------------------------------------------
    
        LabelFrame_Buscar = tk.LabelFrame(self, text="Buscar Artículo", bg="#232327", fg="white", font=("Helvetica", 12, "bold"))
        LabelFrame_Buscar.place(x=10, y=10, width=280, height=80)
        
        self.combox_Buscar = ttk.Combobox(LabelFrame_Buscar , font=("Helvetica", 10), state="readonly", width=10)
        self.combox_Buscar.place(x=5, y=5, width=260, height=40)
        
    #=========================================================================================================
        LabelFrame_Agregar = tk.LabelFrame(self, text="Agregar Artículo", bg="#232327", fg="white", font=("Helvetica", 12, "bold"))
        LabelFrame_Agregar.place(x=10, y=100, width=280, height=420)
        
        # Etiquetas y campos de entrada
        labels = ["Código:", "Nombre:", "Descripción:", "Cantidad:", "Precio:"]
        self.entries = {}
        
        for i, label in enumerate(labels):
            lbl = tk.Label(LabelFrame_Agregar, text=label, bg="#232327", fg="white", font=("Helvetica", 10))
            lbl.place(x=5, y=10 + i*70)
            
            entry = tk.Entry(LabelFrame_Agregar, font=("Helvetica", 10))
            entry.place(x=5, y=35 + i*70, width=260, height=25)
            self.entries[label] = entry
        
        # Botones
        self.btn_agregar = tk.Button(LabelFrame_Agregar, text="Agregar", bg="#3E3EB8", fg="white", activebackground="#5C5CE6", activeforeground="white", bd=0, font=("Helvetica", 10, "bold"), cursor="hand2")
        self.btn_agregar.place(x=5, y=365, width=80, height=30)
        
        self.btn_modificar = tk.Button(LabelFrame_Agregar, text="Modificar", bg="#3E3EB8", fg="white", activebackground="#5C5CE6", activeforeground="white", bd=0, font=("Helvetica", 10, "bold"), cursor="hand2")
        self.btn_modificar.place(x=100, y=365, width=80, height=30)
        
        self.btn_eliminar = tk.Button(LabelFrame_Agregar, text="Eliminar", bg="#3E3EB8", fg="white", activebackground="#5C5CE6", activeforeground="white", bd=0, font=("Helvetica", 10, "bold"), cursor="hand2")
        self.btn_eliminar.place(x=195, y=365, width=80, height=30)
import tkinter as tk
from ventas import Ventas
from inventario import Inventario
from clientes import Clientes
from pedido import Pedidos
from proveedor import Proveedor
from informacion import Informacion

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre, bg="#1E1E2E", highlightthickness=1, highlightbackground="#2A2A40")  
        self.controlador = controlador
        self.place(x=0, y=0, width=1100, height=650)

        self.widgets()
        self.frames = {}
        self.buttons = {}

        for i in (Ventas, Inventario, Clientes, Pedidos, Proveedor, Informacion):
            frame = i(self)
            frame.configure(bg="#232327", highlightthickness=1, highlightbackground="#3E3EB8")
            self.frames[i] = frame
            frame.place(x=0, y=40, width=1100, height=610)

        self.show_frame(Ventas)
        
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        
    def ventas(self):
        self.show_frame(Ventas)
        
    def inventario(self):
        self.show_frame(Inventario)
    
    def clientes(self):
        self.show_frame(Clientes)
        
    def pedidos(self):
        self.show_frame(Pedidos)
    
    def proveedor(self):
        self.show_frame(Proveedor)
        
    def informacion(self):
        self.show_frame(Informacion)
        
    def widgets(self):
        # Aquí puedes crear botones o menús con el mismo estilo moderno
        frame2 = tk.Frame(self, bg="#2A2A40", height=40)
        frame2.place(x=0, y=0, width=1100, height=40)
        
        self.btn_ventas = tk.Button(frame2, text="Ventas", command=self.ventas, bg="#3E3EB8", fg="white", activebackground="#5C5CE6", activeforeground="white", bd=0, font=("Helvetica", 10, "bold"), cursor="hand2")
        self.btn_ventas.place(width=184, height=45)
        
        self.btn_inventario = tk.Button(frame2, text="Inventario", command=self.inventario, bg="#3E3EB8", fg="white", activebackground="#5C5CE6", activeforeground="white", bd=0, font=("Helvetica", 10, "bold"), cursor="hand2")
        self.btn_inventario.place(x=184, width=184, height=45)
        
        self.btn_clientes = tk.Button(frame2, text="Clientes", command=self.clientes, bg="#3E3EB8", fg="white", activebackground="#5C5CE6", activeforeground="white", bd=0, font=("Helvetica", 10, "bold"), cursor="hand2")
        self.btn_clientes.place(x=368, width=184, height=45)
        
        self.btn_pedidos = tk.Button(frame2, text="Pedidos", command=self.pedidos, bg="#3E3EB8", fg="white", activebackground="#5C5CE6", activeforeground="white", bd=0, font=("Helvetica", 10, "bold"), cursor="hand2")
        self.btn_pedidos.place(x=552, width=184, height=45)
        
        self.btn_proveedor = tk.Button(frame2, text="Proveedor", command=self.proveedor, bg="#3E3EB8", fg="white", activebackground="#5C5CE6", activeforeground="white", bd=0, font=("Helvetica", 10, "bold"), cursor="hand2")
        self.btn_proveedor.place(x=736, width=184, height=45)   
        
        self.btn_informacion = tk.Button(frame2, text="Información", command=self.informacion, bg="#3E3EB8", fg="white", activebackground="#5C5CE6", activeforeground="white", bd=0, font=("Helvetica", 10, "bold"), cursor="hand2")
        self.btn_informacion.place(x=920, width=184, height=45)
        
        self.buttons = [self.btn_ventas, self.btn_inventario, self.btn_clientes, self.btn_pedidos, self.btn_proveedor, self.btn_informacion ]
        
        
        
        
         
    """
        button_style = {
            "bg": "#3E3EB8",
            "fg": "white",
            "activebackground": "#5C5CE6",
            "activeforeground": "white",
            "bd": 0,
            "font": ("Helvetica", 10, "bold"),
            "cursor": "hand2"
        }
        botones_info = [
            ("Ventas", Ventas),
            ("Inventario", Inventario),
            ("Clientes", Clientes),
            ("Pedidos", Pedidos),
            ("Proveedor", Proveedor),
            ("Información", Informacion)
        ]
        for idx, (text, frame) in enumerate(botones_info):
            btn = tk.Button(self, text=text, command=lambda f=frame: self.show_frame(f), **button_style)
            btn.place(x=10 + idx*110, y=5, width=100, height=30)
            self.buttons[text] = btn
            # Puedes agregar efectos hover si lo deseas
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#5C5CE6"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#3E3EB8"))
        """""
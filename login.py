from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
from container import Container   # asegúrate de que Container esté en otro archivo

class Login(tk.Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0, y=0, width=1100, height=650)
        self.controlador = controlador
        self.widgets()
        
    def widgets(self):
        fondo = tk.Frame(self, bg="#232327")
        fondo.pack(fill="both", expand=True)
        fondo.place(x=0, y=0, width=1100, height=650)
        
        self.bg_img = Image.open("img/login.jpg")   
        self.bg_img = self.bg_img.resize((1100, 650), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = tk.Label(fondo, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame1 = tk.Frame(fondo, bg="#232327", bd=5)
        frame1.place(x=350, y=150, width=400, height=350)
        
        user = tk.Label(frame1, text="Usuario", bg="#232327", fg="white", font=("Helvetica", 12))
        user.place(x=50, y=50)
        self.username = tk.Entry(frame1, font=("Helvetica", 12))
        self.username.place(x=50, y=80, width=300, height=30)
        self.username.focus()
        
        pas = tk.Label(frame1, text="Contraseña", bg="#232327", fg="white", font=("Helvetica", 12))
        pas.place(x=50, y=130)
        self.password = tk.Entry(frame1, show="*", font=("Helvetica", 12))
        self.password.place(x=50, y=160, width=300, height=30)
        
        btn1 = tk.Button(frame1, text="Iniciar Sesion", command=self.login, bg="#3E3EB8", fg="white",
                         activebackground="#5C5CE6", activeforeground="white", bd=0,
                         font=("Helvetica", 12, "bold"), cursor="hand2")
        btn1.place(x=50, y=220, width=300, height=40)
        
        btn2 = tk.Button(frame1, text="Registrarse", command=self.registro, bg="#3E3EB8", fg="white",
                         activebackground="#5C5CE6", activeforeground="white", bd=0,
                         font=("Helvetica", 12, "bold"), cursor="hand2")
        btn2.place(x=50, y=270, width=300, height=40)
        
    # 🔹 Método para iniciar sesión
    def login(self):
        usuario = self.username.get()
        clave = self.password.get()
        
        # Ejemplo de validación simple
        if usuario == "admin" and clave == "1234":
            self.controlador.show_frame(Container)   # Pasa al Container
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    # 🔹 Método para ir al registro
    def registro(self):
        self.controlador.show_frame(Registro)

class Registro(tk.Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.widgets()
        
    def widgets(self):
        fondo = tk.Frame(self, bg="#232327")
        fondo.pack(fill="both", expand=True)
        fondo.place(x=0, y=0, width=1100, height=650)
        
        self.bg_img = Image.open("img/login.jpg")   
        self.bg_img = self.bg_img.resize((1100, 650), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = tk.Label(fondo, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame1 = tk.Frame(fondo, bg="#232327", bd=5)
        frame1.place(x=350, y=150, width=400, height=350)
        
        user = tk.Label(frame1, text="Usuario", bg="#232327", fg="white", font=("Helvetica", 12))
        user.place(x=50, y=50)
        self.username = tk.Entry(frame1, font=("Helvetica", 12))
        self.username.place(x=50, y=80, width=300, height=30)
        self.username.focus()
        
        pas = tk.Label(frame1, text="Contraseña", bg="#232327", fg="white", font=("Helvetica", 12))
        pas.place(x=50, y=130)
        self.password = tk.Entry(frame1, show="*", font=("Helvetica", 12))
        self.password.place(x=50, y=160, width=300, height=30)
        
        key = tk.Label(frame1, text="Confirmar Contraseña", bg="#232327", fg="white", font=("Helvetica", 12))
        key.place(x=50, y=210)
        self.key = tk.Entry(frame1, show="*", font=("Helvetica", 12))
        self.key.place(x=50, y=240, width=300, height=30)
        
        
        btn3 = tk.Button(frame1, text="Iniciar Sesion", command=self.login, bg="#3E3EB8", fg="white",
                         activebackground="#5C5CE6", activeforeground="white", bd=0,
                         font=("Helvetica", 12, "bold"), cursor="hand2")
        btn3.place(x=50, y=220, width=300, height=40)
        
        btn4 = tk.Button(frame1, text="Registrarse", command=self.registro, bg="#3E3EB8", fg="white",
                         activebackground="#5C5CE6", activeforeground="white", bd=0,
                         font=("Helvetica", 12, "bold"), cursor="hand2")
        btn4.place(x=50, y=270, width=300, height=40)

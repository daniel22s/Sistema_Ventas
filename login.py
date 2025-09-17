from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from container import Container   # tu ventana principal

# -------------------- LOGIN --------------------
class Login(tk.Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.widgets()
        
    def widgets(self):
        # Fondo
        fondo = tk.Frame(self, bg="#232327")
        fondo.pack(fill="both", expand=True)
        
        # Imagen de fondo
        self.bg_img = Image.open("img/login.jpg")   
        self.bg_img = self.bg_img.resize((1100, 650), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = tk.Label(fondo, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Frame central
        frame1 = tk.Frame(fondo, bg="#232327", bd=5)
        frame1.place(x=350, y=150, width=400, height=350)
        
        # Usuario
        user_label = tk.Label(frame1, text="Usuario", bg="#232327", fg="white", font=("Helvetica", 12))
        user_label.place(x=50, y=50)
        self.username = tk.Entry(frame1, font=("Helvetica", 12))
        self.username.place(x=50, y=80, width=300, height=30)
        self.username.focus()
        
        # Contraseña
        pass_label = tk.Label(frame1, text="Contraseña", bg="#232327", fg="white", font=("Helvetica", 12))
        pass_label.place(x=50, y=130)
        self.password = tk.Entry(frame1, show="*", font=("Helvetica", 12))
        self.password.place(x=50, y=160, width=300, height=30)
        
        # Botones
        btn_login = tk.Button(frame1, text="Iniciar Sesion", command=self.login, bg="#3E3EB8", fg="white",
                              activebackground="#5C5CE6", activeforeground="white", bd=0,
                              font=("Helvetica", 12, "bold"), cursor="hand2")
        btn_login.place(x=50, y=220, width=300, height=40)
        
        btn_reg = tk.Button(frame1, text="Registrarse", command=lambda: self.controlador.show_frame(Registro),
                            bg="#3E3EB8", fg="white", activebackground="#5C5CE6", activeforeground="white",
                            bd=0, font=("Helvetica", 12, "bold"), cursor="hand2")
        btn_reg.place(x=50, y=270, width=300, height=40)
        
    # Método para login
    def login(self):
        usuario = self.username.get()
        clave = self.password.get()

        con = sqlite3.connect("usuarios.db")
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                usuario TEXT UNIQUE, 
                clave TEXT
            )
        """)
        
        cur.execute("SELECT * FROM usuarios WHERE usuario=? AND clave=?", (usuario, clave))
        user = cur.fetchone()
        con.close()

        if user:
            messagebox.showinfo("Bienvenido", f"Hola {usuario}")
            self.controlador.show_frame(Container)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")


# -------------------- REGISTRO --------------------
class Registro(tk.Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.widgets()
        
    def widgets(self):
        # Fondo
        fondo = tk.Frame(self, bg="#232327")
        fondo.pack(fill="both", expand=True)
        
        # Imagen de fondo
        self.bg_img = Image.open("img/login.jpg")   
        self.bg_img = self.bg_img.resize((1100, 650), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = tk.Label(fondo, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Frame central
        frame1 = tk.Frame(fondo, bg="#232327", bd=5)
        frame1.place(x=350, y=150, width=400, height=350)
        
        # Usuario nuevo
        user_label = tk.Label(frame1, text="Nuevo Usuario", bg="#232327", fg="white", font=("Helvetica", 12))
        user_label.place(x=50, y=50)
        self.username = tk.Entry(frame1, font=("Helvetica", 12))
        self.username.place(x=50, y=80, width=300, height=30)
        self.username.focus()
        
        # Contraseña nueva
        pass_label = tk.Label(frame1, text="Nueva Contraseña", bg="#232327", fg="white", font=("Helvetica", 12))
        pass_label.place(x=50, y=130)
        self.password = tk.Entry(frame1, show="*", font=("Helvetica", 12))
        self.password.place(x=50, y=160, width=300, height=30)
        
        # Botones
        btn_save = tk.Button(frame1, text="Guardar", command=self.guardar, bg="#3E3EB8", fg="white",
                             activebackground="#5C5CE6", activeforeground="white", bd=0,
                             font=("Helvetica", 12, "bold"), cursor="hand2")
        btn_save.place(x=50, y=220, width=300, height=40)
        
        btn_back = tk.Button(frame1, text="Volver", command=lambda: self.controlador.show_frame(Login),
                             bg="#3E3EB8", fg="white", activebackground="#5C5CE6", activeforeground="white",
                             bd=0, font=("Helvetica", 12, "bold"), cursor="hand2")
        btn_back.place(x=50, y=270, width=300, height=40)
    
    # Método para guardar usuario en SQLite
    def guardar(self):
        usuario = self.username.get()
        clave = self.password.get()

        if not usuario or not clave:
            messagebox.showwarning("Atención", "Debes completar todos los campos")
            return

        con = sqlite3.connect("usuarios.db")
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                usuario TEXT UNIQUE, 
                clave TEXT
            )
        """)

        try:
            cur.execute("INSERT INTO usuarios (usuario, clave) VALUES (?, ?)", (usuario, clave))
            con.commit()
            messagebox.showinfo("Registro", f"Usuario {usuario} registrado con éxito")
            self.controlador.show_frame(Login)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El usuario ya existe")
        finally:
            con.close()

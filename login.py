# login.py
import sys, os
import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
from container import Container  # tu ventana principal

# -------------------- FUNCION PARA RUTAS EN PyInstaller --------------------
def resource_path(relative_path):
    """ Devuelve la ruta absoluta de un recurso, compatible con PyInstaller """
    try:
        base_path = sys._MEIPASS  # Carpeta temporal usada por PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# -------------------- LOGIN --------------------
class Login(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.place(x=0, y=0, width=1100, height=650)
        self.widgets()

    def widgets(self):
        # Fondo
        fondo = Frame(self, bg="#232327")
        fondo.place(x=0, y=0, width=1100, height=650)

        # Imagen de fondo
        img = Image.open(resource_path("img/login.jpg"))
        img = img.resize((1100, 650), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(img)
        self.bg_label = Label(fondo, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame del formulario
        frame1 = Frame(fondo, bg="#232327", bd=5)
        frame1.place(x=350, y=150, width=400, height=350)

        Label(frame1, text="Usuario", bg="#232327", fg="white", font=("Helvetica", 12)).place(x=50, y=50)
        self.username = Entry(frame1, font=("Helvetica", 12))
        self.username.place(x=50, y=80, width=300, height=30)
        self.username.focus()

        Label(frame1, text="Contraseña", bg="#232327", fg="white", font=("Helvetica", 12)).place(x=50, y=130)
        self.password = Entry(frame1, show="*", font=("Helvetica", 12))
        self.password.place(x=50, y=160, width=300, height=30)

        Button(frame1, text="Iniciar Sesion", command=self.login, bg="#3E3EB8", fg="white",
               activebackground="#5C5CE6", activeforeground="white", bd=0,
               font=("Helvetica", 12, "bold"), cursor="hand2").place(x=50, y=220, width=300, height=40)

        Button(frame1, text="Registrarse", command=lambda: self.controlador.show_frame(Registro),
               bg="#3E3EB8", fg="white", activebackground="#5C5CE6", activeforeground="white", bd=0,
               font=("Helvetica", 12, "bold"), cursor="hand2").place(x=50, y=270, width=300, height=40)

    def login(self):
        usuario = self.username.get()
        clave = self.password.get()

        if not usuario or not clave:
            messagebox.showwarning("Atención", "Debes ingresar usuario y contraseña")
            return

        con = sqlite3.connect("usuarios.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario TEXT UNIQUE,
                        clave TEXT)""")

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
    ADMIN_CODE = "SENATI123"  # Código secreto del admin

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.place(x=0, y=0, width=1100, height=650)
        self.widgets()

    def widgets(self):
        fondo = Frame(self, bg="#232327")
        fondo.place(x=0, y=0, width=1100, height=650)

        # Imagen de fondo
        img = Image.open(resource_path("img/login.jpg"))
        img = img.resize((1100, 650), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(img)
        self.bg_label = Label(fondo, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame de registro
        frame1 = Frame(fondo, bg="#232327", bd=5)
        frame1.place(x=350, y=150, width=400, height=400)

        Label(frame1, text="Nuevo Usuario", bg="#232327", fg="white", font=("Helvetica", 12)).place(x=50, y=30)
        self.username = Entry(frame1, font=("Helvetica", 12))
        self.username.place(x=50, y=60, width=300, height=30)
        self.username.focus()

        Label(frame1, text="Nueva Contraseña", bg="#232327", fg="white", font=("Helvetica", 12)).place(x=50, y=110)
        self.password = Entry(frame1, show="*", font=("Helvetica", 12))
        self.password.place(x=50, y=140, width=300, height=30)

        Label(frame1, text="Código de Seguridad", bg="#232327", fg="white", font=("Helvetica", 12)).place(x=50, y=190)
        self.code_entry = Entry(frame1, font=("Helvetica", 12))
        self.code_entry.place(x=50, y=220, width=300, height=30)

        Button(frame1, text="Guardar", command=self.guardar, bg="#3E3EB8", fg="white",
               activebackground="#5C5CE6", activeforeground="white", bd=0,
               font=("Helvetica", 12, "bold"), cursor="hand2").place(x=50, y=270, width=300, height=40)

        Button(frame1, text="Volver", command=lambda: self.controlador.show_frame(Login),
               bg="#3E3EB8", fg="white", activebackground="#5C5CE6", activeforeground="white",
               bd=0, font=("Helvetica", 12, "bold"), cursor="hand2").place(x=50, y=320, width=300, height=40)

    def guardar(self):
        usuario = self.username.get()
        clave = self.password.get()
        codigo = self.code_entry.get()

        if not usuario or not clave or not codigo:
            messagebox.showwarning("Atención", "Debes completar todos los campos")
            return

        if codigo != self.ADMIN_CODE:
            messagebox.showerror("Error", "Código de seguridad incorrecto")
            return

        con = sqlite3.connect("usuarios.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario TEXT UNIQUE,
                        clave TEXT)""")

        try:
            cur.execute("INSERT INTO usuarios (usuario, clave) VALUES (?, ?)", (usuario, clave))
            con.commit()
            messagebox.showinfo("Registro", f"Usuario {usuario} registrado con éxito")
            self.controlador.show_frame(Login)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El usuario ya existe")
        finally:
            con.close()

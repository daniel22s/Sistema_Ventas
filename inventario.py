from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class Inventario(tk.Frame):
    def __init__(self, padre, **kwargs):
        super().__init__(padre, **kwargs)
        self.configure(bg="#232327")
        self.crear_tabla_db()
        self.widgets()
        self.mostrar_articulos()

    #------------------- Base de datos -------------------
    def crear_tabla_db(self):
        self.con = sqlite3.connect("inventario.db")
        self.cur = self.con.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS articulos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT UNIQUE,
                nombre TEXT,
                descripcion TEXT,
                cantidad INTEGER,
                precio REAL
            )
        """)
        self.con.commit()

    #------------------- Interfaz -------------------
    def widgets(self):
        # ---------- TÍTULO ----------
        Label(self, text="Inventario", font=("Helvetica", 20), bg="#232327", fg="white").pack(pady=10)

        # ---------- BUSCADOR ----------
        frame_buscar = tk.LabelFrame(self, text="Buscar Artículo", bg="#232327", fg="white", font=("Helvetica", 12, "bold"))
        frame_buscar.pack(padx=10, pady=10, fill="x")

        self.combox_buscar = ttk.Combobox(frame_buscar, values=["Código", "Nombre", "Descripción"], state="readonly", width=12)
        self.combox_buscar.current(0)
        self.combox_buscar.pack(side="left", padx=5, pady=5)

        self.entry_buscar = tk.Entry(frame_buscar, font=("Helvetica", 12))
        self.entry_buscar.pack(side="left", padx=5, pady=5, fill="x", expand=True)

        self.btn_buscar = tk.Button(frame_buscar, text="Buscar", bg="#3E3EB8", fg="white",
                                    command=self.buscar_articulo, font=("Helvetica", 10, "bold"))
        self.btn_buscar.pack(side="left", padx=5)

        self.btn_mostrar_todos = tk.Button(frame_buscar, text="Mostrar Todos", bg="#3E3EB8", fg="white",
                                           command=self.mostrar_articulos, font=("Helvetica", 10, "bold"))
        self.btn_mostrar_todos.pack(side="left", padx=5)

        # ---------- TREEVIEW ARTÍCULOS ----------
        frame_tabla = tk.LabelFrame(self, text="Artículos", bg="#232327", fg="white", font=("Helvetica", 12, "bold"))
        frame_tabla.pack(padx=10, pady=10, fill="both", expand=True)

        columnas = ("Código", "Nombre", "Descripción", "Cantidad", "Precio")
        self.tabla_articulos = ttk.Treeview(frame_tabla, columns=columnas, show="headings", selectmode="browse")
        for col in columnas:
            self.tabla_articulos.heading(col, text=col)
            self.tabla_articulos.column(col, width=120)
        self.tabla_articulos.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla_articulos.yview)
        self.tabla_articulos.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")

        # Selección solo al hacer click
        self.tabla_articulos.bind("<<TreeviewSelect>>", self.seleccionar_articulo)

        # ---------- AGREGAR / MODIFICAR ----------
        frame_agregar = tk.LabelFrame(self, text="Agregar / Modificar Artículo", bg="#232327", fg="white", font=("Helvetica", 12, "bold"))
        frame_agregar.pack(padx=10, pady=10, fill="x")

        labels = ["Código", "Nombre", "Descripción", "Cantidad", "Precio"]
        self.entries = {}
        for label in labels:
            subframe = tk.Frame(frame_agregar, bg="#232327")
            subframe.pack(fill="x", pady=2)

            tk.Label(subframe, text=label+":", bg="#232327", fg="white", font=("Helvetica", 10), width=12, anchor="w").pack(side="left")
            entry = tk.Entry(subframe, font=("Helvetica", 10))
            entry.pack(side="left", fill="x", expand=True)
            self.entries[label] = entry

        # ---------- BOTONES ----------
        frame_botones = tk.Frame(frame_agregar, bg="#232327")
        frame_botones.pack(pady=5)

        self.btn_agregar = tk.Button(frame_botones, text="Agregar", bg="#3E3EB8", fg="white",
                                     command=self.agregar_articulo, font=("Helvetica", 10, "bold"))
        self.btn_agregar.pack(side="left", padx=5)

        self.btn_modificar = tk.Button(frame_botones, text="Modificar", bg="#3E3EB8", fg="white",
                                       command=self.modificar_articulo, font=("Helvetica", 10, "bold"))
        self.btn_modificar.pack(side="left", padx=5)

        self.btn_eliminar = tk.Button(frame_botones, text="Eliminar", bg="#3E3EB8", fg="white",
                                      command=self.eliminar_articulo, font=("Helvetica", 10, "bold"))
        self.btn_eliminar.pack(side="left", padx=5)

        self.btn_limpiar = tk.Button(frame_botones, text="Limpiar", bg="#3E3EB8", fg="white",
                                     command=self.limpiar_campos, font=("Helvetica", 10, "bold"))
        self.btn_limpiar.pack(side="left", padx=5)

    #------------------- Funciones CRUD -------------------
    def mostrar_articulos(self):
        for item in self.tabla_articulos.get_children():
            self.tabla_articulos.delete(item)
        self.cur.execute("SELECT codigo, nombre, descripcion, cantidad, precio FROM articulos")
        for row in self.cur.fetchall():
            self.tabla_articulos.insert("", "end", values=row)

    def agregar_articulo(self):
        try:
            codigo = self.entries["Código"].get()
            nombre = self.entries["Nombre"].get()
            descripcion = self.entries["Descripción"].get()
            cantidad = int(self.entries["Cantidad"].get())
            precio = float(self.entries["Precio"].get())
            self.cur.execute("INSERT INTO articulos (codigo, nombre, descripcion, cantidad, precio) VALUES (?, ?, ?, ?, ?)",
                             (codigo, nombre, descripcion, cantidad, precio))
            self.con.commit()
            messagebox.showinfo("Éxito", "Artículo agregado")
            self.mostrar_articulos()
            self.limpiar_campos()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El código ya existe")
        except ValueError:
            messagebox.showerror("Error", "Cantidad y Precio deben ser números")

    def modificar_articulo(self):
        selected = self.tabla_articulos.focus()
        if not selected:
            messagebox.showwarning("Atención", "Seleccione un artículo")
            return
        values = self.tabla_articulos.item(selected, "values")
        codigo = values[0]
        try:
            nombre = self.entries["Nombre"].get()
            descripcion = self.entries["Descripción"].get()
            cantidad = int(self.entries["Cantidad"].get())
            precio = float(self.entries["Precio"].get())
            self.cur.execute("UPDATE articulos SET nombre=?, descripcion=?, cantidad=?, precio=? WHERE codigo=?",
                             (nombre, descripcion, cantidad, precio, codigo))
            self.con.commit()
            messagebox.showinfo("Éxito", "Artículo modificado")
            self.mostrar_articulos()
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "Cantidad y Precio deben ser números")

    def eliminar_articulo(self):
        selected = self.tabla_articulos.focus()
        if not selected:
            messagebox.showwarning("Atención", "Seleccione un artículo")
            return
        values = self.tabla_articulos.item(selected, "values")
        codigo = values[0]
        self.cur.execute("DELETE FROM articulos WHERE codigo=?", (codigo,))
        self.con.commit()
        messagebox.showinfo("Éxito", "Artículo eliminado")
        self.mostrar_articulos()
        self.limpiar_campos()

    def buscar_articulo(self):
        criterio = self.combox_buscar.get()
        valor = self.entry_buscar.get()
        if criterio == "Código":
            sql = "SELECT codigo, nombre, descripcion, cantidad, precio FROM articulos WHERE codigo LIKE ?"
        elif criterio == "Nombre":
            sql = "SELECT codigo, nombre, descripcion, cantidad, precio FROM articulos WHERE nombre LIKE ?"
        else:
            sql = "SELECT codigo, nombre, descripcion, cantidad, precio FROM articulos WHERE descripcion LIKE ?"
        self.cur.execute(sql, ('%'+valor+'%',))
        rows = self.cur.fetchall()
        for item in self.tabla_articulos.get_children():
            self.tabla_articulos.delete(item)
        for row in rows:
            self.tabla_articulos.insert("", "end", values=row)

    def seleccionar_articulo(self, event):
        selected = self.tabla_articulos.focus()
        if selected:
            values = self.tabla_articulos.item(selected, "values")
            self.entries["Código"].config(state="normal")
            self.entries["Código"].delete(0, END)
            self.entries["Código"].insert(0, values[0])
            self.entries["Código"].config(state="readonly")
            self.entries["Nombre"].delete(0, END)
            self.entries["Nombre"].insert(0, values[1])
            self.entries["Descripción"].delete(0, END)
            self.entries["Descripción"].insert(0, values[2])
            self.entries["Cantidad"].delete(0, END)
            self.entries["Cantidad"].insert(0, values[3])
            self.entries["Precio"].delete(0, END)
            self.entries["Precio"].insert(0, values[4])

    def limpiar_campos(self):
        for key, entry in self.entries.items():
            entry.config(state="normal")
            entry.delete(0, END)

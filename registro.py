import tkinter as tk
from tkinter import ttk

class TablaRegistros:
    def __init__(self, parent, columnas, titulo):
        self.frame = tk.Frame(parent)
        self.frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Crear la tabla
        self.tabla = ttk.Treeview(self.frame, columns=columnas, show='headings')
        for col in columnas:
            self.tabla.heading(col, text=col)
        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar vertical
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tabla.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tabla.configure(yscrollcommand=self.scrollbar.set)

    def cargar_registros(self, registros):
        self.limpiar()
        for registro in registros:
            self.tabla.insert("", "end", values=(registro['id'], registro['model'], registro['brand'], registro['productionYear'], registro['topSeed']))

    def limpiar(self):
        for row in self.tabla.get_children():
            self.tabla.delete(row)

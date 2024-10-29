import tkinter as tk
from tkinter import ttk, messagebox
from api import Api

class Aplicacion(tk.Tk):
    def __init__(self, api):
        super().__init__()
        self.api = api
        self.titulo = "Aplicación de Registro"
        self.resizable(False, False)  # La ventana no es dimensionable

        self.crear_widgets()

    def crear_widgets(self):
        # Frame para organizar la tabla y el scrollbar
        frame_tabla = tk.Frame(self)
        frame_tabla.pack(fill=tk.BOTH, expand=True)

        # Tabla (Treeview)
        self.tabla = ttk.Treeview(frame_tabla, columns=("ID", "Modelo", "Marca", "Año", "Velocidad Máx"), show='headings')
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Modelo", text="Modelo")
        self.tabla.heading("Marca", text="Marca")
        self.tabla.heading("Año", text="Año")
        self.tabla.heading("Velocidad Máx", text="Velocidad Máx")
        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar vertical para la tabla
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        # Botones de obtener y seleccionar registros
        self.boton_obtener = tk.Button(self, text="Obtener Registros", command=self.cargar_registros)
        self.boton_obtener.pack(pady=10)

        self.boton_seleccionar = tk.Button(self, text="Seleccionar Registro", command=self.seleccionar_registro)
        self.boton_seleccionar.pack(pady=10)

    def cargar_registros(self):
        registros = self.api.obtener_registros()
        for registro in registros:
            self.tabla.insert("", "end", values=(registro.id, registro.model, registro.brand, registro.production_year, registro.top_seed))

    def seleccionar_registro(self):
        selected_item = self.tabla.selection()
        if selected_item:
            item = self.tabla.item(selected_item)
            messagebox.showinfo("Registro Seleccionado", str(item['values']))
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un registro.")

if __name__ == "__main__":
    url_api = "https://6720695ae7a5792f053168d8.mockapi.io/LeyendasEnVelocidad"
    api = Api(url_api)
    app = Aplicacion(api)
    app.title(app.titulo)
    app.mainloop()

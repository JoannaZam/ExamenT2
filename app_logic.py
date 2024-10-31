import tkinter as tk
from tkinter import messagebox
from api import Api
from tabla import TablaRegistros


class Aplicacion:
    def __init__(self, api):
        self.api = api
        self.root = tk.Tk()
        self.root.title("Leyendas en velocidad")
        self.root.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        # Botón para obtener datos
        boton_obtener_datos = tk.Button(self.root, text="Obtener Datos".upper(), command=self.obtener_datos)
        boton_obtener_datos.pack(pady=5)

        # Entrada y botón para buscar registro específico
        label_id = tk.Label(self.root, text="Ingrese el ID del registro a buscar:")
        label_id.pack(pady=5)
        self.entry_id = tk.Entry(self.root)
        self.entry_id.pack(pady=5)
        boton_buscar = tk.Button(self.root, text="Buscar Registro", command=self.buscar_registro)
        boton_buscar.pack(pady=10)

        # Botón para refrescar datos
        boton_actualizar_registro = tk.Button(self.root, text="Actualizar registro", command=self.refrescar_datos)
        boton_actualizar_registro.pack(pady=5)

        # Tabla de todos los registros
        columnas = ("ID", "Modelo", "Marca", "Año", "Velocidad Máx")
        self.tabla_todos = TablaRegistros(self.root, columnas, "Todos los Registros")

        # Tabla para mostrar el registro específico
        self.tabla_especifica = TablaRegistros(self.root, columnas, "Registro Específico")

    def obtener_datos(self):
        registros = self.api.obtener_registros()
        if registros:
            self.tabla_todos.cargar_registros(registros)
        else:
            messagebox.showerror("Error", "No se pudieron obtener los registros.")

    def refrescar_datos(self):
        # Limpiar entrada de ID y la tabla de registro específico
        self.entry_id.delete(0, tk.END)  # Limpia el campo de entrada
        self.tabla_especifica.limpiar()  # Limpia la tabla del registro específico

        # Llama a la función que obtiene y muestra todos los registros
        self.obtener_datos()

    def buscar_registro(self):
        id_buscado = self.entry_id.get()
        if not id_buscado:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID.")
            return

        # Obtener todos los registros nuevamente para buscar el específico
        registros = self.api.obtener_registros()
        registro_encontrado = next((r for r in registros if r['id'] == id_buscado), None)

        if registro_encontrado:
            self.tabla_especifica.cargar_registros([registro_encontrado])
        else:
            messagebox.showinfo("Registro no encontrado", f"No se encontró un registro con el ID {id_buscado}")
            self.tabla_especifica.limpiar()

    def ejecutar(self):
        self.root.mainloop()

import requests

class Api:
    def __init__(self, url):
        self.url = url

    def obtener_registros(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Verifica si hay errores en la respuesta
            registros = response.json()
            return registros
        except requests.RequestException as e:
            print("Error al obtener registros:", e)
            return []

import requests
from datetime import datetime
from registro import Registro


class Api:
    def __init__(self, url):
        self.url = url

    def obtener_registros(self):
        try:
            # Realiza la solicitud a la API
            response = requests.get(self.url)
            response.raise_for_status()  # Verifica si la solicitud fue exitosa

            # Convierte la respuesta JSON en objetos Registro
            registros = []
            for item in response.json():
                production_year = datetime.fromisoformat(item['productionYear'].replace("Z", "+00:00")).year
                registros.append(
                    Registro(item['id'], item['model'], item['brand'], production_year, item['topSeed'])
                )
            return registros

        except requests.exceptions.RequestException as e:
            print(f"Error al obtener los registros: {e}")
            return []

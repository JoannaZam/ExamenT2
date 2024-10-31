from api import Api
from app_logic import Aplicacion

if __name__ == "__main__":
    url_api = "https://6720695ae7a5792f053168d8.mockapi.io/LeyendasEnVelocidad"
    api = Api(url_api)
    app = Aplicacion(api)
    app.ejecutar()  # Inicia la aplicación

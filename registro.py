class Registro:
    def __init__(self, id, model, brand, production_year, top_seed):
        self.id = id
        self.model = model
        self.brand = brand
        self.production_year = production_year
        self.top_seed = top_seed

    def __str__(self):
        return f"{self.model} ({self.brand}): Año {self.production_year}, Velocidad máxima {self.top_seed}"

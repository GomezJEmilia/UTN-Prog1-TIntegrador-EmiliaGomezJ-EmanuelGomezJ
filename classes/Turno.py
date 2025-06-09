class Turno:
    def __init__(self, dni, nombre, hora):
        self.dni = dni
        self.nombre = nombre
        self.hora = hora 

    def __str__(self):
        return f"{self.hora}hs - {self.nombre} (DNI: {self.dni})"
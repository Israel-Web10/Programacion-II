from Figura import Figura
from Coloreado import Coloreado

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado

    def comoColorear(self):
        return "Colorear los cuatro lados"

    def toString(self):
        return f"{super().toString()}, Lado: {self.lado}"
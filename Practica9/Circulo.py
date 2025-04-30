from Figura import Figura
import math

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def area(self):
        return math.pi * self.radio * self.radio

    def perimetro(self):
        return 2 * math.pi * self.radio

    def toString(self):
        return f"{super().toString()}, Radio: {self.radio}"
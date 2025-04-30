from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self):
        self.color = "Sin color"

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def toString(self):
        return f"Color: {self.color}"

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass
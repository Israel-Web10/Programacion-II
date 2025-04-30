from abc import ABC, abstractmethod

class Boleto(ABC):
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0

    @abstractmethod
    def toString(self):
        return f"Numero: {self.numero}, Precio: {self.precio}"
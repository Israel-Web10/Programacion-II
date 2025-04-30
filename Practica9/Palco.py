from Boleto import Boleto

class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.00

    def toString(self):
        return super().toString() + f", Precio: {self.precio}"
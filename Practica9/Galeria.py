from Boleto import Boleto

class Galeria(Boleto):
    def __init__(self, numero, cant_dias):
        super().__init__(numero)
        self.cant_dias = cant_dias
        self.precio = 25.00 if cant_dias >= 10 else 30.00

    def toString(self):
        return f"Numero: {self.numero}, Precio: {self.precio}"
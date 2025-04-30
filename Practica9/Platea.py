from Boleto import Boleto

class Platea(Boleto):
    def __init__(self, numero, cant_dias):
        super().__init__(numero)
        self.cant_dias = cant_dias
        self.precio = 50.00 if cant_dias >= 10 else 60.00

    def toString(self):
        return super().toStrin
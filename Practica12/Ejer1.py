#patrones creacionales
class Producto:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def operar(self):
        pass
class Suma(Producto):
    def operar(self):
        return f"Suma realizada: {self.a + self.b}"
class Resta(Producto):
    def operar(self):
        return f"Resta realizada: {self.a - self.b}"
class Fabrica:
    def crear_producto(self, tipo, a, b):
        if tipo == "suma":
            return Suma(a, b)
        elif tipo == "resta":
            return Resta(a, b)
        else:
            raise ValueError("Tipo desconocido")
f = Fabrica()
p = f.crear_producto("suma", 10, 5)
print(p.operar())
#ventaja:Fabricacrea objetos Sumao Restasin que el cliente necesite saber cómo se instancian.
#Puede agregar fácilmente una clase Multiplicaciony solo modificar la fábrica, sin tocar el código que la usa.



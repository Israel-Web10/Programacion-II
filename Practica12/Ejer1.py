#patrones creacionales
class Producto:
    def operar(self):
        pass
class Suma(Producto):
    def operar(self):
        return "Suma realizada"
class Resta(Producto):
    def operar(self):
        return "Resta realizada"
class Fabrica:
    def crear_producto(self, tipo):
        if tipo == "suma":
            return Suma()
        elif tipo == "resta":
            return Resta()
        else:
            raise ValueError("Tipo desconocido")
f = Fabrica()
p = f.crear_producto("suma")
print(p.operar())
#ventaja:Fabricacrea objetos Sumao Restasin que el cliente necesite saber cómo se instancian.
#Puede agregar fácilmente una clase Multiplicaciony solo modificar la fábrica, sin tocar el código que la usa.



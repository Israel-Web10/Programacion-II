class MotorViejo:
    def __init__(self, nombre: str):
        self.nombre = nombre
    def arranque(self):
        return f"{self.nombre} arrancado"
class Vehiculo:
    def encender(self):
        pass
class Adaptador(Vehiculo):
    def __init__(self, motor_viejo: MotorViejo):
        self.motor = motor_viejo  # referencia al objeto adaptado
    def encender(self):
        return self.motor.arranque()
def cliente_usa(vehiculo: Vehiculo):
    print(vehiculo.encender())

motor = MotorViejo("Motor viejo modelo A")
auto_usable = Adaptador(motor)
cliente_usa(auto_usable)
#Ventaja general:Permite que clases con interfaces incompatibles trabajen juntas sin modificar su código original.
#Ventaja de uso en la práctica:Facilita la integración de componentes antiguos o de terceros en sistemas nuevos.
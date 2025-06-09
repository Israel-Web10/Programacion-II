class MotorViejo:
    def arranque(self):
        return "Motor viejo arrancado"
class Vehiculo:
    def encender(self):
        pass
class Adaptador(Vehiculo):
    def __init__(self, motor_viejo):
        self.motor = motor_viejo
    def encender(self):
        return self.motor.arranque()
def cliente_usa(vehiculo):
    print(vehiculo.encender())

motor = MotorViejo()
auto_usable = Adaptador(motor)
cliente_usa(auto_usable)
#Ventaja general:Permite que clases con interfaces incompatibles trabajen juntas sin modificar su código original.
#Ventaja de uso en la práctica:Facilita la integración de componentes antiguos o de terceros en sistemas nuevos.
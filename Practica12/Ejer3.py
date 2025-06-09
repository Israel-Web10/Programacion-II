class Luz:
    def __init__(self, ubicacion: str):
        self.ubicacion = ubicacion  
    def encender(self):
        print(f" Hay luz en {self.ubicacion} P3 Lab2")
class Comando:
    def ejecutar(self):
        pass
class EncenderLuz(Comando):
    def __init__(self, luz: Luz):
        self.luz = luz  
    def ejecutar(self):
        self.luz.encender()
class Interruptor:
    def __init__(self, cmd: Comando):
        self.cmd = cmd  
    def presionar(self):
        self.cmd.ejecutar()
class Main:
    luz = Luz("laboratorio Basico de informática")
    cmd = EncenderLuz(luz)
    interr = Interruptor(cmd)
    interr.presionar()

#ventaja:El interruptor no necesitas saber cómo se enciende la luz, solo necesita ejecutar un comando.
#ventaja de uso Permite implementar operaciones como deshacer (deshacer), programar acciones y mantener un historial de comandos.

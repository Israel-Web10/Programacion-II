class PlanAntiguo:
    def __init__(self, nombre: str):
        self.nombre = nombre
    def ejecutar(self):
        return f"{self.nombre} Cursando plan antiguo"
class Nuevoplan:
    def iniciar(self):
        pass
class AdaptadorSistema(Nuevoplan):
    def __init__(self, sistema_antiguo: PlanAntiguo):
        self.sistema = sistema_antiguo  
    def iniciar(self):
        return self.sistema.ejecutar()

def darSis(sistema: Nuevoplan):
    print(sistema.iniciar())
class Main:
    sis = PlanAntiguo("Sistema de gestión de Materias: ")
    siscompat = AdaptadorSistema(sis)
    darSis(siscompat)
#Ventaja general:Permite que clases con interfaces incompatibles trabajen juntas sin modificar su código original.
#Ventaja de uso en la práctica:Facilita la integración de componentes antiguos o de terceros en sistemas nuevos.
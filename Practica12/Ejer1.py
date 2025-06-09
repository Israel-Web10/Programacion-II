# Patrones creacionales 
class Materia:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def descr(self):
        pass
class Obligatoria(Materia):
    def descr(self):
        return f"Materia Tomada: {self.nombre}, Nota: {self.nota}"
class Optativa(Materia):
    def descr(self):
        return f"Materia optativa: {self.nombre}, Nota: {self.nota}"
class FabricaMaterias:
    def creamat(self, tipo, nombre, nota):
        tipo = tipo.lower()
        if tipo == "obligatoria":
            return Obligatoria(nombre, nota)
        elif tipo == "optativa":
            return Optativa(nombre, nota)
        else:
            raise ValueError("Materia Indecisa")
class Main:
    fabrica = FabricaMaterias()
    materia = fabrica.creamat("obligatoria", "programacion 2", 66)
    print(materia.descr())

    
#ventaja:Fabricacrea objetos Suma,resta sin saber cómo se instancian.
#Puede agregar fácilmente una clase Multiplicacion y solo modificar la fábrica



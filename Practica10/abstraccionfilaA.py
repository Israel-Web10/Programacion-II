class Persona:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

class Indigena(Persona):
    def __init__(self, nombre, comunidad):
        super().__init__(nombre, "Indígena")
        self.comunidad = comunidad
        self.contaminantes = []
        self.denuncias = []
        self.reclamos = []

    def agregar_contaminante(self, contaminante):
        self.contaminantes.append(contaminante)

    def denunciar_empresa(self, empresa):
        self.denuncias.append(empresa)

    def reclamar_al_gobierno(self, gobierno):
        self.reclamos.append(gobierno)

class Contaminante:
    def __init__(self, nombre, nivel_detectado):
        self.nombre = nombre
        self.nivel_detectado = nivel_detectado

class EmpresaMinera:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

class Gobierno:
    def __init__(self, presidente):
        self.presidente = presidente

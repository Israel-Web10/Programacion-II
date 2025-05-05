class Planta:
    def __init__(self, nombre_cientifico, familia):
        self.nombre_cientifico = nombre_cientifico
        self.familia = familia
        self.distribuciones = []

    def agregar_distribucion(self, distribucion):
        self.distribuciones.append(distribucion)

class CondicionAmbiental:
    def __init__(self, clima, suelo):
        self.clima = clima
        self.suelo = suelo

class BarrerasGeograficas:
    def __init__(self, tipo):
        self.tipo = tipo  

class Distribucion:
    def __init__(self, region, condiciones, barrera):
        self.region = region
        self.condiciones = condiciones 
        self.barrera = barrera          

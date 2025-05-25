class Artista:
    def __init__(self, nombre, ci, anios_exp):
        self.nombre = nombre
        self.ci = ci
        self.anios_exp = anios_exp

class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio

class Obra:
    def __init__(self, titulo, material, artistas, anuncio=None):
        self.titulo = titulo
        self.material = material
        self.artistas = artistas
        self.anuncio = anuncio

class Pintura(Obra):
    def __init__(self, titulo, material, artistas, genero, anuncio=None):
        super().__init__(titulo, material, artistas, anuncio)
        self.genero = genero

def artista_mas_experiencia(pinturas):
    todos_artistas = []
    for pintura in pinturas:
        todos_artistas.extend(pintura.artistas)
    artista_max = max(todos_artistas, key=lambda a: a.anios_exp)
    return artista_max.nombre

def total_venta(pinturas):
    total = 0
    for pintura in pinturas:
        if pintura.anuncio:
            total += pintura.anuncio.precio
    return total

class main():
    # a. Crear un objeto pintura con anuncio y otro sin anuncio
    a1 = Artista("Ana", "123", 5)
    a2 = Artista("Luis", "456", 10)

    anuncio1 = Anuncio(1, 1500)

    pintura_con_anuncio = Pintura("Sol Naciente", "óleo", [a1, a2], "paisaje", anuncio1)
    pintura_sin_anuncio = Pintura("Luz Interior", "acrílico", [a1], "abstracto")

    pinturas = [pintura_con_anuncio, pintura_sin_anuncio]

    # b. Mostrar el nombre del artista con más años de experiencia
    print("b) Artista con más experiencia:", artista_mas_experiencia(pinturas))

    # c. Agregar anuncio a la pintura sin anuncio y calcular el total de venta
    anuncio2 = Anuncio(2, 1800)
    pintura_sin_anuncio.anuncio = anuncio2

    print("c) Total de venta de ambas pinturas:", total_venta(pinturas))



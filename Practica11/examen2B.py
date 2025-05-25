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
        self.artistas = artistas  # lista de artistas
        self.anuncio = anuncio

class Pintura(Obra):
    def __init__(self, titulo, material, artistas, genero, anuncio=None):
        super().__init__(titulo, material, artistas, anuncio)
        self.genero = genero

# --- Funciones adicionales para los incisos ---

def promedio_experiencia(pinturas):
    total = 0
    count = 0
    for pintura in pinturas:
        for artista in pintura.artistas:
            total += artista.anios_exp
            count += 1
    return total / count if count > 0 else 0

def incrementar_precio(pinturas, nombre_artista, incremento):
    for pintura in pinturas:
        for artista in pintura.artistas:
            if artista.nombre == nombre_artista:
                if pintura.anuncio:
                    pintura.anuncio.precio += incremento

# --- Función main() ---
class main():
    # a) Crear dos pinturas con anuncios de venta
    a1 = Artista("Ximena", "111", 6)
    a2 = Artista("Carlos", "222", 10)
    a3 = Artista("Luisa", "333", 4)

    an1 = Anuncio(101, 1200)
    an2 = Anuncio(102, 1600)

    p1 = Pintura("Atardecer", "óleo", [a1, a2], "paisaje", an1)
    p2 = Pintura("Montaña Viva", "acrílico", [a3], "naturaleza", an2)

    pinturas = [p1, p2]

    # b) Calcular promedio de años de experiencia de artistas
    prom = promedio_experiencia(pinturas)
    print("b) Promedio de años de experiencia:", round(prom, 2))

    # c) Incrementar el precio en X a la pintura del artista con nombre X
    nombre_objetivo = "Ximena"
    incremento = 300
    incrementar_precio(pinturas, nombre_objetivo, incremento)

    print("c) Precios actualizados después del incremento:")
    for p in pinturas:
        if p.anuncio:
            print(f"   - {p.titulo}: Bs {p.anuncio.precio}")


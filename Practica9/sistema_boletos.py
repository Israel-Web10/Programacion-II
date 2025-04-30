from abc import ABC, abstractmethod

class Boleto(ABC):
    def __init__(self, numero):
        self.numero = numero
    
    @abstractmethod
    def get_precio(self):
        pass
    
    def _str_(self):
        return f"Número: {self.numero}, Precio: {self.get_precio():.1f}"

class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
    
    def get_precio(self):
        return 100.0

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super()._init_(numero)
        self.dias_anticipacion = dias_anticipacion
    
    def get_precio(self):
        return 50.0 if self.dias_anticipacion >= 10 else 60.0

class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion
    
    def get_precio(self):
        return 25.0 if self.dias_anticipacion >= 10 else 30.0


class Colorado(ABC):
    @abstractmethod
    def como_colorear(self):
        pass

class Figura(ABC):
    def __init__(self, color="negro"):
        self.color = color
    
    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def __str__(self):
        return f"Figura de color {self.color}"
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura, Colorado):
    def __init__(self, lado, color="negro"):
        super().__init__(color)
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return 4 * self.lado
    
    def como_colorear(self):
        return "Colorear los cuatro lados"

class Circulo(Figura):
    def __init__(self, radio, color="negro"):
        super()._init_(color)
        self.radio = radio
    
    def area(self):
        return 3.1416 * (self.radio ** 2)
    
    def perimetro(self):
        return 2 * 3.1416 * self.radio

### Programa de prueba para las figuras
import random

def test_figuras():
    figuras = []
    for _ in range(5):
        tipo = random.randint(1, 2)
        if tipo == 1:  # Cuadrado
            lado = random.randint(1, 10)
            figuras.append(Cuadrado(lado, random.choice(["rojo", "azul", "verde"])))
        else:  # Círculo
            radio = random.randint(1, 10)
            figuras.append(Circulo(radio, random.choice(["rojo", "azul", "verde"])))
    
    for figura in figuras:
        print(f"\n{figura}")
        print(f"Área: {figura.area():.2f}")
        print(f"Perímetro: {figura.perimetro():.2f}")
        if isinstance(figura, Colorado):
            print(figura.como_colorear())

if __name__ == "_main_":
    print("\n--- Ejemplo de Boletos ---")
    palco = Palco(1)
    platea1 = Platea(2, 15)  # Más de 10 días
    platea2 = Platea(3, 5)    # Menos de 10 días
    galeria1 = Galeria(4, 12) # Más de 10 días
    galeria2 = Galeria(5, 3)  # Menos de 10 días
    
    print(palco)
    print(platea1)
    print(platea2)
    print(galeria1)
    print(galeria2)
    
    # Ejemplo de figuras
    print("\n--- Ejemplo de Figuras ---")
    test_figuras()
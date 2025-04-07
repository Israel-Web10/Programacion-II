import math

class AreaFiguras:

    def area(self, *args):
        if len(args) == 1 and isinstance(args[0], (int, float)):
            
            radio = args[0]
            return math.pi * radio ** 2
        elif len(args) == 2 and all(isinstance(arg, (int, float)) for arg in args):
    
            ancho, alto = args
            return ancho * alto
        elif len(args) == 3 and isinstance(args[2], str) and args[2] == 'Triangulo':
        
            base, altura, _ = args
            return (base * altura) / 2
        elif len(args) == 3:
        
            base_menor, base_mayor, altura = args
            return ((base_menor + base_mayor) * altura) / 2
        elif len(args) == 4 and isinstance(args[2], str) and args[2] == 'Pentagono':
    
            lado, apotema, _, _ = args
            perimetro = lado * 5
            return (perimetro * apotema) / 2
        else:
            raise NotImplementedError("Los valores son incorrectos o faltan valores")

figura = AreaFiguras()

print("Area Circulo: ", figura.area(3))
print("Area Rectángulo: ", figura.area(2, 7))
print("Area Triangulo: ", figura.area(5, 9, 'Triangulo'))
print("Area Trapecio: ", figura.area(2, 9, 5))
print("Area Pentagono: ", figura.area(7, 4, 'Pentagono', 'x'))
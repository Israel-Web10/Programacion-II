package Practica4;
public class AreasJava {
    public static class FiguraGeometrica {
    
        public double areaCirculo(double radio) {
            return Math.PI * Math.pow(radio, 2);
        }
    
        public double areaRectangulo(double ancho, double alto) {
            return ancho * alto;
        }
    
        public double areaTriangulo(double base, double altura) {
            return (base * altura) / 2;
        }
    
        public double areaTrapecio(double baseMenor, double baseMayor, double altura) {
            return ((baseMenor + baseMayor) * altura) / 2;
        }
    
        public double areaPentagono(double lado, double apotema, int lados) {
            double perimetro = lado * lados;  
            return (perimetro * apotema) / 2;
        }
    
 
        public class Main {

            public static void main(String[] args) {
                FiguraGeometrica figura = new FiguraGeometrica();
                System.out.println("area circulo: " + figura.areaCirculo(3));
                System.out.println("area rectángulo: " + figura.areaRectangulo(2, 7));
                System.out.println("area triángulo: " + figura.areaTriangulo(5, 9));
                System.out.println("area trapecio: " + figura.areaTrapecio(2, 9, 5));
                System.out.println("area pentágono: " + figura.areaPentagono(7, 4, 5));
                
            }
        }   }
}
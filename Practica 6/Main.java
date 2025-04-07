package Practica6;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        AlgebraVectorial a1 = new AlgebraVectorial(1, 2, 3);
        AlgebraVectorial b1 = new AlgebraVectorial(-2, 1, 0);
        System.out.println("a = " + a1);
        System.out.println("b = " + b1);
        System.out.println("Producto escalar : " + a1.productoEscalar(b1));
        System.out.println("Producto vectorial: " + a1.productoVectorial(b1));
        System.out.println("Proyección de a sobre b : " + a1.proyeccion(b1));
        AlgebraVectorial a2 = new AlgebraVectorial(2, 5);
        AlgebraVectorial b2 = new AlgebraVectorial(4, 10);
        System.out.println("a = " + a2);
        System.out.println("b = " + b2);
        System.out.println("Producto escalar: " + a2.productoEscalar(b2));
        System.out.println("Producto vectorial: " + a2.productoVectorial(b2));
        System.out.println("Proyección de a sobre b: " + a2.proyeccion(b2));
        Scanner sc = new Scanner(System.in);
        System.out.println("\nINGRESE VECTORES:");
        System.out.println("Vector 1 (x y [z]):");
        AlgebraVectorial v1 = leerVector(sc);
        System.out.println("Vector 2 (x y [z]):");
        AlgebraVectorial v2 = leerVector(sc);
        
        System.out.println("\nRESULTADOS:");
        System.out.println("Producto escalar: " + v1.productoEscalar(v2));
        System.out.println("Producto vectorial: " + v1.productoVectorial(v2));
        System.out.println("Proyección de v1 y v2: " + v1.proyeccion(v2));
        
        sc.close();
    }
    
    private static AlgebraVectorial leerVector(Scanner sc) {
        String[] componentes = sc.nextLine().split(" ");
        if (componentes.length == 2) {
            return new AlgebraVectorial(
                Double.parseDouble(componentes[0]),
                Double.parseDouble(componentes[1])
            );
        } else if (componentes.length == 3) {
            return new AlgebraVectorial(
                Double.parseDouble(componentes[0]),
                Double.parseDouble(componentes[1]),
                Double.parseDouble(componentes[2])
            );
        }
        return new AlgebraVectorial(0, 0, 0);
    }
}
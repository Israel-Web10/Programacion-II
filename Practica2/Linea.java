package Practica2;
public class Linea {
    public static class Punto {
        float x, y;

        Punto(float a, float b) {
            x = a;
            y = b;
        }

        float[] coord_cartesianas() {
            return new float[]{x, y};
        }

        double[] coord_polares() {
            double r = Math.sqrt(x * x + y * y);
            double theta = Math.atan2(y, x);
            return new double[]{r, theta};
        }
        @Override
        public String toString() {
            return x + ", " + y;
        }
    }

    Punto p1, p2;

    Linea(Punto punto1, Punto punto2) {
        p1 = punto1;
        p2 = punto2;
    }
    @Override
    public String toString() {
        return "Linea = " + p1 + " Punto " + p2;
    }

    void dibujaLinea() {
        System.out.println("Dibujando una línea desde " + p1 + " hasta " + p2);
    }

    public static void main(String[] args) {
        Punto p1 = new Punto(1, 2);
        Punto p2 = new Punto(3, 4);
        Linea linea = new Linea(p1, p2);

        System.out.println(linea);
        linea.dibujaLinea();
        float[] cartesianCoords = p1.coord_cartesianas();
        System.out.println("Punto p1 coordenadas cartesianas: (" + cartesianCoords[0] + ", " + cartesianCoords[1] + ")");
        double[] polarCoords = p1.coord_polares();
        System.out.println("Punto p1 coordenadas polares: (r = " + polarCoords[0] + ", O = " + polarCoords[1] + ")");
    }   
}

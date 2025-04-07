package Practica1;
public class punto {
    float x, y;

    punto(float a, float b) {
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
        return "Punto(" + x + ", " + y + ")";
    }

    public static void main(String[] args) {
        punto p = new punto(3, 4);

        System.out.println("Coordenadas cartesianas: (" + p.coord_cartesianas()[0] + ", " + p.coord_cartesianas()[1] + ")");

        double[] polares = p.coord_polares();
        System.out.println("Coordenadas polares: (r=" + polares[0] + ", O=" + polares[1] + ")");

        System.out.println("Representación del punto: " + p);
    } 
}
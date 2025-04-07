package Practica6;
public class AlgebraVectorial {
    private double x;
    private double y;
    private double z;
    public AlgebraVectorial(double x, double y) {
        this(x, y, 0);
    }
    
    public AlgebraVectorial(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    public double productoEscalar(AlgebraVectorial otro) {
        return this.x * otro.x + this.y * otro.y + this.z * otro.z;
    }
    public AlgebraVectorial productoVectorial(AlgebraVectorial otro) {
        return new AlgebraVectorial(
            this.y * otro.z - this.z * otro.y,
            this.z * otro.x - this.x * otro.z,
            this.x * otro.y - this.y * otro.x
        );
    }
    public AlgebraVectorial proyeccion(AlgebraVectorial otro) {
        double denominador = otro.x*otro.x + otro.y*otro.y + otro.z*otro.z;
        if (denominador == 0) return null;
        double factor = this.productoEscalar(otro) / denominador;
        return new AlgebraVectorial(
            factor * otro.x,
            factor * otro.y,
            factor * otro.z
        );
    }
    public double getX() { return x; }
    public double getY() { return y; }
    public double getZ() { return z; }
    
    @Override
    public String toString() {
        return String.format("(%.2f, %.2f, %.2f)", x, y, z);
    }
}
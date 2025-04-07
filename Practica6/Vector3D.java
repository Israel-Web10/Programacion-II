package Practica6;

public class Vector3D {
        private double x;
        private double y;
        private double z;
        
        public Vector3D(double x, double y, double z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }
        
        public Vector3D sumar(Vector3D v) {
            return new Vector3D(this.x + v.x, this.y + v.y, this.z + v.z);
        }
        
        public Vector3D multiplicar(double s) {
            return new Vector3D(s * this.x, s * this.y, s * this.z);
        }
        
        public double magnitud() {
            return Math.sqrt(x*x + y*y + z*z);
        }
        
        public Vector3D normalizar() {
            double m = magnitud();
            if (m == 0) throw new ArithmeticException("No se puede normalizar vector cero");
            return new Vector3D(x/m, y/m, z/m);
        }
        
        public double punto(Vector3D v) {
            return this.x * v.x + this.y * v.y + this.z * v.z;
        }
        
        public Vector3D cruz(Vector3D v) {
            return new Vector3D(
                this.y * v.z - this.z * v.y,
                this.z * v.x - this.x * v.z,
                this.x * v.y - this.y * v.x
            );
        }
        
        public boolean esOrtogonal(Vector3D v) {
            return Math.abs(this.punto(v)) < 1e-10;
        }
        
        @Override
        public String toString() {
            return String.format("(%.2f, %.2f, %.2f)", x, y, z);
        }
    }


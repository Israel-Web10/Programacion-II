package Practica8.Diamante;
public class Diamantes {
    


    // Clase A
    static class A {
        private int x;
        private int z;

        public A(int x, int z) {
            this.x = x;
            this.z = z;
        }

        public void incrementaXZ() {
            x++;
            z++;
        }

        public void incrementaZ() {
            z++;
        }

        @Override
        public String toString() {
            return "A(x=" + x + ", z=" + z + ")";
        }

        public int getX() {
            return x;
        }

        public int getZ() {
            return z;
        }
    }

    // Clase B
    static class B {
        private int y;
        private int z;

        public B(int y, int z) {
            this.y = y;
            this.z = z;
        }

        public void incrementaYZ() {
            y++;
            z++;
        }

        public void incrementaZ() {
            z++;
        }

        @Override
        public String toString() {
            return "B(y=" + y + ", z=" + z + ")";
        }

        public int getY() {
            return y;
        }

        public int getZ() {
            return z;
        }
    }

    // Clase D
    static class D extends A {
        private int y;

        public D(int x, int y, int z) {
            super(x, z);
            this.y = y;
        }

        public void incrementaXYZ() {
            super.incrementaXZ(); // Incrementa x y z en clase A
            y++; // Incrementa y
            incrementaZ(); // Incrementa z en la clase A
        }

        @Override
        public String toString() {
            return "D(x=" + getX() + ", y=" + y + ", z=" + getZ() + ")";
        }

        public int getY() {
            return y;
        }
    }

    // Método principal para probar las clases
    public static void main(String[] args) {
        A a = new A(21, 12);
        B b = new B(67, 34);
        D d = new D(13, 43, 45);

        a.incrementaXZ();
        b.incrementaYZ();
        d.incrementaXYZ();

        System.out.println(a); // Imprime objeto A
        System.out.println(b); // Imprime objeto B
        System.out.println(d); // Imprime objeto D
    }
}

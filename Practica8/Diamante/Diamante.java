package Practica8.Diamante;
public class Diamante {
    class A {
        protected int x;
        protected int z;
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
    }
    class B {
        protected int y;
        protected int z;
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
    }
    class D extends A {
        protected int y;
    
        public D(int x, int y, int z) {
            super(x, z);
            this.y = y;
        }
        public void incrementaXYZ() {
            x++;
            y++;
            z++;
        }
    }
    public static void main(String[] args) {
        Diamante diamante = new Diamante();
        B bInstance = diamante.new B(5, 10);
        bInstance.incrementaYZ();
        bInstance.incrementaZ();
        D dInstance = diamante.new D(3, 7, 12);
        dInstance.incrementaXYZ();
        
    }
}


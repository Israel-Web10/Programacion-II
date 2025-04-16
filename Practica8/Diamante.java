package Practica8;
interface A {
    default void saludar() {
        System.out.println("A");
    }
}

interface B extends A {
    default void saludar() {
        System.out.println("B");
    }
}

interface C extends A {
    default void saludar() {
        System.out.println("C");
    }
}

class D implements B, C {
    public void saludar() {
                B.super.saludar();  
    }

    public static void main(String[] args) {
        D obj = new D();
        obj.saludar();
    }
}

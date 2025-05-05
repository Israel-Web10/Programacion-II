public class filaB {

    public static void main(String[] args) {

        Ministerio m1 = new Ministerio();
        Ministerio m2 = new Ministerio("rojo","Estacion Central, Estacion Cementerio, Estacion 16 de Julio");
        
        System.out.println(m1);
        System.out.print(m2);
        m2.eliminarEmpleado(26);
        System.out.print(m2);
        
        System.out.println("------operador(simulacion)-------");
        m1.operador(m2, "saul");
        System.out.println(m1);
        System.out.println(m2);
        
        m1.mostrar(m1.menorEdad());
        m1.mostrar(m1.menorSueldo());
    }
    
}
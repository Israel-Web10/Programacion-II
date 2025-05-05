'''
La solucion aqui presentada solo es un ejemplo, en la programacion nos indican que no existe una solucion unica
por tanto las variaciones que puedan realizarse pueden ser validas dependiendo de lo que les haya pedido el problema;
el como describir sus soluciones es lo importante y que cumpla con los requerimientos del usuario sin errores en lo posible.
'''
from multimethod import multimethod
class LineaTeleferico:
    
    def __init__(self, color="", tramo="", nroCabinas=0, nroEmpleados=4): #si la funcion no recibe argumentos usara los creados por defecto
        self.__color = color
        self.__tramo = tramo
        self.__nroCabinas = nroCabinas
        self.__nroEmpleados = nroEmpleados
        self.__empleados = [["pedro","rojas","luna"],
                            ["lucy", "sosa", "rios"],
                            ["ana", "perez", "rojas"],
                            ["saul", "arce","calle"]]
        self.__edades = [35,43,26,29]
        self.__sueldos = [2500.0,3250.0,2700.0,2500.0]
    
    def __str__(self):
        cad = f"Color: {self.__color}, Tramo: {self.__tramo}, nroCabinas: {self.__nroCabinas}, nroEmpleados: {self.__nroEmpleados}\n"
        cad = cad+ " Empleados: \n"
        for i in range(len(self.__empleados)):
            cad = cad+f"Nombre: {(self.__empleados[i])[0]} {(self.__empleados[i])[1]} {(self.__empleados[i])[2]}, Edad: {self.__edades[i]} sueldo: {self.__sueldos[i]}\n"
        return cad
    
    def eliminarPorApellido(self,x):
        rango = len(self.__empleados)
        for i in range(rango-2):
            if ((self.__empleados[i])[1] ==x or (self.__empleados[i])[2] == x): #se usa or por que asi lo especifica el problema
                self.__empleados.pop(i)#esto facilita la extraccion, con java tenddriamos que recorrer las pociciones hasta el valor eliminado
                self.__edades.pop(i)
                self.__sueldos.pop(i)
                self.__nroEmpleados -=1
    
    def __add__(self,parametros):
        otro, x = parametros
        #x = input("inrgese nombre x: ") #----> aqui llamariamos al valor de x por teclaod de  ser necesario
        if (isinstance(otro, LineaTeleferico)):
            for i in range(len(self.__empleados)):
                if((self.__empleados[i])[0] == x):
                    nombre = (self.__empleados[i])[0]
                    paterno = (self.__empleados[i])[1]
                    materno = (self.__empleados[i])[2]
                    otro.__empleados.append([nombre, paterno, materno])
                    otro.__edades.append(self.__edades[i])
                    otro.__sueldos.append(self.__sueldos[i])
                    self.__empleados.pop(i)
                    self.__edades.pop(i)
                    self.__sueldos.pop(i)
                    self.__nroEmpleados -=1
                    otro.__nroEmpleados +=1
                    break
        return otro
    #creamos metodos para obtener mayor edad y sueldo y mandarlos a la funcion que recibe distintos parametros
    def mayorEdad(self): #funcion creada solo con el objetivo de sacar la mayor edad
        mayor = 0
        for i in range(len(self.__empleados)):
            if(self.__edades[i]>mayor):
                mayor = self.__edades[i]
        return mayor
    
    def mayorSueldo(self): #funcion creada solo con el objetivo de sacar el mayor sueldo
        mayor = 0.0
        for i in range(len(self.__empleados)):
            if(self.__sueldos[i]>mayor):
                mayor = self.__sueldos[i]
        return mayor
#ambos metodos a los que llamamos mostrar() son procedimientos, no devuelven ninugn valor
    @multimethod
    def mostrar(self,e:int): #esta funcion recibira un entero (de la funcion mayorEdad())
        cad = "Empelados con mayor edad: \n"
        for i in range(len(self.__empleados)):
            if(self.__edades[i] == e):
                cad = cad+f"Nombre: {(self.__empleados[i])[0]} {(self.__empleados[i])[1]} {(self.__empleados[i])[2]}, Edad: {self.__edades[i]} sueldo: {self.__sueldos[i]}\n"
        print(cad)
    
    @multimethod
    def mostrar(self, s:float): #esta recibira un flotante(de la funcion mayorSueldo)
        cad = "Empelados con mayor sueldo: \n"
        for i in range(len(self.__empleados)):
            if(self.__sueldos[i] == s):
                cad = cad+f"Nombre: {(self.__empleados[i])[0]} {(self.__empleados[i])[1]} {(self.__empleados[i])[2]}, Edad: {self.__edades[i]} sueldo: {self.__sueldos[i]}\n"
        print(cad)
        
    
class main():
    t01 = LineaTeleferico("rojo", "estacion central, estacion cementerio, estacion 16 de julio",20,4)
    #Segundo teleferico:
    t02 = LineaTeleferico()
    print("primer teleferico: ")
    print(t01)
    print("segundoTeleferico: ")
    print(t02)
    
    print("Eliminar por apellido: (en este caso rojas)")
    t01.eliminarPorApellido("rojas")
    t02.eliminarPorApellido("rojas")
    print(t01)
    print(t02)
    
    print("-------sobrecargar operador(sobrecargamos __add__)--------")
    
    print(t01+(t02,"saul")) #la funcion creada nos obliga a mandar dos parametros de golpe
                            #tambien podriamos llamar al valor de x por teclado
                            #para la fila b solo cambiaria el orden: print(t02+(t01,"saul")) (considrenaod que son objetos Ministerio)
    
    print("---------sobrecargar para mayor edad---------")
    mayEdad=t01.mayorEdad()
    t01.mostrar(mayEdad)#procedimiento
    print("---------sobrecargar para mayor sueldo---------")
    maySueldo = t01.mayorSueldo()
    t01.mostrar(maySueldo)#procediemiento
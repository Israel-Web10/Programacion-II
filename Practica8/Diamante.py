class A:
    def saludar(self):
        print("Hola desde A")

class B(A):
    def saludar(self):
        print("Hola desde B")

class C(A):
    def saludar(self):
        print("Hola desde C")

class D(B, C):
    pass

d = D()
d.saludar()
print(D.__mro__)  

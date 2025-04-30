class A:
    def __init__(self, x, z):
        self.x = x
        self.z = z
    def incrementaXZ(self):
        self.x += 1
        self.z += 1
    def incrementaZ(self):
        self.z += 1
    def __str__(self):
        return f"A(x={self.x}, z={self.z})"
class B:
    def __init__(self, y, z):
        self.y = y
        self.z = z
    def incrementaYZ(self):
        self.y += 1
        self.z += 1
    def incrementaZ(self):
        self.z += 1
    def __str__(self):
        return f"B(y={self.y}, z={self.z})"
class D(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x, z)
        B.__init__(self, y, z)
    def incrementaXYZ(self):
        self.x += 1
        self.y += 1
        self.z += 1
        self.incrementaXZ()  
        self.incrementaYZ()
        return f"D(x={self.x}, y={self.y}, z={self.z})"
a = A(21,12 ) 
b = B(67, 34)
d = D(13, 43, 45)
a.incrementaXZ()
b.incrementaYZ()
d.incrementaXYZ()
print(a)  
print(b)  
print(d)  

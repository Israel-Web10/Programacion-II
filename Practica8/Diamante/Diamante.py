class A:
    def _init_(self, x, z):
        self.x = x
        self.z = z
    def incrementaXZ(self):
        self.x += 1
        self.z += 1
    def incrementaZ(self):
        self.z += 1
class B:
    def _init_(self, y, z):
        self.y = y
        self.z = z
    def incrementaYZ(self):
        self.y += 1
        self.z += 1
    def incrementaZ(self):
        self.z += 1
class D(A, B):
    def _init_(self, x, y, z):
        A._init_(self, x, z)
        B._init_(self, y, z)
    def incrementaXYZ(self):
        self.x += 1
        self.y += 1
        self.z += 1

class A:
    def methodA(self):
        print("A class")
class B(A):
    def methodB(self):
        print("B class")
class C(A):
    def methodC(self):
        print("C class")
class D(B,C):
    def methodD(self):
        print("D class")

d=D()
d.methodA()
d.methodD()
d.methodC()
d.methodB()
        

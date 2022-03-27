class A:
    def methodA(self):
        print("A class")

class B(A):
    def methodB(self):
        print("B class")

class C(B):
    def methodC(self):
        print("C class")

c=C()
c.methodA()
c.methodB()
c.methodC()

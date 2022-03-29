class A:
    def methodA(self):
        print("A class")
class B(A):
    def methodB(self):
        print("B class")
class C(A):
    def methodC(self):
        print("C class")
b=B()
c=C()

b.methodA()
c.methodA()

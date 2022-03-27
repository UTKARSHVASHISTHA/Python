class Rectangle:
    def __init__(self,length,breadth):
        self.l =length
        self.b = breadth
    def area(self):
        return self.l * self.b

class Square:
    def __init__(self,side):
        self.s = side

    def area(self):
        return self.s ** 2
rec = Rectangle(10,20)
squ = Square(10)

print("area of Rectangle is: ",rec.area())
print("area of Square is: ",squ.area())

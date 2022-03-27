class Fruit:
    "I am a class"
    name="Apple"
    def __init__(self,color,size):
        self.color = color
        self.size = size
    def show(self):
        print(f"I am {self.name}, I am {self.color}, and my size is {self.size}")
apple= Fruit("red","8")
apple.show()
print(Fruit.__doc__)
print(Fruit.__name__)



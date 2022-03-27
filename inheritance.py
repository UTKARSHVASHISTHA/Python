class Human:
    def who_am_i(self):
        print("I am a Human")

class Teacher(Human):
    def who_am_i(self):
        print("I am a Teacher")

t=Teacher()
t.who_am_i()

#in output we get the child or local.



class Parent:
    def show(self):
        print("Parent Method")

class Child(Parent):
    def display(self):
        print("Child Method")

c=Child()
c.display()
c.show()

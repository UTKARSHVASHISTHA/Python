#consturctor

class Employee:
    def __init__(self,emp_id,emp_name,emp_salary):
        self.id = emp_id
        self.name = emp_name
        self.salary = emp_salary
    def display(self):
        print("Employee id is:",self.id)     #no need for class 
        print("Employee Name is:",self.name)
        print("Employee salary is:",self.salary)

e1=Employee(1,"ajay",63000)
e2=Employee(2,"amit",65000)

e1.display()
e2.display()




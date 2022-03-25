def num():
    return 10    #return statement is used at the end of the function and returns the result of the function.
print(num())



def sqr(num):
    return num*num
print(sqr(5))



def cube(num):
    return num*num*num
print(cube(5))

cube=cube(9)
print(cube)



def name(name):
    return name
print("Hello",name("Aditya"))




def name(name):
    pass

print("Hello",name("Deepak"))


#Creating a function without return

def sum():
    a=10
    b=20
    c=a+b
    print(c)
sum()


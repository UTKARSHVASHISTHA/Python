try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)
print("Programme will continue")


try:
    print(10/0)
except Exception as e:
    print(e)
print("Programme will continue")

try:
    x=10
    print(y)
except NameError:
    print("Please print valid variable name")
print("Hello Welocme to India")


try:
    print(10/2)
    x=10
    print(y)
except ZeroDivisionError:
    print("Number is Not Divide by zero")
except NameError:
    print("Please define valid varaible name")

print("Hello my program will continue")

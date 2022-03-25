#Logical Operators



num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number :"))
num3=int(input("Enter Third Number :"))

print("\t\t Logical Operation")    # \t means space by 4


#and logical operator


print(num1>=num2 and num3<=num2)
print(num2>=num1 and num2<=num3)


#or logical operator


print(num1>=num2 or num3<=num2)
print(num3<=num2 or num2>=num3)


#not logical operator


print(not(num1>=num2 or num3<=num2))
print(not(num3<=num2 or num2>=num3))


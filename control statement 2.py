#if else statement

   #Syntax:- if condition : code exexcuted when "if" condition is true

#else:condition is false


num1=int(input("Enter a Number:"))
if(num1%2==0):
    print("Even Number")
else:
    print("Odd Number")
      
             
#if elif ladder statement:- more than 2 conditions

    #Syntax: #if condition:
                 #code to be exexcuted if condition is true
             #elif condition1:
                 #code to be executed elif conditon1 is true
             #elif condition2:
                 #code to be executed elif conditon2 is true
             #elif condition3:
                 #code to be executed elif conditon3 is true
             #else:
                 #All conditions are false then else is executed

marks=int(input("Enter your marks:"))
if marks<40:
    print("Fail")
elif marks>40 and marks<=50:
    print("D Grade")
elif marks>50 and marks<=60:
    print("C Grade")
elif marks>60 and marks<=70:
    print("C+ Grade")
elif marks>70 and marks<=80:
    print("B Grade")
elif marks>80 and marks<=90:
    print("B+ Grade")
elif marks>90 and marks<=100:
    print("A Grade")
else:
    print("Invalid Number")

#while loop(infinite loop) and 'while' is a keyword.

i=1               #'i' is a variable.
while(i<10):
    print("Hello")
    i=i+1
    

num=int(input("Enter any number:"))
i=1
while(i<=10):
    print(num*i)
    i=i+1
    

num=int(input("Enter a number:"))
i=1
count_even=0
count_odd=0
while(i<=num):
    if(i%2==0):
        print("Even number ",i)
        count_even=count_even+1
    else:
        print("Odd number ",i)
        count_odd=count_odd+1
    i=i+1
print("Total Even number is: ",count_even)
print("Total Odd number is: ",count_odd)

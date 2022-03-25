minimum_num=int(input("Enter a min. number:"))
maximum_num=int(input("Enter a max. number:"))

count_even=0
count_odd=0

while(minimum_num<=maximum_num):
    if(minimum_num%2==0):
        print("Even number ",minimum_num)
        count_even=count_even+1
        #min=min+1
    else:
        print("Odd number ",minimum_num)
        count_odd=count_odd+1

    minimum_num= minimum_num+1

print("Total Even number is: ",count_even)
print("Total Odd number is: ",count_odd)


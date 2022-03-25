nums=[1,2,3,4,5]
new_nums=[i+10 for i in nums]
power_nums=[i**2 for i in nums]

print(new_nums)
print(power_nums)


nums=[1,1,2,8,14,9,23,36,5,4]

greater_ten = [i for i in nums if(i>10)]
evens = [i for i in nums if(i%2==0)]

print('Greater than ten :',greater_ten)
print('Even numbers list :',evens)

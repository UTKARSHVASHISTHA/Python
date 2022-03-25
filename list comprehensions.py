print([i for i in range(100) if(i%2==0)if(i%5==0)])

print([x+1 if(x%2==0)else x**2 for x in [1,2,3,4,5,6,7,8]])


#Nested list comprehension

List=[[1,2,3],[4,5,6],[3,4]]
print([res**2 for x in List for res in x])


#Dictionary Comprehension

#syntax : {key:expression(i) for (key,i) in iterable}


num=[1,2,3,4]
name=['one','two','three','four']
my_dict={num:name for (num,name) in zip(num,name)}
print(my_dict)

#Python sets comprehensions

#syntax: {expression(i) for i in iterable


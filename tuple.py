#Tuple is immutable(no change)

tuple1=1,2,3,4,5,6,"Amit","Ajay",10.5,True,False,None
print(tuple1)
print(type(tuple1))

t1=()

print(t1)

t1=("Amit","Ajay",10)
print(type(t1))
print(t1)

print(t1[1])
print(t1[2])
print(t1[-1])
print(t1[-3])


t1=("Amit","Ajay",10)
#del t1
#print(t1)

t1=("Amit","Ajay",10,"Ajay")
print(t1.index("Ajay"))
print(t1.count("Ajay"))

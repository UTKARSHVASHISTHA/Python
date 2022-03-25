l1=[1,2,3,"Sourabh","Python",10.5]
print(l1.index(2))
print(l1.index("Sourabh"))  


l1=[1,2,3,4,5,6,["Ajay","Amit"]]
l2=l1

print(l2)
l2[5]="Yess"  #it can be changes
print(l1)

print(id(l1))
print(id(l2))


l1=[1,2,3,4,5,6,["Ajay","Amit"]]
l2=l1.copy()    #no change because of shallow copy
print(l2)

print(id(l1))
print(id(l2))

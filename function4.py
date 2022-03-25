#High order function

l1=['virat','rohit','sachin','jadeja']
print(len(l1))

for i in l1:  #one way
    print(len(i))

#map is a pre defined functon

    
m=map(len,l1)  #using map function
print(list(m))  


print(list(map(len,l1)))

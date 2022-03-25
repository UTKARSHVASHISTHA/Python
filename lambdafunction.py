#Anonymous function or lambda function: use only one time

#we use lambda function with high order function

#Syntax:lambda arg1,arg2,....:Expression
            #or
        #lambda....:Expression

def sqr(a):
    return a*a

l=[1,2,3,4,5,6,7]
print(list(map(sqr,l)))

print(list(map(lambda x:x*x,l)))

x=lambda a:a+a
print(x(5))

x=lambda a,b:a+b
print(x(10,20))

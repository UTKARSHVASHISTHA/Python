def sqr(x):
    return x*x
def cube(a):
    return a*a*a

l=[1,2,3,4,5,6,7,8,9,10]

print(list(map(sqr,l)))
print(list(map(cube,l)))
print(list(map(sqr,range(1,100))))


def check(x):
    if(x%2==0):
        return True
    else:
        return False
print(check(10))
print(check(9))

#always print the true value

l=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(check,l)))
print(list(map(check,l)))

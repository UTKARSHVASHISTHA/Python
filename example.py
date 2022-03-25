def fun(name):
    if(len(name)>=2):
        x,y=name[-2],name[-1]
        print(x,y)
    else:
        print("Please enter string greater than two character ")
fun("d")

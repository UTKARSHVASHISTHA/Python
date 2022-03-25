try:
    a=10/2;
    file=open("my.txt","r")
    print(file.read())
except(ArithmeticError,IOError) as e:
    print(e)
else:
    print("Successfully Done")


try:
    fileptr=open("Python3.txt","w")
    try:
        fileptr.write("Hi i am good")
    finally:
        fileptr.close()
        print("file closed")
except:
    print("Error")



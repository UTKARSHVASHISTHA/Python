
try:
    #this will throw an exception
    fileptr=open("file.txt","r")
except IOError:
    print("file not found")
else:
    print("The file opened successfully")
    fileptr.close()

try:
    a=10/0;
except(ArithmeticError,IOError):
    print("Arithmetic Exception")
else:
    print("Successfully Done")

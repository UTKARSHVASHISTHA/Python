inputString=input("Enter a string")

count=0

for i in inputString:
    count=count+1
newString=inputString[0:2] + inputString[count-2:count]

if(len(inputString)<2):
    print(" ")
else:
    print("Input string=",inputString)
    print("New String=",newString)

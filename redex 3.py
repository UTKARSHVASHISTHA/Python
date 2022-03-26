import re
def isValid(s):
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    return Pattern.match(s)
mob_number=input("Enter mobile number: ")
if(isValid(mob_number)):
    print("Mobile number is Valid..")
else:
    print("Mobile Number is Invalid..")

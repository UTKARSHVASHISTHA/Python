#nested if else

  #syntax:

amt=int(input("Enter Amount:"))
if(amt>=1000):
    amt-=10
    coupen_code=input("Enter Coupen Code")
    if(coupen_code=="India"):
        amt-=10
print("Final amount to pay :",amt)

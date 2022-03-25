#defining the function
def change_string(str):
    str = str + "Hows you"
    print("printing the string inside function :",str)
string1="Hi I am there"

#calling the function
change_string(string1)
print("printing the string outside the function:",string1)


#defining the function
def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("List inside function = ",list1)

#defining the list
list1=[10,30,40,50]
#calling the function
change_list(list1)

print("List outside function = ",list1)

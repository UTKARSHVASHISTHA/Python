import re
txt= "The rain in spain"
x=re.search("r",txt)
print ("The first white space character is located in position: ",x.start())     #start means where it exist
print ("The end white space character is located in position: ",x.end())         #end means +1 value
print ("The end white space character is located in position: ",x.group())       #group means the value name



import re
txt= "The rain in spain"
x=re.findall("he",txt)
print(x)



import re
txt= "The rain in spain"
x=re.split("i",txt)
print(x)


import re
txt="The rain in spain"
x=re.sub("i","9",txt)
print(x)



import re
txt= "The rain in spain"
x=re.findall("[a-n-T]",txt)
print (x)

import re
txt="heo planet"
x=re.findall("he.+o",txt)
print (x)


import re
txt="hellllo planet"
x=re.findall("he.{2,6}o",txt)
print (x)


import re
txt="The rain in spain 2345"
x=re.findall("\\S",txt)
print (x)
if x:
    print("Yes,there is at least one match!")
else:
    print("No match")




#Function can be called wherever it is required.
#Pythin allows us to divide a large program to basic building blocks known as a function.
#It avoids the repetition of the code.
#Two types of functions: 1.User_Defined  2.Built_in

##Creating a function:
#def keyword to define the function


def show():      #show is a function name     #Function Definition
    print("Hello Python")
show()     #function calling


################


def detail(name):    # function definition takes one parameter
    print("Hello",name)

detail("Utkarsh")    #function calling
detail("Kunal")


def student_detail(stu_name,stu_age,stu_course):
    print("Student Name is:",stu_name)
    print("Student Age is:",stu_age)
    print("Student Course is:",stu_course)
    print()

student_detail("Utkarsh",22,"Python")
student_detail("Kunal",20,"Python")





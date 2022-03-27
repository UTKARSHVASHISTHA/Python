class student:
    def insertDetails(self,stu_id,stu_name,stu_course):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_course = stu_course
    def displayDetails(self):
        print("Student Id is: ",self.stu_id)    #here we define the class
        print("Student Name is: ",self.stu_name)
        print("Student Course is: ",self.stu_course)
        print()
s1=student()
s2=student()
s1.insertDetails(1,"Dhoni","Python")
s2.insertDetails(2,"Virat","Python")
s1.displayDetails()
s2.displayDetails()



#method calling would be done by object but function is independent

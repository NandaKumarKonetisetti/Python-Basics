class Student:
    school = "MySchool"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return(self.m1 + self.m2 + self.m3)/3

    def getm1(self):
        return self.m1
    def getm2(self):
        return self.m2
    def getm3(self):
        return self.m3


    def setm1(self,val):
        self.m1 = val

    def setm12(self, val):
        self.m2 = val

    def setm3(self, val):
        self.m3 = val
    @classmethod
    def getSchool(al):
        return al.school


# a method that has nothing to do with instance and class variables then it is said to be a static method
    @staticmethod
    def information(): # Here we are not passing any arguments i meant class and instance arguments
        print("This is a Student class")




s1 = Student(65,85,54)
s2 = Student(68,59,73)


print(s1.getm1())
s2.setm3(56) # To set the value
print(s2.getm3())  # To retrive the value



print("Average of Student 1 is ",s1.average())
print("Average of Student  2 is ",s2.average())
print("The school name is ",Student.getSchool())
Student.information()
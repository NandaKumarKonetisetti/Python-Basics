class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()   # Creation of object for the inner class

    def show(self):
        print(self.name,self.rollno)
       #self.lap.show()


    class laptop:  #Inner Class
        def __init__(self):
            self.company = "Dell"
            self.cpu = "i7"
            self.ram = "32gb"


        def setcpu(self,cp):
            self.cpu = cp

        def show(self):
            print(self.company,self.cpu,self.ram)

st1 = student("Nanda",191811164)
st2 = student("kumar",191811164)
st1.show()

# It can be created only if we create the inner object class inside the outer class
#lap1 = st1.lap
#lap2 = st2.lap
#print(id(lap1))
#print(id(lap2))

lap1 = student.laptop()
lap1.company = "HP"
lap1.setcpu("i9")
lap1.show()



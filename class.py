class device:
    def configuration(self):
        print("4 gb ram internal 128 gb snapdragon 712")


dev1 = device()
dev2 = device()

device.configuration(dev1)   # we can also call configuration method using the class name by passing the object of the class as an argument
device.configuration(dev2)

print(type(dev1))  # In the above line the dev argument goes inside to the self
dev1.configuration()
dev2.configuration()




 #Init method in the class
class laptop:
    def __init__(self,cpu,ram,os):  # T?his init method acts as a  constructor whenever we call the object it also will be called automatically
        self.cpu = cpu
        self.ram = ram
        self.os = os

    def configuration(self):
            print("Configuration is ",self.cpu,self.ram,self.os)

lap1 = laptop("i5","8gb","ios")
lap2 = laptop("i7","4gb","windows")

lap1.configuration()
lap2.configuration()


#Creating another class
class Person:
    def __init__(self):
        self.name = "Nanda"
        self.age = 21
    def update(self):
        self.age = 22
    def compare(self,other):
       return self.age == other.age

p1 = Person()
p2 = Person()

p2.name = "kumar"


p2.update()  # To update the age using the update method inside a class

print(p1.name,p1.age)
print(p2.name,p2.age)

print("The first object id ",id(p1))
print("The second object id",id(p2))

if p1.compare(p2):
    print("Their ages are same")
else :
    print("Their ages are not same")



#Types of variables in a class
#They are two types of variables
#Instance variables --> variables that are assigned inside the init method
#Class Variables -->Variables that are assigned inside  the class but before the init method
class Bike:
    wheels = 4  # It is a class variable
    def __init__(self):
        self.name = "BMW"  #These are instance variables
        self.mileage = 30


# A class variable can be accessed or modified with the help of class name or object name
# Class variables are also called as static variables
b1 = Bike()
b2 = Bike()

b2.mileage = 25
b1.name = "Apache"

Bike.wheels = 6
print(b1.name,b1.mileage,b1.wheels)
print(b2.name,b2.mileage,b2.wheels)
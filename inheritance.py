class A:
    def __init__(self):
        print("In Class A init")
    def feature1(self):
        print("In feature 1 ")
    def feature2(self):
        print("In feature 2 ")
class B:                              # class B is inheriting the features of class A
    def feature3(self):
        print("In feature 3 ")

    def feature4(self):
        print("In feature 4 ")


class C(A,B):
    def __init__(self):
        super().__init__()                  # It will call constructor of the super class A because in multiple inheritance it will call from left hand to right hand side.
        print("In Class C init")

    def feature5(self):
        print("In feature 5")


a1 = A()
a1.feature1()
a1.feature2()


b1 = B()
b1.feature3()
c1 = C();
c1.feature3()
# Python supports single,multilevel and multiple inheritance
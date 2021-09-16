
#Decorators are used to modify the existing function with the help of another function
def divide(a,b):
    print(a/b)



def advanced_div(function):  #Here we are passing the function  as an argument in another function
    def innerfunc(a,b):
        if a<b:
            a,b = b,a
        return  function(a,b)
    return innerfunc
divide1 = advanced_div(divide)
divide1(7,14)

def add(a, b):
    c = a + b
    print(c)


add(2, 9)


def wish():
    print("Happy Birthday")


wish()

r1, r2, r3, r4 = 4, 5, 6, 7
print(r1, r2, r3, r4)


# Returning two values from a funciton
def add_multi(x1, x2):
    x3 = x1 + x2
    x4 = x1 * x2
    return x3, x4


result1, result2 = add_multi(7, 7)
print(result1, result2)


def modify(val):
    print(id(val))
    val = 87
    print("Inside a function", val)
    print("Id inside a function", id(val))


a = 77
print(a)
print(id(a))

modify(a)
print(a)
print(id(a))


# Try to pass the list as an argument and change the value of the list
def update(list):
    print("Inside a function", list)
    print("ID of the list in function", id(list))
    list[7] = 7
    print(list)
    print("After modification", id(list))


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("outside ", id(list))
update(list)
print(list)

# Types of arguments in python
# There are four types of actual arguments in python
# 1.Position
# 2.keyword
# 3.Default
# 4.variable length

print("Arguments in python")


def person(name, age):
    print("Name of the person", name)
    print("Age of the person", age - 5)


person(age=20,
       name="Nanda")  # If we forgot the sequence of arguments in a function then we can use the keywords like this line


# Default argument in funciton
def person1(name, age=19):
    print(name)
    print(age - 7)


person1( "Kumar")  # If we pass the second argument here the second argument will override the default argument if we didnt pass it will show the default arguments
person1("Uday", 28)

print("Passing many arguments")
# Passing many arguments
def sum(a, *b):  # Here the b takes all the arguments except  first one because 'a' takes first argument
    c = a
    for i in b:
        c = c + i
    print(c)


sum(2, 3, 4, 5, 6, 7, 1, 3)


# we can update the above function the code as follows
def done(*num):
    # Here b will come in the form of tuple
    ad = 0
    for val in num:
        ad = ad + val
    print(ad)


done(4,5,8,7,4,7,77,23,43,67,23,46,7,7)




 #Keyworded variable length arguments
def details(name,**data):
     print(name)
     print(data)
     for i,j in data.items():
        print(i,j)


details("Nanda",age = 20,city = "Chennai",PhoneNo = 834089)


name = []
total =  int(input("Enter the total length of the values"))
for i in range(total):
    x = input("Enter the data")
    name.append(x)

def count(name):
    greater = 0
    lesser = 0
    for words in name:
        if len(words) > 5:
            greater = greater+1
        else:
            lesser = lesser +1
    return greater,lesser

output1,output2 = count(name)
print(output1,output2)

#Passing a list as an arguments inside a function

def even_odd(list):
    even_count = 0
    odd_count = 0
    for i in list:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count +=1
    return even_count,odd_count



mixed_data = [2,7,1,65,99,5,9,4,6,8,3,6,1,5,7,3,9]
even,odd = even_odd(mixed_data)
print("Even Numbers are : {} ,Odd numbers are : {}".format(even,odd))
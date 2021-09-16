
from array import *

value = array('i',[1,2,3,9,7,6,5,])

#value.reverse()           To reverse the array
print("It will get the address and length of the ",value.buffer_info())
print("To get the type code of an array",value.typecode)




for i in range(len(value)):
    print(value[i],end = " ")

print()

for i in value:
    print(i,end =" ")

print("\nprinting the elements in an array using while loop")
i = 0
while(i<len(value)):
    print(value[i], end = " ")
    i += 1







print("To get the index of an array manually")
key = 7
for i in range(len(value)):
    if value[i] == key:
        print(i)


print("To get the index of a particular element using the index function ")
print(value.index(7))


 # to copy the values from one array to another array manually
#newarray = array(value.typecode,)



print("How to copy elements from one array to another array and to print them in outpur")

latestArray = array(value.typecode,[])
for i in range(len(value)):
    latestArray.append(value[i])

print(latestArray)



print("To copy the elements from one array to another array using functions")
newarray = array(value.typecode,(a * a for a in value))
print(newarray)


print("To get the array values from the user")
numbers = array('i',[])
length = int (input("Enmter the number of values that you want to insert in the array : "))
for i in range(length):
    val = int (input("Enter the values : "))
    numbers.append(val)

print(numbers)


from functools import reduce
#Lambda Expression in python
square = lambda n :n*n
result = square(9)
print(result)

#Filter map and reduce functions in python


def odd(n):
    return n % 2 != 0



data = [3,2,4,12,67,5,8,9,6,3,5,9,1,8,19,24,26,76,77]
# filter
filter = list (filter(lambda a : a % 2 != 0,data))
print("THe filterd list is ",filter)

#map
map = list(map(lambda n : n*  n,filter))
print("After Modification the data is ",map)
def update(a):
    return a%2 ==0

#Reduce
Reduce = reduce(lambda a,b: a+ b,map)
print("The sum of the numbers in the list is ",Reduce)


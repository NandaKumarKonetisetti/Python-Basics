from numpy import  *
arr = array([1,2.0,9,4,5,6,7,3,5,1],int)
print(arr)
print(arr.dtype)
arr1 = array([8,5,6,2,2,3,8,9,67,9])
arr2 = arr + arr1


print("sum of the array is",sum(arr))
print(sin(arr))
print("The square root of an array is",sqrt(arr))
print("THe conoatenation of two arrays is",concatenate([arr,arr1]))

num1 = array([1,2,3,4])
num2 = array([5,6,7,8])


#num3 = num1   # It will just create another name to the array with same address
#num3 = num1.view() # It will create an array at different location but it will do the shallow copy which means any modifications made in the original array will result in the copied array in shallow copy
num3 = num1.copy() # it will do the deep copy of an array which means if any changes made in the original array will not relect in the copied array

num1[1] = 5;
print(id(num1))
print(id(num3))
print(num1)
print(num3)
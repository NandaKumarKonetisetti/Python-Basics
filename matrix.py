from numpy import *
array1 = array([
                [1,2,3],
                [4,5,6],
                [7,8,9]
                  ])
print(array1)
print("To know that which type of data that the work is going on  : ",array1.dtype)
print("To know the dimensions of the array: ",array1.ndim)
print("To know no of rows and coloumns in the array",array1.shape)
print("To know the size of the array",array1.size);
# To convert an array from multidimensional to the single dimensional array
result = array1.flatten()
print("The  resultant single dimensional array is ",result)




array2 = array([

            [1,2,3,4,5,6],
            [7,8,9,10,11,12]


            ])
result1 = array2.reshape(3,4)
print("The two dimensional array is ",result1)
result2 = array2.reshape(2,2,3)
print("The three dimensional array is ",result2)


mat = matrix(array1)
print("The matrix is ")
print(mat)
m1 = matrix('1,2,3;7,8,9;4,5,6')
print('The another matrix is ')
print(m1)
print("The diagonal elements of a matrix is ",diagonal(m1))
addition = mat + m1
print("The addition of two matridws is \n",addition)
sub = mat - m1
print("The substraction of two matrices is\n",sub)
multi = mat * m1
print("The multiplication of two matrices is\n ",multi)
print("The maximum value in the given matrix is ",m1.max())
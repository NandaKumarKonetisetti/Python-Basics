f = open("data","r")

#print(f.read())   # To read the entire file
#print(f.readline()) # To read the line

#print(f.readlines()) # Returns all the lines where each line is an item in the list object
#print(f.read(40))  #To read the no of characters from the list.
#for data in f:    #To retrieve the whole data from the file
#  print(data,end = "")



f1 = open("Nanda Kumar","a")  # Opens a file in write mode and it helps to create a file if it does not exist
f1.write("Hi I am Nanda Kumar Konetisetty") # In wite mode it will clear the previous data and write the details that are given inside in  write function

f1.write(" How you are ")
for data in f:  # To copy the data from one file to the another file
    f1.write(data)




f5 = open("image.jpg","rb")
print(f5)
pic = open("Pic.JPG","wb") # Write binary file
for value in f5:
    pic.write(value)


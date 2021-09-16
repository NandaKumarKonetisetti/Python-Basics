list = ['Nanda','kumar',1,23,76]
for i in list:
    print(i)

for i in range(7):
    print(i)

for num in range(1,77,5): # range(start,end,step)
    print(num)



for i in range(1,7):
    print(i)



for i in ['a','b','c','d']:
    print(i)




print("Patterns using for loop")
for i in range(4):

    for j in range(4):
        print("# ",end = " ")
    print()



print("printing cross pattern")

for i in range(5):
    for j in range(i+1):
        print("* ",end = "")
    print()



print("Printing Revere the Above pattern")
for i in range(5):
    for j in range(5-i):
        print("* ",end = '')
    print()


print("printing the stars in diagonals")
for i in range(1,6):
    for j in range(1,6):
        if (i==j or i+j ==6 ):
            print("*",end = " ")
        else:
            print(end =" ")
    print()





#Break,continue and pass  in for loop
#Break will come out from the for loop
for i in range(7):
    if i==5:
        break
    else:
        print(i)


#sontinue executes the loop by skipping the current iteration
for i in range(7):
    if i==5:
        continue
    else:
        print(i)

print("Usage of pass keyword")
#In python it is not possible to leave the if statements as empty like so we will use pass keyword in those things but in java and c languages it is possible to leave those things as empty blocks
for i in range(21):
    if(i%2 != 0):
        pass
    else:
        print(i)




print("For else loop in Pyhon")
numbers = [1,6,7,3,9,3,10,15,10]
key = 18
for i in numbers:
    if i ==key:
        print("number found",i)
        break

else :
    print("number not found")



print("Printing the prime n")



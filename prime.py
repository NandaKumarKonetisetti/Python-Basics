number = 9;
for i in range(2,number):
    if number % i == 0:
        print("The given number is not a prime")
        break
else:
    print("The given number is a prime")



print("printing the prime numbers in between a Range")

lower = 2
upper = 7
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):

            if (num % i) == 0:
                 break
        else:
            print(num)










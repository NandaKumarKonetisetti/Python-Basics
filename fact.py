def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact *i
    print(fact)

fa = 5
factorial(fa)
#Recursion using factorial
def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)


val = 5
print(fact(val))




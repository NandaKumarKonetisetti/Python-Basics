
def fibo(num):
    a =0
    b = 1

    if num == 1:
        print(a)
    elif num == 2:
        print(a)
        print(b)
    elif num >2:
        for i in range(2, num):
            c = a + b
            a = b
            b = c
            print(c)

fibo(9)
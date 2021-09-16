

a = 77
b =  7

try:
    print("Opening the colnnection")
    print(a/b)
    val = int(input("Enter the value "))

except ZeroDivisionError as e :
    print("Hey division by zero is not possible ",e)


except ValueError as e :
    print(e)
except Exception as e:
    print(e)

finally:
    print("Closing the connetion")
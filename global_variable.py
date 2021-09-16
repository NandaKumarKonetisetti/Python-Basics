

a =90
b = 77
print(id(a))
def variable():
    a = 7
    x = globals()['a']
    print(id(x))
    print("In funciton",a)
    globals()['a'] = 77

variable()
print("outside a function",a)
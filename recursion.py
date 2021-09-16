import sys

print(sys.getrecursionlimit())  # to get the recursion limit
sys.setrecursionlimit(100)   #to set the recursion limit
count = 0
print(sys.getrecursionlimit())
def greet():
    global count
    count += 1
    print("Nanda", count)
    greet()
greet()

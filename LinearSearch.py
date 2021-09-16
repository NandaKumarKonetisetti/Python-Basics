#My code
pos = -1
def linearsearch(list,key):
    i =0
    while i<len(list):
        if list[i] == key:
            globals()["pos"] = i
            return "found at {}".format(pos+1)
        i = i + 1
    return "not found"






list = [8,9,4,7,2,8.5,9,67]
val = 67

print(linearsearch(list,val))



#Other code

def linearsearch1(list,key):

    for i in range(len(list)):
        if list[i] == key:
            globals()["pos"] = i
            return True

    return False



if linearsearch1(list,val):
    print("Element found at ",pos+1)
else:
    print("Element not Found")


def binarysearch(list,key):
    low =0
    high = len(list)-1

    while low < high:
        mid = (low+high) // 2
        if key < list[mid]:
            high = mid-1
        else:
            if key > list[mid]:
                low = mid +1
            if key == list[mid]:
                return "found at {}".format(mid+1 )



    return "Not Found "






list = [4,5,8,10,32,45,77,87,89]
item = 77
print(binarysearch(list,item))
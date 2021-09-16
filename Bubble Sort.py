def sort(num):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp = num[j]
                num[j]=num[j+1]
                num[j+1]= temp
        print(num)


nums = [4,8,9,5,7,2,1,4,8,6,7,9,8,3,4,2,6]
sort(nums)
print(nums)
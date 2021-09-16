def sort(nums):

    for i in range(len(nums)-1):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j]<nums[minpos]:
               minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)





list = [1,6,9,8,4,3,8,7,6,4,2,5,4,6,1,9,7,7,5]
sort(list)
print(list)
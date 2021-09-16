nums = [1,2,3,4,9,7,8]
print(nums[0])
#it = iter(nums) other way of writing the same code is
it = nums.__iter__()
for i in range(len(nums)):
    print(it.__next__())

print("Using user defined iter and next methods inside the class is given below")
#To define the iterator on ourselves we need to define the two methods iter and next
class digits:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return  self
    def  __next__(self):
        if self.num<8:
            value = self.num
            self.num += 1
            return value

        else:
            raise StopIteration

dig = digits()
for i in dig:
    print(i)



#Generators will give you iterators so we has to use iterable functions to fetch the value or else we can use iter and next functions
def generator():
    yield 1
    yield 2
    yield 3
    yield 7

gene = generator()
print(gene.__next__())#If users wants to call one one object
print(gene.__next__())
print(gene.__next__())

for i in gene:
    print(i)
def gen():
    value =0
    while(value<8):
        sq = value * value
        yield sq
        value += 1


for i in gen():
    print(i)
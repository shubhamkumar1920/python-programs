# generators
# generators are iterators
# iterator,iterable
l = [1,2,3]  #iterable
# for i in l:
#     print(l)


# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

for num in map(lambda a:a**2,l):
    print(num)

# memory ---[..............................................],list
# memory ---(9)

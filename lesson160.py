number1 = [2,4,6,8,10]
number2 = [1,2,3,4,5,6]
evens1 = []
for num in number1:
    evens1.append(num%2==0)
print(evens1)
print(all([True,False,True,True,True]))
print(all([True,True,True,True,True]))

# case2:
numbers1 = [2,4,9,8,10]
# number2 = [1,2,3,4,5,6]
print(all([num%2==0 for num in numbers1]))
print(any([num%2==0 for num in numbers1]))
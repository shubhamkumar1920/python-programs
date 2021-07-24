# advance min() and max()
numbers = [1,2,3,4,5,9]
print(min(numbers))

def func(item):
    return len(item)
names = ['Shubham Kumar','Mohit','ab','2']
print(max(names,key = func))
print(max(names,key = lambda item:len(item)))
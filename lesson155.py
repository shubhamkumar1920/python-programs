numbers = [1,2,3,4]
squares = map(lambda a:a**2,numbers)
number_iter = iter(numbers)
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
# print(next(number_iter)) # error occur stop iteration
print(iter(numbers))
# print(next(numbers)) # error occur 'list' object is not an iterator
numbers = [1,2,3,4]
def squares(a):
    return a**2

print(map(squares,numbers))

def square(a):
    return a**2
squares=list(map(square,numbers))
print(squares)

square = list(map(lambda a:a**2,numbers))
print(squares)

# list comp
squares_new = [i**2 for i in squares]
print(squares_new)

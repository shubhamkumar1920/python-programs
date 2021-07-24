# NOTE- function define karte hai tab parameter function ko call karte hai to usko kahte hai arguments

def multiply_nums(num,*args):
    multiply = 1
    print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply
print(multiply_nums(2,2,3))

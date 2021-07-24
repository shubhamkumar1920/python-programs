# *args with normal parameter

def multiply_nums(*args):
    multiply =1
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(2,2,3))

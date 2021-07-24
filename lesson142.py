# args as argument
def multiply_nums(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply *= i
    return multiply

num = [2,3,4]
print(multiply_nums(*num))

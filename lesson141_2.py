
# NOTE- function define karte hai tab parameter function ko call karte hai to usko kahte hai arguments

def multiply_nums(num1,num2,*args):
    multiply = 1
    print(args)
    for i in args:
        multiply *= i
    return multiply
print(multiply_nums(2,4,3,4))

num1 =2
num2 =4
args =(3,4)

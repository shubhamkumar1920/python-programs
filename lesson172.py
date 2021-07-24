# def add(a,b):
#     '''this function takes two numbers as arguments and return their sum'''
#     return a + b
# print(add(4,5))

from functools import wraps
def print_function_data(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print("you are calling{function._name_}function")
        print(f"{function._doc_}")
        return function(*args,**kwargs)
    return wrapper

@print_function_data
def add(a,b):
    '''this function takes two numbers as arguments and return their sum'''
    return a+b
print(add(4,5))

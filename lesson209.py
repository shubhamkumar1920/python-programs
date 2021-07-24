# make a function 'divide'
# divide(a,b)

# print(divide(4,3)) #2
# print(divide(4,0)) ## please don't divide by zero
# print(divide('4',2))

# soln:-
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        # print('you cannot divide a number by zero')
        print(err)
    except TypeError as err:
        print("numbers must be int or floats")
    except:
        print("unexpected error")
print(divide(10,'2'))
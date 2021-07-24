# chapter 11 exercise1:

# define a function 
# input

# num,iterable(tuple,list)containing numbers as args.

# example
# nums = [1,2,3]
# to_power(3,*nums)

# output
# list ----> [1,8,27]
# if user didn't pass any args then give a user a message ' hey you didn't pass args.
# else
# return list
# note-use list comprehension
# soln:-
def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "you didn't pass any args"
num = [1,2,3]
print(to_power(2,*num))
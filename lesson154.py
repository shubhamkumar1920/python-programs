# filter function
def is_even(a):
    return a%2 == 0

numbers = [3,4,2,1,5,6,9,8,10]
print(filter(is_even,numbers))

# check even from list
# def is_even(a):
    # return a%2 == 0
# numbers = [3,4,1,5,6,9,8,10]
evens=tuple(filter(is_even,numbers))
print(evens)
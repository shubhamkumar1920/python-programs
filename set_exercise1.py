# define a function that take list of strings
# list containing reverse of every string
# NOTE-use list comprehsion because we already did this exercises
# l =['abc','tuv','xyz']
# reverse_string(l)----->['bac','vut','zyx']

# soln:-
# case1:
def reverse_string(l):
    return [name[::-1] for name in l]

print(reverse_string(['abc','tuv','xyz']))
# case2:
def reverse_str(l):
    new_list = []
    for name in l:
        new_list.append(name[::-1])
    return new_list

print(reverse_str(['abc','tuv','xyz']))
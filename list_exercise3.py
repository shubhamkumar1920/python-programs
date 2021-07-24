# define a function that take list of words us arguments and
# return list with reverse of every element in the list
# ['abc','tuv','xyz']-->['cba','vut','zyx']

# soln:-

def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements

words = ['abc','tuv','xyz']
print(reverse_elements(words))
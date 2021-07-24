# define a function which will take list as a argument
# and this function will return a reversed list
# [1,2,3,4]---->[4,3,2,1]
# ['word1','word2']---->['word2','word1']
# note you simply do this with reverse method or [::-1]
# but try to do this with the help of append and return method

# soln:-

def reverse_list(l):
    r_list = []
    for i in range (len(l)):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list

numbers = [1,2,3,4]
print(reverse_list(numbers))

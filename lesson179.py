# define generator function
# take one number as argument
# Generate a sequence of even numbers from 1 to that number
# 5--->2,4
# 7--->2,4,6
# soln:-
def even_generator(n):
    for num in range(2,n+1,2):
        # if num%2==0:
        yield(num)

even_num = even_generator(20)
for num in even_num:
    print(num)

# for num in even_num:
    # print(num)

print(even_generator(20))

# create ypur first generator with generator function
# 1.) generator function

# 10,1 to 10

def num(n):
    for i in range(1,n+1):
        yield(i)

# for number in num(10):
#     print(number)

# memory ----->
numbers = num(10)

for num in numbers:
    print(num)

for num in numbers:
    print(num)
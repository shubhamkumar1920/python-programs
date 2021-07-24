# case1:
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)
# case2:
squares2 = [i**2 for i in range (1,11)]
print(squares2)

# for negative
negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)

# case2:
new_negative = [-i for i in range(1,11)]
print(new_negative)

# string
names = ['Harshit','Mohit','Rohit']
# new_list = ['H','M','R']
new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)

# case2:
new_list2 = [name[0] for name in names]
print(new_list2)
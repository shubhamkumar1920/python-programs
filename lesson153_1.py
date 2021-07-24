numbers = [1,2,3,4]
def squares(a):
    return a**2

# without list comp-or map function
new_list = []
for num in numbers:
    new_list.append(squares(num))
print(new_list)
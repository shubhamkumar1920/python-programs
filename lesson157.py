l1 = [1,3,5,7]
l2 = [2,4,6,8]
l = [(1,2),(3,4),(5,6),(7,8)]
l1,l2 = list(zip(*l))
print(list(l1))
print(list(l2))

# case2:
l1 = [1,3,5,7]
l2 = [2,4,6,8]
new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list)
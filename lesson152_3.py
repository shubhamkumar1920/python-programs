names = ['abc','abcdef','harshit']
# for pos,name in enumerate(names):
#     print(f"{pos}---->{name}")
def find_pos(l,target):
    for pos,name in enumerate(l):
        if name == target:
            return pos
    return -1
print(find_pos(names,'abc'))
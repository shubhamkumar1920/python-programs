# we use enumerate function with for loop to track position of our item in iterable
# how we can do this without enumerate function 
names = ['abc','abcdef','harshit']
# 0 ---'abc'
# 1 --- 'abcdef'
pos = 0
for name in names:
    print(f"{pos}--->{name}")
    pos += 1

for pos,name in enumerate(names):
    print(f"{pos}--->{names}")

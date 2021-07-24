# readfile
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method

# f = open('file1.txt')
# print(f'cursor position -{f.tell()}')

# print(f.read())
# print(f.readline(),end='') 
# print(f'cursor position -{f.tell()}')
# print('before seek method')
# f.seek(0)
# print('after seek method')
# print(f'cursor position -{f.tell()}')
# print(f.read())

# f.close() 

f = open('file1.txt')
# lines = f.readlines()
# print(len(lines)) 
# for line in lines:
#     print(line,end='')
f.close()

f = open(r"g:\python\chapter_18\file2.txt")

# \n,\t
# windows -\
# linux,mac - \

for line in f.readlines()[:2]:
    print(line,end='')
# name, closed
print(f.closed)
f.close
print(f.closed)
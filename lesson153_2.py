# length of word of string
names = ['abc','abcd','abcde']
length = map(len,names)
for i in length:
    print(i)

# case2:
names = ['abc','abcd','abcde']
length = list(map(len,names))
print(length)
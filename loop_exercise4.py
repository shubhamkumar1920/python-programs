# ask a user for name
# example-harshit vashisth
# print count of each words
# output:
# H:1
# a:2
# r:1
# s:3
# n:3
# i:2
# t:2
#  :1
# v:1

# soln:-

name = input("please enter your name")
temp_var=""
i=0
while i < len(name):
    if name[i] not in temp_var:
        print(f"{name[i]}:{name.count(name[i])}")
        i += 1

# sum of n natural number
# ask a user for natural number(n)
# print total from 1 to n

# soln:-

n=input("enter a number:")
n= int(n)
total = 0
i=1
while i<=n:
    total += i
    i += 1
    print(total)
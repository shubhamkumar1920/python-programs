a = int(input(" enter first number: "))
b = int(input(" enter second number: "))
for i in range(1, 50):
    if ((i % a == 0) and (i % b != 0)):  
        print(i,end='')
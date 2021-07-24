# scope
x = 5 #gobal variable

def func():
    global x
    x = 7 #local variables
    return x

print(x)
print(func())
print(x)
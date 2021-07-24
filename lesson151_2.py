# lambda with if,else:
def func(s):
    if len(s) > 5:
        return True
    return False

# cas1:
func = lambda s:True if len(s) > 5 else False
print(func('abcdefg'))

# case2:
func1 = lambda s:len(s) > 5
print(func1('abcdefg'))
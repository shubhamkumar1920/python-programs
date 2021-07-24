def my_sum(*args):
    total=0
    for num in args:
        total += num
    return total
print(my_sum(1,2,3,4))

def my_sum1(*args):
    if all ([(type(arg) == int or type(arg) == float) for arg in args]):
        total =0
        for num in args:
            total+=num
        return total
    else:
        return "wrong input"

print(my_sum1(1,2,3,4,8,9,'harshit',['harshit']))

print(my_sum1(1,2,3,4,8.9))
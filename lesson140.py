# flexible function
def all_total(*args):
    total = 0
    for num in args:
        total += num
    return total

print(all_total(3,4,10,9))
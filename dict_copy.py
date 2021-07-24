# copy method
d = { 'name':'unknown','age':'unknown'}
d1 = d.copy()
print(d1)

print(d1.popitem())
print(d)
print(d1 is d)
print(d1 == d)
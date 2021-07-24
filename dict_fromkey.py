# fromkeys
d = {'name':'unknown','age':'unknown'}
# case1:
d = dict.fromkeys(['name','age','height'],'unknown')
print(d)
# case2:
e = dict.fromkeys(('name','age','height'),'unknown')
print(e)
# case3:
f = dict.fromkeys("abc",'unknown')
print(f)
# case4:
g = dict.fromkeys(range(1,11),'unknown')
print(g)
# case5:
h = dict.fromkeys(['name','age'],['unknown','unknown'])
print(h)
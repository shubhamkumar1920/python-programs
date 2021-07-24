# get method(useful)
d = { 'name':'unknown','age':'unknown'}
print(d['name'])
# case2:
e = {'name':'Shubham','age':'unknown'}
print(e.get('name'))
# case3:
if 'name' in e:
    print('present')
else:
    print('not present')
# case4:
if d.get('name'):
    print('present')
else:
    print('not present')

    
# if None---> False, else----->True
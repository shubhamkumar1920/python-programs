def func(item):
    return len(item)

names=['shubham kumar','mohit','ab','2']
print(max(names,key=func))

print(max(names,key=lambda item:len(item)))

students={
    'shubham':{'score':90,'age':24},
    'mohit':{'score':78,'age':45},
    'rohit':{'score':76,'age':19}
}
student2=[
    {'name':'shubham','score':90,'age':24},
    {'name':'mohit','score':70,'age':19},
    {'name':'rohit','score':60,'age':25}
]

print(max(student2,key=lambda item:item.get('age'))['name'])

max(students,key=lambda item:students[item]['score'])
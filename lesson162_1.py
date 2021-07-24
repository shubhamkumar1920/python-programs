students = {
    'shubham':{'score':90,'age':24},
    'mohit':{'score':75,'age':19},
    'rohit':{'score':76,'age':23}
}
students2 = [
    {'name':'shubham','score':90,'age':24},
    {'name':'mohit','score':70,'age':19},
    {'name':'rohit','score':60,'age':25}
]
print(max(students2,key = lambda item:item.get('age'))['name'])
print(max(students,key=lambda item:students[item]['score']))
fruits = ['grapes','mango','apple']
fruits.sort()
print(fruits)
# case2:
fruits2 = ('grapes','mango','apples')
print(sorted(fruits))
# case3:
fruits3 = {'grapes','mango','apple'}
print(sorted(fruits))

# case4:
guitars = [
    {'model':'yamaha&310','price':8400},
    {'model':'faith naptune','price':50000},
    {'model':'faith apollo venus','price':35000},
    {'model':'taylor814ce','price':45000}
]
sorted_guitars = sorted(guitars,key = lambda d:d['price'],reverse =True)
print(sorted_guitars)
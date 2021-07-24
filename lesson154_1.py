numbers = [3,4,2,1,5,6,9,8,10]
evens = tuple(filter(lambda a:a%2==0,numbers))
print(evens)

# cas2:
even = filter(lambda a:a%2==0,numbers)
for i in even:
    print(i)

new_evens=[i for i in numbers if i%2==0]
print(even)
print(new_evens)
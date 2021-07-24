# we create our list using square brackets = []

number = [1,2,3,4]
print(number)

words = ["word1","word2","word3",]
print(words)

mixed = [1,2,3,4]
print(mixed)

numbers = [1,2,3,4]
print(numbers[2])

word = ["word1","word2","word3"]
print(word[:2])

mixed = [1,2,3,4,"five","six",2.3,None]
print(mixed[-1])

mixed = [1,2,3,4,"five","six",2.3,None]
mixed[1:] = 'two'
print(mixed)

mixed[1:]='two'
print(mixed)

mixed[1:] = ['three','four']
print(mixed)
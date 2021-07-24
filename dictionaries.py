# how to create dictionaries
user = {
    'name':'Shubham',
    'age':24
}
print(user)
print(type(user))

# second method to create dictionary
user1 = dict(name ='Shubham',age = 24)
print(user1)

# how to access data from dictionary
# NOTE- there is no indexing because of unordered collection of data
print(user['name'])
print(user['age'])

# which type of data a dictionary can store ?
# anything
# numbers,strings,list,dictionary

user_info = {
    'name':'shubham',
    'age':24,
    'fav_movies':['coco','kimi no na wa'],
    'fav_tunes':['awakening','fairy tale'],
}
print(user_info['fav_movies'])

# how to add data to empty dictionary
user_info2 = {}
user_info2['name'] = 'mohit'
user_info2['age'] = 19
print(user_info2)
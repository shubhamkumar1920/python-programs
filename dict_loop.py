user_info = {
    'name':'Shubham',
    'age':24,
    'fav_movies':['coco','kiwi no na wa'],
    'fav_tunes':['awakening','fairy tale'],
}
# check if key exist in dictionary

if 'name' in user_info:
    print('present')
else:
    print('not present')

# check if value exist in dictionary

if 24 in user_info.values():
    print('present')
else:
    print('not present')

# loop in dictionaries
for i in user_info:
    print(i)

# values method
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))

# keys method
user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

# loop in dictionaries
for i in user_info:
    print(user_info[i])

# item method
user_items = user_info.items()
print(user_items)
print(type(user_items))

# key value
for key,value  in user_info.items():
    print(f"key is {key} and value is {value}")
# pop method
user_info = {
    'name':'shubham',
    'age':24,
    'fav_movies':['coco','kimi no na wa'],
    'fav_tunes':['awakening','fairy tale'],
}

popped_item = user_info.pop('fav_tunes')
print(f"popped item is {popped_item}")
print(user_info)
print(type(popped_item))

# popped method
popped_item = user_info.popitem()
print(user_info)
print(type(popped_item))
# zip functions
# build in function
user_id = ['user1','user2','user3']
names = ['harshit','mohit','rohit']
print(zip(user_id,names))
print(list(zip(user_id,names)))

# case2:
users_id = ['user1','user2']
# names = ['harshit','mohit','rohit']
print(list(zip(users_id,names)))

# case3:
example = [('a',1),('b',2)]
print(dict(example))

# case4:
# user_id = ['user1','user2','user3']
# names = ['harshit','mohit','rohit']
print(dict(zip(user_id,names)))

# case5:
# user_id = ['user1','user2','user3']
# names = ['harshit','mohit','rohit']
last_names = ['vashistha','kumar','sharma']
print(list(zip(user_id,names,last_names)))
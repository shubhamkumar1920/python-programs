# watch coco
# ask user's name and age
# if user's name start with ('a' or 'A')and age is above 10 then
# print you can watch coco movie'
# else print 'sorry,you cannot watch coco'

# soln:-

user_name = input("enter your name please:")
user_age = input("enter your age please:")
user_age = int(user_age)
if user_age >= 10 and (user_name[0]=='s' or user_name[0]=='S'):
    print("you can watch coco")
else:
    print("you cannot watch coco")
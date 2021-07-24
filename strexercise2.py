# take two comma seperated inputs from user
# 1)user's name,example_"Harshit"
# 2)a single character, "H"

# output-2 print lines
# 1)user's name length
# 2)count the character that user inputed (bonus:case insensitive count)

name,char=input("enter comma seperated name and character:").split(",")
print(f"length of your name is {len(name)}")
print(f"character count:{name.lower().count(char.lower())}")

# case sensitive
print(f"charcter count:{name.count(char)}")

print(f"character count:{name.strip().lower().count(char.strip().lower())}")
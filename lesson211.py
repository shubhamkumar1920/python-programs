# python custom exceptions
# Q - why custom exceptions ?
# A - to increase he readability of code.

# example
class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name) < 8:
        raise NameTooShortError('name is too short')

username = input('enter our name:  ')
validate(username)
print(f'hello{username}')
# NameTooShort
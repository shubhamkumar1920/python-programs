def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

print(is_palindrome("naman"))
print(is_palindrome("horse"))
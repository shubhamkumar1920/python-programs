# define is palindrome function that take one word in string as input
# and return True if it is palindrome else return False
# palindrome-word that reads some backwards as forwards
# example
# is_palindrome("madam")
# is_palindrome("naman")----true
# is_palindrome("horse")----false

# logic(algorithm)
# step 1 -> reverse the string
# step 2 -> compare reversed string with original string
# case 1:
def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

print(is_palindrome("naman"))
print(is_palindrome("horse"))
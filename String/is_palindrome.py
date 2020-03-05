def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

# Tests
print(is_palindrome('Deleveled'))  # True

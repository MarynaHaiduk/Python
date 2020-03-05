def get_consonants(word):
    vowels = "aeoui"
    consonants = ""
    for i in word:
        if i not in vowels:
            consonants += i
    return consonants

# Tests
print(get_consonants("consonant"))  # cnsnnt

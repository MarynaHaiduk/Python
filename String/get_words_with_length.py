def get_words_with_length(s, num):
    return " ".join([i for i in s.split(" ") if len(i) <= num])

# Tests
s = "Get the list of words less than the number"
print(get_words_with_length(s, 3))  # Get the of the

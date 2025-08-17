strings = ['abc', 'you', 'and', 'me']
capitalized = (string.capitalize() for string in strings)
print(tuple(capitalized))
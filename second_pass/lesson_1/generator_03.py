strings = ['hello', 'my', 'name', 'could be']
capitalized = (my_str.capitalize() for my_str in strings)

print(tuple(capitalized))
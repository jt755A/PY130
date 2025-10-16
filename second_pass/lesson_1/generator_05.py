strings = ['hello', 'my', 'name', 'could be']

capitalized = (my_str.capitalize() for my_str in strings
               if len(my_str) >= 5)

print(set(capitalized))
def capitalize(str_list):
    for string in str_list:
        yield string.capitalize()

capitals = capitalize(['the', 'time', 'is', 'now'])
print(tuple(capitals))
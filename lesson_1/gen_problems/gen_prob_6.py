def capitalize(lst):
    for string in lst:
        if len(string) < 5:
            yield string.capitalize()

str_list = ['the', 'timing', 'is', 'now']

print(set(capitalize(str_list)))


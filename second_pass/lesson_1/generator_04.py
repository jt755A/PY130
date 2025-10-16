def capitalize(str_lst):
    for str in str_lst:
        yield str.capitalize()

my_str_lst = ['hello', 'my', 'name', 'could be']

print(tuple(capitalize(my_str_lst)))
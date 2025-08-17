def for_each(callback, iterable):
    for item in iterable:
        callback(item)

for_each(lambda number: print(number**2), [1, 2, 3, 4, 5])
# 1
# 4
# 9
# 16
# 25

pets = ('cat', 'dog', 'fish', 'bearded dragon')
for_each(lambda string: print(string.title()), pets)
# Cat
# Dog
# Fish
# Bearded Dragon

nested_lists = [[1, 2], [3, 4], [5, 6, 7]]
for_each(lambda sublist: sublist.pop(), nested_lists)
print(nested_lists)
# [[1], [3], [5, 6]]
from functools import reduce

reduced = reduce(lambda a, b: a + b, ['hello', 'my', 'name', 'is'])
print(reduced)
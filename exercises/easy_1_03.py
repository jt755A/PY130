from functools import reduce

def product(x, y):
    return x * y

# answer = reduce(product, [1, 2, 3, 4, 5])
answer = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(answer) #120?
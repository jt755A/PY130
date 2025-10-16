def reduce(callback, iterable, starting):
    accum = starting
    for element in iterable:
        accum = callback(element, accum)

    return accum

numbers = [1, 2, 3, 4]

# sum_square = lambda number, accum: (number**2) + accum

# summed_result = reduce(sum_square, numbers, 0)
summed_result = reduce(lambda num, accum: (num**2) + accum, numbers, 0)
print(summed_result)
# 30
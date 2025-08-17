def reduce(callback, iterable, start_value):
    accum = start_value
    for current_item in iterable:
        accum = callback(current_item, accum)

    return accum

numbers = [1, 2, 3, 4] # [1, 4, 9, 16] --> 30
# square = lambda number, accum: accum + number**2
# print(reduce(square, numbers, 0))
total = reduce(lambda number, accum: accum + number**2, numbers, 0)
print(total)
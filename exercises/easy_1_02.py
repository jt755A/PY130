my_nums = [1, 2, 3, 4, 5, 6]

def even(num):
    return num % 2 == 0

even_nums = list(filter(even, my_nums))
even_nums = list(filter(lambda x: x % 2 == 0, my_nums))

print(even_nums)
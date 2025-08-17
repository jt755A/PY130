nums = [1, 2, 3, 4]

def square(num):
    return num**2

sq_lst = list(map(square, nums))
sq_list = list(map(lambda x: x**2, nums))


print(sq_lst)
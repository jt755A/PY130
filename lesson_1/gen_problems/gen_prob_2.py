def get_reciprocals_up_to(max_num):
    num = 1
    while num <= max_num:
        yield 1 / num
        num += 1

reciprocals = get_reciprocals_up_to(10)
for number in reciprocals:
    print(number)
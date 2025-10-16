def reciprocals(n):
    # for x in range(1, n + 1):
    #     yield 1/x
    number = 1
    while number <= n:
        yield 1/number
        number += 1

first_ten = reciprocals(10)
for num in first_ten:
    print(num)
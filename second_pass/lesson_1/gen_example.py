def count_up_to(upper_limit):
    for number in range(upper_limit):
        yield number

counter = count_up_to(3)

print(next(counter))
print(next(counter))
print(next(counter))

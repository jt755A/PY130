def first_five():
    for num in range(1, 6):
        yield num

for number in first_five():
    print(number)
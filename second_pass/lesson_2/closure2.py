def make_counter():
    counter = 0
    def counter_func():
        nonlocal counter
        counter += 1
        return counter

    return counter_func

increment_counter = make_counter()
print(increment_counter())
print(increment_counter())

increment_counter = make_counter()
print(increment_counter())
print(increment_counter())
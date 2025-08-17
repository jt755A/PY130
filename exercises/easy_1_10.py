def generate_strings():
    while True:
        string = input('Enter a string: ')
        if string.strip().casefold() == 'stop':
            break
        yield string

for string in generate_strings():
    print(string)

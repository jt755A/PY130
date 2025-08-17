my_string = 'hello, nice to meet you'

rev_string = (char for char in my_string[::-1])

for char in rev_string:
    print(char)
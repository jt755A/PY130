def register(username, /, age, *, password):
    print(f'U: {username}, p: {password}, age: {age}')


register('cats', 5, password='kibbles')
register('cats', age=5, password='kibbles')
register('cats', age=5, 'kibbles')


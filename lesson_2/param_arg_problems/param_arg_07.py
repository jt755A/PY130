def register(username, /, age, *, password):
    print(f"username: {username}, password: {password}, age: {age}")

register('bob', 10, password='123')
register('bob', age=10, password='123')
register('bob', age=10, '123')


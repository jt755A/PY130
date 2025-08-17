def describe_pet(animal_type, *, name=''):
    return f"Your pet {name} is a {animal_type}"

print(describe_pet('dog', name='fluffy'))
print(describe_pet('dog', 'bunny', name='fluffy'))

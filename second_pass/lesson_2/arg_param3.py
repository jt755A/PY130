def describe_pet(animal_type, *, name=""):
    print(f'My pet {name} is a {animal_type}')

describe_pet('fish', name='Geoffrey')
describe_pet('fish')

def find_person(**kwargs):
    for name, profession in kwargs.items():
        if name == 'Antonina':
            return profession

    return 'Antonina not found'

print(find_person(joe='plumber', bob='blacksmith', Antonina='lawyer'))
def find_person(**kwargs):
    if 'Antonina' in kwargs:
        print(kwargs['Antonina'])

    else:
        print('Antonina not found')


find_person(bob='plumber', tracy='programmer', jeff='nurse')
find_person(bob='plumber', tracy='programmer', Antonina='rocket scientist')

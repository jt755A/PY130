strings = ['hello', 'my', 'name', 'could be']

def capitalized(strings):
    for strng in strings:
        if len(strng) >= 5:
            yield strng.capitalize()

print(set(capitalized(strings)))
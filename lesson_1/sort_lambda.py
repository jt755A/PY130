animals = ["Tiger", 'tiger', "lion", "Lion", "zebra", "Zebra"]
animals_alpha = animals.sort(key=lambda word: word.casefold())
print(animals)

# alpha = sorted(animals, key=lambda word: word.casefold())

# alpha_2 = sorted(animals, key=str.casefold)

# print(animals)
# print(alpha)
# print(alpha_2)

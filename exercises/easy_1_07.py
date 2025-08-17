matrix = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9]
 ]

# flat = [number for row in matrix
#         for number in row]

flat = list(number for row in matrix
        for number in row)

print(flat)
def make_adder(x):
    y = 10
    def adder(z):
        return x + y + z
    return adder

add_with_5 = make_adder(5)

# The closure 'add_with_5' captures both 'x' and 'y'
print("Values in the closure's cells:")
for cell in add_with_5.__closure__:
    print(cell.cell_contents)

# Expected Output:
# Values in the closure's cells:
# 5
# 10
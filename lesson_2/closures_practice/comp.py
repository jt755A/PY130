funcs = [lambda: i for i in [1, 2]]
func1, func2 = funcs

for cell in func1.__closure__:
    print(cell.cell_contents)

for cell in func2.__closure__:
    print(cell.cell_contents)

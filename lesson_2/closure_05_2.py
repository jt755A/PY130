def later2(func, first_arg):
    def inner(second_arg):
        return func(first_arg, second_arg)

    return inner

def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
print(shutdown_warning.__closure__)
for cell in shutdown_warning.__closure__:
    print(cell.cell_contents)
shutdown_warning(30)
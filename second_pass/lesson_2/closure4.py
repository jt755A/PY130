def printer(message):
    print(message)

def later(func, argument):
    def inner():
        return func(argument)

    return inner

print_warning = later(printer, "The system is shutting down!")
print_warning()
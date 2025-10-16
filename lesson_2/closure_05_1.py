def later(func, arg):
    def inner():
        return func(arg)

    return inner

def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()  # The system is shutting down!
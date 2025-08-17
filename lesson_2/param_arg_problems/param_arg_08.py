def print_message(*, message, level="INFO"):
    print(f"{level}{message}")

print_message(message='Hello world')
print_message(message='Hello world', level='breakfast')

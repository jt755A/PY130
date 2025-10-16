def print_message(*, message, level="INFO"):
    print(f'{level}{message}')

print_message(message="and that's it...")
print_message(message="and that's it...", level='Tip-top')
print_message('POSITIONAL', message="and that's it...")


from functools import partial

def greet(name, greeting):
    return f"{greeting}, {name}!"

say_hello_to = partial(greet, "Hello")
print(say_hello_to("Alice"))  # What will this print?
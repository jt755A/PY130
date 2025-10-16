def prefix(text):
    def message(new_text):
        return text + new_text
    return message

bubbles = prefix("()()()()()")

message1 = bubbles('This is a bubble text')
print(message1)
print(bubbles.__closure__)

one_line_result = prefix('<><><><>')('my subsequent message')
print(one_line_result)
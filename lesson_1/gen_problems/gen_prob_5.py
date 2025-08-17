str_list = ['the', 'timing', 'is', 'now']
capitalize = (string.capitalize() for string in str_list
              if len(string) >= 5)

print(set(capitalize))
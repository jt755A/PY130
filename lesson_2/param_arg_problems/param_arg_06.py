def concat_strings(*args, sep=' '):
    return sep.join(args)

print(concat_strings('hi,', 'this', 'is', 'a', 'joined', 'string'))
print(concat_strings('hi,', 'this', 'is', 'a', 'joined', 'string', sep='!!'))


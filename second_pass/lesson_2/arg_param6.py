# keyword only

def concat_strings(*args, sep=' '):
    return sep.join(args)

print(concat_strings('a', 'b', 'c', 'd'))
print(concat_strings('a', 'b', 'c', 'd', sep='!!!'))

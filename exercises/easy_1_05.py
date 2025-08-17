# if x (i.e. select if truthy) - but what about other falsy values?

no_none = list(filter(lambda x: x != None, [None, 0, [], set(), 'hello!']))
no_none = list(filter(lambda value: value is not None,
                      [None, 0, [], set(), 'hello!']))

print(no_none)


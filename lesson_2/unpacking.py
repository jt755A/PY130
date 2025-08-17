# can unpack sets, order will probably change each time

staff = {'Chris', 'Pete',}

# chris, pete, nick = staff

chris, pete, *remaining = staff
print(chris, pete, remaining)

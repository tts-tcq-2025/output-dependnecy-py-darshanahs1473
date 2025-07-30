
def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'


assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')

# Added test to catch unhandled 38
assert(size(38) == 'M') 

print("All is well (maybe!)")

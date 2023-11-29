def is_odd(num):
    """ See if remainder is 1 """
    if isinstance(num, int):
        return num%2 == 1
    else:
        raise AssertionError
    

assert is_odd(1)
assert is_odd(2) == False
assert is_odd.__doc__

has_failed = False
try:
    is_odd("hfasfjahsf")
except AssertionError:
    has_failed = True
assert has_failed
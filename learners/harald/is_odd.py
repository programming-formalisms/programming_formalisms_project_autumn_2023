def is_odd(num):
    """ See if remainder is 1 """
    return num%2 == 1

assert is_odd(1)
assert is_odd(2) == False
assert is_odd.__doc__

try:
    is_odd(1)
except AssertionError:
    has_failed = True
assert has_failed
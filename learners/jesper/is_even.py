# is_even
def is_even(number):
    return number % 2 == 0

assert is_even(0)
assert is_even(1) == False

has_failed = False
try:
    is_even("string")
except AssertionError:
    has_failed = True
assert has_failed

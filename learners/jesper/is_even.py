# is_even
def is_even(number):
    """Function for checking if a number is even."""
    assert type(number) == int
    return number % 2 == 0

assert is_even(0)
assert is_even(1) == False

has_failed = False
try:
    is_even("string")
except AssertionError:
    has_failed = True
assert has_failed

assert is_even.__doc__

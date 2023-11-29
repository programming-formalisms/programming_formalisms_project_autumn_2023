# is_zero
def is_zero(number):
    """Determines if a number is zero."""
    assert isinstance(number, int)
    return number == 0

assert is_zero.__doc__
assert is_zero(0)
assert is_zero(1) == False
assert is_zero(2) == False

has_given_exception = False
try:
    is_zero("wefufewpf")
except AssertionError:
    has_given_exception = True
assert has_given_exception
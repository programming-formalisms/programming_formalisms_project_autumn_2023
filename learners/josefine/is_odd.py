# Exercise: is_odd 

# Function
def is_odd(number: int) -> bool:
    """Return True if the integer number is odd"""
    assert isinstance(number, int)

    return number % 2 == 1


# Tests
assert is_odd.__doc__
assert is_odd(1)
assert is_odd(2) == False

has_raised_assertionerror = False
try:
    is_odd('string')
except AssertionError:
    has_raised_assertionerror = True
assert has_raised_assertionerror

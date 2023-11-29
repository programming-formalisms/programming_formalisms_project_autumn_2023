def is_odd(n):
    """
        Check if a number is odd
        input: integer
        output: bool
    """
    assert isinstance(n, int)

    return n % 2 == 1


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

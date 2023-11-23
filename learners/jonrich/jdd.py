def add_numbers(a, b):
    """Add two numbers together."""
    assert isinstance(a, (int, float)), "a must be a number"
    assert isinstance(b, (int, float)), "b must be a number"
    return a + b


assert add_numbers.__doc__
has_raised_exception = False
try:
    add_numbers("a", "b") == "ab"
except AssertionError:
    has_raised_exception = True
assert has_raised_exception

assert add_numbers(1, 2) == 3

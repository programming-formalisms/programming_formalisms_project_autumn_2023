def add_numbers(a, b):
    """Function for adding two numbers"""
    assert isinstance(a, int), "a must be an integer"
    assert isinstance(b, int), "b must be an integer"
    return a + b


assert add_numbers.__doc__


has_raised = False
try:
    add_numbers("evil string", "another evil")
except AssertionError:
    has_raised = True
assert has_raised

assert add_numbers(1.2, 2.3) > 3.4

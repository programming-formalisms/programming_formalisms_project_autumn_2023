def add_numbers(a, b):
    """Function for adding two numbers"""
    assert isinstance(a, (int, float)), "a must be an integer or float"
    assert isinstance(b, (int, float)), "b must be an integer or float"
    return a + b

def subtract_numbers(a, b):
    assert isinstance(a, (int, float)), "a must be an integer or float"
    assert isinstance(b, (int, float)), "b must be an integer or float"
    return b - a


assert add_numbers.__doc__


has_raised = False
try:
    add_numbers("evil string", "another evil")
except AssertionError:
    has_raised = True
assert has_raised

assert add_numbers(1.2, 2.3) > 3.4

assert add_numbers(1, 2) == 3

assert subtract_numbers(3, 2) == 1

def add_numbers(a, b):
    """Function for adding two numbers"""
    return a + b


assert add_numbers.__doc__


has_raised = False
try:
    add_numbers("evil string", "another evil")
except AssertionError:
    has_raised = True
assert has_raised

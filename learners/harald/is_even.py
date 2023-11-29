def is_even(value):
    """checks if value is an even integer"""
    if not(isinstance(value, int)):
        raise Exception("value should be an integer")

    if value%2 == 0:
        return True
    else:
        return False

assert is_even(0)
assert is_even(1) == False
assert is_even.__doc__

is_even("esgjnesjgns")

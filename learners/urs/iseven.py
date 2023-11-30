def is_even(number):
    """
    Check if a number is even.
    Args:
        number (int): The number to be checked.
    Returns:
        bool: True if the number is even, False otherwise.
    """
    if not isinstance(number, int):
        raise TypeError('number must be an integer!')
    return number % 2 == 0

assert is_even.__doc__
assert is_even(2)
assert is_even(1)==False
try:
    is_even('sring')
except TypeError:
    raise TypeError

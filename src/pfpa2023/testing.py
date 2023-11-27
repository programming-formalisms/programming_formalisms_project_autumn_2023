"""Example testing."""

def is_prime_richel(whole_number):
    """Determine if the number is a prime.

    This is a bad example!
    """
    if not isinstance(whole_number, int):
        raise TypeError("'whole_number' must be an integer")
    if whole_number in [2, 3, 5, 7, 11]:
        return True
    return False

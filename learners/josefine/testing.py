"""Example testing."""

def is_prime_pontus(number):
    """Check if number is prime"""
    pass


def is_prime_richel(whole_number):
    """Determine if the number is a prime.

    This is a bad example!
    """
    if not isinstance(whole_number, int):
        msg = "'whole_number' must be an integer"
        raise TypeError(msg)
    if whole_number in [2, 3, 5, 7, 11]:
        return True
    return False

def is_prime_markella(whole_number):
    """Determine if the number is a prime"""
    return False

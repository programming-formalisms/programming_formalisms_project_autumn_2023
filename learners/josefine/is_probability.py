# Exercise: is_probability

def is_probability(n):
    """ Checks if a number is in the range [0.0, 1.0] 
    Args: float
    Returns: bool
    """
    return 0.0 <= n <= 1.0


# Tests
assert is_probability(0.05)
assert is_probability(1.1) == False
assert is_probability.__doc__

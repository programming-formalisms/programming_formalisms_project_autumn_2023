"""General-purpose functions of moderate complexity.

Moderate complexity' means:
 * a cyclomatic complexity of 1 to 8
 * may have for-loops
 * maximally two variables modified
"""

from random import randint


def is_prime_richel(whole_number):
    """Determine if the number is a prime.

    This is a bad example!
    """
    if not isinstance(whole_number, int):
        raise TypeError("'whole_number' must be an integer")
    if whole_number in [2, 3, 5, 7, 11]:
        return True
    return False

def is_odd(number):
    """
    Check if a number is odd.

    Parameters:
    - number (int): The number to check.

    Returns:
    - bool: True if the number is odd, False otherwise.
    """
    return number % 2 != 0

assert is_odd(4) == False

assert is_odd(1) == True

assert is_odd(1)

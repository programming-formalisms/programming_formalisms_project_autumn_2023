"""Example testing."""

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

def is_prime_jesper(number):
    """My own prime number function"""
    if type(number) != int:
        msg = "needs to be an integer"
        raise TypeError(msg)
    if number > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(number/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (number % i) == 0:
                return False
        else:
            return True
    else:
        return False
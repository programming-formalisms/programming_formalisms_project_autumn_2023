"""Example testing."""
import random


def coin_flip_pontus():
    """Simulate coin flip"""
    return True

def coin_toss_urs():
    """Randomly return True or False."""
    return True


def is_prime_harald(number):
    """Check if number is prime, again"""
    if not(isinstance(number, int)):
        raise TypeError
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True


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

def is_prime_thanadol(number):
    """ 
    Checking the numebr is prime. 
    """

    if number <= 1:
        return False
    else:
        # for 2 and above integer
        if not isinstance(number, int):
            raise TypeError()
        

    
def flip_coin_josefine():
    """Randomly return True or False"""
    return random.randint(0, 1) > 0

def flip_coin_cormac():
    seq = [False, True]
    return random.choice(seq)

1
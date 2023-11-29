# is odd
def is_odd(number):
    '''
    This function check the odd number. 
    '''
    result = number % 2 == 1
    return result

assert is_odd(1)
assert is_odd(0) == False
assert is_odd.__doc__
assert is_odd("string")
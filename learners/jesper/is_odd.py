# is odd
def is_odd(number):
    '''
    This function check the odd number. 
    '''
    #assert type(number) == int
    
    result = number % 2 == 1
    return result

has_failed = False
try:
    is_odd("string")
except TypeError:
    has_failed = True
assert has_failed

assert is_odd(1)
assert is_odd(0) == False
assert is_odd.__doc__
assert is_odd(1.0)

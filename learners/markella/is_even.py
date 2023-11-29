def is_even(number):
    assert isinstance(number, int)
    
    res = number % 2  
    return res == 1

assert is_even(2) == True
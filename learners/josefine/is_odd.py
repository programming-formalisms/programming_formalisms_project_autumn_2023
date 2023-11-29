# Exercise: is_odd 

def is_odd(number):
    return number % 2 == 1

assert is_odd(1)
assert is_odd(2) == False

has_raised_typeerror = False
try:
    is_odd('string')
except TypeError:
    has_raised_typeerror = True
assert has_raised_typeerror == False
    

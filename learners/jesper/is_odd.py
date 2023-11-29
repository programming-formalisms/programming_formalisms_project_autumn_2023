# is odd
def is_odd(number):
    result = number % 2 == 1
    return result

assert is_odd(1)
assert is_odd(0) == False
def is_even(number):
    if not isinstance(number, int):
        raise TypeError('number must be an integer!')
    return number % 2 == 0

assert is_even(2)
assert is_even(1)==False
#assert is_even("a")
assert is_even.__doc__

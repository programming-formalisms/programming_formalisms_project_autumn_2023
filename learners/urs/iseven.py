def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

assert is_even(2)
assert is_even(1)==False
assert is_even("a")
# is_odd

def is_odd(x):
	"""
	Determines wheteher a number is odd.
	:param x: int, input number
	:return: bool
	"""
	return x % 2 == 1
	
assert not is_odd(4)
assert is_odd(1.1)

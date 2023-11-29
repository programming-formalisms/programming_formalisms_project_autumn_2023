# is_odd

def is_odd(x):
	"""
	Determines wheteher a number is odd.
	:param x: int, input number
	:return: bool
	"""
	if isinstance(x, int):
		return x % 2 == 1
	else:
		raise TypeError("Give an integer as input")
	
assert not is_odd('a')
assert is_odd(5)

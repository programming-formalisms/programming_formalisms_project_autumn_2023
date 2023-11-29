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
		return False
	
assert not is_odd(4)
print(is_odd(1.1))

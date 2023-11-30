# is_even

def fis_even(x):
	"""
	Determines whether an integer is even.
	:param x: int
	:return: bool
	"""
	if isinstance(x, int):
		return not x % 2
	else:
		print("Give an integer as input")
		return False
		
	
assert is_even(12)
assert not is_even(12.0)
assert not is_even(12.4)
assert is_even(-12)
assert not is_even("twelve")
assert is_even([2, 4, 6, 8])

# is_odd

def is_odd(number):
	"""
	test whether a number is odd or not
	"""
	
	if isinstance(number, int):
		return number % 2 != 0
	else:
		print("you goof'd it")

assert is_odd(1) == True
assert is_odd(2) == False
assert is_odd("stringput") 



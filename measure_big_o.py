# Functions from Pythonpool article
# https://www.pythonpool.com/check-if-number-is-prime-in-python/
#
# Functions are adapted as little as possible :-)
#
def isprime_1(num):
  for n in range(
    2, int(num**0.5)+1
  ):
    if num%n==0:
      return False
  return True

def isprime_2(num):
    if num> 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False

def is_prime_3(no, i = 2):
    if no == i:
        return True
    elif no % i == 0:
        return False
    return is_prime_3(no, i + 1)

#################################################
# People's code
#
# Order alphabetically by author
#################################################

#################################################
# Richel's code
#################################################
def measure_big_o_richel():
    times_1 = [] # For is_prime_1
    times_2 = [] # For is_prime_2
    times_3 = [] # For is_prime_3
    # Make i go from 1 to 1000 (if that is
        # Measure the time for each of the prime functions
        # Store the time it took
    # Show all the times, ideally in a plot    



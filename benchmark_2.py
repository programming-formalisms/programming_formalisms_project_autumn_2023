"""Benchmarks code."""

if __debug__:
    msg = "Do not benchmark in debug mode. Tip: run 'python -O benchmark_2.py''"
    e = RuntimeError(msg)
    raise e


def is_sorted(data): 
    """Determines if data is sorted."""
    return data == sorted(data)

def richel_sort(data):
    """Sorts data by Richelsort."""
    while not is_sorted(data):
        from random import shuffle
        shuffle(data)
    return data

def create(): 
   """Create the data to be sorted."""
   return list(range(0, 10))

def reverse(x): 
    """Reverse the list."""
    x.reverse() 
    return x

def sort(x): 
    """Sort the list."""
    return richel_sort(x)

def do_complex_calculation(): 
    """Does a complex calculation.

    Vague wording is intentional.
    """
    return sort(reverse(create()))

import cProfile
cProfile.run("do_complex_calculation()")

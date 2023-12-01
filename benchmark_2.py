"""Benchmarks code."""

def is_sorted(data): return data == sorted(data)

def richel_sort(data):
    while not is_sorted(data):
        from random import shuffle
        shuffle(data)
    return data

def create(): return list(range(0, 10))
def reverse(x): 
    x.reverse() 
    return x
def sort(x): return richel_sort(x)

def my_function(): return sort(reverse(create()))

import cProfile
cProfile.run("my_function()")

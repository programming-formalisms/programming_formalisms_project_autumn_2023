"""Benchmarks code."""

import cProfile
import sys

from pfpa2023.testing import (
  is_prime_harald,
  is_prime_jesper,
  is_prime_pontus,
  is_prime_richel,
  is_prime_thanadol,
)

def run_benchmark():
    """Put here the code you want to benchmark"""
    for i in range(0, 10000):
        is_prime_harald(i)
        is_prime_jesper(i)
        is_prime_pontus(i)
        is_prime_richel(i)
        is_prime_thanadol(i)


def do_benchmark():
    """Benchmark this project."""
    cProfile.run(
        "run_benchmark()"
    )

if __debug__:
    msg = "Do not benchmark in debug mode. Tip: run 'python -O benchmark.py''"
    e = RuntimeError(msg)
    raise e
do_benchmark()

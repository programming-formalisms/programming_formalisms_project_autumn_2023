"""The Programming Formalisms Learner Project.

Project used in the UPPMAX Programming Formalisms course
in autumn 2023.

Usage, from the root folder:

python3 main.py
"""

# Do not start with 'src.', 
# install the package instead:
#
# python3 -m pip install .
#
# (in the root folder)
from pfpa2023.testing import (
    is_prime_richel,
)

if __name__ == "__main__":
    print("13 is prime: ", is_prime_richel(13)) # noqa: T201 print is used as a stub

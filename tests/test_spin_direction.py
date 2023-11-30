"""Tests all function in src.pf_example.duck."""
import unittest

from pfpa2023.spin_direction import (
    SpinDirection,
)


class TestDuck(unittest.TestCase):

    """Class to test the code in src.pf_example.duck."""

    def test_can_create_params(self):
        """#20: Can create a spin direction."""
        SpinDirection()

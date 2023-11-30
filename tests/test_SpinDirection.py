"""Tests all function in src.pf_example.duck."""
import unittest

from src.pfpa2023.SpinDirection import (
    SpinDirection,
)


class TestDuck(unittest.TestCase):

    """Class to test the code in src.pf_example.duck."""

    def test_can_create_params(self):
        """#20: Can create a spin direction."""
        SpinDirection()

"""Tests all function in src.pf_example.duck."""
import unittest

from src.pfpa2023.duck import (
    Duck,
)


class TestDuck(unittest.TestCase):

    """Class to test the code in src.pfpa2023.duck."""

    def test_can_create_duck(self):
        """#14: Can construct a Duck."""
        Duck()

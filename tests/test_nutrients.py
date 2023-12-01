"""Tests all function in src/pfpa2023/nutrients.py."""
import unittest

from src.pfpa2023.nutrients import (
    Nutrients,
)


class TestNutrients(unittest.TestCase):

    """Class to test the code in src.pfpa2023.nutrients."""

    def test_can_create_params(self):
        """#22: Can create Nutrients."""
        Nutrients()

"""Tests all function in src.pf_example.duck."""
import unittest

from src.pf_example.bacterium import (
    Bacterium,
)


class TestBacterium(unittest.TestCase):

    """Class to test the code in src.pf_example.duck."""

    def test_can_create_params(self):
        """#23: Can create a Bacterium."""
        Bacterium()

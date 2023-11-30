"""Tests all function in src.pf_example.coordinate."""
import unittest

from src.pf_example.coordinate import (
    Coordinate,
)


class TestCoordinate(unittest.TestCase):

    """Class to test the code in src.pf_example.coordinate."""

    def test_can_create_params(self):
        """#32: Can create a Coordinate."""
        Coordinate()

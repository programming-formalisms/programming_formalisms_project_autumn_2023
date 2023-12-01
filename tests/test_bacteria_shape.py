"""Tests all function in src.pfpa2023.bacteria_shape."""
import unittest

from src.pfpa2023.bacteria_shape import (
    BacteriaShape,
)


class TestBacteriaShape(unittest.TestCase):

    """Class to test the code in src.pfpa2023.simulation_parameters."""

    def test_can_create_params(self):
        """#15: Can construct a BacteriaShape."""
        BacteriaShape()

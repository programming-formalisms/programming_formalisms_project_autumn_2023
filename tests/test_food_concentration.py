"""Tests all function in src.pf_example.duck."""
import unittest

from src.pfpa2023.food_concentration import (
    FoodConcentration,
)


class TestFoodConcentration(unittest.TestCase):

    """Class to test the code in src.pf_example.duck."""

    def test_can_create_params(self):
        """#[issue_number]: Can create a Duck."""
        FoodConcentration()
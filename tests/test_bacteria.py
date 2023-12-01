"""Tests all function in src.pfpa2023.bacteria."""
import unittest

from src.pf_example.bacteria import (
    Bacteria,
)


class TestBacteria(unittest.TestCase):

    """Class to test the code in src.pfpa2023.bacteria."""

    def test_can_create_params(self):
        """#[39]: Can create a Bacteria."""
        Bacteria()

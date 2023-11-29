"""Test the functions in src.pfpa2023.testing."""
import unittest

from src.pfpa2023.testing import (
    is_prime_richel, is_prime_jesper
)


class TestTestingSolutions(unittest.TestCase):

    """Class to test all function."""

    def test_is_prime_richel(self):
        """Test 'is_prime_richel'."""
        self.assertIsNotNone(is_prime_richel.__doc__)
        self.assertRaises(TypeError, is_prime_richel, "evil string")
        self.assertRaises(TypeError, is_prime_richel, 0.7)
        self.assertFalse(is_prime_richel(-1))
        self.assertFalse(is_prime_richel(0))
        self.assertFalse(is_prime_richel(1))
        self.assertTrue(is_prime_richel(2))
        self.assertTrue(is_prime_richel(3))
        self.assertFalse(is_prime_richel(4))
        self.assertTrue(is_prime_richel(5))
        self.assertFalse(is_prime_richel(6))

    def test_is_prime_jesper(self):
        """Test 'is_prime_jesper'."""
        self.assertIsNotNone(is_prime_jesper.__doc__)
        self.assertRaises(TypeError, is_prime_jesper, "string")
        self.assertTrue(is_prime_jesper(2))
        self.assertFalse(is_prime_jesper(1))
        self.assertTrue(is_prime_jesper(11))
        self.assertFalse(is_prime_jesper(12))



"""Test the functions in src.pfpa2023.testing."""
import unittest

from learners.josefine.testing import (
    is_prime_richel, is_prime_pontus, is_prime_markella
)


class TestTestingSolutions(unittest.TestCase):

    """Class to test all function."""

    def test_is_prime_pontus(self):
        """Test 'is_prime_pontus'."""
        self.assertIsNotNone(is_prime_pontus.__doc__)

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

    def test_is_prime_markella(self):
        """Test 'is_prime_markella'."""
        self.assertIsNotNone(is_prime_markella.__doc__)
        self.assertTrue(is_prime_markella(7))
    


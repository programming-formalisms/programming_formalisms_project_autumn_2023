"""Test the functions in src.pfpa2023.testing."""
import unittest

from src.pfpa2023.testing import (
    is_prime_harald, is_prime_jesper, is_prime_richel, is_prime_pontus, is_prime_thanadol
)


class TestTestingSolutions(unittest.TestCase):

    """Class to test all function."""

    def test_is_prime_harald(self):
        """Test 'is_prime_harald'."""
        self.assertIsNotNone(is_prime_harald.__doc__)
        self.assertFalse(is_prime_harald(1))
        self.assertFalse(is_prime_harald(4))
        self.assertTrue(is_prime_harald(2))
        self.assertRaises(TypeError, is_prime_harald, "evil string")
        self.assertTrue(is_prime_harald(5))
        self.assertFalse(is_prime_harald(-1))
        # test below is first prime larger than signed int maximum
        # test is true, but takes 130 seconds on my machine
        # self.assertTrue(is_prime_harald(2147483659))

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

    def test_is_prime_jesper(self):
        """Test 'is_prime_jesper'."""
        self.assertIsNotNone(is_prime_jesper.__doc__)
        self.assertRaises(TypeError, is_prime_jesper, "string")
        self.assertTrue(is_prime_jesper(2))
        self.assertFalse(is_prime_jesper(1))
        self.assertTrue(is_prime_jesper(11))
        self.assertFalse(is_prime_jesper(12))

    def test_is_prime_thanadol(self):
        """Test 'is_prime_thanadol'."""
        self.assertIsNotNone(is_prime_thanadol.__doc__)
        self.assertRaises(TypeError, is_prime_thanadol, "string")
        self.assertRaises(TypeError, is_prime_thanadol, 1.1)
        self.assertFalse(is_prime_thanadol(0))
        self.assertTrue(is_prime_thanadol(2))

"""Tests all function in src.pf_example.ThresholdConc."""
import unittest

from src.pf_example.ThresholdConc import (
    ThresholdConc,
)


class TestThresholdConc(unittest.TestCase):

    """Class to test the code in src.pf_example.ThresholdConc."""

    def test_can_create_params(self):
        """#14: Can construct a ThresholdConc."""
        ThresholdConc()

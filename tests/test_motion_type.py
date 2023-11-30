"""Tests all function in src/pfpa2023/motion_type.py."""
import unittest

from src.pfpa2023.motion_type import (
    MotionType
)


class TestMotionType(unittest.TestCase):

    """Class to test the code in src.pfpa2023.motion_type."""

    def test_can_create_params(self):
        """#[issue_number]: Can create MotionType."""
        MotionType()
"""Tests all function in src.pf2023_example.envir."""
import unittest

from src.pf_example.enviro import(
    Environment,
)


class TestEnvironment(unittest.TestCase):

  """Class to test the code in src.pf2023_example.enviro."""

  def test_can_create_params(self):

    """#14: Can construct a Environment."""

    Environment()
   


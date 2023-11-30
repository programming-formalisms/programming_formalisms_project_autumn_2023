"""Tests all function in src.pf_example.Environment.""" 
import unittest

from src.pf_example.Environment import 
( Environment,
) 

class TestEnvironment(unittest.TestCase): 
  """Class to test the code in src.pf_example.Environment."""
  def test_can_create_params(self): 
    """#14: Can construct a Environment.""" 
    Environment()

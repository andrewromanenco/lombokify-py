from mock import Mock
import unittest

from lombokify.parameters_collector import ParametersCollector
from lombokify.utils import tree_root_from_file

class TestParametersCollector(unittest.TestCase):

  def test_parameters_collection(self):
    root = tree_root_from_file('tests/res/Example1.java')
    testee = ParametersCollector()
    testee.process(root)
    self.assertEqual(testee.params,
      [['primitive', 'int', 'x'],
      ['primitive', 'double', 'y'],
      ['reference', 'NotNull.SomeClass', 'obj']])

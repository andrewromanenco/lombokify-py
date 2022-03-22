from mock import Mock
import unittest

from lombokify.antlr_generated.Java8Parser import Java8Parser

from lombokify.class_declaration_collector import ClassDeclarationCollector
from lombokify.utils import tree_root_from_file

class TestClassDeclarationCollector(unittest.TestCase):

  def test_listener_trigerred_for_class_def(self):
    root = tree_root_from_file('tests/res/Example1.java')
    testee = ClassDeclarationCollector()
    testee.process(root)
    self.assertEqual(len(testee.nodes), 1)
    self.assertIsInstance(testee.nodes[0], Java8Parser.NormalClassDeclarationContext)

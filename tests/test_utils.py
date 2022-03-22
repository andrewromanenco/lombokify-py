import unittest
from lombokify.antlr_generated.Java8Parser import Java8Parser
from lombokify.utils import tree_root_from_file
from lombokify.utils import walk_tree

from lombokify.antlr_generated.Java8Parser import Java8Parser
from lombokify.antlr_generated.Java8ParserListener import Java8ParserListener

class TestUtils(unittest.TestCase):
  def test_read_tree_from_file(self):
    root = tree_root_from_file('tests/res/Example1.java')
    self.assertIsInstance(root, Java8Parser.CompilationUnitContext)

  def test_walk_tree(self):
    root = tree_root_from_file('tests/res/Example1.java')
    class Listener(Java8ParserListener):
      def __init__(self):
        self.class_found = False

      def enterNormalClassDeclaration(self, ctx:Java8Parser.NormalClassDeclarationContext):
        self.class_found = True
    listener = Listener()
    walk_tree(root, listener)
    self.assertTrue(listener.class_found)

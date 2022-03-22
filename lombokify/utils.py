from antlr4 import CommonTokenStream
from antlr4 import FileStream
from antlr4 import ParseTreeWalker
from lombokify.antlr_generated.Java8Lexer import Java8Lexer
from lombokify.antlr_generated.Java8Parser import Java8Parser
from lombokify.antlr_generated.Java8ParserListener import Java8ParserListener

# Read file from a path to a comilation unit from grammar
def tree_root_from_file(path_to_file):
  lexer = Java8Lexer(FileStream(path_to_file))
  stream = CommonTokenStream(lexer)
  parser = Java8Parser(stream)
  return parser.compilationUnit()

# Tree walker util
def walk_tree(tree, listener):
  walker = ParseTreeWalker()
  walker.walk(listener, tree)

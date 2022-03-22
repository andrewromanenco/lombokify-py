from antlr4 import ParseTreeWalker
from lombokify.antlr_generated.Java8Parser import Java8Parser
from lombokify.antlr_generated.Java8ParserListener import Java8ParserListener

# Collect all Class nodes
class ClassDeclarationCollector(Java8ParserListener):
  def __init__(self):
    self.nodes = []
  def process(self, tree_node):
    ParseTreeWalker().walk(self, tree_node)
  def enterNormalClassDeclaration(self, ctx:Java8Parser.NormalClassDeclarationContext):
    self.nodes.append(ctx)

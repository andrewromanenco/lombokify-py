from antlr4 import ParseTreeWalker
from lombokify.antlr_generated.Java8Parser import Java8Parser
from lombokify.antlr_generated.Java8ParserListener import Java8ParserListener

# Collect all parameters in a given tree
class ParametersCollector(Java8ParserListener):
  def __init__(self):
    self.params = []
    self.next_param = None
  def process(self, tree_node):
    ParseTreeWalker().walk(self, tree_node)
  def enterFormalParameterList(self, ctx:Java8Parser.FormalParameterListContext):
    self.next_param = [None, None, None]
  def enterReceiverParameter(self, ctx:Java8Parser.ReceiverParameterContext):
      pass
  def enterUnannPrimitiveType(self, ctx:Java8Parser.UnannPrimitiveTypeContext):
    if self.next_param:
      self.next_param[0] = 'primitive'
      self.next_param[1] = ctx.getText()
  def enterUnannReferenceType(self, ctx:Java8Parser.UnannReferenceTypeContext):
    if self.next_param:
      self.next_param[0] = 'reference'
      self.next_param[1] = ctx.getText()
  def enterVariableDeclaratorId(self, ctx:Java8Parser.VariableDeclaratorIdContext):
    if self.next_param:
      self.next_param[2] = ctx.getText()
    assert self.next_param[0]
    assert self.next_param[1]
    assert self.next_param[2]
    self.params.append(self.next_param)
    self.next_param = [None, None, None]

import sys
from lombokify.utils import walk_tree
from lombokify.utils import tree_root_from_file

if __name__ == '__main__':
  tree = tree_root_from_file(sys.argv[1])
  print(type(tree))
  # walk_tree(tree, LombokifyListener())

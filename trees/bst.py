from binary_tree import *

class BST(BinaryTree):
  def insert(self, value):
    self.__insert(self.root, value)

  def search(self, value):
    return self.__search(self.root, value)

  def __insert(self, start_node, value):
    if start_node.value < value:
      if start_node.right:
        self.__insert(start_node.right, value)
      else:
        start_node.right = Node(value)
    else:
      if start_node.left:
        self.__insert(start_node.left, value)
      else:
        start_node.left = Node(value)

  def __search(self, start_node, value):
    if start_node:
      if start_node.value == value:
        return True
      elif value > start_node.value:
        return self.__search(start_node.right, value)
      else:
        return self.__search(start_node.left, value)
    return False
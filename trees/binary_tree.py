class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self, root_value):
    self.root = Node(root_value)

  def search(self, value):
    return self.__search(self.root, value)

  def preorder_print(self):
    return self.__preorder_print(self.root, [])

  def inorder_print(self):
    return self.__inorder_print(self.root, [])

  def postorder_print(self):
    return self.__postorder_print(self.root, [])

  def __search(self, start_node, value):
    if start_node:
      return(
        start_node.value == value or
        self.__search(start_node.left, value) or
        self.__search(start_node.right, value)
      )
    return False

  def __preorder_print(self, start_node, traversal):
    if start_node:
      traversal.append(start_node.value)
      self.__preorder_print(start_node.left, traversal)
      self.__preorder_print(start_node.right, traversal)
    return traversal

  def __inorder_print(self, start_node, traversal):
    if start_node:
      self.__inorder_print(start_node.left, traversal)
      traversal.append(start_node.value)
      self.__inorder_print(start_node.right, traversal)
    return traversal

  def __postorder_print(self, start_node, traversal):
    if start_node:
      self.__postorder_print(start_node.left, traversal)
      self.__postorder_print(start_node.right, traversal)
      traversal.append(start_node.value)
    return traversal
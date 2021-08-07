class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self, root_value):
    self.root = Node(root_value)

  def search(self, start_node, value):
    if start_node:
      return start_node.value == value or self.search(start_node.left, value) or self.search(start_node.right, value)

  def preorder_print(self, start_node, traversal = []):
    if start_node:
      traversal.append(start_node.value)
      self.preorder_print(start_node.left, traversal)
      self.preorder_print(start_node.right, traversal)
    return traversal

  def inorder_print(self, start_node, traversal = []):
    if start_node:
      self.inorder_print(start_node.left)
      traversal.append(start_node.value)
      self.inorder_print(start_node.right)
    return traversal

  def postorder_print(self, start_node, traversal = []):
    if start_node:
      self.postorder_print(start_node.left)
      self.postorder_print(start_node.right)
      traversal.append(start_node.value)
    return traversal
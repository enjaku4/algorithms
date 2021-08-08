import re
import operator

class MathParser:
  def __init__(self, string):
    self.string = string

  def calculate(self):
    tree = self.__build_tree(Tree(), 0)
    return tree.calculate()

  def __build_tree(self, tree, index):
    if index >= len(self.__operations_array()):
      return tree

    value = self.__operations_array()[index]

    if value == '(':
      sub_tree, index = self.__build_tree(Tree(), index + 1)
      tree.append(sub_tree.root)
    elif value == ')':
      return (tree, index)
    elif value in Tree.OPERATIONS.keys():
      if tree.root.value in ['+', '-'] and value in ['*', '/']:
        tree.swap_right(Node(value))
      else:
        tree.swap_root(Node(value))
    else:
      tree.append(Node(float(value)))

    return self.__build_tree(tree, index + 1)

  def __operations_array(self):
    return re.findall(r'\d+\.?\d*|\+|-|\*|/|\(|\)', re.sub(r'^-|(?<=\()-', '0-', self.string))

class Tree:
  OPERATIONS = { '+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div }

  def __init__(self):
    self.root = Node('+')
    self.root.left = Node(0)

  def calculate(self):
    return self.__evaluate(self.root)

  def swap_root(self, node):
    node.left, self.root = self.root, node

  def swap_right(self, node):
    node.left, self.root.right = self.root.right, node

  def append(self, node):
    current_node = self.root

    while current_node.right:
      current_node = current_node.right

    current_node.right = node

  def __evaluate(self, current_node):
    if current_node.is_leaf():
      return current_node.value

    return self.OPERATIONS[current_node.value](
      self.__evaluate(current_node.left),
      self.__evaluate(current_node.right)
    )

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def is_leaf(self):
    return self.left is None and self.right is None
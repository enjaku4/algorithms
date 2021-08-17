import re
import operator

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def is_leaf(self):
    return self.left is None and self.right is None

class Tree:
  OPERATIONS = { '+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div }

  def __init__(self):
    self.root = Node('+')
    self.root.left = Node(0)

  def calculate(self):
    return self.__evaluate(self.root)

  def append_operation(self, node):
    if self.root.value in ['+', '-'] and node.value in ['*', '/']:
      node.left, self.root.right = self.root.right, node
    else:
      node.left, self.root = self.root, node

  def append_value(self, node):
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

class MathParser:
  def __init__(self, string):
    self.string = string

  def calculate(self):
    tree = self.__build_tree(Tree(), 0)
    return tree.calculate()

  def __build_tree(self, tree, index):
    if index == len(self.__operations_array()):
      return tree

    elem = self.__operations_array()[index]

    if elem == '(':
      sub_tree, index = self.__build_tree(Tree(), index + 1)
      tree.append_value(sub_tree.root)
    elif elem == ')':
      return (tree, index)
    elif elem in Tree.OPERATIONS.keys():
      tree.append_operation(Node(elem))
    else:
      tree.append_value(Node(float(elem)))

    return self.__build_tree(tree, index + 1)

  def __operations_array(self):
    return re.findall(r'\d+\.?\d*|\+|-|\*|/|\(|\)', re.sub(r'^-|(?<=\()-', '0-', self.string))

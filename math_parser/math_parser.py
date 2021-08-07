import re
import operator

class MathParser:
  def __init__(self, string):
    self.string = string

  def calculate(self):
    tree = self.__build_tree()
    return tree.calculate()

  def __build_tree(self):
    tree = MathTree(float(self.__operations_array()[1]))

    for operation, value in zip(self.__operations_array()[0::2], self.__operations_array()[1::2])[1:]:
      tree.add(operation, float(value))

    return tree

  def __operations_array(self):
    return re.findall(r'\d+\.?\d*|\+|-|\*|/|\(|\)', re.sub(r'\(-', '(0-', '(' + self.string + ')'))

class MathTree:
  OPERATIONS = { '+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div }

  def __init__(self, root_value):
    self.root = MathNode(root_value)

  def add(self, operation, value):
    node = MathNode(operation)
    node.right = MathNode(value)

    if self.root.value in ['+', '-'] and operation in ['*', '/']:
      self.__append_right(node)
    else:
      self.__swap_root(node)

  def calculate(self):
    return self.__evaluate(self.root)

  def __append_right(self, node):
    node.left, self.root.right = self.root.right, node

  def __swap_root(self, node):
    node.left, self.root = self.root, node

  def __evaluate(self, current_node):
    if current_node.is_leaf():
      return current_node.value

    return self.OPERATIONS[current_node.value](
      self.__evaluate(current_node.left),
      self.__evaluate(current_node.right)
    )

class MathNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def is_leaf(self):
    return self.left is None and self.right is None
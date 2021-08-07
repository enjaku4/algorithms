import unittest
from binary_tree import *

class Test(unittest.TestCase):
  def setUp(self):
    self.tree = BinaryTree(1)
    self.tree.root.left = Node(2)
    self.tree.root.right = Node(3)
    self.tree.root.left.left = Node(4)
    self.tree.root.left.right = Node(5)

  def test_search(self):
    for i in range(1,6):
      self.assertTrue(self.tree.search(i))
    self.assertFalse(self.tree.search(6))

  def test_preorder_print(self):
    self.assertEqual(self.tree.preorder_print(), [1,2,4,5,3])

  def test_inorder_print(self):
    self.assertEqual(self.tree.inorder_print(), [4,2,5,1,3])

  def test_postorder_print(self):
    self.assertEqual(self.tree.postorder_print(), [4,5,2,3,1])

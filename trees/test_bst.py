import unittest
from bst import BST

class Test(unittest.TestCase):
  def setUp(self):
    self.tree = BST(4)
    self.tree.insert(2)
    self.tree.insert(1)
    self.tree.insert(3)
    self.tree.insert(5)

  def test_search(self):
    for i in range(1,6):
      self.assertTrue(self.tree.search(i))
    self.assertFalse(self.tree.search(6))

  def test_order(self):
    self.assertEqual(self.tree.inorder_print(), [1,2,3,4,5])

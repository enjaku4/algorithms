import unittest
from stack import Stack

class TestStack(unittest.TestCase):
  def setUp(self):
    self.stack = Stack()

  def test_pop_empty_stack_returns_none(self):
    self.assertIsNone(self.stack.pop())

  def test_pop_after_push_returns_pushed_value(self):
    self.stack.push(42)
    self.assertEqual(self.stack.pop(), 42)

  def test_pop_after_multiple_pushes_returns_last_pushed_value(self):
    self.stack.push(42)
    self.stack.push(0)
    self.assertEqual(self.stack.pop(), 0)

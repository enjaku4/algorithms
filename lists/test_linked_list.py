import unittest
from linked_list import *

class TestLinkedList(unittest.TestCase):
  def setUp(self):
    self.list = LinkedList()

  def test_head_of_empty_list_is_none(self):
    self.assertIsNone(self.list.head())

  def test_tail_of_empty_list_is_none(self):
    self.assertIsNone(self.list.tail())

  def test_appending_changes_tail(self):
    self.list.append(5)
    self.assertEqual(self.list.tail().value, 5)
    self.list.append(59)
    self.assertEqual(self.list.tail().value, 59)

  def test_prepending_changes_head(self):
    self.list.prepend(5)
    self.assertEqual(self.list.head().value, 5)
    self.list.prepend(59)
    self.assertEqual(self.list.head().value, 59)

  def test_searching_for_nonexistent_node_finds_nothing(self):
    self.assertIsNone(self.list.find(5))

    self.list.append(13)
    self.assertIsNone(self.list.find(7))

  def test_searching_for_existing_node_finds_it(self):
    self.list.append(5)
    self.assertIsInstance(self.list.find(5), Node)
    self.assertEqual(self.list.find(5).value, 5)

  def test_inserting_node_after_nonexistent_node_does_nothing(self):
    self.list.insert(3, after = 4)
    self.assertIsNone(self.list.find(3))

    self.list.append(68)
    self.list.insert(56, after = 12)
    self.assertIsNone(self.list.find(56))

  def test_inserting_node_after_existing_node_inserts_it(self):
    self.list.append(68)
    self.list.insert(3, after = 68)
    self.assertIsNotNone(self.list.find(3))

    self.list.append(22)
    self.list.insert(33, after = 3)
    self.assertIsNotNone(self.list.find(33))

  def test_deleting_nonexistent_node_does_nothing(self):
    self.list.delete(3)
    self.assertIsNone(self.list.head())

    self.list.append(68)
    self.list.delete(3)
    self.assertIsNotNone(self.list.head())

  def test_deleting_existing_node_deletes_it(self):
    self.list.append(68)
    self.list.delete(68)
    self.assertIsNone(self.list.head())
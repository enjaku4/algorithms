import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):
  def setUp(self):
    self.table = HashTable()

  def test_empty_table_lookup_finds_nothing(self):
    self.assertFalse(self.table.lookup('foo'))

  def test_non_existent_value_lookup_finds_nothing(self):
    self.table.store('Foo')
    self.assertFalse(self.table.lookup('foo'))

  def test_existing_value_lookup_finds_it(self):
    self.table.store('Foo')
    self.assertTrue(self.table.lookup('Foo'))
    self.table.store('FooBar')
    self.assertTrue(self.table.lookup('FooBar'))
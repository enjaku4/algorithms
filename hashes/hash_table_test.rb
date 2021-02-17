require 'minitest/autorun'
require 'byebug'

require_relative 'hash_table'

class HashTableTest < Minitest::Test
  def setup
    @hash_table = HashTable.new
  end

  def test_calculates_hash_value
    assert_equal(181, @hash_table.hash_value('Foo'))
  end

  def test_empty_table_lookup_finds_nothing
    refute(@hash_table.lookup('foo'))
  end

  def test_not_empty_table_finds_nothing
    @hash_table.store('Foo')
    refute(@hash_table.lookup('foo'))
  end

  def test_finds_stored_value
    @hash_table.store('Foo')
    assert(@hash_table.lookup('Foo'))
  end

  def test_finds_stored_value_in_case_of_collision
    @hash_table.store('Foo')
    @hash_table.store('FooBar')
    assert(@hash_table.lookup('FooBar'))
  end
end
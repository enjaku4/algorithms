require 'minitest/autorun'
require 'byebug'

require_relative 'linked_list'

class LinkedListTest < Minitest::Test
  def setup
    @list = LinkedList.new
  end

  def test_head_of_empty_list_is_nil
    assert_nil(@list.head)
  end

  def test_tail_of_empty_list_is_nil
    assert_nil(@list.tail)
  end

  def test_appending_x_changes_tail_to_x
    @list.append(42)
    assert_equal(@list.tail.value, 42)

    @list.append(398)
    assert_equal(@list.tail.value, 398)
  end

  def test_appending_does_not_change_existing_head
    @list.append(42)
    @list.append(8)
    assert_equal(@list.head.value, 42)
  end

  def test_prepending_x_changes_head_to_x
    @list.prepend(42)
    assert_equal(@list.head.value, 42)

    @list.prepend(398)
    assert_equal(@list.head.value, 398)
  end

  def test_prepending_does_not_change_existing_tail
    @list.prepend(42)
    @list.prepend(8)
    assert_equal(@list.tail.value, 42)
  end

  def test_searching_for_nonexistent_previous_node_returns_nil
    assert_nil(@list.find_before(5))

    @list.append(5)
    assert_nil(@list.find_before(5))

    @list.append(59)
    assert_nil(@list.find_before(5))
  end

  def test_finds_previous_node
    @list.append(5)
    @list.append(59)
    assert_kind_of(LinkedList::Node, @list.find_before(59))
    assert_equal(@list.find_before(59).value, 5)
  end

  def test_searching_for_nonexistent_node_returns_nil
    assert_nil(@list.find(5))

    @list.append(13)
    assert_nil(@list.find(5))
  end

  def test_finds_node
    @list.append(5)
    @list.append(59)
    assert_kind_of(LinkedList::Node, @list.find(59))
    assert_equal(@list.find(59).value, 59)
  end

  def test_inserting_after_nonexistent_node_does_nothing
    @list.insert(3, after: 4)
    assert_nil(@list.find(3))

    @list.append(68)
    @list.insert(3, after: 4)
    assert_nil(@list.find(3))
  end

  def test_inserts_new_node_after_tail
    @list.append(68)
    @list.insert(3, after: 68)
    assert_equal(@list.find_before(3).value, 68)
  end

  def test_inserts_new_node_in_between
    @list.append(68)
    @list.append(139)
    @list.insert(33, after: 68)
    assert_equal(@list.find_before(33).value, 68)
    assert_equal(@list.find_before(139).value, 33)
  end

  def test_deleting_nonexistent_node_does_nothing
    @list.delete(3)
    assert_nil(@list.head)

    @list.append(68)
    @list.delete(3)
    assert_equal(@list.head.value, 68)
  end

  def test_deletes_the_only_node
    @list.append(68)
    @list.delete(68)
    assert_nil(@list.head)
  end

  def test_deletes_head
    @list.append(68)
    @list.append(5)
    @list.delete(68)
    assert_equal(@list.head.value, 5)
  end

  def test_deletes_node_in_between
    @list.append(9)
    @list.append(23)
    @list.append(5)
    @list.delete(23)
    assert_equal(@list.find_before(5).value, 9)
  end

  def test_deletes_tail
    @list.append(9)
    @list.delete(5)
    assert_equal(@list.tail.value, 9)
  end
end

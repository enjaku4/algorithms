require 'minitest/autorun'
require 'byebug'

require_relative 'stack'

class StackTest < Minitest::Test
  def setup
    @stack = Stack.new
  end

  def test_pop_empty_stack_returns_nil
    assert_nil(@stack.pop)
  end

  def test_pop_after_push_returns_pushed_value
    @stack.push(42)
    assert_equal(42, @stack.pop)
  end

  def test_pop_after_two_pushes_returns_last_pushed_value
    @stack.push(42)
    @stack.push(0)
    assert_equal(0, @stack.pop)
  end
end

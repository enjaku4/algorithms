require 'minitest/autorun'
require 'byebug'

require_relative 'bubble'

class BubbleTest < Minitest::Test
  def test_bubble_sorts
    arr = Array.new(10) { rand 100 }
    assert_equal(Bubble.sort(arr), arr.sort)
  end

  def test_does_nothing_with_empty_array
    arr = []
    assert_empty(Bubble.sort(arr))
  end
end

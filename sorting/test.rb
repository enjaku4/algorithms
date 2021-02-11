require 'minitest/autorun'
require 'byebug'

require_relative 'bubble'
require_relative 'merge'

class Test < Minitest::Test
  ALGORITHMS = [Bubble, Merge]

  def test_sorts
    ALGORITHMS.each do |algorithm|
      10.times do
        arr = Array.new(10) { rand(100) }
        assert_equal(arr.sort, algorithm.sort(arr))
      end
    end
  end

  def test_does_nothing_with_empty_array
    ALGORITHMS.each do |algorithm|
      assert_empty(algorithm.sort([]))
    end
  end
end

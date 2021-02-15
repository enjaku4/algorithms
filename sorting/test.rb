require 'minitest/autorun'
require 'byebug'

require_relative 'bubble'
require_relative 'merge'
require_relative 'quick'

class Test < Minitest::Test
  ALGORITHMS = [Bubble, Merge, Quick]

  def test_sorts_array
    10.times do
      arr = Array.new(100) { rand(100) }

      ALGORITHMS.each do |algorithm|
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

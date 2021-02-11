require 'minitest/autorun'
require 'byebug'

require_relative 'queue'

class QueueTest < Minitest::Test
  def setup
    @queue = Queue.new
  end

  def test_peek_empty_queue_returns_nil
    assert_nil(@queue.peek)
  end

  def test_peek_after_enqueue_returns_enqueued_value
    @queue.enqueue(42)
    assert_equal(42, @queue.peek)
  end

  def test_peek_after_two_enqueues_returns_first_enqueued_value
    @queue.enqueue(42)
    @queue.enqueue(0)
    assert_equal(42, @queue.peek)
  end

  def test_dequeue_empty_queue_returns_nil
    assert_nil(@queue.dequeue)
  end

  def test_dequeue_after_enqueue_returns_enqueued_value
    @queue.enqueue(42)
    assert_equal(42, @queue.dequeue)
  end

  def test_dequeue_after_two_enqueues_returns_first_enqueued_value
    @queue.enqueue(42)
    @queue.enqueue(0)
    assert_equal(42, @queue.dequeue)
  end
end

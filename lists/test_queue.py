import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
  def setUp(self):
    self.queue = Queue()

  def test_peek_empty_queue_returns_none(self):
    self.assertIsNone(self.queue.peek())

  def test_peek_after_enqueue_returns_enqueued_value(self):
    self.queue.enqueue(42)
    self.assertEqual(self.queue.peek(), 42)

  def test_peek_after_multiple_enqueues_returns_first_enqueued_value(self):
    self.queue.enqueue(42)
    self.queue.enqueue(0)
    self.assertEqual(self.queue.peek(), 42)

  def test_dequeue_empty_queue_returns_none(self):
    self.assertIsNone(self.queue.dequeue())

  def test_dequeue_after_enqueue_returns_enqueued_value(self):
    self.queue.enqueue(42)
    self.assertEqual(self.queue.dequeue(), 42)

  def test_dequeue_after_two_enqueues_returns_first_enqueued_value(self):
    self.queue.enqueue(42)
    self.queue.enqueue(0)
    self.assertEqual(self.queue.dequeue(), 42)

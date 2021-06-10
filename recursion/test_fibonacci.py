import unittest
from fibonacci import calc_fib

class TestFibonacci(unittest.TestCase):
  def test_when_position_negative(self):
    with self.assertRaises(ValueError):
      calc_fib(-1)
      calc_fib(-42)

  def test_when_position_lte_1(self):
    self.assertEqual(calc_fib(0), 0)
    self.assertEqual(calc_fib(1), 1)

  def test_when_position_gt_1(self):
    self.assertEqual(calc_fib(4), 3)
    self.assertEqual(calc_fib(5), 5)
    self.assertEqual(calc_fib(9), 34)
    self.assertEqual(calc_fib(14), 377)
    self.assertEqual(calc_fib(21), 10946)

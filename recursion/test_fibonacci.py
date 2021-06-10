import unittest
from fibonacci import calc_fib

class TestFibonacci(unittest.TestCase):
  def test_when_position_negative(self):
    with self.assertRaises(ValueError):
      calc_fib(-1)
      calc_fib(-42)

  def test_when_position_lte_1(self):
    self.assertEqual(0, calc_fib(0))
    self.assertEqual(1, calc_fib(1))

  def test_when_position_gt_1(self):
    self.assertEqual(3, calc_fib(4))
    self.assertEqual(5, calc_fib(5))
    self.assertEqual(34, calc_fib(9))
    self.assertEqual(377, calc_fib(14))
    self.assertEqual(10946, calc_fib(21))

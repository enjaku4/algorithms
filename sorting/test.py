import unittest
import random
import bubble
import merge
import quick

class Test(unittest.TestCase):
  def setUp(self):
    self.algorithms = [bubble, merge, quick]

  def test_sorting(self):
    for _ in range(10):
      arr = random.sample(range(100), 100)

      for algorithm in self.algorithms:
        self.assertEqual(algorithm.sort(arr), sorted(arr))

  def test_sorting_empty_array_does_nothing(self):
    for algorithm in self.algorithms:
      self.assertEqual(algorithm.sort([]), [])

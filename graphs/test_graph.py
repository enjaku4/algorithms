import unittest
from graph import *

class TestGraph(unittest.TestCase):
  def setUp(self):
    self.graph = Graph()
    self.graph.insert_node(0)
    self.graph.insert_edge(100, 1, 2)
    self.graph.insert_edge(101, 1, 3)
    self.graph.insert_edge(102, 1, 4)
    self.graph.insert_edge(103, 3, 4)

  def test_edge_list(self):
    self.assertEqual(self.graph.get_edge_list(), [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)])

  def test_adjacency_list(self):
    self.assertEqual(
      self.graph.get_adjacency_list(), [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
    )

  def test_adjacency_matrix(self):
    self.assertEqual(
      self.graph.get_adjacency_matrix(),
      [[0, 0,   0,   0,   0],
       [0, 0, 100, 101, 102],
       [0, 0,   0,   0,   0],
       [0, 0,   0,   0, 103],
       [0, 0,   0,   0,   0]]
    )

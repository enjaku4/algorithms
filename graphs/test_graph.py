import unittest
from graph import Graph

class TestGraphRepresentation(unittest.TestCase):
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

class TestGraphTraversal(unittest.TestCase):
  def setUp(self):
    self.graph = Graph()
    self.graph.insert_node(6)
    self.graph.insert_edge(51, 0, 1)
    self.graph.insert_edge(51, 1, 0)
    self.graph.insert_edge(9950, 0, 3)
    self.graph.insert_edge(9950, 3, 0)
    self.graph.insert_edge(10375, 0, 5)
    self.graph.insert_edge(10375, 5, 0)
    self.graph.insert_edge(9900, 1, 3)
    self.graph.insert_edge(9900, 3, 1)
    self.graph.insert_edge(9130, 1, 4)
    self.graph.insert_edge(9130, 4, 1)
    self.graph.insert_edge(9217, 2, 3)
    self.graph.insert_edge(9217, 3, 2)
    self.graph.insert_edge(932, 2, 4)
    self.graph.insert_edge(932, 4, 2)
    self.graph.insert_edge(9471, 2, 5)
    self.graph.insert_edge(9471, 5, 2)

  def test_dfs(self):
    self.assertEqual(self.graph.dfs(2), [2, 3, 0, 1, 4, 5])

  def test_bfs(self):
    self.assertEqual(self.graph.bfs(2), [2, 3, 4, 5, 0, 1])

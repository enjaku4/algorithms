class Node:
  def __init__(self, value):
    self.value = value
    self.edges = []

  def get_adjacencies(self):
    edges_from = filter(lambda edge: edge.node_from == self, self.edges)
    return None if not edges_from else map(lambda edge: (edge.node_to.value, edge.value), edges_from)

class Edge:
  def __init__(self, value, node_from, node_to):
    self.value = value
    self.node_from = node_from
    self.node_to = node_to

class Graph:
  def __init__(self):
    self.nodes = []
    self.edges = []

  def insert_node(self, node_val):
    self.nodes.append(Node(node_val))

  def insert_edge(self, edge_val, node_from_val, node_to_val):
    node_from = None
    node_to = None

    for node in self.nodes:
      if node_from_val == node.value:
        node_from = node
      if node_to_val == node.value:
        node_to = node

    if node_from == None:
      node_from = Node(node_from_val)
      self.nodes.append(node_from)

    if node_to == None:
      node_to = Node(node_to_val)
      self.nodes.append(node_to)

    edge = Edge(edge_val, node_from, node_to)

    node_from.edges.append(edge)
    node_to.edges.append(edge)

    self.edges.append(edge)

  def get_edge_list(self):
    return map(lambda edge: (edge.value, edge.node_from.value, edge.node_to.value), self.edges)

  def get_adjacency_list(self):
    return map(lambda node: (node.get_adjacencies()), self.nodes)

  def get_adjacency_matrix(self):
    result = []

    for node_from in self.nodes:
      row = []

      for node_to in self.nodes:
        value = 0

        for edge in self.edges:
          if edge.node_from == node_from and edge.node_to == node_to:
            value = edge.value

        row.append(value)

      result.append(row)

    return result

  def dfs(self, start_node_value):
    start_node = self.__find_node(start_node_value)
    return map(lambda node: node.value, self.__dfs(start_node, []))

  def bfs(self, start_node_value):
    start_node = self.__find_node(start_node_value)
    return map(lambda node: node.value, self.__bfs(start_node))

  def __dfs(self, node, visited):
    visited.append(node)

    for edge in filter(lambda edge: edge.node_from == node, node.edges):
      if edge.node_to not in visited:
        self.__dfs(edge.node_to, visited)

    return visited

  def __bfs(self, node):
    queue, visited = [node], []

    while(len(queue) > 0):
      visited.append(queue.pop(0))

      node = visited[-1]

      for edge in filter(lambda edge: edge.node_from == node, node.edges):
        if edge.node_to not in queue and edge.node_to not in visited:
          queue.append(edge.node_to)

    return visited

  def __find_node(self, value):
    for node in self.nodes:
      if node.value == value:
        return node

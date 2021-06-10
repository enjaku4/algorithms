class Node:
  def __init__(self, value, next_node):
    self.value = value
    self.next_node = next_node

class LinkedList:
  def __init__(self):
    self.__head = None

  def head(self):
    return self.__head

  def tail(self):
    node = self.__head

    while node:
      if node.next_node:
        node = node.next_node
      else:
        return node

  def append(self, value):
    if self.__head:
      self.tail().next_node = Node(value, None)
    else:
      self.prepend(value)

  def prepend(self, value):
    self.__head = Node(value, self.__head)

  def find(self, value):
    node = self.__head

    while node:
      if node.value == value:
        return node
      else:
        node = node.next_node

  def insert(self, value, after):
    node = self.find(after)

    if node:
      node.next_node = Node(value, node.next_node)

  def delete(self, value):
    if self.__head:
      if self.__head.value == value:
        self.__head = self.__head.next_node
      else:
        node = self.__head

        while node.next_node:
          previous = node
          node = node.next_node

          if node.value == value:
            previous.next_node = node.next_node
            return

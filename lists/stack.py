from linked_list import LinkedList

class Stack:
  def __init__(self):
    self.list = LinkedList()

  def push(self, value):
    self.list.prepend(value)

  def pop(self):
    if self.list.head():
      result = self.list.head().value
      self.list.delete(result)
      return result
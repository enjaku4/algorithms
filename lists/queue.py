from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.list = LinkedList()

  def peek(self):
    if self.list.head():
      return self.list.head().value

  def enqueue(self, value):
    self.list.append(value)

  def dequeue(self):
    if self.list.head():
      result = self.list.head().value
      self.list.delete(result)
      return result
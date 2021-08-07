from linked_list import LinkedList

class Stack(LinkedList):
  def push(self, value):
    self.prepend(value)

  def pop(self):
    if self.head():
      result = self.head().value
      self.delete(result)
      return result
from linked_list import LinkedList

class Queue(LinkedList):
  def peek(self):
    if self.head():
      return self.head().value

  def enqueue(self, value):
    self.append(value)

  def dequeue(self):
    if self.head():
      result = self.head().value
      self.delete(result)
      return result
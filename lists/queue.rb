require_relative 'linked_list'

class Queue
  def initialize
    @list = LinkedList.new
  end

  def peek
    @list.head&.value
  end

  def enqueue(value)
    @list.append(value)
  end

  def dequeue
    result = @list.head&.value
    @list.delete(result)
    result
  end
end
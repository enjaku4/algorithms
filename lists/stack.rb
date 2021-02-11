require_relative 'linked_list'

class Stack
  def initialize
    @list = LinkedList.new
  end

  def push(value)
    @list.prepend(value)
  end

  def pop
    result = @list.head&.value
    @list.delete(result)
    result
  end
end
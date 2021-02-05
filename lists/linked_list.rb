class LinkedList
  class Node
    attr_accessor :next, :value

    def initialize(value = nil, next_node: nil)
      @value = value
      @next = next_node
    end
  end

  attr_reader :head

  def initialize
    @head = nil
  end

  def find(value)
    return nil unless head
    return head if head.value == value
    find_before(value)&.next
  end

  def find_before(value)
    node = head

    while node&.next
      return node if node.next.value == value
      node = node.next
    end
  end

  def tail
    node = head

    while node
      return node unless node.next
      node = node.next
    end
  end

  def append(value)
    head ? tail.next = Node.new(value) : prepend(value)
  end

  def prepend(value)
    @head = Node.new(value, next_node: head)
  end

  def insert(value, after:)
    node = find(after)
    node.next = Node.new(value, next_node: node.next) if node
  end

  def delete(value)
    return nil unless head
    @head = head.next and return if head.value == value

    node = find_before(value)
    node.next = node.next.next if node
  end
end

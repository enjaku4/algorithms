module Fibonacci
  def self.calculate(index)
    return index if [0,1].include?(index)
    calculate(index - 1) + calculate(index - 2)
  end
end
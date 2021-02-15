module Quick
  extend self

  def sort(arr)
    return arr if arr.empty?

    pivot = arr[0]
    left = sort(arr[1..-1].select { |elem| elem < pivot })
    right = sort(arr[1..-1].select { |elem| elem >= pivot })
    left + [pivot] + right
  end
end
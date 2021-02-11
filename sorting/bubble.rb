module Bubble
  extend self

  def sort(arr)
    loop do
      swapped = false

      for index in 0..(arr.length - 2) do
        if arr[index] > arr[index + 1]
          arr[index], arr[index+1] = arr[index+1], arr[index]
          swapped = true
        end
      end

      return arr unless swapped
    end
  end
end
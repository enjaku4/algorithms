class Bubble
  def self.sort(arr)
    sorting = true

    while sorting
      sorting = false

      arr[0..-2].each_with_index do |val, index|
        if val > arr[index + 1]
          arr[index], arr[index + 1] = arr[index + 1], val
          sorting = true
        end
      end
    end

    arr
  end
end
module Merge
  extend self

  def sort(arr)
    return arr if arr.length <= 1

    middle = arr.length / 2
    left = arr.take(middle)
    right = arr.drop(middle)
    merge(sort(left), sort(right))
  end

  private

    def merge(arr1, arr2)
      merged = []

      while arr1.any? && arr2.any?
        if arr1.first < arr2.first
          merged.push(arr1.shift)
        else
          merged.push(arr2.shift)
        end
      end

      merged += arr1
      merged += arr2
    end
end
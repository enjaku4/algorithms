def sort(arr):
  if arr == []:
    return arr

  pivot = arr[0]

  left = sort([i for i in arr[1:] if i < pivot])
  right = sort([i for i in arr[1:] if i >= pivot])

  return left + [pivot] + right
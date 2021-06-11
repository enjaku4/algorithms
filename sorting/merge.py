def sort(arr):
  if len(arr) <= 1:
    return arr

  middle = len(arr) / 2

  left = arr[:middle]
  right = arr[middle:]

  return __merge(sort(left), sort(right))

def __merge(arr1, arr2):
  merged = []

  while arr1 and arr2:
    if arr1[0] < arr2[0]:
      merged.append(arr1.pop(0))
    else:
      merged.append(arr2.pop(0))

  merged += arr1
  merged += arr2

  return merged
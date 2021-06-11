class HashTable:
  def __init__(self):
    self.table = [None] * 10000

  def store(self, string):
    hash_value = HashableString(string).hash_value()

    if self.table[hash_value] is None:
      self.table[hash_value] = [string]
    else:
      self.table[hash_value].append(string)

  def lookup(self, string):
    bucket = self.table[HashableString(string).hash_value()]

    return bucket is not None and (string in bucket)

class HashableString(str):
  def hash_value(self):
    return ord(self[0]) + ord(self[1])
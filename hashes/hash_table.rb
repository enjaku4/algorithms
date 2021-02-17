class HashTable
  def initialize
    @table = []
  end

  def hash_value(str)
    str[0].ord + str[1].ord
  end

  def lookup(str)
    @table[hash_value(str)].to_a.include?(str)
  end

  def store(str)
    bucket = @table[hash_value(str)]
    @table[hash_value(str)] = bucket.to_a + [str]
  end
end
module MathParser
  extend self

  def calculate(str)
    @@operations_array = parse(str)
    collapse_parens!
  end

  private

    def parse(str)
      "(#{str})".gsub('(-', '(0-').scan(Regexp.new('\*|/|\+|-|\(|\)|\d+\.?\d*')).map do |char|
        char[Regexp.new('\d')] ? char.to_f : char.to_sym
      end
    end

    def collapse_parens!
      return @@operations_array[0] if @@operations_array.size == 1

      process_operations(:*, :/)
      process_operations(:+, :-)

      @@operations_array.delete_at(paren_r)
      @@operations_array.delete_at(paren_l)

      collapse_parens!
    end

    def process_operations(*operations)
      in_paren = @@operations_array[paren_l..paren_r]

      return if (in_paren & operations).empty?

      operation_index = in_paren.index { |elem| operations.include?(elem) } + paren_l
      operation = @@operations_array[operation_index]
      operation_result = @@operations_array[operation_index - 1].public_send(operation, @@operations_array[operation_index + 1])
      @@operations_array[(operation_index - 1)..(operation_index + 1)] = operation_result

      process_operations(*operations)
    end

    def paren_l
      @@operations_array.rindex(:'(')
    end

    def paren_r
      @@operations_array[paren_l..].index(:')') + paren_l
    end
end

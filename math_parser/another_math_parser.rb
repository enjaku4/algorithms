class AnotherMathParser
  def initialize(str)
    @operations_array = OperationsArray.parse(str)
  end

  def calculate
    collapse_operations_array_parens
    @operations_array[0]
  end

  private

    def collapse_operations_array_parens
      return if @operations_array.in_parens.empty?

      process_operations_in_parens(:*, :/)
      process_operations_in_parens(:+, :-)

      @operations_array.delete_parens

      collapse_operations_array_parens
    end

    def process_operations_in_parens(*operations)
      operation_index = @operations_array.index_in_parens(*operations)
      operation_index ? @operations_array.calculate_at(operation_index) : return

      process_operations_in_parens(*operations)
    end

    class OperationsArray < Array
      def self.parse(str)
        new("(#{str})".gsub('(-', '(0-').scan(Regexp.new('\d*\.?\d|\*|/|\+|-|\(|\)')).map do |char|
          char[Regexp.new('\d')] ? char.to_f : char.to_sym
        end)
      end

      def paren_left_index
        rindex(:'(')
      end

      def paren_right_index
        self[paren_left_index..].index(:')') + paren_left_index if paren_left_index
      end

      def in_parens
        paren_left_index && paren_right_index ? self[paren_left_index..paren_right_index] : []
      end

      def index_in_parens(*symbs)
        in_parens.index { |elem| symbs.include?(elem) } + paren_left_index if (in_parens & symbs).any?
      end

      def calculate_at(operation_index)
        operation_result = self[operation_index - 1].public_send(self[operation_index], self[operation_index + 1])
        self[(operation_index - 1)..(operation_index + 1)] = operation_result
      end

      def delete_parens
        delete_at(paren_right_index)
        delete_at(paren_left_index)
      end
    end
end

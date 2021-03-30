require 'rspec'
require 'byebug'
require_relative 'fibonacci'

describe Fibonacci do
  describe '.calculate' do
    it { expect(described_class.calculate(0)).to eq(0) }
    it { expect(described_class.calculate(1)).to eq(1) }
    it { expect(described_class.calculate(4)).to eq(3) }
    it { expect(described_class.calculate(5)).to eq(5) }
    it { expect(described_class.calculate(9)).to eq(34) }
    it { expect(described_class.calculate(14)).to eq(377) }
  end
end

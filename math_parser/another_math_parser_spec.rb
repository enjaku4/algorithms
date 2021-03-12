require 'rspec'
require 'byebug'
require_relative 'another_math_parser'

describe AnotherMathParser do
  describe '.calculate' do
    it { expect(described_class.new('1+11').calculate).to eq(12.0) }
    it { expect(described_class.new('-1+11').calculate).to eq(10.0) }
    it { expect(described_class.new('34-25').calculate).to eq(9.0) }
    it { expect(described_class.new('4*8').calculate).to eq(32.0) }
    it { expect(described_class.new('13/2').calculate).to eq(6.5) }
    it { expect(described_class.new('-2+31*1-4/2').calculate).to eq(27.0) }
    it { expect(described_class.new('4/2*7').calculate).to eq(14.0) }
    it { expect(described_class.new('-5*2/2').calculate).to eq(-5.0) }
    it { expect(described_class.new('4-1+13').calculate).to eq(16.0) }
    it { expect(described_class.new('-7/2-5*2+4').calculate).to eq(-9.5) }
    it { expect(described_class.new('13-4*2+(4-9/3)-1').calculate).to eq(5.0) }
    it { expect(described_class.new('1+(44-28)/(2+7*(5-3))-2').calculate).to eq(0.0) }
    it { expect(described_class.new('36-4+(-4.0/2+1)*(1+7*(-1-3))-23').calculate).to eq(36.0) }
  end
end

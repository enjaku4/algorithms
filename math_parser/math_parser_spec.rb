require 'rspec'
require 'byebug'
require_relative 'math_parser'

describe MathParser do
  describe '.parse' do
    it { expect(described_class.parse('1+11')).to eq(12.0) }
    it { expect(described_class.parse('-1+11')).to eq(10.0) }
    it { expect(described_class.parse('34-25')).to eq(9.0) }
    it { expect(described_class.parse('4*8')).to eq(32.0) }
    it { expect(described_class.parse('13/2')).to eq(6.5) }
    it { expect(described_class.parse('-2+31*1-4/2')).to eq(27.0) }
    it { expect(described_class.parse('4/2*7')).to eq(14.0) }
    it { expect(described_class.parse('-5*2/2')).to eq(-5.0) }
    it { expect(described_class.parse('4-1+13')).to eq(16.0) }
    it { expect(described_class.parse('-7/2-5*2+4')).to eq(-9.5) }
    it { expect(described_class.parse('13-4*2+(4-9/3)-1')).to eq(5.0) }
    it { expect(described_class.parse('1+(44-28)/(2+7*(5-3))-2')).to eq(0.0) }
    it { expect(described_class.parse('36-4+(-4.0/2+1)*(1+7*(-1-3))-23')).to eq(36.0) }
  end
end

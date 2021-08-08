import unittest
from math_parser import MathParser

class TestMathPasrser(unittest.TestCase):
  def test_math_parser(self):
    self.assertEqual(MathParser('1+11').calculate(), 12.0)
    self.assertEqual(MathParser('-1+11').calculate(), 10.0)
    self.assertEqual(MathParser('34-25').calculate(), 9.0)
    self.assertEqual(MathParser('4.25*8').calculate(), 34.0)
    self.assertEqual(MathParser('13/2').calculate(), 6.5)
    self.assertEqual(MathParser('-2+31*1-4/2').calculate(), 27.0)
    self.assertEqual(MathParser('4/2*7').calculate(), 14.0)
    self.assertEqual(MathParser('-5*2/2').calculate(), -5.0)
    self.assertEqual(MathParser('4-1.1+13').calculate(), 15.9)
    self.assertEqual(MathParser('-7/2-5*2+4').calculate(), -9.5)
    self.assertEqual(MathParser('20-4/2*5-3*3+3.3').calculate(), 4.3)
    self.assertEqual(MathParser('13-4*2+(4-9/3)-1').calculate(), 5.0)
    self.assertEqual(MathParser('1+(44-28)/((5-3)*7+2)-2').calculate(), 0.0)
    self.assertEqual(MathParser('36.01-4+(-4.0/2+1)*(1+7.455*(-1-3))-23').calculate(), 37.83)
    self.assertEqual(MathParser('(4+3)*4-2.5/5').calculate(), 27.5)

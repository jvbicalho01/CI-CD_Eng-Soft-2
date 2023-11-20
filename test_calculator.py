# from typing_extensions import Self
import pytest

from calculator import Calculator

class TestCalculator:
    
    def setup(self):
        self.calc = Calculator()
    
    def test_sum(self):
        assert(self.calc.sum(1, 2) == 3)

    def test_subtraction(self):
        assert(self.calc.subtract(5, 4) == 1)

    def test_subtraction_negative_result(self):
        assert(self.calc.subtract(6, 7) == -1)

    def test_multiplication(self):
        assert(self.calc.mult(3, 2) == 6)

    def test_division(self):
        assert(self.calc.div(10, 5) == 2)

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
          self.calc.div(10,0)
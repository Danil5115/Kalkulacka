import unittest
import math
from app import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
        self.assertEqual(self.calc.get_last_result(), 5)

    def test_sin(self):
        result = self.calc.sin(math.pi / 2)
        self.assertAlmostEqual(result, 1.0, places=7)
        self.assertAlmostEqual(self.calc.get_last_result(), 1.0, places=7)

    def test_get_last_result(self):
        self.calc.add(1, 1)
        self.assertEqual(self.calc.get_last_result(), 2)
        self.calc.sin(0)
        self.assertEqual(self.calc.get_last_result(), 0.0)

if __name__ == '__main__':
    unittest.main()

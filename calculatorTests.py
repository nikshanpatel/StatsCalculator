import unittest
from calculator import Calculator

class MyTestCase(unittest.TestCase):
    def test_instantiate_calc(self):
        calc = Calculator
        self.assertIsInstance(calc, Calculator)


if __name__ == '__main__':
    unittest.main()

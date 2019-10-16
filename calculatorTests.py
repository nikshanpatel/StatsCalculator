import unittest
from calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calc(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_result_property_calc(self):
        calc = Calculator()
        self.assertEqual(calc.result, 4)

    def test_result_property_calc(self):
        calc = Calculator()
        self.assertEqual(calc.result, 4)
        self.assertEqual(calc.add(2,2), 4)


if __name__ == '__main__':
    unittest.main()

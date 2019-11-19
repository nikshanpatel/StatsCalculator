import unittest
from CsvReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/UnitTestStats.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        test_data = CsvReader('Tests/Data/UnitTestStats.csv').data
        first_row = ([i for i in test_data if i['Mean'] != ''])[0]
        mean_value = float(first_row['Mean'])
        self.assertEqual(self.statistics.mean(), mean_value)

    def test_median_statistics(self):
        test_data = CsvReader('Tests/Data/UnitTestStats.csv').data
        first_row = ([i for i in test_data if i['Median'] != ''])[0]
        median_value = float(first_row['Median'])
        self.assertEqual(self.statistics.median(), median_value)

    def test_mode_statistics(self):
        test_data = CsvReader('Tests/Data/UnitTestStats.csv').data
        first_row = ([i for i in test_data if i['Mode'] != ''])[0]
        mode_value = float(first_row['Mode'])
        self.assertEqual(self.statistics.mode(), str(mode_value))


if __name__ == '__main__':
    unittest.main()
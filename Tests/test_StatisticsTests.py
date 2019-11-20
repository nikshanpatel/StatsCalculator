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

    def test_sample_mean_statistics(self):
        test_data = CsvReader('Tests/Data/UnitTestStats.csv').data
        first_row = ([i for i in test_data if i['Sample_Mean'] != ''])[0]
        sample_mean_value = float(first_row['Sample_Mean'])
        self.assertEqual(self.statistics.sample_mean(), sample_mean_value)

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

    def test_pv_statistics(self):
        test_data = CsvReader('Tests/Data/UnitTestStats.csv').data
        first_row = ([i for i in test_data if i['Pop_Var'] != ''])[0]
        pop_var = float(first_row['Pop_Var'])
        self.assertEqual(self.statistics.pv(), pop_var)

    def test_psd_statistics(self):
        test_data = CsvReader('Tests/Data/UnitTestStats.csv').data
        first_row = ([i for i in test_data if i['Pop_Std_Dev'] != ''])[0]
        pop_std_dev = float(first_row['Pop_Std_Dev'])
        self.assertEqual(self.statistics.psd(), pop_std_dev)

    def test_pcc_statistics(self):
        test_data = CsvReader('Tests/Data/UnitTestStats.csv').data
        first_row = ([i for i in test_data if i['Pop_Cor_Coef'] != ''])[0]
        pop_cor_coef = float(first_row['Pop_Cor_Coef'])
        self.assertEqual(self.statistics.pcc(), pop_cor_coef)

    def test_zscore_statistics(self):
        test_data = CsvReader('Tests/Data/UnitTestStats.csv').data
        first_row = ([i for i in test_data if i['Z_Score'] != ''])[0]
        z_score = float(first_row['Z_Score'])
        self.assertEqual(self.statistics.z(), z_score)


if __name__ == '__main__':
    unittest.main()
from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.SampleMean import get_sample_mean

from CsvReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = []
        test_data = CsvReader(filepath).data
        for row in test_data:
            self.data.append(float(row['Value1']))
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result

    def sample_mean(self):
        self.result = get_sample_mean(self.data, 10)
        return self.result

    def median(self):
        self.result = median(self.data)
        return self.result

    def mode(self):
        self.result = mode(self.data)
        return self.result

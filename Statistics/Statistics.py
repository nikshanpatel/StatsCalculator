from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.SampleMean import get_sample_mean
from Statistics.PopulationStandardDeviation import standard_deviation
from Statistics.PopulationCorrelationCoefficient import population_correlation_coefficient
from Statistics.PopulationVariance import population_variance
from Statistics.Standardized_or_Z_Score import z_score

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

    # Population Correlation Coefficient
    def pcc(self):
        self.result = population_correlation_coefficient(self.data, self.data)
        return self.result

    # Population Standard Deviation
    def psd(self):
        self.result = standard_deviation(self.data)
        return self.result

    # Population Variance
    def pv(self):
        self.result = population_variance(self.data)
        return self.result

    def z(self):
        self.result = z_score(self.data[0], self.data)
        return self.result

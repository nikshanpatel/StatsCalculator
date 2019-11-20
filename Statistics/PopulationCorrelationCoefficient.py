from Statistics.Mean import mean
from Statistics.PopulationStandardDeviation import standard_deviation
from Calculator.Division import division
from Calculator.Multiplication import multiplication
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition


def population_correlation_coefficient(list_x, list_y):
    total = 0
    σ_x = standard_deviation(list_x)
    σ_y = standard_deviation(list_y)
    for i in list_x:
        diff_x = subtraction(list_x[i], mean(list_x))
        diff_y = subtraction(list_y[i], mean(list_y))
        total = total + multiplication(division(diff_x, σ_x), division(diff_y, σ_y))
    return multiplication(division(1, addition(len(list_x), len(list_y))), total)

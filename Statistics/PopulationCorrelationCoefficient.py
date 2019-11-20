from Statistics.Mean import mean
from Statistics.PopulationStandardDeviation import standard_deviation
from Calculator.Division import division
from Calculator.Multiplication import multiplication
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition


def population_correlation_coefficient(list_x, list_y):
    total = 0
    x = standard_deviation(list_x)
    y = standard_deviation(list_y)
    for i in range(len(list_x)):
        diff_x = subtraction(list_x[i], mean(list_x))
        diff_y = subtraction(list_y[i], mean(list_y))
        total = total + multiplication(division(diff_x, x), division(diff_y, y))
    return round(float(multiplication(division(1, addition(len(list_x), len(list_y))), total)),4)

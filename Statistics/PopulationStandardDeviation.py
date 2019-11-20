from Statistics.PopulationVariance import population_variance


def standard_deviation(lst):
    result = (population_variance(lst)) ** 0.5
    return round(float(result),3)

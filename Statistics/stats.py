from collections import Counter

def sum(data):
    total = 0
    for i in data:
        total += i
    return total


def mean(data):
    total = sum(data)
    mean_value = 0
    mean_value = total / len(data)
    return mean_value


def median(data):
    n = len(data)
    data.sort()
    if n % 2 == 0:
        median1 = data[n // 2]
        median2 = data[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = data[n // 2]
    return median


def mode(data):
    n = len(data)
    data_val = Counter(data)
    get_mode = dict(data_val)
    mode = [k for k, v in get_mode.items() if v == max(list(data_val.values()))]
    if len(mode) == n:
        get_mode = "No mode found"
    else:
        get_mode = "Mode is / are: " + ', '.join(map(str, mode))
    return get_mode


def square(value):
    square_value = 0
    square_value = value * value
    return square_value


def sqrt(x):
    if (x == 0) or (x == 1):
        return x
    sqrt_val = 1
    result = 1
    while result <= x:
        sqrt_val += 1
        result = sqrt_val * sqrt_val
    return sqrt_val -1


def deviation(value_1, mean_value):
    dev_val = 0
    dev_val = (value_1 - mean_value)
    return dev_val


def deviation_sqr(data, mean_value):
    dev_sqr = 0
    for i in data:
        dev_sqr += square(deviation(i, mean_value))
    return dev_sqr


def variance(data, mean_value):
    var_val = 0
    dev_sqr = deviation_sqr(data, mean_value)
    var_val = dev_sqr / len(data)
    return var_val


def standard_deviation(data):
    mean_val = mean(data)
    sqr_val = square(mean_val)
    var_val = variance(data, mean_val)
    pop_stdv = sqrt(var_val)
    return pop_stdv


def population_proportion(feature_x, population):
    data_x_prop = feature_x / population
    return data_x_prop


if __name__ == '__main__':
    data = [42,86,51,77,20,96,71,40,57,42]
    data_sum = sum(data)
    data_mean = mean(data)
    data_median = median(data)
    data_mode = mode(data)
    data_square = deviation_sqr(data, data_mean)
    data_variance = variance(data, data_mean)
    data_sqrt = sqrt(data_variance)
    data_std_dev = standard_deviation(data)

    print("DATA = " + str(data))
    print("TOTAL = " + str(data_sum))
    print("MEAN = " + str(data_mean))
    print("MEDIAN = " + str(data_median))
    print("MODE = " + str(data_mode))
    print("DEVIATION SQUARE = " + str(data_square))
    print("VARIANCE = " + str(data_variance))
    print("SQUARE ROOT = " + str(data_sqrt))
    print("STD DEVIATION = " + str(data_std_dev))
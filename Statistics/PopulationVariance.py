from Statistics.Mean import mean


def population_variance(lst):
    # below is population variance formula
    ttl = 0
    for i in range(len(lst)):
        ttl += (lst[i] - mean(lst)) ** 2
    result = ttl / len(lst)
    return round(float(result),3)

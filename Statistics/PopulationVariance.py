from Statistics.Mean import mean


def population_variance(lst):
    # below is population variance formula
    ttl = 0
    for i in lst:
        ttl = (lst[i] - mean(lst)) ** 2
        return ttl
    result = ttl / len(lst)
    return result

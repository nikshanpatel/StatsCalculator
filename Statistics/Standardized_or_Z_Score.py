from Statistics.Mean import mean


def z_score(a, lst):
    z = (a - mean(lst)) / len(lst)
    return z

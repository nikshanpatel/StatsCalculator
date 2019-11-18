from collections import Counter


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

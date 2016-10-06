def percents(x, y):
    """What percentage of x is y"""
    One_percent = x / 100
    result = y / One_percent
    return result


def print_percents(x,y):
    """Print what percentage of x is y"""
    result = (str(y) + " is " + str(percents(x, y)) + " % of " + str(x))
    print(result)


percents(200, 50)
def percents(x, y):
    one_percent = x / 100
    result = y / one_percent
    print(str(y) + " is " + str(result) + "% of " + str(x))
    return percents


def print_percents(x, y):
    print(percents(x, y))


percents(200, 10)

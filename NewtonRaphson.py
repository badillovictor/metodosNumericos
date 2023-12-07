from tabulate import tabulate


def calculate_error(xi, prev):
    return abs(round((xi - prev) / xi, decimals))


def getrow(i, x, fx, fpx, prev):
    x = round(x - (fx / fpx), decimals)
    fx = round((x ** 3) - (10 * x) - 5, decimals)
    fpx = round((3 * (x ** 2) - 10), decimals)
    e = calculate_error(x, prev)
    return [i, x, fx, fpx, e]


if __name__ == '__main__':
    # f(x) = x^3-10x-5
    print('Metodo Newton-Raphson f(x) = x^3-10x-5')
    table = [['i', 'Xi', 'f(Xi)', 'f\'(Xi)', 'error']]
    decimals = 8
    error = 0.0000001
    i = 0
    x = 3.0
    fx = round((x ** 3) - (10 * x) - 5, decimals)
    fpx = round((3 * (x ** 2) - 10), decimals)
    e = calculate_error(x, 0)
    table.append([i, x, fx, fpx, e])
    prev = table[-1][1]
    while e > error:
        i += 1
        table.append(getrow(i, table[-1][1], table[-1][2], table[-1][3], prev))
        e = table[-1][-1]
        prev = table[-1][1]
    print(tabulate(table))
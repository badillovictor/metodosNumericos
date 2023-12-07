from tabulate import tabulate


def calculate_error(xi, prev):
    return abs(round((xi - prev) / xi, decimals))


def getrow(i, xi, xi1, fxi, fxi1, prev):
    xi = round(xi - ((fxi * (xi - xi1)) / (fxi - fxi1)), decimals)
    xi1 = xi - 1
    fxi = round((xi ** 3) - (10 * xi) - 5, decimals)
    fxi1 = round((xi1 ** 3) - (10 * xi1) - 5, decimals)
    e = calculate_error(xi, prev)
    return [i, xi, xi1, fxi, fxi1, e]


if __name__ == '__main__':
    # f(x) = x^3-10x-5
    print('Metodo Secante f(x) = x^3-10x-5')
    table = [['i', 'Xi', 'Xi-1', 'f(Xi)', 'f(Xi-1B)', 'error']]
    decimals = 8
    error = 0.0000001
    i = 0
    xi = 3.0
    xi1 = xi - 1
    fxi = round((xi ** 3) - (10 * xi) - 5, decimals)
    fxi1 = round((xi1 ** 3) - (10 * xi1) - 5, decimals)
    e = calculate_error(xi, 0)
    table.append([i, xi, xi1, fxi, fxi1, e])
    prev = table[-1][1]
    while e > error:
        i += 1
        table.append(getrow(i, table[-1][1], table[-1][2], table[-1][3], table[-1][4], prev))
        e = table[-1][-1]
        prev = table[-1][1]
    print(tabulate(table))
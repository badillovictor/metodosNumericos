from tabulate import tabulate

def calculate_error(xi, xt):
    return abs(round((xi - xt) / xi, 8))


def getrow(i, xi, xu, xt):
    xr = round((xi + xu) / 2, 3)
    fxi = round((xi ** 3) - (10 * xi) - 5, 8)
    fxr = round((xr ** 3) - (10 * xr) - 5, 8)
    fxifxr = round(fxi * fxr, 8)
    e = calculate_error(xr, xt)
    return [i, xi, xu, xr, fxi, fxr, fxifxr, e]


if __name__ == '__main__':
    # f(x) = x^3-10x-5
    print('Metodo Biseccion f(x) = x^3-10x-5')
    table = [['i', 'xi', 'xu', 'xr','f(xi)', 'f(xr)', 'f(xi)f(xr)', 'error']]
    error = 0.000001
    i = 0
    xi = 3
    xu = 4
    xt = 0
    e = 1
    while e > error:
        i += 1
        table.append(getrow(i, xi, xu, xt))
        if table[-1][6] > 0:
            xi = table[-1][3]
        else:
            xu = table[-1][3]
        e = table[-1][-1]
        xt = table[-1][3]
    print(tabulate(table))



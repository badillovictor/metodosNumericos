from tabulate import tabulate

def calculate_error(xi, xt):
    return abs(round((xi - xt) / xi, decimals))


def getrow(i, a, b, prev):
    fa = round((a ** 3) - (10 * a) - 5, decimals)
    fb = round((b ** 3) - (10 * b) - 5, decimals)
    xi = round(((a * fb) - (b * fa)) / (fb - fa), decimals)
    fxi = round((xi ** 3) - (10 * xi) - 5, decimals)
    fafxi = round(fa * fxi, decimals)
    e = calculate_error(xi, prev)
    return [i, a, b, xi, fa, fb, fxi, fafxi, e]


if __name__ == '__main__':
    # f(x) = x^3-10x-5
    print('Metodo Falsa Posicion f(x) = x^3-10x-5')
    table = [['i', 'A', 'B', 'xi', 'f(A)', 'f(B)', 'f(xi)', 'f(xi)f(xi)', 'error']]
    decimals = 8
    error = 0.0000001
    i = 0
    a = 3
    b = 4
    prev = 0
    e = 1
    while e > error:
        i += 1
        table.append(getrow(i, a, b, prev))
        if table[-1][7] < 0:
            a = table[-1][3]
        else:
            b = table[-1][3]
        e = table[-1][-1]
        prev = table[-1][3]
    print(tabulate(table))
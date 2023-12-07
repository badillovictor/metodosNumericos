from tabulate import tabulate


def calculate_x():
    xtemp[0] = round((b[0] - x[1] - a[0][2] * x[2]) / a[0][0], decimals)
    xtemp[1] = round((b[1] - a[1][0] * xtemp[0] + x[2]) / a[1][1], decimals)
    xtemp[2] = round((b[2] + a[0][2] * xtemp[0] - b[0] * xtemp[1]) / a[2][2], decimals)
    errors[0] = round(calculate_error(xtemp[0], x[0]), decimals)
    errors[1] = round(calculate_error(xtemp[1], x[1]), decimals)
    errors[2] = round(calculate_error(xtemp[2], x[2]), decimals)


def calculate_error(x, prev):
    return abs(round((x - prev) / x, decimals))


if __name__ == '__main__':
    # 10x + y + 2z = 3
    # 4x + 6y - z = 9
    # -2x + 3y + 8z = 51
    k = 1
    decimals = 8
    error = 0.0000001
    a = [
        [10, 1, 2],
        [4, 6, -1],
        [-2, 3, 8],
    ]
    b = [3, 9, 51]
    x = [0, 0, 0]
    errors = [1, 1, 1]
    xtemp = [0, 0, 0]
    table = [['i', 'x', 'y', 'z', 'Error x', 'Error y', 'Error z']]
    print('Metodo Gauss-Seidel')
    print('10x + y + 2z = 3')
    print('4x + 6y - z = 9')
    print('-2x + 3y + 8z = 51')
    while errors[0] > error and errors[1] > error and errors[2] > error:
        calculate_x()
        table.append([k, xtemp[0], xtemp[1], xtemp[2], errors[0], errors[1], errors[2]])
        k += 1
        for i in range(len((x))):
            x[i] = xtemp[i]
    print(tabulate(table))

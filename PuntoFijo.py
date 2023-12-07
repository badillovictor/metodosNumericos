def calculate_fx(xi):
    return round((10 * xi + 5) ** (1 / 3), 8)


def calculate_error(xi, xt):
    return abs(round((xi - xt) / xi, 8))


def print_row(i, xi, xt):
    string = '{0}\t\t{1}\t\t{2}'.format(i, xi, calculate_error(xi, xt))
    print(string)


if __name__ == '__main__':
    # f(x) = x^3-10x-5
    # g(x) = (10x-5)^(1/3)
    k = 1
    x = 3.5
    temp = 0
    error = 0.000001
    print('i\t\txi\t\t\t\tError Relativo')
    while calculate_error(x, temp) > error:
        k += 1
        temp = x
        x = calculate_gx(x)
        print_row(k, x, temp)

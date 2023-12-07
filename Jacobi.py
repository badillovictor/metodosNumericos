def calculate_x():
    print('X1 = [' + str(b[0]) + ' - (' + str(a[0][1]) + ')(' + str(round(x[1], 5)) + ') - (' + str(a[0][2]) + ')(' + str(round(x[2], 5)) + ')] ÷ ' + str(a[0][0]))
    xtemp[0] = (b[0] - a[0][1] * x[1] - a[0][2] * x[2]) / a[0][0]
    print('X2 = [' + str(b[1]) + ' - (' + str(a[1][0]) + ')(' + str(round(x[0], 5)) + ') - (' + str(a[1][2]) + ')(' + str(round(x[2], 5)) + ')] ÷ ' + str(a[1][1]))
    xtemp[1] = (b[1] - a[1][0] * x[0] - a[1][2] * x[2]) / a[1][1]
    print('X3 = [' + str(b[2]) + ' - (' + str(a[2][0]) + ')(' + str(round(x[0], 5)) + ') - (' + str(a[2][1]) + ')(' + str(round(x[1], 5)) + ')] ÷ ' + str(a[2][2]))
    xtemp[2] = (b[2] - a[2][0] * x[0] - a[2][1] * x[1]) / a[2][2]


def print_and_check():
    flag1 = False
    flag2 = False
    flag3 = False
    print(
        '\nX1 =', round(xtemp[0], 5),
        '\nX2 =', round(xtemp[1], 5),
        '\nX3 =', round(xtemp[2], 5), '\n'
    )
    print('Error X1 = (' + str(round(xtemp[0], 5)) + ' - ' + str(round(xtemp[0], 5)) + ') ÷ ' + str(round(xtemp[0], 5)) + ' = ' + str(round(abs((xtemp[0] - x[0]) / xtemp[0]), 5)))
    if (abs(xtemp[0] - x[0]) / xtemp[0]) < error:
        flag1 = True
    print('Error X2 = (' + str(round(xtemp[1], 5)) + ' - ' + str(round(xtemp[1], 5)) + ') ÷ ' + str(round(xtemp[1], 5)) + ' = ' + str(round((abs(xtemp[1] - x[1]) / xtemp[1]), 5)))
    if (abs(xtemp[1] - x[1]) / xtemp[1]) < error:
        flag2 = True
    print('Error X3 = (' + str(round(xtemp[2], 5)) + ' - ' + str(round(xtemp[2], 5)) + ') ÷ ' + str(round(xtemp[2], 5)) + ' = ' + str(round((abs(xtemp[2] - x[2]) / xtemp[2]), 5)))
    print('\n')
    if (abs(xtemp[2] - x[2]) / xtemp[2]) < error:
        flag3 = True
    if flag1 and flag2 and flag3:
        return False
    else:
        return True


if __name__ == '__main__':
    k = 1
    error = 0.05
    a = [
        [6, 2, 1],
        [-1, 8, 2],
        [1, -1, 6],
    ]
    b = [22, 30, 23]
    x = [0, 0, 0]
    xtemp = [0, 0, 0]
    print('Iteración numero', k)
    calculate_x()
    while print_and_check():
        for i in range(len(xtemp)):
            x[i] = xtemp[i]
        k += 1
        print('Iteración numero', k)
        calculate_x()
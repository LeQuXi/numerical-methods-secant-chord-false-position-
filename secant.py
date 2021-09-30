import numpy as np;
import matplotlib.pyplot as plt


def func(x):
    return 0.85 * x ** 4 - 9.92 * x ** 3 + 40.02 * x ** 2 - 64.68 * x + 34.25


def Secant(func, x0, x1):
    e = 1e-10
    N = 100
    print('\n\nIterations:')
    counter = 1
    condition = True
    while condition:
        if func(x0) == func(x1):
            print('ERROR!')
            break

        x2 = x0 - (x1 - x0) * func(x0) / (func(x1) - func(x0))
        print('Iteration-%d, x2 = %0.4f and f(x2) = %0.6f' % (counter, x2, func(x2)))
        x0 = x1
        x1 = x2
        counter = counter + 1

        if counter > N:
            print('No Root Found!')
            break

        condition = abs(func(x2)) > e
    print('\n Exact root is: %0.8f' % x2)
    return x2


x1 = Secant(func, 0, 5)
print('\n x = {0:.20f} f(x) = {1:.20f}'.format(x1, func(x1)))
x = np.linspace(0, 7, 100)
y = func(x)
plt.plot(x, y)
plt.grid()
plt.plot(x1, func(x1), markersize=7, marker='o')

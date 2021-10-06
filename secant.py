import math
import numpy as np;
import matplotlib.pyplot as plt
def func(x):
    return 0.85 * x ** 4 - 9.92 * x ** 3 + 40.02 * x ** 2 - 64.68 * x + 34.25 
def SearchforRoots(func,a1,a2):
    step=0.01
    x1 = a1; f1 = func(a1)
    x2 = a1 + step; f2 = func(x2)
    while f1*f2 > 0.0:
        if x1 >= a2:
            return None,None
        x1 = x2; f1 = f2
        x2 = x1 + step; f2 = func(x2)
    return x1,x2

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

def TotalRoots(func, a1, a2, eps=1e-6):
    print ('The roots on the interval [%f, %f] are:' % (a1,a2))
    #roots = []
    while 1:
        x1,x2 = SearchforRoots(func,a1,a2)
        if x1 != None:
            a1 = x2
            root = Secant(func,x1,x2)
            plt.plot(root, func(root), markersize=7, marker='o')
            #roots.appened(root) after all return array itself
            if root != None:
                pass
                print (round(root,-int(math.log(eps, 10))))
        else:
            print ('\nDone')
            break
TotalRoots(func, 0, 5)
x = np.linspace(0, 5, 100)
y = func(x)
plt.plot(x, y)
plt.grid()
plt.show()

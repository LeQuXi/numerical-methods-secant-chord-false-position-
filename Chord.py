import numpy as np

import matplotlib.pyplot as plt

import math

 

def func(x):

    return 0.85*x**4-9.92*x**3+40.02*x**2-64.68*x+34.25

 

def Chord(func,x0,x1):
    e=1e-10
    Counter = 1
    print('\n\nITERATIONSOFCHORD')
    condition = True
    while condition:
        x2 = (x1*func(x0)- x0*func(x1))/(func(x0)-func(x1))
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (Counter, x2, func(x2)))
        if func(x0) * func(x2) < 0:
           x1 = x2
        else:
            x0 = x2
        Counter = Counter + 1
        condition = abs(func(x2)) > e
    print('\nRequired root is: %0.8f' % x2)
    return x2
x1 = Chord(func, 0, 5)
x = np.linspace(0, 6, 100)
y = func(x)
plt.plot(x,y)
plt.grid()
plt.plot(x1, func(x1), markersize=7, marker='o')

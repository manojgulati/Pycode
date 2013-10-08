# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt

# <codecell>

def derivative(f):
    def compute(x, dx):
        return (f(x+dx) - f(x))/dx
    return compute

# <codecell>

def newtons_method(f, x, dx=0.000001, tolerance=0.000001):
    '''f is the function f(x)'''
    df = derivative(f)
    while True:
        x1 = x - f(x)/df(x, dx)
        t = abs(x1 - x)
        if t < tolerance:
            break
        x = x1
    return x

# <codecell>

def f(x):
    '''
    here solve x for ...
    3*x**5 - 2*x**3 + 1*x - 37 = 0
    '''
    return 3*x**5 - 2*x**3 + 1*x - 37
x_approx = 1  # rough guess
# f refers to the function f(x)
x = newtons_method(f, x_approx)
print("Solve for x in 3*x**5 - 2*x**3 + 1*x - 37 = 0")
print("x = %0.12f" % x)

# <codecell>

x = np.linspace(0,5,100,True)
y = 3*x**5 - 2*x**3 + 1*x - 37

# <codecell>

plot(x,y)

# <codecell>



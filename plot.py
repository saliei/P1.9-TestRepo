from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rc('font', family='monospace')

step = 0.1
start = -3
stop = -start
# include stop
xval = np.arange(start, stop+step, step)

if len(sys.argv) < 2:
    print("Usage: plot.py <func-number>")
    print("\t <func-number>: 1: f(x)=x")
    print("\t <func-number>: 2: f(x)=x**2")
    print("\t <func-number>: 3: f(x)=x**3")
    print("\t <func-number>: 4: f(x)=sin(x)")
    print("\t <func-number>: 5: f(x)=cos(x)")
    print("\t <func-number>: 6: f(x)=tan(x)")
    exit(1)

funcNum = int(sys.argv[1])

def f1(x):
    return x

def f2(x):
    return x**2

def f3(x):
    return x**3

def f4(x)
    return np.sin(x)

def f5(x):
    return np.cos(x)

def f6(x):
    return np.tan(x)

def runFunc(i):
    return{
            1: f1(xval),
            2: f2(xval),
            3: f3(xval),
            4: f4(xval),
            5: f5(xval),
            6: f6(xval),
            }[i]

yval = runFunc(funcNum)

plt.plot(xval, yval, lw=1, ls='-', marker='o', ms=3)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

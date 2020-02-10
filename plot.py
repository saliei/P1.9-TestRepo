from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rc('font', family='monospace')

step = 0.1
start = -5
stop = -start
# include stop
xval = np.arange(start, stop+step, step)

if len(sys.argv) < 2:
    print("Usage: plot.py <func-number>")
    print("\t <func-number>: 1: f(x)=x")
    exit(1)

funcNum = int(sys.argv[1])

def f1(x):
    return x

def f2(x):
    return np.exp(x)

def f3(x):
    return np.sqrt(np.abs(x))

def runFunc(i):
    return{
            1: f1(xval)
            }[i]

yval = runFunc(funcNum)

plt.plot(xval, yval, lw=1, ls='-', marker='o', ms=3)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

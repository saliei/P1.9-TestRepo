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
funcNum = int(sys.argv[1])

def f1(x):
    return x

def f2(x):
    return np.sin(x)

def f3(x):
    return np.cos(x)

def f4(x):
    return np.tan(x)

def runFunc(i):
    return{
            1: f1(xval)
            }[i]

yval = runFunc(funcNum)

plt.plot(xval, yval, lw=1, ls='-', marker='o', ms=3)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

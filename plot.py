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

def f(x):
    return x


def runFunc(i):
    return{
            1: f(xval)
            }[i]

yval = runFunc(funcNum)

plt.plot(xval, yval, lw=1, ls='-', marker='o', ms=3)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

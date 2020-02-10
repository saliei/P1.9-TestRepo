import sys
import numpy as np
import matplotlib.pyplot as plt

step = 0.1
start = -5
stop = -start
# include stop
xval = np.linspace(start, stop+step, step)
funcNum = int(sys.argv[1])

def f(x):
    return x


def runFunc(i):
    return{
            1: f(x)
            }[x]

yval = runFunc(funcNum)

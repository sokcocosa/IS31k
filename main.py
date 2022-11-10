import math

import matplotlib.pyplot as plt
import numpy as np



def func(x):

    return math.cos(x) - x ** 2


if __name__ == '__main__':

    xmin = -10.0
    xmax = 10.0

    count = 500

    xlist = np.linspace(xmin, xmax, count)

    ylist = [func(x) for x in xlist]

    plt.plot(xlist, ylist)

    plt.show()

import matplotlib.pyplot as plt
import numpy as np


def weib(x,n,a):
    return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)
a=5
count, bins, ignored = plt.hist(np.random.weibull(a,1000))
plt.show()

print(bins)
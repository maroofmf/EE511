'''
Author: Maroof Mohammed Farooq
USC ID: 7126869945
Subject code: EE 511
Project #: 1
Problem #: 4
'''

import scipy
import scikits.bootstrap as bootstrap
import random as rand
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli
plt.style.use('ggplot')

no_coin_tosses = 13
no_experiments = 50
no_heads=0
heads=[]
tails=[]
probability=[]


heads =[6, 9, 12, 7, 9, 11, 10, 7, 9, 8, 8, 12, 9, 9, 7, 12,
        9, 8, 7, 9, 12, 8, 9, 10, 9, 8, 7, 9, 8, 8,10, 8, 9,
        9, 10, 11, 10, 9, 9, 6, 9, 7, 7, 9, 10, 12, 8, 10, 10, 7]

for trial in range(0,1000):
    bootStapSet = np.random.choice(heads,size=(1,len(heads)),replace=True)
    probability.append(np.sum(bootStapSet)/(no_coin_tosses*no_experiments))


#Histogram
plt.hist(probability,bins=40)
plt.title("Histogram of probabilities")
plt.xlabel("Probability")
plt.ylabel("Frequency")
plt.show()

print('The lower confidence is:',np.percentile(probability,2.5))
print('The upper confidence is:',np.percentile(probability,97.5))



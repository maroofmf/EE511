'''
Author: Maroof Mohammed Farooq
USC ID: 7126869945
Subject code: EE 511
Project #: 1
Problem #: 3
'''

import scipy
import scikits.bootstrap as bootstrap
import random as rand
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli
plt.style.use('ggplot')

means=[]
fileName = 'NJGAS.dat'
file= open(fileName,'r')
fileData = file.read().splitlines()
fileData = [int(i) for i in fileData]

for trial in range(0,10000):
    bootStrapSet = np.random.choice(fileData,size=(1,len(fileData)),replace=True)
    # bootStrapSet = np.random.choice(fileData,size=(1,200),replace=True)
    means.append(scipy.mean(bootStrapSet))
#Histogram
plt.hist(means,bins=40)
plt.title("Histogram of means")
plt.xlabel("Mean of data")
plt.ylabel("Frequency")
plt.show()

print('The sample data mean is: ',np.mean(fileData))
print('The lower confidence is:',np.percentile(means,2.5))
print('The higher confidence is:',np.percentile(means,97.5))



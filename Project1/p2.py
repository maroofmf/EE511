'''
Author: Maroof Mohammed Farooq
USC ID: 7126869945
Subject code: EE 511
Project #: 1
Problem #: 2
'''

''' Import all the libraries '''
import random as rand
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli
plt.style.use('ggplot') # Plot Style

''' Initializing all variables '''
no_coin_tosses = 13
no_experiments = 50
no_heads=0
heads=[]
tails=[]

'''
Format of Data from the experiment performed:
heads =[#_of_heads_from_experiment_1,#_of_heads_from_experiment_1,
        ......,#_of_heads_from_experiment_50]
'''

heads =[6, 9, 12, 7, 9, 11, 10, 7, 9, 8, 8, 12, 9, 9, 7, 12,
        9, 8, 7, 9, 12, 8, 9, 10, 9, 8, 7, 9, 8, 8,10, 8, 9,
        9, 10, 11, 10, 9, 9, 6, 9, 7, 7, 9, 10, 12, 8, 10, 10, 7]
cumulativeHeads = np.cumsum(heads)

'''Plotting'''
#Plotting Scatterplot
plt.figure(1)
plt.scatter(range(1,len(heads)+1),cumulativeHeads)
plt.title('ScatterPlot')
plt.ylabel("# of heads")
plt.xlabel("Experiment Number")

#Plotting Histogram
plt.figure(2)
plt.hist(heads,bins=40)
plt.title("Histogram of # of heads")
plt.xlabel("# of heads")
plt.ylabel("Frequency")

#Tally Plotting
plt.figure(3)
y_axis=[]
for value in range(0,len(heads)):
    y_axis.append((cumulativeHeads[value])/(no_coin_tosses*(value+1)))

x_axis = np.linspace(1,no_experiments,num=no_experiments)
plt.plot(x_axis,y_axis,c='Red')
plt.title("Running Tally")
plt.xlabel("Experiment Number")
plt.ylabel("Probability of obtaining heads")
plt.show()  #Show all the plots
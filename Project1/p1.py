'''
Author: Maroof Mohammed Farooq
USC ID: 7126869945
Subject code: EE 511
Project #: 1
Problem #: 1
'''

''' All libraries '''
import random as rand
import pandas as pd
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')   # Plotting style

''' Initializing Variables '''
no_coin_tosses = 13
no_experiments = 50
no_heads=0
heads=[]
tails=[]

'''
Format of Data from the experiment performed:
heads =[#_of_heads_from_experiment_1,#_of_heads_from_experiment_1,
        ,......,#_of_heads_from_experiment_50]
'''

heads =[7, 8, 7, 6, 5, 4, 9, 6, 3, 8, 5, 10, 9, 7, 6,
        7, 7, 6, 4, 6, 6, 9, 6, 11, 7, 10, 5, 7, 7, 9,
        2, 5, 7, 10, 8, 7, 7, 7, 3, 7, 7, 10, 6, 7, 6,
        6, 4, 6, 8, 6]

cumulativeHeads = np.cumsum(heads)


''' Plotting the results '''

#Plotting Scatterplot
plt.figure(1)
plt.scatter(np.linspace(1,no_experiments,num=no_experiments),cumulativeHeads)
plt.title('ScatterPlot')
plt.ylabel("# of heads")
plt.xlabel("Experiment Number")

#Plotting Histogram
plt.figure(2)
plt.hist(heads,bins=20)
plt.title("Histogram of # of heads")
plt.xlabel("# of heads")
plt.ylabel("Frequency")

# Running Tally Plotting
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


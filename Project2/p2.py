"""
Author: Maroof Mohammed Farooq
USC ID: 7126869945
EE 511
Project 2
Problem 1
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.special
from scipy.stats import chisquare
import random


class bimodalRNG():
    def __init__(self,sampleSize):
        self.sampleSize = sampleSize
        self.randNumbers1=[]
        self.randNumbers2=[]
        self.rejectCount1 = 0
        self.rejectCount2 = 0

    def functionDef(self,xValue):

        if 0 < xValue <= 1:
            return((0.5*(xValue**7)*((1-xValue)**4))/(scipy.special.beta(8,5)))  #max is 1.5

        if 4 < xValue <= 5:
            return(0.5*(xValue-4))      #max is 0.5

        if 5 < xValue <= 6:
             return(-0.5*(xValue-6))     #max is 0.5

        else:
            return(0)

    def uniformGenerator(self,*args):
        if not args: return(np.random.uniform(0,1,size=1)[0])
        return(np.random.uniform(args[0],args[1],size=1)[0])

    def rngProcessing1(self):
        xValue = 6*self.uniformGenerator()
        yThreshold = self.functionDef(xValue)
        yValue = 1.5*self.uniformGenerator()
        if yValue<yThreshold:
            return([xValue,1])
        else:
            return([xValue,-1])

    def rngProcessing2(self):
        xValue = random.choice([self.uniformGenerator(),self.uniformGenerator(4,6)])
        yThreshold = self.functionDef(xValue)
        yValue = 1.5*self.uniformGenerator()
        if yValue<yThreshold:
            return([xValue,1])
        else:
            return([xValue,-1])

    def rngGen(self):
        while len(self.randNumbers1) < self.sampleSize:
            randomNumber1 = self.rngProcessing1()
            if randomNumber1[1]==1:
                self.randNumbers1.append(randomNumber1[0])
            elif randomNumber1[1]==-1:
                self.rejectCount1 +=1
            print("Obtaining Random Number Set 1 {} % complete".format((len(self.randNumbers1)/(self.sampleSize))*100))

        while  len(self.randNumbers2) < self.sampleSize:
            randomNumber2 = self.rngProcessing2()
            if randomNumber2[1]==1:
                self.randNumbers2.append(randomNumber2[0])
            elif randomNumber2[1]==-1:
                self.rejectCount2 +=1
            print("Obtaining Random Number Set 2 {} % complete".format((len(self.randNumbers2)/(self.sampleSize))*100))

        return(self.randNumbers1,self.randNumbers2)

    def efficiency(self):
        return(self.rejectCount1/self.sampleSize,self.rejectCount2/self.sampleSize)



def main():
    randomNumbersObject = bimodalRNG(1000)  #enter the number of samples here!
    randomNumbers = randomNumbersObject.rngGen()
    efficiency = randomNumbersObject.efficiency()
    print('The rejection rate for Rejection Sampling with single uniform envelope = {} '.format(efficiency[0]))
    print('The rejection rate for Rejection Sampling with convex envelopes = {} '.format(efficiency[1]))

    plt.figure(1)
    plt.hist(randomNumbers[0],bins=100)
    plt.title("Rejection Sampling with single uniform envelope")
    plt.xlabel("Random Number Value")
    plt.ylabel("Frequency")

    plt.figure(2)
    plt.hist(randomNumbers[1],bins=100)
    plt.title("Rejection Sampling with convex envelopes")
    plt.xlabel("Random Number Value")
    plt.ylabel("Frequency")
    plt.show()



#BoilerPlate Syntax
if __name__ == '__main__':
    main()


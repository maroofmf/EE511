"""
Author: Maroof Mohammed Farooq
USC ID: 7126869945
EE 511
Project 2
Problem 2
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.special
import scipy.stats as sci
import random

class functions():
    def __init__(self):
        self.junk = 0

    def halfNormal(self,*args):
        theta = args[0]
        x=args[1]
        return(((2*theta)/(math.pi))*np.exp((-(x*theta)**2)/math.pi))

    def uniformGenerator(self,*args):
        lowerBound=0
        upperBound=1
        if args: lowerBound = args[0]; upperBound = args[1]
        return(np.random.uniform(lowerBound, upperBound, size=1)[0])

    def exponential(self,*args):
        lambdaParam = args[0]
        x=args[1]
        return(lambdaParam*np.exp(-lambdaParam*x))

    def beta(self,*args):
        alpha = args[0]
        beta = args[1]
        x = args[2]
        return(((x**(alpha-1))*((1-x)**(beta-1)))/(scipy.special.beta(alpha,beta)))

    def expGen(self,*args):
        lambdaParam = 1
        if args: lambdaParam = args[0];
        return(np.random.exponential(lambdaParam,size=1)[0])


class randomGenerator():
    def __init__(self,sampleSize):
        self.sampleSize = sampleSize
        self.randNumbers1=[]
        self.randNumbers2=[]
        self.functions = functions()

    def rngProcessing1(self):
        xValue = self.functions.expGen(1)
        yThreshold = self.functions.halfNormal(1,xValue)
        yValue = 0.64 * self.functions.uniformGenerator(0,1)
        if yValue<yThreshold:
            return([xValue,1])
        else:
            return([xValue,-1])

    def rngProcessing2(self):
        xValue = self.functions.uniformGenerator()
        yThreshold = self.functions.beta(2,5,xValue)
        yValue = 2.5*self.functions.uniformGenerator()
        if yValue<yThreshold:
            return([xValue,1])
        else:
            return([xValue,-1])

    def rngGen(self):
        while len(self.randNumbers1) < self.sampleSize:
            randomNumber1 = self.rngProcessing1()
            if randomNumber1[1]==1:
                self.randNumbers1.append(randomNumber1[0])
            print("Obtaining Random Number Set 1 {} % complete"
                  .format((len(self.randNumbers1)/(self.sampleSize))*100))

        while  len(self.randNumbers2) < self.sampleSize:
            randomNumber2 = self.rngProcessing2()
            if randomNumber2[1]==1:
                self.randNumbers2.append(randomNumber2[0])
            print("Obtaining Random Number Set 2 {} % complete"
                  .format((len(self.randNumbers2)/(self.sampleSize))*100))

        return(self.randNumbers1,self.randNumbers2)

def main():
    randomNumbersObject = randomGenerator(1000)  #enter the number of samples here!
    randomNumbers = randomNumbersObject.rngGen()

    plt.figure(1)
    plt.hist(randomNumbers[0],bins=25)
    plt.title("Rejection Sampling for Half Normal Distribution")
    plt.xlabel("Random Number Value")
    plt.ylabel("Frequency")

    plt.figure(2)
    plt.hist(randomNumbers[1],bins=25)
    plt.title("Rejection Sampling for Beta Distribution")
    plt.xlabel("Random Number Value")
    plt.ylabel("Frequency")
    plt.show()



#BoilerPlate Syntax
if __name__ == '__main__':
    main()


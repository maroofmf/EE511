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


class bimodalRNG():
    def __init__(self,sampleSize):
        self.sampleSize = sampleSize
        self.randNumbers=[]
        self.rejectCount = 0

    def functionDef(self,xValue):

        if 0 < xValue <= 1:
            return((0.5*(xValue**7)*((1-xValue)**4))/(scipy.special.beta(8,5)))  #max is 1.5

        if 4 < xValue <= 5:
            return(0.5*(xValue-4))      #max is 0.5

        if 5 < xValue <= 6:
             return(-0.5*(xValue-6))     #max is 0.5

        else:
            return(0)

    def uniformGenerator(self):
        return(np.random.uniform(0,1,size=1)[0])

    def randomNG(self):
        xValue = 6*self.uniformGenerator()
        yThreshold = self.functionDef(xValue)
        yValue = 1.5*self.uniformGenerator()
        if yValue<yThreshold:
            return([xValue,1])
        else:
            return([xValue,-1])

    def rngGen1(self):
        for value in range(0,self.sampleSize):
            randomNumber = self.randomNG()
            if randomNumber[1]==1:
                self.randNumbers.append(randomNumber[0])
            else:
                self.rejectCount +=1
        return(self.randNumbers)

    def efficiency(self):
        return(self.rejectCount/self.sampleSize)



def main():
     randomNumbersObject = bimodalRNG(1000)
     randomNumbers = randomNumbersObject.rngGen1()
     efficiency = randomNumbersObject.efficiency()
     print(efficiency)
     plt.hist(randomNumbers,bins=100)
     plt.show()


#BoilerPlate Syntax
if __name__ == '__main__':
    main()
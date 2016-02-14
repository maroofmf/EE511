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
from scipy.stats import chisquare

class rngWeibull():
    def __init__(self,shapeParam,totalSamples):
        self.totalSamples = totalSamples
        self.shapeParam = shapeParam
        self.randomGenerator=[]
        self.weibullPDFValues={}
        self.chiVal = 0

    def uniformGenerator(self):
        return(np.random.uniform(0,1,size=1)[0])

    def weibullGenerator(self):
        for size in range(0,self.totalSamples):
            randNumber = ((-math.log1p(-self.uniformGenerator()))**(1/self.shapeParam))
            self.randomGenerator.append(randNumber)
        return(self.randomGenerator)

    def weibullPDF(self,xValue):
        self.weibullPDFValues = (xValue ,(self.shapeParam * (xValue)**(self.shapeParam-1)
                                          * np.exp(-xValue ** self.shapeParam)))
        return(self.weibullPDFValues)

    def chiSquareValue(self,bins,count,scale):
        dof = len(bins)-1
        observedValue = count
        xValue = []
        chiSquare = []
        [xValue.append((bins[value]+bins[value+1])/2) for value in range(0,dof)]
        expectedValue = self.weibullPDF(np.asarray(xValue))
        expectedValue = expectedValue[1]*scale

        [chiSquare.append(((observedValue[value]-expectedValue[value])**2)/(expectedValue[value]))
                            for value in range(0, dof)]

        return(sum(chiSquare))


def main():
    randomNumbersObject = rngWeibull(5,1000)
    randomNumbers = randomNumbersObject.weibullGenerator()
    xValue = np.arange(1,100.)/50.
    weibullPDF = randomNumbersObject.weibullPDF(xValue)

    plt.figure(1)
    count, bins, ignored = plt.hist(randomNumbers)
    scale = count.max()/weibullPDF[1].max()
    plt.plot(weibullPDF[0],weibullPDF[1]*scale)

    chiValue = randomNumbersObject.chiSquareValue(bins,count,scale)

    print('The Chi Square Value is:', chiValue)
    plt.show()

#BoilerPlate Syntax
if __name__ == '__main__':
    main()




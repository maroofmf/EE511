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

class rngWeibull():
    def __init__(self,shapeParam,totalSamples):
        self.totalSamples = totalSamples
        self.shapeParam = shapeParam
        self.randomGenerator=[]

    def uniformGenerator(self):
        return(np.random.uniform(0,1,size=1)[0])

    def weibullGenerator(self):
        for size in range(0,self.totalSamples):
            randNumber = ((-math.log1p(-self.uniformGenerator()))**(1/self.shapeParam))
            self.randomGenerator.append(randNumber)

        return(self.randomGenerator)




def main():
    randomNumbersObject = rngWeibull(5,1000)
    randomNumbers = randomNumbersObject.weibullGenerator()





    #Plotting
    plt.figure(1)
    plt.hist(randomNumbers)
    plt.figure(2)
    plt.hist(np.random.weibull(5,1000))
    plt.show()






#BoilerPlate Syntax
if __name__ == '__main__':
    main()




import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import halfnorm
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.special
import random




class functions():
    def __init__(self):
        self.someshit = 0

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



o=functions()
a=np.linspace(0,1,100)
num2 = o.beta(2,5,a)
print(np.max(num2))
plt.figure(1)
plt.plot(a,num2)

#
plt.show()

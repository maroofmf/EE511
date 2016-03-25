'''
Author: Maroof Mohammed Farooq
USC ID: 7126869945
Subject code: EE 511
Project #: 3
Problem #: 1
'''

''' Import Libraries '''
import numpy as np
from matplotlib import pyplot as plt
import gmmRNG as gmm
import specialFunctions as sf
import time
start_time = time.time()

''' Inputs'''
sampleSize = 300

'''Generate Random Numbers '''

mixingCoefficient = [0.45, 0.55]
centroids = [ np.array([0,0]), np.array([3,1])]
covariance = [np.array([[2,0.5],[0.7,1]]),np.array([[2,0.4],[1,3]])]
randomSamples = gmm.sample_gaussian_mixture(centroids, covariance, mc=mixingCoefficient, samples=sampleSize)

plt.plot(randomSamples[:,0], randomSamples[:,1], '.')

''' Plot GMM '''

for i in range(len(mixingCoefficient)):
    x1, x2 = gmm.gauss_ellipse_2d(centroids[i], covariance[i])
    plt.plot(x1, x2, 'k', linewidth=2)

plt.xlabel('$x_1$'); plt.ylabel('$x_2$')
plt.show()

''' Implementing GMM to estimate pdf Parameters'''

probabilityTable = []
estimateCentroids = [ np.array([0,0]), np.array([0.1,0.1])]
estimateCovariance = [np.diag((1,1)),np.diag((1.01,1.01))]
estimateMixingCoefficient = [0.3,0.7]
clusterOneResponsibility = 0
clusterTwoResponsibility = 0

for junkValue in range(0,1000):
    probabilityTable = []
    clusterOneResponsibility = 0
    clusterTwoResponsibility = 0
    for x1,x2 in randomSamples:
        clusterOnePDF = estimateMixingCoefficient[0]*gmm.mulnormpdf(np.array([x1,x2]),estimateCentroids[0], estimateCovariance[0])
        clusterTwoPDF = estimateMixingCoefficient[1]*gmm.mulnormpdf(np.array([x1,x2]),estimateCentroids[1], estimateCovariance[1])
        clusterOneProbability = clusterOnePDF/(clusterOnePDF+clusterTwoPDF)
        clusterTwoProbability = clusterTwoPDF/(clusterTwoPDF+clusterOnePDF)
        probabilityTable.append(np.array([clusterOneProbability,clusterTwoProbability]))

    for p1,p2 in probabilityTable:
        clusterOneResponsibility += p1
        clusterTwoResponsibility += p2

    clusterOne_estimateMixingCoefficient = clusterOneResponsibility/sampleSize
    clusterTwo_estimateMixingCoefficient = clusterTwoResponsibility/sampleSize

    estimateMixingCoefficient = [clusterOne_estimateMixingCoefficient, clusterTwo_estimateMixingCoefficient]

    clusterOne_estimateCentroids = [0,0]
    clusterTwo_estimateCentroids = [0,0]
    clusterOne_estimateCovariance = np.array([[0,0],[0,0]])
    clusterTwo_estimateCovariance = np.array([[0,0],[0,0]])

    for index in range(0,sampleSize):
        clusterOne_estimateCentroids += (randomSamples[index]*probabilityTable[index][0])
        clusterTwo_estimateCentroids += (randomSamples[index]*probabilityTable[index][1])

    estimateCentroids = [(1/clusterOneResponsibility)*clusterOne_estimateCentroids,(1/clusterTwoResponsibility)*clusterTwo_estimateCentroids]

    for i in range(0,sampleSize):
        clusterOne_estimateCovariance = clusterOne_estimateCovariance + (probabilityTable[i][0])*sf.outerProduct(list(randomSamples[i]-estimateCentroids[0]))
        clusterTwo_estimateCovariance = clusterTwo_estimateCovariance + (probabilityTable[i][1])*sf.outerProduct(list(randomSamples[i]-estimateCentroids[1]))

    estimateCovariance = [(1/clusterOneResponsibility)*clusterOne_estimateCovariance,(1/clusterTwoResponsibility)*clusterTwo_estimateCovariance]


print('The Actual Covariances are: \n',covariance,'\n')
print('The Estimated Covariances are: \n',estimateCovariance,'\n')

print('The Actual Centroids are: \n',centroids,'\n')
print('The Estimated Centroids are: \n',estimateCentroids,'\n')

print('The Actual Mixing Coefficients are: \n',mixingCoefficient,'\n')
print('The Estimated Centroid are: \n',estimateMixingCoefficient,'\n')

print("--- %s seconds ---" % (time.time() - start_time))





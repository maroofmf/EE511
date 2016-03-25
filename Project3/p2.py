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
import re
import specialFunctions as sf
import time
start_time = time.time()

''' Regex Processing '''
input_File = 'old-faithful.txt'
fileObject = open(input_File,'r')
fileData = str(fileObject.read())

extractRelevantData = re.findall(r'(\d+)\s+([\d.]+)\s+([\d.]+)', fileData)

dataPoints = []


for index,eruption,waiting in extractRelevantData:
    dataPoints.append((float(eruption),float(waiting)))

dataPoints = np.array(dataPoints)
sampleSize = len(dataPoints)
dataMeanX = np.mean(dataPoints[0:sampleSize,0])
dataMeanY = np.mean(dataPoints[0:sampleSize,1])
dataConv = np.cov(dataPoints[0:sampleSize,0])
dataConv = np.cov(dataPoints[0:sampleSize,1])

''' Implementing GMM to estimate pdf Parameters'''


probabilityTable = []
estimateCentroids = [ np.array([dataMeanX,dataMeanY]), np.array([dataMeanX+0.1,dataMeanY+0.1])]
estimateCovariance = [np.diag((dataConv,dataConv)),np.diag((dataConv+0.1,dataConv+0.1))]
estimateMixingCoefficient = [0.5,0.5]
clusterOneResponsibility = 0
clusterTwoResponsibility = 0

for junkValue in range(0,1000):
    probabilityTable = []
    clusterOneResponsibility = 0
    clusterTwoResponsibility = 0
    for x1,x2 in dataPoints:
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
        clusterOne_estimateCentroids += (dataPoints[index]*probabilityTable[index][0])
        clusterTwo_estimateCentroids += (dataPoints[index]*probabilityTable[index][1])

    estimateCentroids = [(1/clusterOneResponsibility)*clusterOne_estimateCentroids,(1/clusterTwoResponsibility)*clusterTwo_estimateCentroids]

    for i in range(0,sampleSize):
        clusterOne_estimateCovariance = clusterOne_estimateCovariance + (probabilityTable[i][0])*sf.outerProduct(list(dataPoints[i]-estimateCentroids[0]))
        clusterTwo_estimateCovariance = clusterTwo_estimateCovariance + (probabilityTable[i][1])*sf.outerProduct(list(dataPoints[i]-estimateCentroids[1]))

    estimateCovariance = [(1/clusterOneResponsibility)*clusterOne_estimateCovariance,(1/clusterTwoResponsibility)*clusterTwo_estimateCovariance]

print('The Estimated Covariances are: \n',estimateCovariance,'\n')
print('The Estimated Centroids are: \n',estimateCentroids,'\n')
print('The Estimated Mixing Coefficients are: \n',estimateMixingCoefficient,'\n')


plt.plot(dataPoints[:,0], dataPoints[:,1], '.')

''' Plot GMM '''

for i in range(len(estimateMixingCoefficient)):
    x1, x2 = gmm.gauss_ellipse_2d(estimateCentroids[i], estimateCovariance[i])
    plt.plot(x1, x2, 'k', linewidth=2)

plt.xlabel('$x_1$'); plt.ylabel('$x_2$')
plt.show()


print("--- %s seconds ---" % (time.time() - start_time))


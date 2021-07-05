import numpy as np
from sklearn import datasets
import random

def kmeans(x_train, k):
    changed = True
    center = np.array(random.sample(x_train, k))
    dist = np.zeros((150, k))
    # Loop until the center won't change
    while changed:
        for i in range(k):
            C = np.tile(center[i,:], (150,1))
            dist[:,i]=np.sqrt(np.sum((x_train-C)**2,axis=1))

        labels = np.argmin(dist, axis=1)
        newcenter = np.zeros((k,4))
        for i in range(k):
            newcenter[i,:] =  np.average(x_train[labels==i,:], axis=0)
        changed = (newcenter == center).all() == False
        center = newcenter
    # Calculate the number of each group
    num_of_each_type = np.array([x_train[labels == i,:].shape[0] for i in range(k)])
    # Calcultate the total distance of the classification
    totalDistance = 0
    for i in range(k):
        #print sum(labels==i)
        newCenter = np.tile(center[i,:], (sum(labels==i),1))
        #print "dist"+str(np.sum((x_train[labels==i,:]-newCenter)**2,axis=1))
        totalDistance += np.sum((np.sum((x_train[labels==i,:]-newCenter)**2,axis=1)))
    # return type labels and total distance and number of each type
    return labels, np.sqrt(totalDistance), num_of_each_type

# Loading data
iris = datasets.load_iris()
x_train = iris.data
y_train = iris.target

k = 3
n = 10 # num of loops
labels = {}
num = {}
totalDist = np.zeros(n)
minDist = 10**6
minIndex = 0
for j in range(n):
    labels[j], totalDist[j], num[j] = kmeans(x_train, k)
    if totalDist[j] < minDist:
        minIndex = j
        minDist = totalDist[j]

# Print the classification results
print "Number of samples in each claster is " + str(num[minIndex]) + "."
#print "\t\t %-15s %-15s %-15s" %("setosa", "versicolor", "virginica")
print "\t\t %-15s %-15s %-15s" %("type0", "type1", "type2")
for i in range(k):
    a = sum((y_train[labels[minIndex]==i])==0)*1.0/(x_train[labels[minIndex]==i,:]).shape[0]
    b = sum((y_train[labels[minIndex]==i])==1)*1.0/(x_train[labels[minIndex]==i,:]).shape[0]
    c = sum((y_train[labels[minIndex]==i])==2)*1.0/(x_train[labels[minIndex]==i,:]).shape[0]
    print "%8s\t %-15.4f %-15.4f %-15.4f" %("cluster"+str(i), a, b, c)


# Navie Bayes Classification
# Author: Qun Liu
# Date  : 2015-4-14

import numpy as np
from sklearn import datasets

def NBIris(x_test):
    # load train data to x_train and y_train
    iris = datasets.load_iris()
    x_train = iris.data
    y_train = iris.target
    # calculate the probability of each type
    p_y = np.array([y_train[y_train == i].shape[0] / float(x_train.shape[0]) for i in range(3)])

    # calculate the average and stddev of normal distribution
    ave = np.zeros((3,4))
    sigma = np.zeros((3,4))
    for i in range(3):
        ave[i,:] = np.average(x_train[y_train==i, :], axis=0)
        sigma[i,:] = np.std(x_train[y_train==i, :], axis=0)

    x_test_matrix = np.tile(x_test, (3,1))
    # calcualte the probability of p(xi|y) with the equation of normal distribution
    p_xy = 1.0/sigma/np.sqrt(2*np.pi)*np.exp(-(x_test_matrix-ave)**2/2.0/sigma**2)
    # change the probability to log, because the value may be too small
    log_p_yx = np.sum(np.log(p_xy), axis=1)+np.log(p_y)
    # return the index of max probability, and it's also the type label
    y_test = np.argmax(log_p_yx)
    return y_test

x_test = np.array([6, 2.0, 5.5, 1.0])
print "The type of " + str(x_test) + " is " + str( NBIris(x_test)) + "."

#!/usr/bin/python
import numpy as np

# L1 = n * 2 matrix
# L2 = n * 2 matrix
# RF = array of recombination frequencies of size (n-1) 
# k  = number of progenies to produce
def cross2(L1, L2, RF, k):
	# number of columns in L1
	n = L1.shape[1]

	# RC = (2 k) * n matrix
	# and first 0.5 probability to RF
	# duplicate the probabilities 2*k times vertically
	# compare the probabilities with random 2k* n matrix
	# the first column means which side to choose
	# 0 means up and 1 means down
	# the rest of the columns mean if they need to change column
	# 0 means don't change column and 1 means change column
	probabilities = np.hstack((np.array([0.5]), RF))
	RC = np.random.random((2*k, n))<=np.tile(probabilities, [2*k, 1])
	#print "RC"
	#print RC

	# Cumulative products of elements along row
	# it shows which columns to choose in Y1 and Y2
	# In fDown, 0 means up and 1 means down
	# In fUp, 0 means down and 1 means up
	cumprodRC = np.cumprod(1-2*RC, axis=1)
	fDown = cumprodRC < 0
	fDown = np.reshape(fDown, (2*k, n), order='F')
	fUp  = cumprodRC > 0
	fUp = np.reshape(fUp, (2*k, n), order='F')
	#print "fDown"
	#print fDown

	# copy the up sides of L1&L2 and combine them
	# copy the down sides of L1&L2 and and combine them
	# duplicate the combined matrix k times and 
	# put them in a n * (2*k) matrices
	splittedL1 = np.vsplit(L1, 2)
	splittedL2 = np.vsplit(L2, 2)
	#print "splittedL1"
	#print splittedL1
	#print "splittedL1[0]"
	#print splittedL1[0]
	combinedUp = np.vstack((splittedL1[0], splittedL2[0]))
	combinedDown = np.vstack((splittedL1[1], splittedL2[1]))
	Y1 = np.tile(combinedUp, [k, 1])
	Y2 = np.tile(combinedDown, [k, 1])
	#print "Y1"
	#print Y1
	#print "Y2"
	#print Y2

	# multiple elements in Y1 and Y2  
	# by fUp and fDown respectively
	# and add them
	# this is the result
	Y = fUp*Y1 + fDown*Y2
	#print "Y"
	#print Y

	# reshape 2k * n matrix to 2*n*k matrix
	Y = np.vsplit(Y, k)

	return Y

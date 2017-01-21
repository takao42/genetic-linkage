#!/usr/bin/python
import numpy as np

# L1 = n * 2 matrix
# L2 = n * 2 matrix
# RF = (n-1) * 1 matrix of recombination frequencies
# k  = number of progenies to produce
def cross2(L1, L2, RF, k):
	# number of rows in L1
	# octave code
	#n = size(L1,1);
	n = L1.shape[0]

	# RC = n * (2*k) matrix
	# and first 0.5 probability to RF
	# duplicate the probabilities 2*k times
	# compare the probabilities with random n * (2*k) matrix
	# this(RC) shows which side has to be chosen
	# the first row means which side to choose
	# 0 means left and 1 means right
	# the rest of the rows mean if they need to change row
	# 0 means don't change row and 1 means change row
	# octave code
	#RC = rand(n,2*k)<=repmat([0.5; RF],1,2*k);
	probabilities = np.vstack((np.array([[0.5]]), RF))
	RC = np.random.random((n, 2*k))<=np.tile(probabilities, [1, 2*k])

	# Cumulative products of elements along column
	# it shows which columns to choose in Y1 and Y2
	# In fRight, 0 means left and 1 means right
	# In fLeft, 0 means right and 1 means left
	# numpy comprod is much slower than octave comprod
	# octave code
	#f = cumprod(1-2*RC) <= 0;
	cumprodRC = np.cumprod(1-2*RC, axis=0)
	fRight = cumprodRC < 0
	fRight = np.reshape(fRight, (n,2*k), order='F')
	fLeft  = cumprodRC > 0
	fLeft = np.reshape(fLeft, (n,2*k), order='F')
	#print "fRight"
	#print fRight

	# copy the left sides of L1&L2 and combine them
	# copy the right sides of L1&L2 and and combine them
	# duplicate the combined matrix k times and 
	# put them in a n * (2*k) matrices
	# octave code
	#Y1 = repmat([L1(:,1),L2(:,1)],1,k);
	#Y2 = repmat([L1(:,2),L2(:,2)],1,k);
	splittedL1 = np.hsplit(L1, 2)
	splittedL2 = np.hsplit(L2, 2)
	#print "splittedL1"
	#print splittedL1
	#print "splittedL1[0]"
	#print splittedL1[0]
	combinedLeft = np.hstack((splittedL1[0], splittedL2[0]))
	combinedRight = np.hstack((splittedL1[1], splittedL2[1]))
	Y1 = np.tile(combinedLeft, [1, k])
	Y2 = np.tile(combinedRight, [1, k])
	#print "Y1"
	#print Y1
	#print "Y2"
	#print Y2

	# multiple each element in Y1 and Y2  
	# by fLeft and fRight respectively
	# and add them
	# this is the result
	# octave code
	#Y1(f) = Y2(f);
	Y = fLeft*Y1 + fRight*Y2
	#print "Y"
	#print Y

	# reshape n * 2k matrix to n*2*k matrix
	# octave code
	#Y1 = reshape(Y1,n,2,k);
	Y = np.hsplit(Y, k)

	return Y

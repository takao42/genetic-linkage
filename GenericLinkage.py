#!/usr/bin/python
import numpy as np
import multiprocessing as mp
from functools import partial

# L1 = n * 2 matrix
# L2 = n * 2 matrix
# RF = array of recombination frequencies of size (n-1) 
# k  = number of progenies to produce
def cross2(L1, L2, RF, k):
	# number of columns in L1
	n = L1.shape[1]

	# RC = 2k by n matrix
	# and first 0.5 probability to RF
	# duplicate the probabilities 2k times vertically
	# compare the probabilities with random 2k by n matrix
	# the first column means which side to choose
	# 0 means up and 1 means down
	# the rest of the columns mean if they need to change column
	# 0 means don't change column and 1 means change column
	probabilities = np.hstack((np.array([0.5]), RF))
	RC = np.random.random((2*k, n))<=np.tile(probabilities, [2*k, 1])

	# Cumulative products of elements along row
	# it shows which columns to choose in Y1 and Y2
	# In fDown, 0 means up and 1 means down
	# In fUp, 0 means down and 1 means up
	cumprodRC = np.cumprod(1-2*RC, axis=1)
	fDown = cumprodRC < 0
	fDown = np.reshape(fDown, (2*k, n), order='F')
	fUp  = cumprodRC > 0
	fUp = np.reshape(fUp, (2*k, n), order='F')

	# copy the up sides of L1&L2 and combine them
	# copy the down sides of L1&L2 and and combine them
	# duplicate the combined matrix k times and 
	# put them in a 2k by n matrices
	splittedL1 = np.vsplit(L1, 2)
	splittedL2 = np.vsplit(L2, 2)
	combinedUp = np.vstack((splittedL1[0], splittedL2[0]))
	combinedDown = np.vstack((splittedL1[1], splittedL2[1]))
	Y1 = np.tile(combinedUp, [k, 1])
	Y2 = np.tile(combinedDown, [k, 1])

	# multiple elements in Y1 and Y2  
	# by fUp and fDown respectively
	# and add them
	# this is the result
	Y = fUp*Y1 + fDown*Y2

	# reshape 2k by n matrix to k by 2 by n matrix
	Y = np.reshape(Y, (k, 2, n), order='C')

	return Y

# L1 = n * 2 matrix
# L2 = n * 2 matrix
# RF = array of recombination frequencies of size (n-1) 
# k  = number of progenies to produce
# i  = current job number
def cross2iterable(L1, L2, RF, k, i):
	print("Job " + str(i))

	progenies = cross2(L1, L2, RF, k)
	#print("progenies.shape {}".format(progenies.shape))

	return progenies 

# multi processing version
# L1 = n * 2 matrix
# L2 = n * 2 matrix
# RF = array of recombination frequencies of size (n-1) 
# k  = number of progenies to produce
def cross2mp(L1, L2, RF, k):

	# if this value is too big, you memory cant hold 
	# all the data and therefore the total execution time
	# will be very slow
	maxTotalJobSize = 200
	# number of jobs
	numCores = numJobs = mp.cpu_count()
	numJobs = numCores
	# number of progenies to produce per job
	progenyPerJob = k//numJobs
	
	while(progenyPerJob*numCores > maxTotalJobSize):
		numJobs = numJobs * 2
		progenyPerJob = k//numJobs
		#print("numJobs {}, progenyPerJob {}".format(numJobs, progenyPerJob))

	theRestNum = k%numJobs 
	print("numJobs {}, progenyPerJob {}, theRestNum {}".format(numJobs, progenyPerJob, theRestNum))

	progenyList = []

	# use multi-thread to calculate
	if (numJobs != 0):
		iterable = range(0, numJobs)
		pool = mp.Pool()
		func = partial(cross2iterable, L1, L2, RF, progenyPerJob)
		progenyList = pool.map(func, iterable)
		pool.close()
		pool.join()
		#print("progenyList[0].shape {}".format(progenyList[0].shape))

	# convert the list to a numpy array
	progenies = np.array(progenyList)
	# convert the shape to (numJobs*progenyPerJob) by 2 by n 
	# from numJobs by progenyPerJob by 2 by n
	progenies = np.reshape(progenies, (numJobs*progenyPerJob,2,L1.shape[1]))
	#print("progenies\n {}".format(progenies))

	# do the rest
	if (theRestNum != 0):
		theRestProgenies = cross2iterable(L1,L2,RF,theRestNum,numJobs)
		#print("theRestProgenies\n {}".format(theRestProgenies))
		progenies = np.concatenate((progenies, theRestProgenies), axis=0)

	#print("progenies\n {}".format(progenies))

	return progenies 

# single processing version with memory management
# L1 = n * 2 matrix
# L2 = n * 2 matrix
# RF = array of recombination frequencies of size (n-1) 
# k  = number of progenies to produce
def cross2sp(L1, L2, RF, k):

	# if this value is too big, you memory cant hold 
	# all the data and therefore the total execution time
	# will be very slow
	maxTotalJobSize = 100
	# number of jobs
	numCores = numJobs = mp.cpu_count()
	numJobs = numCores
	# number of progenies to produce per job
	progenyPerJob = k//numJobs
	
	while(progenyPerJob*numCores > maxTotalJobSize):
		numJobs = numJobs * 2
		progenyPerJob = k//numJobs
		#print("numJobs {}, progenyPerJob {}".format(numJobs, progenyPerJob))

	theRestNum = k%numJobs 
	print("numJobs {}, progenyPerJob {}, theRestNum {}".format(numJobs, progenyPerJob, theRestNum))

	progenyList = []
	rangeNumJobs = range(numJobs)
	n = L1.shape[1]
	# use multi-thread to calculate
	if (numJobs != 0):
		for i in rangeNumJobs:	
			progenyList.append(cross2iterable(L1,L2,RF,progenyPerJob,i))
		#print("progenyList[0].shape {}".format(progenyList[0].shape))

	# convert the list to a numpy array
	progenies = np.array(progenyList)
	#print(progenies.shape)

	# convert the shape to (numJobs*progenyPerJob) by 2 by n 
	# from numJobs by progenyPerJob by 2 by n
	progenies = np.reshape(progenies, (numJobs*progenyPerJob,2,L1.shape[1]))
	#print("progenies\n {}".format(progenies))

	# do the rest
	if (theRestNum != 0):
		theRestProgenies = cross2iterable(L1,L2,RF,theRestNum,numJobs)
		#print("theRestProgenies\n {}".format(theRestProgenies))
		progenies = np.concatenate((progenies, theRestProgenies), axis=0)

	#print("progenies\n {}".format(progenies))

	return progenies 

#!/usr/bin/python
import numpy as np
from functools import partial
import multiprocessing

# return an array of generated progenies
# L1 = numRow * 2 matrix
# L2 = numRow * 2 matrix
# rf = array of recombination frequencies
# numProgenies = number of generated DNAs
def cross(L1, L2, rf, numProgenies):
	# get number of rows of L1
	numRows = L1.shape[0]
	# if L1 and L2 don't have the same number of rows
	if (numRows != L2.shape[0]):
		print("these matrices don't have the same number of rows")
		return None 
	# if not enough recombination frequencies are provided
	if (len(rf) != numRows-1):
		print("not enough recombination frequencies")
		return None

	# create a list of matrices
	progenies = [None]*numProgenies
	#progenies = np.full(numProgenies, None)

	# create progenies
	i = 0
	while (i < numProgenies):
		progenies[i] = cross1(L1, L2, rf, numRows, i)
		i += 1

	return progenies 


# multithreding version of cross function
# it is about 2-3 times as fast as normal cross
# return an array of generated progenies
# L1 = numRow * 2 matrix
# L2 = numRow * 2 matrix
# rf = array of recombination frequencies
# numProgenies = number of generated DNAs
def crossParallel(L1, L2, rf, numProgenies):
	# get number of rows of L1
	numRows = L1.shape[0]
	# if L1 and L2 don't have the same number of rows
	if (numRows != L2.shape[0]):
		print("ERROR: these matrices don't have the same number of rows")
		return None 
	# if not enough recombination frequencies are provided
	if (len(rf) != numRows-1):
		print("ERROR: not enough recombination frequencies")
		return None

	# create a list of matrices
	progenies = [None]*numProgenies

	# use multithread to calculate
	
	iterable = range(0, numProgenies)
	pool = multiprocessing.Pool()
	func = partial(cross1, L1, L2, rf, numRows)
	projenies = pool.map(func, iterable)
	pool.close()
	pool.join()

	return progenies 


# return generated progeny
# L1 = numRow * 2 matrix
# L2 = numRow * 2 matrix
# rf = array of recombination frequencies
# numRows = number of rows in matrices
def cross1(L1, L2, rf, numRows, iterable):
	print("  generating progeny " + str(iterable+1))

	# creating numRow * 2 matrix
	print("    generating an empty progeny (all zeros) ")
	progeny = np.zeros((numRows,2)) 	

	# evaluating first row in L1 with 50/50 probability
	# if randomValIndex is 0, it means the left value was chosen
	# if randomValIndex is 1, it means the right value was chosen
	print("    evaluating L1 and making left side of progeny matrix")
	randomValIndex = np.random.randint(2)
	randomVal = L1[0][randomValIndex]
	progeny[0][0] = randomVal

	# evaluate other rows in L1
	for i in range(numRows-1):      
		# randomValIndex will be a weighted random index
		# of the value from each row in L1

		# decide the weights based on 
		# which side the value was on the previous row
		if (randomValIndex == 0):
			leftWeight = 1-rf[i]
		elif (randomValIndex == 1):
			leftWeight = rf[i]

		# get the random value and index from choices and weights
		randomvalue = np.random.rand()
		if (randomvalue <= leftWeight):
			randomValIndex = 0
		else:
			randomValIndex = 1

		# substitute the gained value into progeny
		progeny[i+1][1] = L1[i+1][randomValIndex]

		
	# evaluating first row in L2 with 50/50 probability
	# if randomValIndex is 0, it means the left value was chosen
	# if randomValIndex is 1, it means the right value was chosen
	print("    evaluating L2 and making right side of progeny matrix")
	randomValIndex = np.random.randint(2)
	randomVal = L2[0][randomValIndex]
	progeny[0][1] = randomVal

	# evaluate other rows in L2	
	for i in range(numRows-1):   
		# randomValIndex will be a weighted random index
		# of the value from each row in L2

		# decide the weights based on 
		# which side the value was on the previous row
		if (randomValIndex == 0):
			leftWeight = 1-rf[i]
		elif (randomValIndex == 1):
			leftWeight = rf[i]

		# get the random value and index from choices and weights
		randomvalue = np.random.rand()
		if (randomvalue <= leftWeight):
			randomValIndex = 0
		else:
			randomValIndex = 1

		# substitute the gained value into progeny
		progeny[i+1][1] = L2[i+1][randomValIndex]

	return progeny


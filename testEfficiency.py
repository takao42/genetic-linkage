#!/usr/bin/python
from GenericLinkage import cross
from GenericLinkage import crossParallel
import numpy as np

# matrix[row][column]

if __name__ == '__main__':    
	# create random binary matrices 
	# with 1.4 million numRows and two columns
	# creating numRow * 2 matrix
	#numRows = 140
	numRows = 1400000
	numColumns = 2
	print("generating matrix 1.4 million rows (L1)")
	L1 = np.random.randint(2, size=(numRows,2))

	print("generating matrix 1.4 million rows (L2)")
	L2 = np.random.randint(2, size=(numRows,2))


	# generate an array with 1.4 million - 1 elements
	# from a uniform distribution between 0 and 1, 
	# and then set RF as that vector multiplied by 0.1.
	print("generating an array of size 1.4 million - 1")
	rf = np.random.random_sample((numRows-1,))
	rf *= 0.1

	# generate progenies
	print("generating 30 progenies")
	#progenies = cross(L1, L2, rf, 2)
	progenies = crossParallel(L1, L2, rf, 30)

	if(progenies == None):
		print("error")
	else:
		print("jobs done")
		print(progenies[1])
		
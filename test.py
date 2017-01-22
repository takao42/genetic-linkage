#!/usr/bin/python
import numpy as np
from timer import Timer
from GenericLinkage import *

def test0():
	L1 = np.array([[0,0,0,0,0],[1,1,1,1,1]])
	#print "L1"
	#print L1
	L2 = np.array([[1,1,1,1,1],[0,0,0,0,0]])
	#print "L2"
	#print L2
	RF = np.array([0.05,0.05,0.05,0.05])
	#print "RF"
	#print RF

	with Timer('generating 3 progenies'):
		Y = cross2(L1,L2,RF,3)

	print "Y"
	print Y

def test1():
	# number of rows in a gene
	n = 1400000
	# number of progenies to produce
	k = 30
	# generate two random 2 by n matrices
	# filled with random 0 and 1
	L1 = np.random.randint(2, size=(2,n))
	L2 = np.random.randint(2, size=(2,n))
	# array of recombination frequencies of size (n-1) 
	RF = 0.1*np.random.random(n-1)
	# generate progenies
	with Timer('generating 30 progenies'):
		Y = cross2(L1,L2,RF,k)

def test2():
	# up in column-based corresponds to left in row-based
	# down in column-based corresponds to right in row-based
	# conversion from column-based to row-based
	# will be done by rotating the matrices
	# by 270 degrees

	L1 = np.array([[0,1],[0,1],[0,1],[0,1],[0,1]])
	L2 = np.array([[1,0],[1,0],[1,0],[1,0],[1,0]])
	RF = np.array([[0.05],[0.05],[0.05],[0.05]])
	# convert
	L1 = np.rot90(L1, 3)
	L2 = np.rot90(L2, 3)
	RF = RF[:,0]
	print "L1"
	print L1
	print "L2"
	print L2
	print "RF"
	print RF

	with Timer('generating 3 progenies'):
		Y = cross2(L1,L2,RF,3)

	#print "Y"
	#print Y

def test3():
	# up in column-based corresponds to left in row-based
	# down in column-based corresponds to right in row-based
	# conversion from column-based to row-based
	# will be done by rotating the matrices
	# by 270 degrees


	# number of rows in a gene
	n = 1400000
	#n = 6480
	# number of progenies to produce
	k = 30
	#k = 3240
	# generate two random n*2 matrices
	# filled with 0 and 1
	L1 = np.random.randint(2, size=(n,2))
	L2 = np.random.randint(2, size=(n,2))
	# generate (n-1)*1 matrix of random recombination frequencies
	RF = 0.1*np.random.random((n-1, 1))
	# generate progenies

	# convert
	L1 = np.rot90(L1, 3)
	L2 = np.rot90(L2, 3)
	RF = RF[:,0]

	with Timer('generating 30 progenies'):
		Y = cross2(L1,L2,RF,k)



if __name__ == '__main__':    
	test1()
	
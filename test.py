#!/usr/bin/python
import numpy as np
from timer import Timer
from GenericLinkage import *

def test1():
	# number of rows in a gene
	#n = 5
	n = 1400000
	# k  = number of progenies to produce
	#k = 3
	k = 30
	# generate two random n*2 matrices
	# filled with 0 and 1
	L1 = np.random.randint(2, size=(n,2))
	L2 = np.random.randint(2, size=(n,2))
	# generate (n-1)*1 matrix of random recombination frequencies
	RF = 0.1*np.random.random((n-1, 1))
	# generate progenies
	with Timer('generating 30 progenies'):
		Y = cross2(L1,L2,RF,k)

def test2():
	L1 = np.array([[0,1],[0,1],[0,1],[0,1],[0,1]])
	#print "L1"
	#print L1
	L2 = np.array([[1,0],[1,0],[1,0],[1,0],[1,0]])
	#print "L2"
	#print L2
	RF = np.array([[0.05],[0.05],[0.05],[0.05]])
	#print "RF"
	#print RF

	with Timer('generating 3 progenies'):
		Y = cross2(L1,L2,RF,3)

	print "Y"
	print Y


if __name__ == '__main__':    
	test1()
	
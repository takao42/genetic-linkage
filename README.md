# genetic-linkage

Efficient module that can be used to calculate multiple progeny from two genomes.

Developed as part of an [undergradutate research at Iowa State University](http://lib.dr.iastate.edu/undergradresearch_symposium/2017/presentations/82/).

This is [the research poster](https://github.com/takao42/GenomicSelectionSimulator/blob/master/poster.pdf).

## Dependency

sudo pip install numpy

## How to use this module

#### Parameters:

L1 = 2 by n matrix representation of genome<br>
L2 = 2 by n matrix representation of genome<br>
RF = array of recombination frequencies of size (n-1) <br>
k  = number of progeny to produce<br>

#### Return:

k by 2 by n matrix representation of genomes

## Description

Genome can be expressed as 2 by n matrix of 0s and 1s.  Such as <br>
0 1 1 0 1 1 0<br>
1 0 1 0 1 0 1<br>

Each row represents a chromosome and each column represents a locus. Each number is an allele. 0 means an useless allele and 1 means an useful allele.

These values are obtained by observing the phenotype and genotype of the target plant.

Lets say 90% of the tall plants of the same species shares an allele of G at locus 3. Then this value is considered an useful allele at that specific locus.

So if another plant has a genome of the following,

A G C T G A<br>
A G G G T A

then the third allele in the second row can be expressed as 1.

The progeny can be calculated using the following algorithm.

1. Take one genome and starts from either row. 
2. Go to the next column and change the row with the probability of the recombination frequency.
3. Repeat this until the end and construct 1 by n matrix using the chosen values
4. Do the same for the other genome as well.
5. Stick them together to make a 2 by n matrix

## Usage Example

	L1 = np.array([[0,0,0,0,0],[1,1,1,1,1]])
	L2 = np.array([[1,1,1,1,1],[0,0,0,0,0]])
	L1 = np.array(L1, dtype=np.int8)
	L2 = np.array(L2, dtype=np.int8)
	RF = np.array([0.05,0.05,0.05,0.05])
	Y = cross2(L1,L2,RF,3)

## Contributions

- [Takao Shibamoto](https://github.com/takao42) - main developer
- [Dr. Lizhi Wang](https://www.imse.iastate.edu/directory/faculty/lizhi-wang/) - mentor
- [ISU Industrial and Manufacturing Systems Engineering](https://www.imse.iastate.edu/)
- [ISU University Honors Program](https://www.honors.iastate.edu/)

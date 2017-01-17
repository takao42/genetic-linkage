# genetic-linkage

This python module can be used to produce multiple progenies from two genes.

A gene is defined as n * 2 matrix filled with 0 and 1s.
0 means it is useless for certain purpose such as making a plant that is strong to certain desease.
1 means it is usefull.

##Explanation
cross - crosses two genes and produces multiple progenies<br>
crossParallel - multi threading version of cross. usually 2-3 times as fast as the single threading one<br>
cross1 - crosses two genes and produces one progeny

##Dependency
sudo pip install numpy

Compiled with Python 2.7<br>
I don't recommend using Python 3 because it is slower than python 2.



#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

import time

def getPrimeTable(scope):
	primes = [1] * scope
	for i in xrange(2, int(scope ** .5) + 1):
		if primes[i]:
			for m in xrange(i ** 2, scope, i):
				primes[m] = 0
	primes[0], primes[1] = 0, 0
	return primes

def isPermutation(a, b):
	tmp = [0] * 10
	while a > 0:
		tmp[a % 10] += 1
		a /= 10
	while b > 0:
		tmp[b % 10] -= 1
		b /= 10
	for i in tmp:
		if i:
			return False
	return True

def solution():
	primes = getPrimeTable(10000)
	for i in xrange(1489, len(primes)):
		if primes[i]:
			for j in xrange(i + 1, len(primes)):
				if primes[j] and primes[(i + j) /2]:
					if isPermutation(i, j) and isPermutation(j, (i + j) / 2):
						print 'The answer is {}' .format(str(i) + str((i + j) / 2) + str(j))
						return

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()

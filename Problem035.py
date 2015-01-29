#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

import time

def primeTable(scope):
	primeList = [1] * scope
	for i in xrange(2, int(scope ** .5) + 1): 
		if primeList[i]:
			for m in xrange(i ** 2, scope, i):
				primeList[m] = 0
	primeList[0], primeList[1] = 0, 0
	return primeList

def rotateNumber(x):
	rotateList = [str(x)]
	rotate = str(x)[1:] + str(x)[:1]
	while rotate != str(x):
		rotateList.append(rotate)
		rotate = str(rotate)[1:] + str(rotate)[:1]
	return rotateList

def solution():
	primes = primeTable(10 ** 6)
	cirPrimes = list()
	for i in xrange(2, 10 ** 6):
		flag = 0
		if primes[i]:
			for r in rotateNumber(i):
				if not primes[int(r)]:
					flag = 1
			if not flag:
				cirPrimes.append(i)
	print 'The answer is {}' .format(len(cirPrimes))

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()

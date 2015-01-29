#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
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

def isPandigital(number):
	length = len(str(number))
	if sorted(set(str(number))) == sorted(set([str(i) for i in range(1, len(str(number)) + 1)])):
		return True
	else:
		return False

def solution():
	primes = getPrimeTable(10000000)
	for i in xrange(7986543, 1234566, -1):
		if primes[i] and isPandigital(i):
			print i, '\n'
			print 'The answer is {}' .format(i)
			return
	for i in xrange(9876, 1233, -1):
		if primes[i] and isPandigital(i):
			print 'The answer is {}' .format(i)
			return 

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
